#include <iostream>  
#include <direct.h>  
#include <io.h>  
#include <fstream>  
#include <sstream>
using namespace std;

//http://www.cnblogs.com/summerRQ/articles/2375749.html

bool make_dir(const std::string& pathName)
{ 
	if (::_mkdir(pathName.c_str()) < 0)
	{
		std::cout << "create path error" << std::endl;
		return false;
	}
	return true;
}

void dfsFolder(string folderPath, string despath, ofstream &fout)
{
	_finddata_t FileInfo;
	string strfind = folderPath + "\\*";
	long Handle = _findfirst(strfind.c_str(), &FileInfo);

	if (Handle == -1L)
	{
		cerr << "can not match the folder path" << endl;
		exit(-1);
	}
	do{
		//判断是否有子目录
		if (FileInfo.attrib & _A_SUBDIR)
		{
			if ((strcmp(FileInfo.name, ".") != 0) && (strcmp(FileInfo.name, "..") != 0))
			{
				string newPath = folderPath + "\\" + FileInfo.name;
				string newdesPath = despath + "\\" + FileInfo.name;
				make_dir(newdesPath);
				dfsFolder(newPath, newdesPath, fout);
			}
		}
		else
		{
			string nowSrcFilePath = folderPath + "\\" + FileInfo.name;
			string newdesFilePath = despath + "\\" + FileInfo.name;
			std::ifstream in;
			in.open(nowSrcFilePath);
			if (!in)
			{
				std::cout << "open src file : " << nowSrcFilePath << " failed" << std::endl;
			}
			std::ofstream out;
			out.open(newdesFilePath);
			if (!out)
			{
				std::cout << "create new file : " << newdesFilePath << " failed" << std::endl;
				in.close();
			}
			out << in.rdbuf();
			out.close();
			in.close();
		}
	} while (_findnext(Handle, &FileInfo) == 0);

	_findclose(Handle);
	fout.close();
}

int main(int argc, char *argv[])
{ 
	string strfind = "F:\\git\\algorithm";
	string strdes = "F:\\git\\123";
	ofstream fout;
	dfsFolder(strfind,strdes, fout);
	return 0;
}