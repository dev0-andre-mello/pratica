import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

np.random.seed(42)
DAYS = 252

def generate_prices(initial_price: float, volatility: float, tendency: float) -> np.ndarray:
    returns = np.random.normal(tendency / DAYS, volatility / np.sqrt(DAYS), DAYS)
    prices = initial_price * np.exp(np.cumsum(returns))
    return prices

stocks = {
    "PETR4": {"initial_price": 28.0, "volatility": 0.2, "tendency": 0.05},
    "VALE3": {"initial_price": 100.0, "volatility": 0.3, "tendency": 0.1},
    "ITUB4": {"initial_price": 20.0, "volatility": 0.15, "tendency": 0.03},
}

def calculate_returns(prices: np.ndarray) -> np.ndarray:
    return np.diff(prices) / prices[:-1]

def calculate_moving_volatility(returns: np.ndarray, window=21) -> np.ndarray:
    vol = np.array([
        np.std(returns[max(0, i - window):i]) * np.sqrt(DAYS)
        for i in range(1, len(returns) + 1)
    ])
    return vol

def moving_average(prices: np.ndarray, window: int) -> np.ndarray:
    return np.convolve(prices, np.ones(window) / window, mode='valid')

def calculate_sharpe(returns: np.ndarray, risk_free_rate=0.1075) -> float:
    excess = returns - risk_free_rate / DAYS
    return np.mean(excess) / np.std(excess) * np.sqrt(DAYS)

def calculate_max_drawdown(prices: np.ndarray) -> float:
    peak = np.maximum.accumulate(prices)
    drawdown = (peak - prices) / peak
    return np.max(drawdown)

def calculate_var(returns: np.ndarray, confidence=0.95) -> float:
    return np.percentile(returns, (1 - confidence) * 100)


# ── Processing ────────────────────────────────────────────────
results = {}

for name, params in stocks.items():
    prices = generate_prices(**params)
    returns = calculate_returns(prices)
    results[name] = {
        "prices": prices,
        "returns": returns,
        "total_return": (prices[-1] / prices[0] - 1) * 100,
        "daily_average": np.mean(returns) * 100,
        "annualized_volatility": np.std(returns) * np.sqrt(DAYS) * 100,
        "sharpe": calculate_sharpe(returns),
        "max_drawdown": calculate_max_drawdown(prices) * 100,
        "var_95": calculate_var(returns) * 100,
        "moving_volatility": calculate_moving_volatility(returns),
        "mm21": moving_average(prices, 21),
        "mm63": moving_average(prices, 63),
    }

returns_matrix = np.column_stack([r["returns"] for r in results.values()])
correlation = np.corrcoef(returns_matrix.T)


# ── Terminal Report ───────────────────────────────────────────
print("=" * 60)
print("  Analysis of Simulated Stock Prices")
print("=" * 60)

for name, metrics in results.items():
    print(f"\n{'-' * 40}")
    print(f"  {name}")
    print(f"{'-' * 40}")
    print(f"  Total Return:           {metrics['total_return']:+.2f}%")
    print(f"  Daily Average Return:   {metrics['daily_average']:+.4f}%")
    print(f"  Annualized Volatility:  {metrics['annualized_volatility']:.2f}%")
    print(f"  Sharpe Ratio:           {metrics['sharpe']:.2f}")
    print(f"  Max Drawdown:           {metrics['max_drawdown']:.2f}%")
    print(f"  Value at Risk (95%):    {metrics['var_95']:.2f}%")

print(f"\n{'=' * 40}")
print("  Correlation Matrix")
print(f"{'=' * 40}")
names = list(results.keys())
for i, n1 in enumerate(names):
    for j, n2 in enumerate(names):
        if j > i:
            print(f"  {n1} x {n2}: {correlation[i, j]:.3f}")


# ── Charts ────────────────────────────────────────────────────
colors = {"PETR4": "#00D4AA", "VALE3": "#FF6B6B", "ITUB4": "#FFD93D"}
bg    = "#0D1117"
bg2   = "#161B22"
text  = "#E6EDF3"
grid  = "#21262D"

fig = plt.figure(figsize=(16, 12), facecolor=bg)
fig.suptitle("Analysis of Simulated Stock Prices",
             fontsize=16, color=text, fontweight="bold", y=0.98)

gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.45, wspace=0.35)

# Chart 1 — Normalized price evolution
ax1 = fig.add_subplot(gs[0, :])
ax1.set_facecolor(bg2)
for name, data in results.items():
    norm = data["prices"] / data["prices"][0] * 100
    ax1.plot(norm, color=colors[name], linewidth=1.5, label=name, alpha=0.9)
ax1.axhline(100, color=grid, linestyle="--", linewidth=0.8)
ax1.set_title("Price Evolution (Normalized to 100)", fontsize=10, color=text, pad=8)
ax1.legend(facecolor=bg, edgecolor=grid, labelcolor=text, fontsize=9)
ax1.tick_params(colors=text)
ax1.spines[:].set_color(grid)
ax1.set_xlim(0, DAYS - 1)

# Chart 2 — Moving averages (PETR4)
ax2 = fig.add_subplot(gs[1, :2])
ax2.set_facecolor(bg2)
name = "PETR4"
d = results[name]
ax2.plot(d["prices"], color=colors[name], linewidth=1, label="Price", alpha=0.5)
ax2.plot(range(20, DAYS), d["mm21"], color="#FFFFFF", linewidth=1.5, label="MA 21")
ax2.plot(range(62, DAYS), d["mm63"], color="#FF9F43", linewidth=1.5, linestyle="--", label="MA 63")
ax2.set_title(f"Moving Averages — {name}", color=text, fontsize=10, pad=8)
ax2.legend(facecolor=bg, edgecolor=grid, labelcolor=text, fontsize=8)
ax2.tick_params(colors=text)
ax2.spines[:].set_color(grid)
ax2.set_xlim(0, DAYS - 1)

# Chart 3 — Rolling volatility
ax3 = fig.add_subplot(gs[1, 2])
ax3.set_facecolor(bg2)
for name, data in results.items():
    ax3.plot(data["moving_volatility"] * 100, color=colors[name], linewidth=1.2, label=name)
ax3.set_title("Rolling Volatility (21-day window)", color=text, fontsize=10, pad=8)
ax3.legend(facecolor=bg, edgecolor=grid, labelcolor=text, fontsize=8)
ax3.tick_params(colors=text)
ax3.spines[:].set_color(grid)

# Chart 4 — Return distribution
ax4 = fig.add_subplot(gs[2, 0])
ax4.set_facecolor(bg2)
for name, data in results.items():
    ax4.hist(data["returns"] * 100, bins=30, alpha=0.6,
             color=colors[name], label=name, edgecolor='none')
ax4.axvline(0, color='white', linewidth=0.8, linestyle='--')
ax4.set_title("Distribution of Daily Returns", color=text, fontsize=10, pad=8)
ax4.legend(facecolor=bg, edgecolor=grid, labelcolor=text, fontsize=8)
ax4.tick_params(colors=text)
ax4.spines[:].set_color(grid)
ax4.set_xlabel("Return (%)", color=text, fontsize=8)

# Chart 5 — Sharpe ratio
ax5 = fig.add_subplot(gs[2, 1])
ax5.set_facecolor(bg2)
names_list = list(results.keys())
sharpes = [results[n]["sharpe"] for n in names_list]
bars = ax5.bar(names_list, sharpes, color=[colors[n] for n in names_list], width=0.5)
ax5.axhline(1.0, color='white', linestyle='--', linewidth=0.8, alpha=0.5)
ax5.set_title("Sharpe Ratio", color=text, fontsize=10, pad=8)
ax5.tick_params(colors=text)
ax5.spines[:].set_color(grid)
for bar, val in zip(bars, sharpes):
    ax5.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
             f"{val:.2f}", ha='center', color=text, fontsize=9, fontweight='bold')

# Chart 6 — Correlation matrix
ax6 = fig.add_subplot(gs[2, 2])
ax6.set_facecolor(bg2)
ax6.imshow(correlation, cmap='RdYlGn', vmin=-1, vmax=1, aspect='auto')
ax6.set_xticks(range(3))
ax6.set_yticks(range(3))
ax6.set_xticklabels(names_list, color=text, fontsize=8)
ax6.set_yticklabels(names_list, color=text, fontsize=8)
ax6.set_title("Correlation between Returns", color=text, fontsize=10, pad=8)
ax6.spines[:].set_color(grid)
for i in range(3):
    for j in range(3):
        ax6.text(j, i, f"{correlation[i, j]:.2f}",
                 ha='center', va='center', color='black', fontsize=9, fontweight='bold')

plt.savefig("/home/whitedev/Documents/main/pratica/exercicios/analysis.png", dpi=150, bbox_inches='tight', facecolor=bg)
print("\nAnalysis completed and saved as 'analysis.png'.")
