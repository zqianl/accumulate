//一个由小写字母组成的字符串可以看成一些同一字母的最大碎片组成的。
//例如,"aaabbaaac"是由下面碎片组成的:'aaa','bb','c'。牛牛现在给定一个字符串,
//请你帮助计算这个字符串的所有碎片的平均长度是多少。

#include<iostream>
#include<vector>
#include<string>
#include<iomanip>

using namespace std;

int main(int argc, char **agrv)
{
	string s;
	cin >> s;
	if (s.empty())
	{
		cout << "Invalid parameter!" << endl;
		return 0;
	}
	vector<int>midResult;
	double result = 0;
	int count = 1;
	char currChar = *s.begin();
	if (s.size()>1)
	{
		for (auto c = s.begin() + 1; c != s.end(); ++c)
		{
			if (*c == currChar)
				count += 1;
			else
			{
				midResult.push_back(count);
				currChar = *c;
				count = 1;
			}
		}
		midResult.push_back(count);
		for (auto i = midResult.begin(); i<midResult.end(); ++i)
			result += *i;
		result /= midResult.size();
	}
	else
		result = 1;

	//输出精度的控制，小数点后几位
	cout << setiosflags(ios::fixed);
	cout.precision(2); 
	cout << result << endl;

	////另一种精度控制方法
	//char str[20];
	//sprintf(str, "%.2f", result);
	//cout << str << endl;

	return 0;
}