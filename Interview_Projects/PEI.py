# Given conversion rates from two different groups, write a function to perform a t-test to determine 
# if there is a statistically significant difference between the two groups.
import numpy as np
from scipy.stats import ttest_ind
# Sample data
group_a = np.random.binomial(1, 0.3, 100)
group_b = np.random.binomial(1, 0.35, 100)

ttest_ind = 