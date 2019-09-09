list = [1,1]
def fib(n):
	if n > len(list)-1:
		list.append(fib(n-1) + fib(n-2))
	return list[n]



print(fib(10))
