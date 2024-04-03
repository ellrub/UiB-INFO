# Exercise 1
# def detailed_knap_sack(capacity, weights, values, n):
def detailed_knap_sack(value, weights, max_capacity):
    grid = [[0 for x in range(max_capacity + 1)] for x in range(len(value) + 1)]

    for i in range(1, len(value) +1):
        for w in range(1, max_capacity + 1):
            if weights[i - 1] <= w:
                grid[i][w] = max(values[i - 1] + 
                                grid[i - 1][w - weights[i - 1]],
                                grid[i - 1][w])
            else:
                grid[i][w] = grid[i - 1][w]

    w = max_capacity
    n = len(values)
    items = []
    for i in range(n, 0, -1):
        if grid[i][w] != grid[i - 1][w]:
            items.append(weights[i - 1])
            w -= weights[i - 1]
    
    print(f'{grid[n][max_capacity]}$')
    print('Weights:', items)

values = [120, 200, 150, 350, 100, 90]
weights = [15, 20, 40, 50, 20, 10]
capacity = 100

print(f'Max value to put in knapsack of capasity {capacity}:')
detailed_knap_sack(values, weights, capacity)
