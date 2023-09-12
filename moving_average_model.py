
# Created by Getro Lucas

import numpy as np
import pandas as pd


class moving_average():
    def __init__(
        self,
        df : pd.DataFrame,
        freq : str = None,
        periods : int = 12
    ):
        '''
        Moving Average Forecaster.
        
        Parameters
        ----------
        df: pd.DataFrame containing the history.
        periods: Int number of periods to forecast forward.
        freq: Any valid frequency for pd.date_range, such as 'D' or 'M'.
        '''
        self.df = df
        self.freq = freq
        self.periods = periods
        
        if self.freq is None:
            self.freq = pd.infer_freq(self.df.ds.tail(3))
        
    def make_future_dataframe(
        self,
        response_col: str = 'y'
    ) -> pd.DataFrame:
        '''
        Returns
        ----------
        pd.DataFrame with future dates for predictions.

        '''
        
        future = pd.Series(
            pd.date_range(
                start=self.df.ds.max(),
                periods=self.periods + 1,
                freq=self.freq
            )
        )
        future = future[-self.periods:]
        future = pd.DataFrame({'ds':future})
        future[response_col] = np.nan

        return future
    
    # Moving Average Forecaster
    def predict(
        self,
        future: pd.DataFrame,
        response_col: str = 'y',
        window: int = 3,
        dimension_col: bool = True,
        dimension_col_name: str = 'Categories'
    ) -> pd.DataFrame:
        '''
        Parameters
        ----------
        df: pd.DataFrame with historical data using to calculate moving average
        df_future: pd.DataFrame with future dates.
        response_col: Values column name
        window: Window size to calculate moving average
        periods: Int number of periods to forecast forward.
        dimension_col: If you have multiples time-series to predict using loop, so True, else False. 
        dimension_col_name: If 'dimension_col' is True, the name of dimension column. 

        Returns
        ----------
        pd.DataFrame with historical dates, real values and predictions.

        '''
        df = self.df.reset_index(drop=True)
        forecast = future.copy()
        df['predict'] = list(df[response_col].rolling(window=window).mean())
        values = list(df[response_col])

        for i in range(self.periods):
            values.append(np.mean(values[-window:]))

        forecast['predict'] = values[-self.periods:]

        if dimension_col:
            forecast[dimension_col_name] = df[dimension_col_name][0]
        else:
            pass

        df2 = pd.concat((df, forecast), ignore_index=True)

        return df2
