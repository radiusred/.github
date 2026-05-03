# Social Media Pack — US-Session Gap Three-Article Series

Status: Ready for Testy review and approval
Source: Quanty source packs (RAD-644)
Target: Bluesky + LinkedIn
Timeline: Publish articles on three consecutive days (Mon/Tue/Wed or similar); space social posts across day-of and day+1

---

## Article 1: Spike-Fade and Naive Breakouts

### Bluesky — Lead Post (Day 0)

Type: Thread with link

Post 1:
```
Our mean-reversion portfolio sits dormant for 9 out of every 24 hours.

So early on, we asked: can we harvest momentum alpha during US session hours the same way we harvest mean-reversion alpha during European quiet?

First attempt: a breakout strategy. Seemed obvious.

It wasn't. Here's what we learned: [link to blog article]
```

Facets: `#SystematicTrading`, `#QuantResearch`

Post 2 (reply thread):
```
Result: the strategy was generating trades, but the "breakout" candle was often the entire move.

The next bars frequently retraced back through the entry.

Microstructure doesn't lie. And the microstructure of the US session says something important about why we still have that gap.
```

### LinkedIn — Lead Post (Day 0)

Link placement: First comment (not in main post)

Post:
```
The easiest gap in a trading portfolio is the one nobody wants to fill.

Ours was obvious: most of our portfolio alpha came from a short, quiet European window. The rest of the day was noise we were trying to avoid.

Except we weren't supposed to avoid it forever. So we tested: can we harvest trend-following alpha during the US session the same way we harvest mean-reversion alpha at open?

First attempt was a momentum breakout strategy. The logic was sound. The execution was not.

The breakout candle was often the entire move. The next bars retraced it. Many trades hit the stop without reaching targets.

This is what microstructure mismatch looks like. It's not a tuning problem. It's not a signal-design problem. It's a "this market moves in a way your strategy wasn't built to handle" problem.

We documented it anyway. 

The full story is in the comments: [link]. It's the first of three.

#SystematicTrading #ResearchProcess #OpenSource #Trading
```

### Follow-up Social Post (Day 1 or 2)

Bluesky:
```
One research rule: microstructure fit comes before tuning.

A strategy isn't a tuning problem until you confirm it's hitting the right kind of market event.

We learn that lesson multiple times. [link to next article]
```

LinkedIn:
```
Not every failure is a tuning problem.

Sometimes a strategy is hitting the wrong market-time-resolution combination, and no amount of parameter adjustment is going to fix that.

That's not the end of research. That's where real research begins.
```

---

## Article 2: Donchian Channels on Gold

### Bluesky — Lead Post (Day 1)

Type: Thread with link

Post 1:
```
After our first attempt to fill the gap failed, we took a step back. The board ran a ChatGPT research sweep.

Three candidates came back. The most promising: Donchian Channel Breakout on Gold.

Gold is supposed to trend. Channel breakouts are supposed to capture trends.

Seemed obvious.

[link to article]
```

Facets: `#SystematicTrading`, `#QuantResearch`

Post 2 (reply):
```
Both variants failed our initial performance bar.

Not marginal fails. Every metric was clearly negative.

Same market. Same archetype. Different timeframe = different microstructure.
```

### LinkedIn — Lead Post (Day 1)

Link placement: First comment

Post:
```
Gold trends. Donchian channels are built for trends.

So when the board suggested testing Donchian Channel Breakout on Gold to fill our US-session gap, it seemed like the obvious move.

Both variants failed in discovery testing.

And here's the lesson: the fact that Gold trends on higher timeframes tells you almost nothing about whether it has the right microstructure for a channel breakout during specific market hours.

Trend-following is real. The archetype is sound. But market + timeframe + session hours is a three-variable problem, and we were only thinking about the first one.

Full report: [link]

#SystematicTrading #ResearchProcess #MarketMicrostructure
```

---

## Article 3: ORB Filter Stacking

### Bluesky — Lead Post (Day 2)

Type: Thread with link

Post 1:
```
After two consecutive failures to fill the US-session gap, we had one more idea.

Maybe the signal was sound but weak. Maybe we just needed to filter it better.

We tested Opening Range Breakout with multiple conviction filters layered on top.

In discovery: it worked.

In validation: it didn't.

Here's why: [link to article]
```

Facets: `#QuantResearch`, `#SystematicTrading`

Post 2 (reply):
```
This is the filter trap.

When you add conviction filters to a signal with no real edge, you're not making the signal better. You're fitting noise.

Fewer trades. Better-looking metrics. Improved performance.

All of it collapses in validation because the filters weren't removing bad trades — they were removing trades at random.
```

### LinkedIn — Lead Post (Day 2)

Link placement: First comment

Post:
```
Here's the trap that catches most quant researchers at least once.

When a signal is weak (marginal performance, lots of false starts), you add filters. More conviction. More selectivity.

And it works. In discovery.

In discovery, the filters do exactly what they're supposed to do: trade count falls, metrics improve, performance looks better.

You move to validation.

Everything reverses.

What happened? You didn't build a better signal. You built a *more selective* signal—and in discovery, that selection was biased by luck. In validation, the same filters that looked good before now just reduce trade count without adding edge.

This is how you end up publishing a strategy that passed discovery and failed in real trading.

We tested this specific sequence three different ways (different strategy archetypes) on the same market-time-resolution combo and hit the same wall every time.

The lesson: the US-session gap isn't a signal problem. It's a microstructure problem.

Full series:
- Article 1: [link]
- Article 2: [link]
- Article 3: [link]

#QuantResearch #SystematicTrading #ResearchProcess
```

### Series Conclusion Post (Day 3 or later)

Bluesky:
```
Three attempts to fill a gap. Three different archetypes. Same failure mode.

The US session's microstructure doesn't reward trend-following breakout strategies, at least not at the timeframes and session windows we were working with.

That's not a tuning problem. That's a boundary condition.

And that's how real research works.
```

LinkedIn:
```
Three independent research directions. Three different strategy archetypes. Three out-of-sample failures.

All of them hit the same wall: the US session's microstructure isn't built for the strategies we tested.

Not because the strategies are bad. Not because we chose the wrong instruments. Not because we need to tune harder.

Because that specific market-time-session combination has characteristics that don't reward these approaches, and the more you filter to try to catch the "right" signals, the more you're just fitting noise.

Knowing where your strategies *don't* work is just as important as knowing where they do.

#QuantResearch #SystematicTrading #TradingResearch
```

---

## Scheduling Notes

- **Don't post all three on the same day.** Spread them over 2-3 days to maintain reader engagement and avoid over-saturation.
- **Space LinkedIn and Bluesky.** Publish Bluesky link post on day of article publish. Publish LinkedIn post same day or day+1.
- **Use facet tags on Bluesky.** All posts use `#SystematicTrading` and `#QuantResearch` facets (not plain text tags).
- **Keep links in LinkedIn comments.** Main LinkedIn posts should be link-free; place article URLs in the first company-page comment for cleaner formatting.
- **Follow-up posts are optional.** Only post follow-up social if timing feels right. Better to skip a post than to force content.

---

## Approval Checklist

- [ ] Testy review and approval complete
- [ ] Article URLs finalized and embedded in social drafts
- [ ] LinkedIn company-page credentials confirmed ready
- [ ] Publish schedule decided by board (which days, which platforms)
- [ ] All posts checked for Bluesky facet formatting
