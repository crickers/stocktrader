import yfinance
df = yfinance.download('AAPL', start='2020-01-01', end='2020-10-02')
df.to_csv('AAPL.csv')

CREATE TABLE IF NOT EXISTS stock(
    id INTEGER PRIMARY KEY,
    symbol TEXT NOT NULL UNIQUE,
    company TEXT NOT NULL
)
