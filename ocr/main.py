import os
from easyocr import Reader

dir = os.path.dirname(__file__)
jpgs_dir = os.path.join(dir, 'jpgs')

reader = Reader(['en', 'ch_sim'])  # 指定语言，这里包括英文和简体中文

# 获取目录下所有jpg文件
jpgs = [f for f in os.listdir(jpgs_dir) if f.endswith('.jpg')]


# results = reader.readtext(os.path.join(dir, 'test.jpg'))  # 读取单个图片
# for (bbox, text, prob) in results:
#     print(f'{bbox}, {text}, {prob}')
# 读取所有图片

for jpg in jpgs:
    results = reader.readtext(os.path.join(jpgs_dir, jpg))
    i = 0
    is_shang_wen_hui_gu = False
    is_yu_gao = False
    is_english = False
    shang_wen_hui_gu_str = '回顾：'
    yu_gao_str = '预告：'
    for (bbox, text, prob) in results:
        print(f'{bbox}, {text}, {prob}')
    # 输出到文件
    with open(os.path.join(dir, 'output.txt'), 'w', encoding='utf-8') as f:
        for (bbox, text, prob) in results:
            if i == 1:
                print(text)
                f.write(text)
                f.write('\n')

            if is_shang_wen_hui_gu:
                if bbox[1][0] > 250:
                    shang_wen_hui_gu_str += text
            if is_yu_gao:
                if bbox[1][0] > 250:
                    yu_gao_str += text
            if text.strip() == '上文回顾':
                is_shang_wen_hui_gu = True
            if text.strip() == '本期预告':
                is_yu_gao = True
                is_shang_wen_hui_gu = False
            i += 1

        print(shang_wen_hui_gu_str)
        print(yu_gao_str)
        f.write(shang_wen_hui_gu_str)
        f.write('\n')
        f.write(yu_gao_str)
        f.write('\n')
