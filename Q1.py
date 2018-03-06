import Model as Model

NUMBER_GAMES = 1000 # number of games within each simulation
NUMBER_FLIPS = 20 # number of coin flips within each game
HEADS_PROB = 0.5 # probability of heads

# Create games
Money = Model.Simulation(1, NUMBER_GAMES, HEADS_PROB)

# Simulate games
MoneyOutcomes = Money.simulate(NUMBER_FLIPS)

# print the average payout
print('Expected payout:', MoneyOutcomes.get_expected_payout())
print('95% t-based CI', MoneyOutcomes.get_payout_t_CI_(0.05))

# print the loss probability
print('Probability of loss', MoneyOutcomes.get_probability_of_loss())
print('95% t-based CI of loss:', MoneyOutcomes.get_probability_t_CI(0.05))

