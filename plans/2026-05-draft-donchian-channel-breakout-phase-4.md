# Textbook Trend-Following on the Wrong Instrument: Why Donchian Channels Failed on Gold

## Why the board suggested Donchian

After our first attempt to fill the US-session gap failed, the board ran a ChatGPT research sweep to get independent strategy recommendations. Three candidates came back: ADX-Gated Session Breakout, NY Open Intraday Momentum, and Donchian Channel Breakout.

Of the three, Donchian looked the most promising. Trend-following on commodities is a well-studied archetype, and Gold is the textbook example of a market that trends persistently enough to reward channel breakouts. The Donchian Channel itself is elegant: it simply trades the breakout of the highest high and lowest low over a lookback period, assuming that any genuine trend will push into new N-bar territory.

It seemed obvious. Gold was supposed to be the answer.

## The hypothesis: harvest trends on the right instrument

The intuition was straightforward. Unlike the equity index and FX pairs we'd tested before, Gold is designed to trend. It's a safe-haven asset that responds to macro shocks, geopolitical events, and policy shifts with sustained directional moves. A channel breakout—trading the first breakout of a range—should capture the opening of those moves.

We tested multiple configurations across different timeframes and parameter settings to find the combination that would work best on this instrument.

## Testing: both variants failed

The discovery period covered several years of intraday data with spread-aware fills.

Both variants failed our initial performance bar. The faster variant was unprofitable across all metrics, generating many round trips with poor returns. The slower variant was less bad but still failed.

The relationship between the two variants was revealing: slowing the approach down made it *less bad*, not *good*. There was no nearby parameter adjustment that would have fixed it.

## Why it failed: microstructure doesn't trend

This was harder to understand than the first failure. Gold *does* trend on higher timeframes. The asset class *is* designed for trend-following. But the intraday microstructure at the timeframe and session hours we needed doesn't exhibit the kind of sustained directional moves that this approach requires.

What we were seeing was exactly the kind of behavior that kills breakout systems: many small reversions, fewer large trends, and a high proportion of false starts that never develop into sustained moves.

The issue wasn't the asset or the archetype. It was the specific combination: the asset, the timeframe, and the session window. Longer timeframes might have shown different behavior. Different session windows might have shown different behavior. But in the exact market-time-resolution combination we needed, this strategy archetype didn't have edge.

## What changed after

We added another layer to our research process: validate not just the strategy archetype, but the *market-timeframe-session combination* it's supposed to work on.

Gold is a trend-following market. Donchian channels are a trend-following strategy. But the conjunction of Gold + intraday resolution + US session hours didn't produce the Donchian edge in the data. We could have spent weeks tuning parameters, adding filters, or trying different exit logic. Instead, we documented the microstructure mismatch and moved on.

Later, when every Phase 4 and Phase 5 candidate we tested on the US session hit the same wall, we started to see a pattern. The gap wasn't about the specific strategy. It was about the microstructure of the market during those hours.

## What we published

- Full technical report: [RAD-320](/RAD/issues/RAD-320)
- Implementation report: [RAD-344](/RAD/issues/RAD-344)

---

*Radius Red learns in public. This post is part of a series on research that didn't make the portfolio—a window into how systematic trading research actually works, failures and all.*

*Series: [The US-session gap is structural, not a tuning problem](/RAD/issues/RAD-643)*
