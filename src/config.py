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

# List of US states
# The 'country' gets populated with things like 'texas' etc.
# We can use this list to group them all together as part of the cleaning

US_STATES = [
    "Alaska",
    "Alabama",
    "Arkansas",
    "American Samoa",
    "Arizona",
    "California",
    "Colorado",
    "Connecticut",
    "District ",
    "of Columbia",
    "Delaware",
    "Florida",
    "Georgia",
    "Guam",
    "Hawaii",
    "Iowa",
    "Idaho",
    "Illinois",
    "Indiana",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Massachusetts",
    "Maryland",
    "Maine",
    "Michigan",
    "Minnesota",
    "Missouri",
    "Mississippi",
    "Montana",
    "North Carolina",
    "North Dakota",
    "Nebraska",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "Nevada",
    "New York",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Puerto Rico",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Virginia",
    "Virgin Islands",
    "Vermont",
    "Washington",
    "Wisconsin",
    "West Virginia",
    "Wyoming",
]
