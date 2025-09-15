import axelrod as axl
players = [s() for s in axl.axelrod_first_strategies]
tournament = axl.Tournament(players, turns=200, repetitions=5)
results = tournament.play()

# Output the rankings
print("Tournament Results Rankings:")
print("=" * 40)
for i, (player, score) in enumerate(results.ranking):
    print(f"{i+1}. {player}: {score:.3f}")
