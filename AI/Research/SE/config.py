# Training:

training_step = 5000
batch_size = 150
# display log:
showstep = 500
#-------------------------

# CCU configs:

# Use CCU:
use_CCU = True
# number of iterations before self-evolution:
CCU_gap = 250 
# Number of operations:
CCU_number_of_choices = 3
# Number of features used in CCU:
CCU_Atten_features = 6
#-------------------------

# Model config:

# Drop out rate:
hidden_unit = 128
drop_out = 0.15
init_layers = 1

threshold = 0.15
warm_up = 2000
