from bisect import bisect_right

def jobScheduling(startTime, endTime, profit):
    # Combine the job details and sort by end time
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    n = len(jobs)

    # dp array to store maximum profit at each step
    dp = [0] * (n + 1)

    # Extract job details
    starts = [job[0] for job in jobs]
    ends = [job[1] for job in jobs]
    profits = [job[2] for job in jobs]

    for i in range(1, n + 1):
        # Binary search to find the latest non-overlapping job
        idx = bisect_right(ends, starts[i - 1]) - 1

        # Include current job profit + dp of the last non-overlapping job
        include_profit = profits[i - 1] + dp[idx + 1]

        # Exclude current job
        exclude_profit = dp[i - 1]

        # Store the maximum profit
        dp[i] = max(include_profit, exclude_profit)

    return dp[-1]

startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]

print(jobScheduling(startTime, endTime, profit))
