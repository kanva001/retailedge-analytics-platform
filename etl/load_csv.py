from pathlib import Path

BASE_PATH = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_PATH / "data" / "curated"


def save_to_csv(df, filename):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / filename
    df.to_csv(path, index=False)
    print(f"Saved: {path}")
