import os
import yaml
from pathlib import Path


def load_scenarios(suite_dir: str) -> list[dict]:
    """Load all YAML scenario files from a directory."""
    scenarios = []
    for f in sorted(Path(suite_dir).glob("*.yaml")):
        with open(f) as fh:
            data = yaml.safe_load(fh)
            if isinstance(data, list):
                scenarios.extend(data)
            elif isinstance(data, dict):
                scenarios.append(data)
    return scenarios
