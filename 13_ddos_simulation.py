# Experiment 13: DDoS Attack Simulation (discrete network/server model)
# Models a server with limited capacity and a finite request queue, receiving
# traffic from legitimate clients and (optionally) a botnet, with and
# without a rate-limiting / blacklisting defence.
import random

CAPACITY   = 100      # requests the server can process per second
QUEUE_SIZE = 200      # maximum waiting requests
LEGIT      = 10       # legitimate clients
LEGIT_RATE = 4        # requests / second / legitimate client
DURATION   = 10       # seconds simulated

def simulate(bots, bot_rate, defence, seed=1):
    rng = random.Random(seed)
    queue, blocked, strikes = [], set(), {}
    sent = served = 0
    rows = []
    for sec in range(1, DURATION + 1):
        arrivals = [("L%d" % i, True) for i in range(LEGIT) for _ in range(LEGIT_RATE)]
        arrivals += [("B%d" % i, False) for i in range(bots) for _ in range(bot_rate)]
        sent_now = sum(1 for _, ok in arrivals if ok)
        sent += sent_now
        if defence:                                  # per-source rate limit + blacklist
            count, allowed = {}, []
            for src, ok in arrivals:
                if src in blocked:
                    continue
                count[src] = count.get(src, 0) + 1
                if count[src] <= 5:
                    allowed.append((src, ok))
            for src, c in count.items():
                strikes[src] = strikes.get(src, 0) + 1 if c > 5 else 0
                if strikes[src] >= 3:
                    blocked.add(src)
            arrivals = allowed
        rng.shuffle(arrivals)
        for req in arrivals:
            if len(queue) < QUEUE_SIZE:
                queue.append(req)
        done, queue = queue[:CAPACITY], queue[CAPACITY:]
        ok_now = sum(1 for _, ok in done if ok)
        served += ok_now
        rows.append((sec, sent_now, ok_now, len(queue), len(blocked)))
    return sent, served, rows

def report(title, bots, bot_rate, defence):
    sent, served, rows = simulate(bots, bot_rate, defence)
    print(f"--- {title} ---")
    print("Sec | Legit sent | Legit served | Queue | Blocked IPs")
    for r in rows:
        print(f"{r[0]:3d} | {r[1]:10d} | {r[2]:12d} | {r[3]:5d} | {r[4]:5d}")
    print(f"Legitimate requests served: {served}/{sent} ({served / sent * 100:.1f}%)\n")

report("Normal traffic (no attack)", 0, 0, False)
report("DDoS: 20 bots x 50 req/s, no defence", 20, 50, False)
report("DDoS: 20 bots x 50 req/s, rate limit + blacklist", 20, 50, True)
