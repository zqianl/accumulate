//һ����Сд��ĸ��ɵ��ַ������Կ���һЩͬһ��ĸ�������Ƭ��ɵġ�
//����,"aaabbaaac"����������Ƭ��ɵ�:'aaa','bb','c'��ţţ���ڸ���һ���ַ���,
//���������������ַ�����������Ƭ��ƽ�������Ƕ��١�

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

	//������ȵĿ��ƣ�С�����λ
	cout << setiosflags(ios::fixed);
	cout.precision(2); 
	cout << result << endl;

	////��һ�־��ȿ��Ʒ���
	//char str[20];
	//sprintf(str, "%.2f", result);
	//cout << str << endl;

	return 0;
}