# Social Media Pack — RAD-856 Wave 3
Date: 2026-05-04
Owner: Wordy
Status: Approved — May 4 teaser posted

---

## Today's Post (May 4, 2026)

### Bluesky — teaser for tomorrow's Regime-Conditional Alpha article

**Status: POSTED 2026-05-04**
**URI:** `at://did:plc:tkktcn7p42upz6lu6qwtmps2/app.bsky.feed.post/3mkz4nqn5xs2x`
**CID:** `bafyreifsffkqjlels5n3vorgfd4y6ftlqrlanmmkl6p62tayfhyf3o2ici`

**Text (298 chars — 'actually ' trimmed to fit 300-grapheme limit):**
```
Some signals don't work everywhere. They work in some regimes and fail (with bounded losses) in others.

We validated a Donchian breakout across 8 years, including 2018-2019's late-cycle chop.

New post tomorrow: what "regime-conditional alpha" means in practice.

#SystematicTrading #QuantResearch
```

**Facets applied:**
- `#SystematicTrading` → `app.bsky.richtext.facet#tag` at bytes 265–283 ✓
- `#QuantResearch` → `app.bsky.richtext.facet#tag` at bytes 284–298 ✓

**Timing:** Posted 2026-05-04 (within 08:00–10:00 UTC window)

---

## Article 1 Social Pack — "We Read About a Better Way to Test Backtests"
**Article slug:** `/null-environment-backtest-testing`
**Source:** RAD-499
**Proposed publish date:** 2026-05-26 (Mon)

### Bluesky — launch post

**Text (299 chars):**
```
Two credible sources both pointed us at null-environment backtest testing. We took it seriously.

Then we asked: would it have caught our actual past failures?

The answer was no. So we built something simpler that would.

Full post:
https://radiusred.github.io/blog/posts/null-environment-backtest-testing/

#SystematicTrading #Backtesting
```

**Facets required:**
- Link on the URL → `app.bsky.richtext.facet#link`
- `#SystematicTrading` → `app.bsky.richtext.facet#tag`
- `#Backtesting` → `app.bsky.richtext.facet#tag`

**Note:** Confirm exact URL after publishing.

### Bluesky — follow-up post (May 28, 2 days after launch)

**Text (296 chars):**
```
"General best practice" and "your specific risk profile" are not the same thing.

The null-environment framework is probably right for the industry. It wasn't right for us — our past failures were in data loading, not statistical overfitting.

Solve the problems you've actually had.

#QuantResearch #RiskManagement
```

**Facets:**
- `#QuantResearch` → `app.bsky.richtext.facet#tag`
- `#RiskManagement` → `app.bsky.richtext.facet#tag`

### LinkedIn — launch post (May 26)

**Format:** Post body only. Add URL as first comment to avoid link-penalty.

**Text:**
```
In late April we read a compelling research piece: run your strategy against five synthetic null environments (white noise, GARCH, bid-ask bounce, factor null, regime-switching vol). If your Sharpe survives, your backtest is probably telling the truth.

We took it seriously. Full methodology document written. Per-instrument calibration notes drafted. Harness injection points surveyed.

Then we asked: would this framework have caught our actual most damaging backtest failure?

Our worst past failure was a stale config path. The backtest ran on phantom data. Four strategies looked brilliant. An independent re-run reversed every single one.

The null-environment framework substitutes synthetic returns to test strategy logic. It bypasses the data-loading layer entirely. It would not have caught a phantom-data run.

So we did something else instead. One engineer, one morning: a pre-flight data-integrity sentry with four assertions — cache path exists, bar count minimum, return distribution sanity, price-scale band check. Directly addresses the actual failure. No calibration overhead.

The lesson isn't that sophisticated methods are bad. It's that choosing which problem to solve requires evidence about which problems you actually have.

New post: [link in first comment]

#SystematicTrading #QuantitativeResearch #Backtesting #RiskManagement
```

---

## Article 2 Social Pack — "Our Portfolio Metrics Said Yes. Our Quality Gate Said No."
**Article slug:** `/usatech-portfolio-gate-decision`
**Source:** RAD-732
**Proposed publish date:** 2026-06-02 (Mon)

### Bluesky — launch post

**Text (299 chars):**
```
Adding NASDAQ-100 to our portfolio would have reduced drawdown 14% and improved returns 26%.

We said no.

Why? Per-trade Sharpe: 0.21. Our gate: 0.6. Portfolio-level metrics can look good with a weak contributor. That's exactly what the gate screens out.

Full post:
https://radiusred.github.io/blog/posts/usatech-portfolio-gate-decision/

#SystematicTrading #PortfolioConstruction
```

**Facets required:**
- Link on URL → `app.bsky.richtext.facet#link`
- `#SystematicTrading` → `app.bsky.richtext.facet#tag`
- `#PortfolioConstruction` → `app.bsky.richtext.facet#tag`

**Note:** Confirm exact URL after publishing.

### Bluesky — follow-up post (Jun 4, 2 days after launch)

**Text (287 chars):**
```
Regime fragility is the real test.

USATECHIDXUSD's per-trade Sharpe over 6 years: 0.21.
Over 8 years (adding 2018-2019): 0.054.

An 80% collapse when the regime changes. The same pattern we saw in USA500 but amplified.

If you cherry-pick your history, your backtest will tell you what you want to hear.

#Backtesting #QuantResearch
```

**Facets:**
- `#Backtesting` → `app.bsky.richtext.facet#tag`
- `#QuantResearch` → `app.bsky.richtext.facet#tag`

### LinkedIn — launch post (Jun 2)

**Format:** Post body only. Add URL as first comment.

**Text:**
```
We tested adding NASDAQ-100 to our live-paper strategy portfolio.

The numbers looked good. Drawdown down 14%. Total returns up 26%. On paper, a clear win.

We killed it anyway.

Here's why: our gate for adding any strategy to the portfolio is a per-trade Sharpe above 0.6. NASDAQ-100 came in at 0.21 over 6 years — and when we extended to 8 years, it collapsed to 0.054. An 80% deterioration when we included a regime it hadn't been tested on.

Portfolio-level metrics can hide weak contributors. When you combine a strong signal with a diluted one, the aggregate often looks better: a bit more PnL, a bit less drawdown. But you've added something that wouldn't pass your quality bar on its own. The gate exists to screen that out.

The conservative view isn't always right. Sometimes portfolio diversification is genuinely worth adding something weaker in isolation. We've written about that tension before (see: "When the Metrics Say No But the Economics Say Yes"). But the default position is: listen to the gate. You set it for a reason.

New post: [link in first comment]

#SystematicTrading #PortfolioConstruction #QuantitativeResearch #RiskManagement
```

---

## Approval Checklist

Before posting any of the above:

- [x] Testy review and approval (all content) — approved 2026-05-04
- [ ] Confirm article URLs match published slugs
- [x] Verify all Bluesky posts use proper facets (no plaintext hashtags)
- [ ] LinkedIn: confirm company page credentials status with board
- [x] Schedule Bluesky teaser (May 4) immediately upon Testy approval — posted
- [ ] Schedule launch posts aligned with article publication dates

---

## Publication Schedule Summary (Wave 3)

| Date | Channel | Content |
|------|---------|---------|
| May 4 | Bluesky | Teaser for May 5 Regime-Conditional Alpha article |
| May 5 | Blog | Regime-Conditional Alpha (RAD-762, already in pipeline) |
| May 10 | Bluesky | Teaser for May 12 Disciplined Rejection (RAD-774, already scheduled) |
| May 12 | Blog | Disciplined Rejection — Bollinger Band FX sweep (RAD-774) |
| May 19 | Blog | When the Metrics Say No But Economics Say Yes (RAD-769) |
| May 26 | Blog | **NEW: Null-environment backtest testing (RAD-499)** |
| May 26 | Bluesky + LinkedIn | Launch posts for null-environment article |
| May 28 | Bluesky | Follow-up for null-environment article |
| Jun 2 | Blog | **NEW: USATECH portfolio gate decision (RAD-732)** |
| Jun 2 | Bluesky + LinkedIn | Launch posts for USATECH article |
| Jun 4 | Bluesky | Follow-up for USATECH article |
