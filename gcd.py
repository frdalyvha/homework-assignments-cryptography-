def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)
print("Their greatest common dividor is",gcd(int(input("Enter the first number: ")),int(input("Enter the second number: "))))