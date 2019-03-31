import random
import math

def get_payout(play_num):
    total_sum = 0

    for i in range(play_num):
        total_sum += pow(2, i)

    return total_sum

observation_num = 100  #take 100 observations
observed_mean = 0
inner_u = []

for j in range(observation_num):
    total_number = 10000
    u = 0
    inner_iter_num = 100   #gambling 100 times

    for i in range(inner_iter_num):

        current_playing_num = 1
        while True:
            judging_wining = random.random() * 38

            if judging_wining <= 18:    #wining
                if current_playing_num == 1:
                    u += 1
                else:
                    u += pow(2, current_playing_num) - get_payout(current_playing_num)
                break
            
            else:                       #losing
                if get_payout(current_playing_num) >= total_number:
                    u -= total_number   #oops, already Tap out.
                    break
                current_playing_num += 1

    u = u / inner_iter_num
    observed_mean += u
    inner_u.append(u)

sum_of_square = 0

observed_mean /= observation_num

for i in range(observation_num):
    sum_of_square += pow((inner_u[i] - observed_mean), 2)

variance = 1/(observation_num - 1) * sum_of_square
deviation = math.sqrt(variance)

# calculate boundary for confidence interval
upper_bound_of_confidence_interval = observed_mean + 1.96 * deviation / math.sqrt(observation_num)
lower_bound_of_confidence_interval = observed_mean - 1.96 * deviation / math.sqrt(observation_num)

# count how many samples are in confidence interval
count_in = 0
for i in inner_u:
    if upper_bound_of_confidence_interval >= i and lower_bound_of_confidence_interval <= i:
        count_in += 1

print('There are ', count_in * 100 / observation_num, '% samples in the confidence interval')
print('With mean:', observed_mean)
