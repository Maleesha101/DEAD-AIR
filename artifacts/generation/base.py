"""Base classes and generator registry for deterministic campaign artifacts."""

from __future__ import annotations

import abc
from pathlib import Path
from typing import Dict, List, Optional

from .manifest import ArtifactRecord, validate_safe_path


class BaseArtifactGenerator(abc.ABC):
    """Abstract base class for all challenge stage artifact generators."""

    @property
    @abc.abstractmethod
    def stage_id(self) -> str:
        """The identifier of the stage (e.g. '01-osint')."""

    @property
    @abc.abstractmethod
    def description(self) -> str:
        """Brief description of the generated artifact set."""

    @abc.abstractmethod
    def generate(self, output_dir: Path, seed: int = 1337) -> List[ArtifactRecord]:
        """Generates stage artifacts deterministically into output_dir.

        Must return a list of ArtifactRecord instances.
        All written paths must be strictly within output_dir.
        """


class GeneratorRegistry:
    """Registry coordinating multiple stage artifact generators."""

    def __init__(self) -> None:
        self._generators: Dict[str, BaseArtifactGenerator] = {}

    def register(self, generator: BaseArtifactGenerator) -> None:
        self._generators[generator.stage_id] = generator

    def get(self, stage_id: str) -> Optional[BaseArtifactGenerator]:
        return self._generators.get(stage_id)

    def list_stages(self) -> List[str]:
        return sorted(self._generators.keys())

    def generate_all(self, output_dir: Path, seed: int = 1337) -> List[ArtifactRecord]:
        all_records: List[ArtifactRecord] = []
        for stage_id in self.list_stages():
            generator = self._generators[stage_id]
            records = generator.generate(output_dir, seed=seed)
            all_records.extend(records)
        return all_records


class SyntheticSampleGenerator(BaseArtifactGenerator):
    """Reference generator demonstrating deterministic generation and manifest emission."""

    @property
    def stage_id(self) -> str:
        return "00-bootstrap"

    @property
    def description(self) -> str:
        return "Synthetic bootstrap evidence file used for pipeline verification"

    def generate(self, output_dir: Path, seed: int = 1337) -> List[ArtifactRecord]:
        rel_path = f"{self.stage_id}/sample_signal.txt"
        target_path = validate_safe_path(output_dir, rel_path)
        target_path.parent.mkdir(parents=True, exist_ok=True)

        content = (
            f"# DEAD AIR SYNTHETIC ARTIFACT BOOTSTRAP\n"
            f"Seed: {seed}\n"
            f"Station: PCRN-RELAY-04\n"
            f"Frequency: 162.400 MHz\n"
            f"Status: CARRIER_LOST\n"
        ).encode("utf-8")

        with open(target_path, "wb") as f:
            f.write(content)

        import hashlib
        h = hashlib.sha256(content).hexdigest()
        return [
            ArtifactRecord(
                path=rel_path,
                sha256=h,
                size_bytes=len(content),
                stage=self.stage_id,
                visibility="public",
                description=self.description,
            )
        ]
