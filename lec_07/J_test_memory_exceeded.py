# Get the number of days
num_days = int(input())

# Create  3 lists to store start and stop indices and colors
start_indices = list()
stop_indices = list()
colors = list()

# Get start, stop indices and color and append to corresponding list
for i in range(num_days):
    start_indices.append(int(input()))
    stop_indices.append(int(input()))
    colors.append(int(input()))

query_size = int(input())
queries = list()
for _ in range(query_size):
    queries.append(int(input()))

# Define the maximum size of the fence (add +1 to account for starting at 0)
max_size_fence = max(stop_indices) + 1

# List of colors for the entire fence
fence = [-1] * max_size_fence

# Populate the fence with corresponding colors
for k in range(num_days):
    for index in range(stop_indices[k] - start_indices[k] + 1):
        fence[start_indices[k] + index] = colors[k]

for query in queries:
    print(fence[query], end=" ")
