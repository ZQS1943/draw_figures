import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Example data: Replace this with your actual data
# Let's assume we have 17 user cases, 30 attacker cases, and 5 models
user_cases = 17
attacker_cases = 30
models = 5

# Generate a random binary matrix for each model (replace this with your actual data)
# Shape of data: (user_cases, attacker_cases, models)
data = np.random.randint(2, size=(user_cases, attacker_cases, models))

# Aggregate the data: Sum the binary results across models for each test case
# Shape of aggregated_data: (user_cases, attacker_cases)
aggregated_data = np.sum(data, axis=2)

# Create the heat map
plt.figure(figsize=(14, 10))
sns.heatmap(aggregated_data, annot=True, cmap='viridis', cbar=True, 
            xticklabels=range(1, attacker_cases+1), yticklabels=range(1, user_cases+1))
plt.title('Attacker Success Rate Heatmap')
plt.xlabel('Attacker Cases')
plt.ylabel('User Cases')
plt.savefig('./heatmap.png', dpi=300)
