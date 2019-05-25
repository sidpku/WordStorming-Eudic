# 主程序
FILENAME = 'raw_material.txt'

with open(FILENAME, encoding='UTF-8') as source_file:
    content = source_file.readlines()

# 开关，如果1则开始录入单词。
switch = 0
output = ''

for line in content:
    for i in line:
        if i == '@' or i == '@':
            switch = 1 - switch
        elif switch == 1:
            output = output + i
        else:
            pass
    if output[-1] == ';':
        continue
    output = output + ';'

# print(output)
with open('output.txt',mode='w') as output_file:
    output_file.write(output)

