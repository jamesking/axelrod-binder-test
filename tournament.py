import axelrod as axl
players = [s() for s in axl.axelrod_first_strategies]
tournament = axl.Tournament(players, turns=200, repetitions=5)
results = tournament.play()

# Output the rankings
print("Tournament Results Rankings:")
print("=" * 40)
for rank, player_index in enumerate(results.ranking):
    player = players[player_index]
    score = results.normalised_scores[player_index]
    print(f"{rank+1}. {player}: {score[0]:.3f}")
