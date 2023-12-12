file_list = ['task_3/1.txt', 'task_3/2.txt', 'task_3/3.txt']

def count_lines():
    count = 0
    for line in f:
        if line.strip():
            count += 1
    return count

lines = []
count_dict = {}

for files in file_list:
    with open(files, encoding='utf-8') as f:
        lines.append(count_lines())
        for file, line in zip(file_list, lines):
            count_dict[file] = line

for i in enumerate(lines):
    for files in file_list:
        try:
            min_ = min(count_dict.values())
            if count_dict.get(files) == min_:
                with open(files, encoding='utf-8') as f:
                    with open('task_3/result.txt', 'a', encoding='utf-8') as result:
                        x = f.readlines()
                        # print(files)
                        result.write(f'{files}\n{count_dict[files]}\n')
                        for i in x:
                            result.write(i.strip('    '))
                        result.write(f'\n')
                del count_dict[files]
        except ValueError:
            print('Файлы закончились')
            break