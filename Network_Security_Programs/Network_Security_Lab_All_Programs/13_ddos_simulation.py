capacity = 100
legit_clients = 10
legit_rate = 4
bots = 20
bot_rate = 50
limit = 5

def run(title, attack, defence):
    print("---", title, "---")
    print("Sec | Legit sent | Legit served | Attack requests | Blocked bots")
    blocked = 0
    total_sent = 0
    total_served = 0
    for sec in range(1, 11):
        legit = legit_clients * legit_rate
        attack_requests = 0
        if attack:
            if defence and sec > 3:
                blocked = bots
            if defence:
                attack_requests = (bots - blocked) * limit
            else:
                attack_requests = bots * bot_rate
        total = legit + attack_requests
        if total <= capacity:
            served = legit
        else:
            served = int(capacity * legit / total)
        total_sent += legit
        total_served += served
        print("%3d | %10d | %12d | %15d | %12d" % (sec, legit, served, attack_requests, blocked))
    print("Legitimate requests served: %d/%d (%.1f%%)\n" % (total_served, total_sent, total_served / total_sent * 100))

run("Normal traffic (no attack)", False, False)
run("DDoS: 20 bots x 50 req/s, no defence", True, False)
run("DDoS: 20 bots x 50 req/s, rate limit + blacklist", True, True)
