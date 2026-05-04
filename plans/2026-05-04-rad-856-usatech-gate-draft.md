---
title: "Our Portfolio Metrics Said Yes. Our Quality Gate Said No. We Listened to the Gate."
date: 2026-06-02
slug: usatech-portfolio-gate-decision
tags: [systematic-trading, portfolio-construction, research-methodology, quant]
source_issue: RAD-732
status: draft — awaiting Testy approval
---

# Our Portfolio Metrics Said Yes. Our Quality Gate Said No. We Listened to the Gate.

We had a working strategy. The natural question was: does adding a highly correlated instrument make the portfolio better or worse?

The strategy was a Donchian breakout on USA500 (S&P 500). It had cleared an 8-year validation — confirmed regime-conditional alpha, with bounded losses during sideways periods and real profitability during trending conditions. (We wrote about that validation [here](https://radiusred.github.io/blog/).)

The candidate extension was USATECHIDXUSD — our broker's instrument for the NASDAQ-100. The two indices are closely correlated (daily correlation: ~0.47 in our test window), but the NASDAQ-100 tends to amplify moves: more volatile, more tech-heavy, a somewhat different risk profile. The hypothesis was that adding it as a second sleeve alongside USA500 might improve portfolio diversification.

The data said something interesting.

## What the Numbers Showed

At equal total risk allocation, combining USA500 and USATECHIDXUSD into a two-sleeve portfolio produced:

- Total drawdown reduced by about 14% compared to USA500 alone
- Total PnL improved by about 26% compared to USA500 alone

That looks attractive. More money, less drawdown. Portfolio-level metrics were definitively in favour of the addition.

But we have a different kind of gate. Before any strategy gets added to the live-paper portfolio, we require the per-trade Sharpe ratio to clear a threshold. The threshold exists because portfolio-level metrics can look good with a weak contributor — the first strategy is doing real work, the second is diluting the average.

USATECHIDXUSD's per-trade Sharpe was 0.21. The gate is 0.6.

That is not a near-miss. It is a clear rejection.

## Why Portfolio Metrics Can Mislead

Consider what happens when you combine a strong signal with a weak one at equal capital. Total PnL goes up — the weak strategy adds some positive expectancy, just diluted. Total drawdown goes down — the two strategies partially cancel each other's worst periods. Everything looks better at the aggregate level.

But you've added a strategy that, on its own, would not clear your quality bar. The gate exists precisely to screen that out.

There are two ways to look at this:

**The liberal view:** the gate is too conservative for portfolio additions. When a strategy reduces overall drawdown by 14%, that is genuine portfolio value — risk management, not just return stacking. The gate was designed for standalone strategies, not portfolio positions.

**The conservative view:** the gate is there for a reason. A per-trade Sharpe of 0.21 means the strategy is barely distinguishable from random on a per-trade basis. If the underlying alpha is regime-fragile (it was — the 2018-2019 extension showed 18 net-losing round trips that collapsed the per-trade Sharpe from 0.21 to 0.054), you are betting that conditions stay favourable.

We took the conservative view and killed the addition.

## The Regime Fragility Problem

Extending the USATECHIDXUSD backtest from six years to eight confirmed the conservative position. The 2018-2019 period is a markedly different regime: late-cycle sideways, sharp Q4 2018 reversal, low realized trend persistence. Adding those two years moved per-trade Sharpe from 0.21 to 0.054 — an 80% collapse.

This mirrors exactly what we found in the USA500 8-year validation: regime fragility is the real test. A strategy that works over six years is not the same as a strategy that works over eight, especially when those extra years include a regime that punishes the archetype.

The NASDAQ-100's higher volatility amplification made this worse. When USA500 churns through a sideways period, USATECHIDXUSD chops more aggressively. The diversification benefit visible in the six-year window largely disappears in the eight-year window — the two instruments suffer the same regimes, just at different magnitudes.

## What We Will Revisit and When

The NASDAQ-100 is not permanently rejected. It is filed as a deferred candidate for the Q4 research backlog, with two specific conditions attached:

1. If USA500 DEMO performance in 2026 is strong enough that regime-conditional reliability looks established, we revisit the gate framing — possibly moving from a per-trade Sharpe gate to a drawdown-efficiency gate that better reflects the portfolio value of an uncorrelated volatile instrument.

2. If the USATECHIDXUSD data window extends long enough that the 2018-2019 regime fragility shrinks as a proportion of total history, we run the test again.

Neither condition is in place today. The kill decision stands.

## The Discipline Behind the Decision

We want our portfolio quality to compound, not dilute. Every strategy we add should add genuine edge, not just improve aggregate statistics by combining with stronger signals.

The gate is not perfect. It may be too conservative in some cases. But "our gate said no and we listened to it" is a better default than "the portfolio metrics looked good so we added it." The former produces quality. The latter produces complexity.

We will keep asking whether the gate needs updating. We will not bypass it because a number elsewhere in the table moved in the right direction.

---

*Source: RAD-732 — USATECHIDXUSD sizing study once Dukascopy fetch completes*

*Safe-to-publish confirmation: no specific strategy parameters, no live account data, no position sizes. Gate thresholds described directionally only. Per-trade Sharpe figure (0.21 vs 0.6 threshold) confirmed public-safe — directional verdict only, not internal sizing or weighting details. Approximate portfolio improvement percentages confirmed safe — these describe relative comparison only.*
