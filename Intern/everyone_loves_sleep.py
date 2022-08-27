def main():
	t = int(input())
	for i in range(t):
		n, h, m = input().split(" ")
		n, h, m = [int(n), int(h), int(m)]
		time = 60*h + m
		total = 24*60
		for i in range(n):
			h1, m1 = input().split()
			h1, m1 = [int(h1), int(m1)]
			currentTime = 60*h1 + m1
			sleepTime = 0
			if(currentTime < time):
				sleepTime = 24*60 + currentTime - time
			else:
				sleepTime = currentTime - time
			total = min(total, sleepTime)
		print(f"{total//60} {total%60}")

if(__name__ == "__main__"):
	main()
