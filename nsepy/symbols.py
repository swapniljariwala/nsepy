import pandas as pd
import io
from nsepy.urls import equity_symbol_list_url


def get_symbol_list():
    res = equity_symbol_list_url()
    df = pd.read_csv(io.StringIO(res.content.decode('utf-8')))
    return df
