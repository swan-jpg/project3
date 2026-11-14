import yfinance as yf 
from pathlib import Path

def load_data(Tickers, start, end, path):

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    data = yf.download(Tickers,
                    start=start,
                    end= end,
                    auto_adjust=True, 
                    interval='1d',
                    progress=True,
    )
    prices = data['Close']
    prices.to_csv(path)
    return prices

def asset_returns(prices):
    prices = prices.pct_change().dropna()
    return prices
        
def portfolio_pnl(returns, portfolio):
    pnl = 0
    for ticker, exposure in portfolio.items():
        pnl = pnl + returns[ticker] * exposure
    return pnl

if __name__ == "__main__": 
    pass 





