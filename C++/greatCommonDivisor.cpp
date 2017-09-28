#include <iostream>

using namespace std;

//gcd(a,b) = gcd(b,a mod b) 

int greatCommonDivisor(int x, int y)
{
	int z = y;
	while (x%y != 0)
	{
		z = x%y;
		x = y;
		y = z;
	}
	return z;
}

int greatCommonDivisor1(int a, int b)
{
	while (a != b)
	{
		if (a>b)
			a = a - b;
		else
			b = b - a;
	}
	return a;
}

int greatCommonDivisor2(int x, int y)
{
	int temp = 0;
	for (temp = x;; temp--)
	{
		if (x%temp == 0 && y%temp == 0)
			break;
	}
	return temp;
}

int main(int argc, char **argv)
{
	int a = 10;
	int b = 20;
	int result = greatCommonDivisor(a, b);
	cout << result << endl;
	return 0;
}

//多个数字的最大公约数
#include <iostream>
using namespace std;

int Partition(int a, int b){
	if (b == 0)
		return a;
	return Partition(b, a % b);
}

int Start(int a[], int q){
	if (q>0){
		a[q - 1] = Partition(a[q - 1], a[q]);
		return Start(a, q - 1);
	}
	return a[0];
}

int main()
{
	int a[4] = { 12, 24, 30, 36 };
	cout << Start(a, 3);
	return 0;
}