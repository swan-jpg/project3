import numpy as np
from .data_loader import asset_returns, portfolio_pnl
from scipy.stats import norm


class VaR: 
    def __init__(self, prices, exposures, confidence=0.95):
        self.exposures = exposures
        self.confidence = confidence
        self.returns_pct = asset_returns(prices)
        self.pnl = portfolio_pnl(self.returns_pct, exposures)
        
    def parametric_var(self):
        mean = self.pnl.mean(axis=0,skipna=True)
        volatility = self.pnl.std(axis=0,skipna=True)

        percentile = norm.ppf(1 - self.confidence, mean, volatility)
        return -percentile

    def historical_var(self):
        percentile = np.quantile(self.pnl, 
                                 (1-self.confidence), axis = 0)
        return -percentile

    def monte_carlo_var(self, simulations=10000, seed=None):
        mean = self.pnl.mean(axis=0,skipna=True)
        volatility = self.pnl.std(axis=0,skipna=True)

        # older method for randomness that is apparently outdated
        # simulated_pnl = np.random.normal(loc=mean,scale=volatility, size=simulations)

        rng = np.random.default_rng(seed)
        simulated_pnl = rng.normal(loc=mean,
                                   scale=volatility,
                                   size=simulations)
        return -np.quantile(simulated_pnl, 1-self.confidence)

    # Expected shortfall
    def conditional_var(self):
        pass

def max_drawdown(exposure):
    returns_pct = portfolio_pnl(exposure)

    value = (1 + returns_pct).cumprod()
    peak = value.cummax().clip(lower=1.0)
    dd_pct = value / peak - 1

    return {
        "mdd_pct": dd_pct.min(),
        "trough_date": dd_pct.idxmin(),
    }
if __name__ == "__main__":
    pass


