#include<string>
#include<iostream>
#include <fstream>
#include<sstream> 

using namespace std;

int main()
{
	ifstream in("charSplit.txt");
	ofstream out1("3.txt");
	ofstream out2("4.txt");
	string line;
	int numLine = 0;
	while (getline(in, line))
	{
		int i = 0;
		for (auto &c : line)
		{
			if (c == 120)
			{
				++i;
				break;
			}
		}
		if (i == 1)
		{
			for (auto &c : line)
			{
				switch (c){
				case 120:c = 32; break;
				case 58:c = 32; break;
				case 121:c = 32; break;
				case 116:c = 32; break;
				case 104:c = 32; break;
				default:;
				}
			}
			istringstream text(line);
			string word;
			int j = 0;
			while (text >> word)
			{
				if (j != 0 && j != 3)
				{
					if (numLine % 2 == 0)
						out1 << word << " ";
					else
						out2 << word << " ";
				}
				++j;
			}
			if (numLine % 2 == 0)
				out1 << endl;
			else
				out2 << endl;
		}
		++numLine;
	}
	return 0;
}