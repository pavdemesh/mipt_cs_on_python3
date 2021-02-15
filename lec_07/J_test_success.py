# Get the number of days
num_days = int(input())

# Create  a list to store input data
coloring_data = list()

# Get start, stop indices and color and append to corresponding list
for i in range(num_days):
    start_index = int(input())
    stop_index = int(input())
    color = int(input())
    coloring_data.append([start_index, stop_index, color])

coloring_data.reverse()

query_size = int(input())

for i in range(query_size):
    plate_query = int(input())
    for color_set in coloring_data:
        if color_set[0] <= plate_query <= color_set[1]:
            print(color_set[2], end=" ")
            break
