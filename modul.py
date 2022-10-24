workers = []
with open('data_user.txt', 'r', encoding='utf-8') as data:
    for line in data:
        temp = {}
        s = line.split(',')
        temp['id_worker'] = int(s[0])
        temp["second_name"] = s[1]
        temp['first_name'] = s[2]
        temp['last_name'] = s[3]
        temp['post'] = s[4]
        temp['min_salary'] = int(s[5])
        temp['max_salary'] = int(s[6])
        workers.append(temp)
    print(workers)


