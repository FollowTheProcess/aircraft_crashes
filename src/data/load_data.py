"""
Stuff to enable easy loading/cleaning of the data.

Author: Tom Fleet
Created: 03/01/2021
"""


import pandas as pd

from src.config import RAW_DATA


class Data:
    def __init__(self) -> None:
        self.path = RAW_DATA.joinpath("Airplane_Crashes_and_Fatalities_Since_1908.csv")

    def __repr__(self) -> str:
        return "Data()"

    @staticmethod
    def _reorder_columns(df: pd.DataFrame) -> pd.DataFrame:
        """
        Easy reordering of dataframe columns. Takes in and returns
        a dataframe so can be called in df.pipe.

        Args:
            df (pd.DataFrame): Dataframe in.

        Returns:
            pd.DataFrame: Dataframe out.
        """

        new_col_order = [
            "date",
            "year",
            "month",
            "location",
            "country",
            "sector",
            "operator",
            "type",
            "aboard",
            "fatalities",
            "ground",
            "summary",
        ]

        df = df[new_col_order]

        return df

    @staticmethod
    def _determine_sector(operator: str) -> str:
        """
        Method to discretise the operator columns into
        Miltary, Commercial, or Private.

        To be called in a Series.apply.

        Args:
            operator (str): Contents of df['operator']

        Returns:
            str: One of Military, Commercial, or Private
        """

        if "military" in operator.lower():
            return "Military"
        elif "private" in operator.lower() or "business" in operator.lower():
            return "Private"
        else:
            return "Commercial"

    def load(self, clean: bool = True) -> pd.DataFrame:
        """
        Method to load in the data.

        User can choose to load from raw 'clean = False'
        or load cleaned 'clean = True'

        Args:
            clean (bool, optional): Whether to load in the cleaned data
                Defaults to True.

        Returns:
            pd.DataFrame: Dataframe containing requested data.
        """

        if not clean:
            return pd.read_csv(self.path)
        else:
            df = (
                pd.read_csv(self.path, parse_dates=["Date"])
                .drop(columns=["Flight #", "Registration", "cn/In", "Route", "Time"])
                .rename(columns=str.lower)
                .dropna()
                .applymap(lambda x: x.strip() if isinstance(x, str) else x)
                .assign(
                    year=lambda x: x["date"].dt.year.astype("int64"),
                    month=lambda x: x["date"].dt.month_name().astype("string"),
                    location=lambda x: x["location"].astype("string"),
                    country=lambda x: x["location"]
                    .str.strip()
                    .str.split(",")
                    .str.get(-1)
                    .astype("category"),
                    operator=lambda x: x["operator"].astype("string"),
                    type=lambda x: x["type"].astype("string"),
                    aboard=lambda x: x["aboard"].astype("int64"),
                    fatalities=lambda x: x["fatalities"].astype("int64"),
                    ground=lambda x: x["ground"].astype("int64"),
                    summary=lambda x: x["summary"].astype("string"),
                    sector=lambda x: x["operator"]
                    .apply(self._determine_sector)
                    .astype("category"),
                )
                .pipe(self._reorder_columns)
            )

            return df
