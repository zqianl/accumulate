#include <iostream>  
#include "copyDir.h"  
using namespace std;

int main(int argc, char *argv[])
{
#ifdef _WIN32  
	std::string src = "F:\\git\\algorithm";
	std::string des = "F:";
	CopyDir cd;
	cd.copy(src, des);
#else  
	std::string src = "/media/myUbuntu/F/data/test";
	std::string des = "/media/myUbuntu/F/data/test2";
	CopyDir cd;
	cd.copy(src, des);
#endif  
	return 0;
}