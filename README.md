# Aircraft Crashes

Analysis of aircraft crash data.

Tom Fleet, Jan 2021

## Install Instructions

If you want to install this project to run the code or experiment with it. Follow the below steps precisely.

*You will need the [conda package manager](https://www.anaconda.com/products/individual) to recreate the environment*

Clone the repo into your desired local directory

Navigate to the project root:

``` bash
cd <your_absolute_path_to_aircraft_crashes>
```

Create the project environment from the environment.yml:

``` bash
conda env create --file environment.yml
```

Install the project in editable mode (Note the . telling pip to install from the current directory):

``` bash
pip install -e .
```

**Warning:** Only install this project inside a virtual environment. Pip cannot fully uninstall -e installed projects.

## Project Organisation

------------

    ├── LICENSE
    ├── README.md          <- Top level README (this document).
    ├── Data
    │   ├── Final          <- The final data sets for modelling.
    │   ├── Processed      <- Intermediate data that has been transformed or otherwise processed.
    │   └── Raw            <- The original, immutable data dump.
    │
    ├── Models             <- Trained and serialised models, model predictions, model summaries or mlflow data.
    │
    ├── Notebooks          <- Jupyter notebooks. Typically containing EDA or other exploratory content.
    │
    ├── Reports            <- Generated analysis as HTML, PDF, LaTeX, markdown etc.
    │   └── Figures        <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment,
    │                         generated with `conda env export > environment.yml
    │ 
    ├── tasks.py           <- Project level automation tasks in invoke. Run `invoke --list` for help.
    │
    ├── setup.py           <- makes project pip installable `pip install -e .` so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── config.py      <- Top level src config file.
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │                     predictions
    │   │
    │   └── visualisation  <- Scripts to create exploratory and results oriented visualizations
    │
    └── tests              <- Unit tests for src

<p><small>Project structure adapted from the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

## High Level Summary

*A brief summary of the findings of the project and some of the key takeaways, some clear and concise figures to demonstrate any points you make*
