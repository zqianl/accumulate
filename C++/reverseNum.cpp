#include <iostream>
#include<cstring>
#include<sstream>
#include<algorithm>
#include<vector>

using namespace std;
//这种方法只能完成int型数字，不够通用
int ReverseNum(int number)
{
	vector<int>vecNum;
	while (number != 0)
	{
		int remain = number % 10;
		vecNum.push_back(remain);
		number /= 10;
	}
	int sum = 0;
	for (unsigned int i = 0; i < vecNum.size(); ++i)
	{
		sum += vecNum[i] * (int)pow(10, vecNum.size() - 1 - i);
	}
	return sum;
}

//这种方法比较通用且写法简单
double ReverseNum1(double number)
{
	double revNum;
	char a[100];
	sprintf(a, "%f", number);
	_strrev(a);
	revNum = atof(a);  //从字符串转成double型，用这种方法
	return revNum;
}
//这种方法也比较通用且写法简单
double ReverseNum2(double number)
{
	double revNum;
	stringstream str;
	str << number;
	string s = str.str();
	reverse(s.begin(), s.end());
	revNum = atof(s.c_str());
	return revNum;
}

//转成int
int ReverseNum2(int number)
{
	int revNum;
	char a[100];
	sprintf(a, "%d", number);
	_strrev(a);
	//sscanf(a, "%d", &revNum);
	revNum = atoi(a);  //从字符串转成int型，两种方法等价
	return revNum;
}

int main(int argc, char **argv)
{
	double a = 12.34;
	double revA = ReverseNum3(a);
	cout << revA << endl;
	int b = 1234;
	int revB = ReverseNum2(b);
	cout << revB << endl;
	system("pause");
	return 0;
}

//总结：
//1.数字转成字符串
//这里两种方法均可，第二种写法较为简单
//sprintf atoi sscanf接受的字符串参数均为字符指针，但由于字符数组可以直接赋值给字符指针，
//因此，字符数组也是完全没问题的  注意sscanf处理double时会出错
#include <iostream>  
#include <sstream>  

using namespace std;

int main()
{
	double number = 12.34;
	//方法1：string的思路
	//stringstream str;
	//str << number;
	//string s = str.str();
	//cout << s << endl;

	//const char *b = s.c_str();
	//cout << b << endl;

	//char a[100];
	//sprintf(a, "%s", b);
	//cout << a << endl;

	//方法2：
	char a[100];
	sprintf(a, "%.2f", number);
	cout << a << endl;

	string s = a;
	cout << s << endl;

	char *b = a;
	cout << b << endl;
	return 0;
}

//2.字符串转成数字
//虽有三种方法，第二种速度较快且写法最简单，可以处理string，char *,char a[]三种类型
#include <iostream>  
#include <sstream>  

using namespace std;

int main()
{
	string s="12.34";
	//方法1：string的思路
	stringstream str(s);
	float number;  //float和double都对
	str >> number;
	cout << number << endl;

	//方法2：
	double number = atof(s.c_str()); //格式本身是double，可以转成float
	cout << number << endl;

	//方法3：
	float number;//这里用float是正确的，但是用double就不对了
	sscanf(s.c_str(), "%f", &number);
	cout << number << endl;

	return 0;
}

//总结：
//字符串、字符数组与字符指针之间的转化关系
string s = “12qwe”;
char* str = ",";
char a[] = “qrew”;

char* str = "123";
string s = str; //正确
char s[] = str; //错误  

string s = “123”；
const char *str = s.c_str(); //正确。注意s.c_str()是带有const属性的，因此char *str = s.c_str(); 是错误的
char a[] = s; //错误  加上常量属性也不对

char a[] = "1,b";
string s = a; //正确  但是反过来就是错误的
char *p = a; //正确

//string 和char *赋给char a[]的办法：
string s2 = "34";
const char *c2 = s2.c_str();
char s1[20];
sprintf(s1, "%s", c2);  //这么做的意义在于：字符串相较或比较等必须保证第一个为字符数组才行，字符串指针不行

