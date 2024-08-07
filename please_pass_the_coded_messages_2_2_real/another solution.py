def largest_group_divisible_by_three(numbers):
    n = len(numbers)

    dp = [[None for _ in range(3)] for _ in range(n + 1)]
    dp[0][0] = []

    for i in range(1, n + 1):
        for j in range(3):
            if dp[i - 1][j] is not None:
                if dp[i][j] is None or len(dp[i][j]) < len(dp[i - 1][j]):
                    dp[i][j] = dp[i - 1][j].copy()

            prev_mod_sum = (j - numbers[i - 1]) % 3
            if dp[i - 1][prev_mod_sum] is not None:
                new_subset = dp[i - 1][prev_mod_sum] + [numbers[i - 1]]

                if dp[i][j] is None or len(new_subset) > len(dp[i][j]):
                    dp[i][j] = new_subset

    return dp[n][0] if dp[n][0] is not None else []
