def maxProfit(prices, n, k):
	pro= [[0 for i in range(k + 1)]
				for j in range(n)]
	for i in range(1, n):
		for j in range(1, k + 1):
			maxi= 0
			for l in range(i):
				maxi = max(maxi, prices[i] -prices[l] + pro[l][j - 1])
			pro[i][j] = max(pro[i - 1][j], maxi)
	return pro[n - 1][k]
k = 2
prices = [10,22,5,75,65,80]
n = len(prices)
print("Maximum profit is:",
	maxProfit(prices, n, k))
