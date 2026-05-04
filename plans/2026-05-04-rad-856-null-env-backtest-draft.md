---
title: "We Read About a Better Way to Test Backtests. Then We Checked If It Applied to Us."
date: 2026-05-26
slug: null-environment-backtest-testing
tags: [systematic-trading, backtesting, research-methodology, quant]
source_issue: RAD-499
status: draft — awaiting Testy approval
---

# We Read About a Better Way to Test Backtests. Then We Checked If It Applied to Us.

In late April, two independent research sources landed in the same place: *your backtests probably pass for the wrong reasons*.

An arXiv paper on implementation risk in backtesting (2603.20319) flagged Sharpe divergence versus null baselines as a missing discipline. A Vertox Quant piece called "Backtests Lie" laid out a concrete framework: run your strategy on five synthetic null environments and see if the Sharpe holds up. If it does, great. If it doesn't, your backtest is telling you something false.

The five environments in the framework are:
- White noise returns (no structure)
- GARCH(1,1) vol-clustered returns (vol structure, no signal)
- Bid-ask bounce MA(1) (short-horizon artefact simulation)
- Factor null (returns from a linear factor model with no alpha)
- Regime-switching vol (market regimes with no persistent signal)

The idea is sound. If a strategy beats all five synthetic environments, it is harder to dismiss as an overfitting artefact. We took it seriously.

## The Test We Ran Before Running the Tests

Before writing a single line of null-environment harness code, we ran a different test: *would this framework have caught our actual past failures?*

That question matters because frameworks are not free. Building a calibrated null-environment harness takes real engineering time — probably a week or two of a senior researcher's attention. That is budget. To justify spending it, we needed evidence that the class of failures it catches is the class of failures we have actually suffered.

Our canonical failure on record was [RAD-246](https://github.com/radiusred). A configuration bug — a stale `cache_dir` path pointing to a directory that no longer existed — caused a backtest run to execute on phantom data: an empty series returning synthetic zeros. Four instruments showed wildly positive results. An independent re-run with the correct cache path reversed every one of them.

So: would null-environment testing have caught that?

## The Answer Was No

Null-environment tests substitute synthetic return series and probe the *strategy logic*. They bypass the data-loading layer entirely. The RAD-246 failure was in the data-loading layer — a config resolution problem. Both the in-sample and out-of-sample windows were running on phantom data, so the gap between them that null-environment tests look for simply did not exist in the failing run.

The K_eff / ΔZ statistics that the Vertox framework computes measure in-sample vs. out-of-sample overfit. When both samples are on phantom data, neither shows anomalous overfit — the strategy looks consistent because it is consistently wrong on the same empty series.

The framework catches real problems. Overfitting. Regime leakage. Microstructure exploitation of bid-ask artefacts. HAC inflation. These are all genuine failure modes for quantitative strategies. We just have no historical evidence of being bitten by any of them. We have direct evidence of a data-integrity failure.

Spending two weeks building a framework that addresses a hypothetical risk while the failure class we *have* encountered goes unaddressed is not a good trade.

## What We Did Instead

We filed a smaller, targeted piece of engineering work: a data-integrity sentry that runs as a pre-flight check inside every backtest. Four assertions:

1. `cache_dir` exists and is reachable (directly catches RAD-246)
2. Bar count meets a configurable minimum (detects phantom or truncated data)
3. Return distribution sanity check (detects price-scale inversion — a separate, real bug we caught in production)
4. Price-scale band check (catches cents-vs-dollars confusion in instrument data)

No statistical machinery. No calibration. No regime-switching parameterisation. One engineer, one day.

The full null-environment methodology document lives in our research archive in case the board wants to revisit it. If we ever catch the team actually suffering a statistical overfitting failure, we will promote that investigation from the archive to an active workstream.

## The Actual Lesson

The lesson is not that sophisticated research is bad. The lesson is that *choosing which problem to solve requires evidence about which problems you actually have*.

Two independent, credible sources converged on null-environment testing as a gap in standard practice. They are probably right as a general statement about the industry. But general best practice and your specific risk profile are not the same thing.

Before building a solution for a problem class, ask: have I been bitten by this class? If yes — great, the investment is justified. If no — what *have* I been bitten by, and is there a targeted solution for that?

The data-integrity sentry we shipped takes a morning to write and directly addresses the only backtest failure we have on record. The null-environment framework would take two weeks and addresses failures we haven't seen.

We went with the morning.

---

*Source: RAD-499 — Investigate null-environment backtest falsification framework*

*Safe-to-publish confirmation: no proprietary strategy parameters, no account details, no live position data. Failure mode described at architectural level only. RAD-246 failure mechanism (stale config path) is confirmed public-safe.*
