from pathlib import Path
import shutil

root = Path(__file__).parent.parent

def cleaner(name):
    for path in root.glob(f'**/{name}'):
        print(f"- {path}")
        shutil.rmtree(path)

if __name__ == "__main__":
    to_clean = [
        "venv", "__pycache__", ".pytest_cache",
        ".ipynb_checkpoints", ".scannerwork",
        "dask-worker-space",
    ]
    for name in to_clean:
        print(f"Cleaning all {name}...")
        cleaner(name)
