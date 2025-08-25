from pathlib import Path


def get_resource_path(resource_name: str) -> str:
    """Obtain the path of a test file."""
    root = Path(__file__).parent / "resources"
    return str(root / resource_name)
