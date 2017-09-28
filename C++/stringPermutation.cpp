#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
	string str;
	cin >> str;
	sort(str.begin(), str.end());
	cout << str << endl;
	while (next_permutation(str.begin(), str.end()))
	{
		cout << str << endl;
	}
	return 0;
}

//#include <cstdio>
//#include <algorithm>
//#include <cstring>
//#define MAX 100
//
//using namespace std;
//
//int main()
//{
//	int length;
//	char str[MAX];
//	gets(str);
//	length = strlen(str);
//	sort(str, str + length);
//	puts(str);
//	while (next_permutation(str, str + length))
//	{
//		puts(str);
//	}
//	return 0;
//}