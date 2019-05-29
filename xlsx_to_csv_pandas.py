import pandas as pd


def xlsx_to_csv_pd(path_xlsx,path_csv):
    data_xls = pd.read_excel(path_xlsx, index_col=0)
    data_xls.to_csv(path_csv, encoding='utf-8')


if __name__ == '__main__':
    path_xlsx = r'C:\Users\Administrator\Desktop\Python聚类\数据_以Excel保存_横向.xlsx'
    path_csv = r'C:\Users\Administrator\Desktop\Python聚类\loan_data.csv'
    xlsx_to_csv_pd(path_xlsx, path_csv)


