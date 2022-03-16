def fib(n):
	if n == 0:
		return 0
	if n==1 or n==2:
		return 1

	else:
		return fib(n-1) + fib(n-2)


def fibonacci():
  try:
    num = int(input("enter a number for fibonacci:"))
    assert num > 0 
    print("the", num, "number of the fibonacci sequence is", fib(num))
  except AssertionError :
    print("please input a positive value")
    fibonacci()

if __name__ == "__main__":
  fibonacci()