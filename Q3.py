import Model as Model
NUMBER_GAMES = 1000 # number of games within each simulation
NUMBER_FLIPS = 20 # number of coin flips within each game
HEADS_PROB = 0.5 # probability of heads

# Create games
Money = Model.Simulation(1, NUMBER_GAMES, HEADS_PROB)
# Simulate games
MoneyOutcomes = Money.simulate(NUMBER_FLIPS)

print('The casino owner estimates are a steady-state simulation because he can play unlimited times')
print('Therefore, estimated payout is', MoneyOutcomes.get_expected_payout())
print('95% Confidence Interval is', MoneyOutcomes.get_payout_t_CI_(0.05))

number_GAMES = 10
number_FLIPS = 20
heads_PROB = 0.5
NUM_SIM_COHORTS = 1000
ALPHA = 0.05

multiSim = Model.MultiSim(
    ids= range(NUM_SIM_COHORTS),
    number_games= [number_GAMES] * NUM_SIM_COHORTS,
    heads_prob= [heads_PROB] * NUM_SIM_COHORTS
)
# Simulate all
multiSim.simulate(number_FLIPS)

# print projected mean payout
print('The gambler is a transition-state simulation because of a small number of observations')
print('The estimated payout is', multiSim.get_overall_mean_payouts())
print('95% projection interval is', multiSim.get_PI_mean_payouts(ALPHA))
