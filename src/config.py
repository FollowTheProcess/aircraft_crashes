"""
Top level config file for the project.

Purpose
---------
Here you can put any global constants that the rest of the project can refer to.

Examples include: project directories and filepaths, data dtypes, model parameters etc.

Author
------
Tom Fleet

License
-------
MIT

"""


from pathlib import Path

# Key project directories, using pathlib for os-agnostic relative paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA = PROJECT_ROOT / "Data" / "Raw"
PROCESSED_DATA = PROJECT_ROOT / "Data" / "Processed"
FINAL_DATA = PROJECT_ROOT / "Data" / "Final"
FIGURES = PROJECT_ROOT / "Reports" / "Figures"
MODELS = PROJECT_ROOT / "Models"
