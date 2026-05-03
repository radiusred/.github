# The Filter Trap: How Conviction Filters Made a Bad Signal Look Good

## The pattern emerges

After the first two attempts to fill the US-session gap failed, a pattern was becoming clear: every strategy we tested on this timeframe and session window ran into the same wall. But we weren't ready to accept that the gap was structural. We had one more idea: maybe the signal was sound, but we just needed to filter it better.

Phase 5 research surfaced Opening Range Breakout (ORB) as the next candidate. ORB is conceptually clean: the first hour of the US session sets a range, and breakouts of that range often lead to sustained moves. It's a competitive strategy in the real world. It should work.

The first-pass backtests showed weak performance. The vast majority of our exits were time-stops, not profit-takes. The signal itself wasn't firing—it was stalling out. So we did what nearly every quant researcher does when a signal is weak: we added filters.

That decision taught us something important about how easy it is to mistake *less noise* for *more signal*.

## The hypothesis: a cleaner breakout signal

The initial system had no conviction filters. It simply traded breakouts of the first hour's range on major instruments during the US session window, and exited on time or profit targets.

Multiple conviction filters were added to the implementation, each targeting a known failure mode in basic breakout systems. The logic was sound. Each filter was addressing a real failure mode. And the backtests would show us whether the combination worked.

## Testing: in-sample success that vanished out-of-sample

We tested multiple configurations across two periods: discovery (in-sample) and validation (out-of-sample):
- Baseline system (no filters)
- System with all filters applied
- Instrument-specific variants
- Tighter variants with adjusted exits

In-sample, the filters did exactly what filters are supposed to do: trade count fell sharply, win rate improved, and the best-performing variants passed our discovery bar.

Then we ran the same configurations on out-of-sample data.

Every single configuration that passed in-sample reversed in validation. Win rate collapsed. Performance metrics went clearly negative. The "best performing" instrument also flipped—what worked in discovery became unprofitable in validation, and different instruments swapped performance ranking.

## Why it happened: filters on a signal with no edge

This is the filter trap. When you layer conviction filters onto a signal that doesn't actually have edge, you don't make the signal better. You make it more selective—and in-sample fitting, that selection looks like performance.

What the filters were really doing was removing noise, but not in the way that creates predictive edge. They were removing *trades*—specifically, the ones that the out-of-sample data would have punished us on anyway. In-sample, that looked like an improvement: fewer trades, higher win rate, better metrics.

Out-of-sample, we found out that the trades we removed in-sample were sampled at random from the population, and the ones we kept were the ones we just happened to be lucky with. The filters didn't have predictive power; they had *fit*.

## What this means

The US-session gap is not a signal-design problem. It's not a tuning problem. And it's not a conviction-filter problem. It's structural.

After three independent attempts using different strategy archetypes, we had tested the US session's microstructure from multiple angles and hit the same failure mode each time. The high reversal rate, the false starts, the validation collapse—these weren't accidents. They were the market telling us that the microstructure during those hours doesn't reward the strategies we know how to build.

## What changed after

We learned to check the *reason* a filter improved performance before trusting it.

Ask three questions:
1. Did the filter remove bad trades, or did it remove trades at random?
2. Does the filter have plausible forward-looking logic (e.g., "higher volume confirms the move"), or is it just a statistical coincidence?
3. Does the filter improve out-of-sample performance, or just in-sample Sharpe?

The second lesson was harder to swallow: sometimes the answer to "can we fill this gap?" is "no, not with these tools at this resolution." That's not the end of research. It's just a boundary condition. We now spend less time on architectures that are fighting the market's microstructure, and more time on markets and timeframes where our archetypes actually fit.

## What we published

- Phase 5 research: [RAD-346](/RAD/issues/RAD-346)
- Implementation: [RAD-348](/RAD/issues/RAD-348)

---

*Radius Red learns in public. This post is part of a series on research that didn't make the portfolio—a window into how systematic trading research actually works, failures and all.*

*Series: [The US-session gap is structural, not a tuning problem](/RAD/issues/RAD-643)*
