#include <iostream>
#include<cstring>
#include<sstream>
#include<algorithm>
#include<vector>

using namespace std;
//���ַ���ֻ�����int�����֣�����ͨ��
int ReverseNum(int number)
{
	vector<int>vecNum;
	while (number != 0)
	{
		int remain = number % 10;
		vecNum.push_back(remain);
		number /= 10;
	}
	int sum = 0;
	for (unsigned int i = 0; i < vecNum.size(); ++i)
	{
		sum += vecNum[i] * (int)pow(10, vecNum.size() - 1 - i);
	}
	return sum;
}

//���ַ����Ƚ�ͨ����д����
double ReverseNum1(double number)
{
	double revNum;
	char a[100];
	sprintf(a, "%f", number);
	_strrev(a);
	revNum = atof(a);  //���ַ���ת��double�ͣ������ַ���
	return revNum;
}
//���ַ���Ҳ�Ƚ�ͨ����д����
double ReverseNum2(double number)
{
	double revNum;
	stringstream str;
	str << number;
	string s = str.str();
	reverse(s.begin(), s.end());
	revNum = atof(s.c_str());
	return revNum;
}

//ת��int
int ReverseNum2(int number)
{
	int revNum;
	char a[100];
	sprintf(a, "%d", number);
	_strrev(a);
	//sscanf(a, "%d", &revNum);
	revNum = atoi(a);  //���ַ���ת��int�ͣ����ַ����ȼ�
	return revNum;
}

int main(int argc, char **argv)
{
	double a = 12.34;
	double revA = ReverseNum3(a);
	cout << revA << endl;
	int b = 1234;
	int revB = ReverseNum2(b);
	cout << revB << endl;
	system("pause");
	return 0;
}

//�ܽ᣺
//1.����ת���ַ���
//�������ַ������ɣ��ڶ���д����Ϊ��
//sprintf atoi sscanf���ܵ��ַ���������Ϊ�ַ�ָ�룬�������ַ��������ֱ�Ӹ�ֵ���ַ�ָ�룬
//��ˣ��ַ�����Ҳ����ȫû�����  ע��sscanf����doubleʱ�����
#include <iostream>  
#include <sstream>  

using namespace std;

int main()
{
	double number = 12.34;
	//����1��string��˼·
	//stringstream str;
	//str << number;
	//string s = str.str();
	//cout << s << endl;

	//const char *b = s.c_str();
	//cout << b << endl;

	//char a[100];
	//sprintf(a, "%s", b);
	//cout << a << endl;

	//����2��
	char a[100];
	sprintf(a, "%.2f", number);
	cout << a << endl;

	string s = a;
	cout << s << endl;

	char *b = a;
	cout << b << endl;
	return 0;
}

//2.�ַ���ת������
//�������ַ������ڶ����ٶȽϿ���д����򵥣����Դ���string��char *,char a[]��������
#include <iostream>  
#include <sstream>  

using namespace std;

int main()
{
	string s="12.34";
	//����1��string��˼·
	stringstream str(s);
	float number;  //float��double����
	str >> number;
	cout << number << endl;

	//����2��
	double number = atof(s.c_str()); //��ʽ������double������ת��float
	cout << number << endl;

	//����3��
	float number;//������float����ȷ�ģ�������double�Ͳ�����
	sscanf(s.c_str(), "%f", &number);
	cout << number << endl;

	return 0;
}

//�ܽ᣺
//�ַ������ַ��������ַ�ָ��֮���ת����ϵ
string s = ��12qwe��;
char* str = ",";
char a[] = ��qrew��;

char* str = "123";
string s = str; //��ȷ
char s[] = str; //����  

string s = ��123����
const char *str = s.c_str(); //��ȷ��ע��s.c_str()�Ǵ���const���Եģ����char *str = s.c_str(); �Ǵ����
char a[] = s; //����  ���ϳ�������Ҳ����

char a[] = "1,b";
string s = a; //��ȷ  ���Ƿ��������Ǵ����
char *p = a; //��ȷ

//string ��char *����char a[]�İ취��
string s2 = "34";
const char *c2 = s2.c_str();
char s1[20];
sprintf(s1, "%s", c2);  //��ô�����������ڣ��ַ�����ϻ�Ƚϵȱ��뱣֤��һ��Ϊ�ַ�������У��ַ���ָ�벻��

