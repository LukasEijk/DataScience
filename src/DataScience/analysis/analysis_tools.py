import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pandas as pd
import numpy as np

def analyse_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    """Produce and analyse raw data.

       Function fits 16th and 84th percentiles.

    Args:
        raw_data: a dataframe containing the raw data.

    Returns:
        pd.DataFrame containing fit results.
    """
    pct16 = []
    pct84 = []
    x_mean = []
    bins = np.arange(raw_data['x'].min(),raw_data['x'].max(), 100)
    for k in range(len(bins) -1):
        idx = (raw_data['x'] >= bins[k]) & (raw_data['x'] < bins[k+1])
        pct16.append(np.percentile(raw_data['y'][idx],16))
        pct84.append(np.percentile(raw_data['y'][idx],84))
        x_mean.append(np.mean(raw_data['x'][idx]))
    return pd.DataFrame({'pct16': pct16, 'pct84': pct84, 'x_mean': x_mean})


def generate_data(n: int = 1000) -> pd.DataFrame:
    """Generate data points.

    Args:
        n: Number of datapoints. Defaults to 1000.

    Returns:
        dataframe with raw data.
    """
    np.random.seed(42)
    x = np.linspace(0,2500, n)
    noise_component = np.random.rand(n)
    y = (x + x*noise_component/3)
    return pd.DataFrame({'x': x, 'y': y})
