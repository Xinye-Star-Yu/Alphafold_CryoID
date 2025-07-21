import pathlib
import requests

def download_alphafold(uniprot_id: str,
                       out_dir: str = "alphafold_models",
                       formats: tuple[str, ...] = ("pdb", "cif"),
                       timeout: int = 15):
    """
    Download the AlphaFold model for `uniprot_id`.
    - Saves the first available format to <out_dir>/<uniprot_id>.<ext>
    - Returns the pathlib.Path of the saved file, or None if nothing found.
    """
    out_path = pathlib.Path(out_dir)
    out_path.mkdir(exist_ok=True)

    for ext in formats:
        url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.{ext}"
        try:
            r = requests.get(url, timeout=timeout)
            if r.ok and r.content and not r.text.startswith("<!DOCTYPE"):
                file_path = out_path / f"{uniprot_id}.{ext}"
                file_path.write_bytes(r.content)
                print(f"Saved {file_path.resolve()}")
                return file_path
            else:
                print(f"{ext.upper()} file not found (status {r.status_code}). Trying next format…")
        except requests.RequestException as err:
            print(f"Download error for {ext}: {err}")

    # no format succeeded
    print("File not found")
    return None

# test
example_id = "A0A1U7UAC1"
download_alphafold(example_id)
