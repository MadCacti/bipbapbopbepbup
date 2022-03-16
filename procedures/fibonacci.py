def fib(n):
	if n < 0:
		print("Cannot be negative number")

	if n == 0:
		return 0
	if n==1 or n==2:
		return 1

	else:
		return fib(n-1) + fib(n-2)


def fibonacci():
    num = int(input("enter a number for fibonacci:"))
    if num < 0:
        print("please input a positive value")
    else:
        print("the", num, "number of the fibonacci sequence is", fib(num))

if __name__ == "__main__":
   fibonacci()