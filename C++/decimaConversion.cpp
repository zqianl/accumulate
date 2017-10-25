#include<iostream>
#include<string>
using namespace std;
//�������֮���ת��

/**
* s1  ת��֮ǰ����
* s2  ת��֮�����
* d1  ԭ������
* d2  ��Ҫת���Ľ�����
*     ����9��λ���ô�д'A'��'Z'��ʾ��2��16λ����ͨ����֤
*/
void conversion(string s1, string &s2, long d1, long d2){

	//˼·�����ǽ�ԭ��ת����ʮ������ -> ����ʮ������ת����Ŀ����Ƶ���
	long i, j, t, num;
	char c;
	num = 0;
	//��ת����ʮ������
	for (i = 0; i < s1.size(); i++){
		if (s1[i] >= '0'&&s1[i] <= '9'){
			t = s1[i] - '0';
		}
		else t = s1[i] - 'A' + 10;
		//�ο�ʮ���Ƶķ�ʽ
		num = num*d1 + t;
	}
	i = 0;
	s2 = "";
	while (1){

		t = num%d2;
		num /= d2;
		if (t <= 9)s2 = to_string(t) + s2;
		else s2 = (char)((t - 10 + 'A')) + s2;
		if (num == 0)break;
	}
}

int main(){
	string str1, str2;
	long d1, d2;
	while (cin >> str1 >> d1 >> d2){
		conversion(str1, str2, d1, d2);
		cout << str2 << endl;
	}
	return 0;
}
