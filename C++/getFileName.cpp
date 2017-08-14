
#include<iostream>  
#include<vector>
#include <sstream>
#include<io.h>  
using namespace std;
int main(){
	vector<string> fileName;
	_finddata_t file;
	long lf;
	//输入文件夹路径  
	if ((lf = _findfirst("F:\\keyan\\*.*", &file)) == -1)
		cout << "Not Found!" << endl;
	else{
		//输出文件名  
		cout << "file name list:" << endl;
		while (_findnext(lf, &file) == 0){
			fileName.push_back(file.name);
		}
	}
	_findclose(lf);
	for (auto &i : fileName)
		cout << i << endl;
	return 0;
}