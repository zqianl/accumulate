#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>

using namespace std;

void strReplace(string &str, const char &str1, const char &strRe)
{
	replace(str.begin(), str.end(), str1, strRe);
}

int main()
{
	string str;
	getline(cin,str);
	char str1 = ' ';
	char strRe = '%';
	strReplace(str, str1, strRe);
	cout << str << endl;
	return 0;
}
 
