
// testSqlDlg.cpp : ʵ���ļ�
//

#include "stdafx.h"
#include "testSql.h"
#include "testSqlDlg.h"
#include "afxdialogex.h"
#include <winsock.h> 
#include <mysql.h>

#pragma comment(lib, "ws2_32.lib")  
#pragma comment(lib, "libmysql.lib") 

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// ����Ӧ�ó��򡰹��ڡ��˵���� CAboutDlg �Ի���

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// �Ի�������
	enum { IDD = IDD_ABOUTBOX };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV ֧��

// ʵ��
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(CAboutDlg::IDD)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CtestSqlDlg �Ի���



CtestSqlDlg::CtestSqlDlg(CWnd* pParent /*=NULL*/)
	: CDialogEx(CtestSqlDlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CtestSqlDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CtestSqlDlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BUTTON1, &CtestSqlDlg::OnBnClickedButton1)
END_MESSAGE_MAP()


// CtestSqlDlg ��Ϣ�������

BOOL CtestSqlDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// ��������...���˵�����ӵ�ϵͳ�˵��С�

	// IDM_ABOUTBOX ������ϵͳ���Χ�ڡ�
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// ���ô˶Ի����ͼ�ꡣ  ��Ӧ�ó��������ڲ��ǶԻ���ʱ����ܽ��Զ�
	//  ִ�д˲���
	SetIcon(m_hIcon, TRUE);			// ���ô�ͼ��
	SetIcon(m_hIcon, FALSE);		// ����Сͼ��

	// TODO:  �ڴ���Ӷ���ĳ�ʼ������

	return TRUE;  // ���ǽ��������õ��ؼ������򷵻� TRUE
}

void CtestSqlDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// �����Ի��������С����ť������Ҫ����Ĵ���
//  �����Ƹ�ͼ�ꡣ  ����ʹ���ĵ�/��ͼģ�͵� MFC Ӧ�ó���
//  �⽫�ɿ���Զ���ɡ�

void CtestSqlDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // ���ڻ��Ƶ��豸������

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// ʹͼ���ڹ����������о���
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// ����ͼ��
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

//���û��϶���С������ʱϵͳ���ô˺���ȡ�ù��
//��ʾ��
HCURSOR CtestSqlDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}



void CtestSqlDlg::OnBnClickedButton1()
{
	
	MYSQL mydata;

	//��ʼ�����ݿ�  
	mysql_library_init(0, NULL, NULL);

	mysql_init(&mydata);

	mysql_options(&mydata, MYSQL_SET_CHARSET_NAME, "gbk");

	mysql_real_connect(&mydata, "localhost", "root", "mysqlpsbc", "test", 3306, NULL, 0);


	//sql�ַ���  
	CString sqlstr;

	//����һ����  
	sqlstr = "CREATE TABLE IF NOT EXISTS user_info";
	sqlstr += "(";
	sqlstr +=
		"user_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique User ID',";
	sqlstr +=
		"user_name VARCHAR(100) CHARACTER SET gb2312 COLLATE gb2312_chinese_ci NULL COMMENT 'Name Of User',";
	sqlstr +=
		"user_second_sum INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'The Summation Of Using Time'";
	sqlstr += ");";
	if (0 == mysql_query(&mydata, sqlstr.GetBuffer())) {
		
	}
	else {
		
		mysql_close(&mydata);
		return ;
	}

	//����в�������  
	sqlstr =
		"INSERT INTO user_info(user_name) VALUES('��˾����'),('һ������'),('��������'),('����С��'),('����');";
	if (0 == mysql_query(&mydata, sqlstr.GetBuffer() )) {
		
	}
	else {
		
		mysql_close(&mydata);
		return ;
	}

	//��ʾ�ղŲ��������  
	sqlstr = "SELECT user_id,user_name,user_second_sum FROM user_info";
	MYSQL_RES *result = NULL;
	if (0 == mysql_query(&mydata, sqlstr.GetBuffer() )) {

		//һ����ȡ�����ݼ�  
		result = mysql_store_result(&mydata);
		//ȡ�ò���ӡ����  
		int rowcount = mysql_num_rows(result);

		//ȡ�ò���ӡ���ֶε�����  
		unsigned int fieldcount = mysql_num_fields(result);
		MYSQL_FIELD *field = NULL;
		for (unsigned int i = 0; i < fieldcount; i++) {
			field = mysql_fetch_field_direct(result, i);
			field->name;
		}

		//��ӡ����  
		MYSQL_ROW row = NULL;
		row = mysql_fetch_row(result);
		while (NULL != row) {
			for (int i = 0; i < fieldcount; i++) {
				 row[i] ;
			}
			
			row = mysql_fetch_row(result);
		}

	}
	else {
		
		mysql_close(&mydata);
		return;
	}


	//ɾ���ղŽ��ı�  
	sqlstr = "DROP TABLE user_info";
	if (0 == mysql_query(&mydata, sqlstr.GetBuffer() )) {

	}
	else {
		mysql_close(&mydata);
		return ;
	}
	mysql_free_result(result);
	mysql_close(&mydata);
	mysql_server_end();

}
