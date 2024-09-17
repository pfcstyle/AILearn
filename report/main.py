import os
import re

dir = os.path.dirname(__file__)


import pandas as pd

file_name = '1'

def extract_number(title):
    match = re.search(r'总第(\d+)期', title)
    if match:
        return match.group(1)
    else:
        match = re.search(r'总第_(\d+)_期', title)
        if match:
            return match.group(1)
        else:
            match = re.search(r'总第 (\d+) 期', title)
            if match:
                return match.group(1)
            else:
                match = re.search(r'总第_(\d+)期', title)
                if match:
                    return match.group(1)
    return 0

def read_excel_and_extract(file_path):
    # 使用pandas读取Excel文件
    excel_data = pd.read_excel(file_path, engine='openpyxl')
    first_title = excel_data.columns[0]
    excel_data.columns = ['key', 'value']
    all_list = pd.DataFrame(columns=['number', 'title', 'huigu', 'yugao'])
    with open(os.path.join(dir, f'{file_name}.txt'), 'w', encoding='utf-8') as f:
        index = first_title.index('读书会\n')
        # f.write(first_title[index:].replace('读书会\n', ''))
        # f.write('\n')
        title = '\n' + first_title[index:].replace('读书会\n', '').replace('_', '').replace(' ', '') + '\n'
        number = extract_number(title)
        huigu = ''
        yugao = ''
        for index, row in excel_data.iterrows():
            if pd.isna(row['key']):
                continue
            if '上文回顾' in row['key']:
                str = row['value'].replace('\n', '')
                huigu = f"回顾：{str}" + '\n'
                # f.write(f"回顾：{str}")
                # f.write('\n')
            if '本期预告' in row['key']:
                str = row['value'].replace('\n', '')
                yugao = f"预告：{str}" + '\n'
                if index > excel_data.shape[0] - 3:
                    all_list.loc[len(all_list)] = [number, title, huigu, yugao]
                    break
                # f.write(f"预告：{str}")
                # f.write('\n')
            if '读书会\n' in row['key']:
                all_list.loc[len(all_list)] = [number, title, huigu, yugao]
                new_title = row['key']
                index = new_title.index('读书会\n')
                title = '\n' + new_title[index:].replace('读书会\n', '').replace('_', '').replace(' ', '') + '\n'
                number = extract_number(title)
                
                # f.write('\n')
                # f.write(title[index:].replace('读书会\n', ''))
                # f.write('\n')
        # 对all_list进行排序，根据number从小到大
        all_list['number'] = all_list['number'].astype(int)
        all_list = all_list.sort_values(by='number')
        for index, row in all_list.iterrows():
            f.write(row['title'])
            f.write(row['huigu'])
            f.write(row['yugao'])

read_excel_and_extract(os.path.join(dir, f'{file_name}.xlsx'))
