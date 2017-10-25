#include<iostream>
#include<cstdio>
#include <bitset>

using namespace std;
//������ƴ�ӣ���tongbuma��tongbuma+1...ת�ɶ����ƽ��е���ƴ�ӣ�
//����1��2��������0000001100000001��ʮ���Ʊ�ʾ
bool Encode(unsigned __int64 cell, unsigned __int64* p, int cstart, int clength, int istart)
{
	int i, j;
	unsigned __int64 base = 1;
	unsigned __int64 t1;
	t1 = *p;
	for (i = cstart, j = istart; i<cstart + clength; i++, j++)
	{
		t1 = t1&(~(base << j));
		if (((cell >> i)&base) != 0)
		{
			t1 |= base << j;
		}
	}
	*p = t1;
	return true;
}

int main()
{
	unsigned __int64 a = 1;
	unsigned __int64* pWord = &a;
	unsigned __int64 tongbuma = 1;
	int count = 0;
	for (int i = 0; i < 10; ++i, ++tongbuma)
	{
		Encode(tongbuma, pWord, 0, 8, count);
		count += 8;
	}
	cout << *pWord << endl;
	cout << bitset<16>(*pWord) << endl;
	return 0;
}

