#include<iostream>
#include<vector>
#include<string>
#include<set>

using namespace std;

vector<string> StringSplit(const string &str, const set<char> &targetChar)
{
	vector<string>strSplit;
	string::const_iterator subStrBegin = str.begin();
	bool flagEndTarget = false;
	for (auto i = str.begin(); i != str.end(); ++i)
	{
		if (targetChar.find(*i) != targetChar.end())
		{
			if (i != subStrBegin)
			{
				string midStr(subStrBegin, i);
				strSplit.push_back(midStr);
			}
			if (i != str.end() - 1)
				subStrBegin = i + 1;
			else
				flagEndTarget = true;
		}
	}
	if (flagEndTarget == false)
	{
		string midStr(subStrBegin, str.end());
		strSplit.push_back(midStr);
	}
	return strSplit;
}

int main(int argc, char **argv)
{
	//string str{ "|qwer.sdf..xcv||.|rwer||." };
	string str{ "|q.." };
	set<char> targetChar{ '|', '.' };
	vector<string>strSplit = StringSplit(str, targetChar);
	for (auto i = strSplit.begin(); i != strSplit.end(); ++i)
		cout << *i << endl;
	return 0;
}