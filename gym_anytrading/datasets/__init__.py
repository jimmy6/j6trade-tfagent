from .utils import load_dataset as _load_dataset
from .utils import load_j6_dataset as _load_j6_dataset

# Load FOREX datasets
FOREX_EURUSD_1H_ASK = _load_dataset('FOREX_EURUSD_1H_ASK', 'Time')

# Load Stocks datasets
STOCKS_GOOGL = _load_dataset('STOCKS_GOOGL', 'Date')

# Load XAUUSD datasets
FOREX_XAUUSD_1M_ASK = _load_j6_dataset('xau_usd_OHLC2.0Tp1.0Cl100Vp')
