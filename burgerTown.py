def max_happiness(N, restaurants):
    # Sort restaurants based on their position (X)
    restaurants.sort()

    # Dictionary to store max happiness at each position
    dp = {}

    # Try starting at each restaurant
    max_happy = 0

    for i in range(N):
        x, a, b = restaurants[i]

        # Initialize max happiness at this position as the burger happiness
        dp[x] = a

        # Check all previous restaurants to see if moving from them gives a better result
        for j in range(i):
            prev_x, prev_a, prev_b = restaurants[j]

            # Happiness from previous restaurant + burger happiness - sadness from looking at windows
            happiness = dp[prev_x] + a - sum(restaurants[k][2] for k in range(j + 1, i))

            # Store max happiness at this position
            dp[x] = max(dp[x], happiness)

        # Update the overall max happiness
        max_happy = max(max_happy, dp[x])

    # Return max happiness or 0 if all values are negative
    return max(0, max_happy)


# Taking user input
N = int(input("Enter the number of restaurants: "))

restaurants = []
print("Enter X (position), A (burger happiness), B (sadness from looking at windows) for each restaurant:")
for _ in range(N):
    x, a, b = map(int, input().split())
    restaurants.append((x, a, b))

# Call the function and print the result
print("Maximum Happiness:", max_happiness(N, restaurants))
