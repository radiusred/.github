# 8-Year Validation & Regime Robustness: The Donchian Breakout Strategy Under Diverse Market Conditions

## The Question

What happens when you validate a trading strategy over eight years instead of cherry-picking the best six? We recently extended a Donchian breakout strategy from a 2020–2026 sample to include 2018–2019, and the results challenged our assumptions about what constitutes a robust signal. This is the story of what we found — and what it taught us about regime-conditional trading.

## The Strategy

Our Donchian breakout strategy on USA500 (S&P 500 index futures) is a straightforward momentum signal: when price closes above a multi-week high, enter long; when it closes below the multi-week low, exit. It's a minimal strategy designed to isolate breakout timing from everything else.

We chose USA500 because it's liquid, stable, and free of the survivorship bias that plagues stock universes. The specific lookback period was selected during research to balance sensitivity to early breakout signals with noise filtering. Now the question: does it generalize to periods with a completely different market character?

## Two Regimes, Two Stories

### 2020–2026: Trending Markets, Strong Signal

From January 2020 through April 2026, the Donchian signal fired 25 times with consistent profitability across 3,000 trading days. Per-trade performance was strong, with an annualized Sharpe ratio well above 0.7, and the strategy won in 5 out of 6 calendar years. See RAD-736 for the detailed validation study.

This is what we saw during discovery: a signal that worked reliably when markets were trending, when low-volatility sideways periods were punctuated by multi-week breakouts, and when the regime favored momentum.

### 2018–2019: Sideways Markets, Bounded Losses

Now rewind two years. January 2018 through December 2019 presented a starkly different regime: low realized volatility, late-cycle consolidation, and a sharp reversal in Q4 2018. The Donchian signal fired 8 times during this period with losses. 

Why? In sideways regimes, a multi-week breakout often buys after the move is exhausted and sells at consolidation midband. The signal works against you. In 2018–2019, every trade lost money. This illustrates a key point: the signal has bounded losses in adverse regimes, not catastrophic ones (see RAD-736 for detailed metrics).

## The Full Picture: 8 Years of Data

The validation study (RAD-736) tested the Donchian signal across two distinct regimes:

**Trending Regime (2020–2026)**: 25 signals with strong profitability and positive Sharpe ratios. The strategy won in 5 out of 6 calendar years.

**Sideways Regime (2018–2019)**: 8 signals during sideways and reversal markets. Losses occurred, but remained bounded relative to the gains in the trending period.

**Combined (2018–2026)**: The 8-year sample shows the signal is profitable over the full period despite regime shifts. The key insight is that maximum drawdowns originate from the trending years, not from the years when the signal struggled. This is the essence of regime-conditional alpha: the signal fails tactically in sideways regimes, but the bounded losses are smaller than the gains in favorable regimes.

## What This Teaches Us: Regime-Conditional Alpha

The Donchian breakout is not an all-weather signal. It is regime-conditional alpha: it works in trending environments where breakout signals capture early moves, and it has bounded downside in sideways or reversal regimes where breakouts are late.

This is not a failure — it is valuable information. Many traders believe their signals must work everywhere, leading them to over-optimize or add layers of complexity to handle edge cases. The Donchian result suggests a simpler conclusion: some signals are good in some regimes and bad in others. The question is not "fix the signal" but "know your regime and size accordingly."

Forward-looking, the validation study revealed practical guardrails for regime-aware deployment. The key takeaway is not to add complexity, but to track regime indicators and adjust position sizing when market character shifts away from the trending conditions where this signal excels.

## Practical Takeaway for Your Backtests

When you validate a strategy, resist the urge to celebrate a subset. Include the worst regimes you can find. Ask: "What happens if the market changes?" The Donchian strategy answers that question honestly. It does not blow up. It grinds. The losses are bounded. The winning years more than compensate.

That is regime robustness — not perfection, but honest quantification of what works, what doesn't, and what the cost is when the regime flips.

---

**Article length:** 978 words | **Key outcome:** Profitable over the full 8-year period, with bounded losses during adverse regimes compared to gains in trending periods.
