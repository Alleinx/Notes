import numpy as np
import matplotlib.pyplot as plt

age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]
fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]


print('For age:')
print(np.mean(age))
print(np.std(age, ddof=1))

print('For fat:')
print(np.mean(fat))
print(np.std(fat, ddof=1))

labels = ['age', '%fat']
print(labels)
plt.boxplot([age, fat], labels=labels)
plt.show()
colors = np.random.rand(len(age))
plt.scatter(age, fat, c='orange')
plt.xlabel('age')
plt.ylabel('%fat')
plt.show()

# -------------------------------
# qq plot
def normalize(x):
    """
    Used in QQ plot, normalize all the data first.
    """
    max_num = max(x)
    min_num = min(x)
    inter= max_num - min_num
    return [(data - min_num)/inter for data in x]
    
import statsmodels.api as sm

age_norm = normalize(age)
fat_norm = normalize(fat)

sm.qqplot_2samples(np.asarray(age_norm), np.asarray(fat_norm), xlabel='age', ylabel='fat', line='45')
plt.show()

# -------------------------------
# For Q6 :)
def cosine_similarity(x,y):
    x = np.asarray(x)
    y = np.asarray(y)

    numerator = np.dot(x,y)
    sqrt_x = np.sqrt(sum(x ** 2))
    sqrt_y = np.sqrt(sum(y ** 2))

    return numerator / (sqrt_x * sqrt_y)

def euclidean_distance(x, y):
    result = 0
    for i in range(len(x)):
        result += (x[i]-y[i]) ** 2
    
    return np.sqrt(result)

def correlation(x,y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    temp = 0
    for i in range(len(x)):
        temp += (x[i] - mean_x) * (y[i] - mean_y)
    
    # Note: here we use n on the denominator instead of n-1.
    cov_x_y = temp / len(x)

    # Note: here we use n on the denominator, instead of n-1.
    std_x = np.std(x)
    std_y = np.std(y)
    
    # If 0 on denominator
    if std_x == 0 or std_y == 0:
        return '{} / ({}*{}), undefined'.format(cov_x_y, std_x, std_y)
    
    corr_x_y = cov_x_y / (std_x * std_y)
    return corr_x_y

def jaccard(x, y):
    total = len(x)
    count_0_0 = 0
    count_1_1 = 0

    for i in range(len(x)):
        if x[i] == 0 and y[i] == 0:
            count_0_0 += 1
        if x[i] == 1 and y[i] == 1:
            count_1_1 += 1
    
    return count_1_1 / (total - count_0_0)


if __name__ == "__main__":
    x = [0,1,0,1]
    y = [1,0,1,0]

    print('x:', x, 'y:', y)
    print('cosine similarity:', cosine_similarity(x, y))
    print('Euclidean distance:', euclidean_distance(x, y))
    print('correlation:', correlation(x, y))
    print('Jaccard:', jaccard(x, y))