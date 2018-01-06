#coding=utf-8
import xlrd,os
from public.log import Logger

logger=Logger().get_loger()
def get_case(name,sheel):   #得到用例
    try:
        path=os.getcwd()
        case_path=path+"/%s.xlsx"%name
        data=xlrd.open_workbook(case_path)
        table = data.sheet_by_name(sheel)
        try:
            case = []  # 存放case
            dict = {}  # 存放api
            testcase = []  # 存放case
            nrows = table.nrows  # 行
            ncols = table.ncols  # 列
            for j in range(nrows):
                case.append(table.row_values(j))
            print range(nrows - 1)
            for i in range(nrows - 1):
                for l in range(ncols):
                    dict[case[0][l]] = case[i][l]
                testcase.append(dict)
            return testcase
        except (BaseException, Exception):
            logger.error('获取case失败')
    except (ValueError, Exception):
        logger.error('传入无效的参数')



