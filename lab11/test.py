import re
from datetime import datetime

pattern = ' - - \\[| '

file_name = 'access_log.txt'
date_format = '%d/%b/%Y:%H:%M:%S'
date_from = datetime.strptime('08/Mar/2004:07:11:37', date_format)
date_to = datetime.strptime('10/Mar/2004:11:41:52', date_format)
file1 = open(file_name, 'r')
lines = file1.readlines()

count = 0
result_dict = {}
# Strips the newline character
for line in lines:
    count += 1
    splitted_line = re.split(pattern, line)

    print(splitted_line)
    print(count, line.strip())

    device_initiator = splitted_line[0]
    date_time_str = splitted_line[1]
    date_time_of_log = datetime.strptime(date_time_str, date_format)
    if date_from < date_time_of_log < date_to:
        result_dict[device_initiator] = result_dict.get(device_initiator, 0) + 1

for k, v in sorted(result_dict.items(), key=lambda item: item[1], reverse=True):
    print(f'{k} => {v}')