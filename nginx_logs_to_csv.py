import csv

f = open("/var/log/nginx/access.log", "r")
w =  open('nginxlogs.csv', 'w', newline='')
lines = f.readlines()
writer = csv.writer(w, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
writer.writerow(['sourceIP, date, Time, RequestType, Status'])

for line in lines:
     source_ip = line[:line.index('-'):]
     date = line[line.index('[')+1:line.index('[')+12]
     time = line[line.index(date)+12:line.index(date)+20]
     request_type = line[line.index(']')+3:line.index(']')+6]
     request_status = line[line.index('HTTP')+10:line.index('HTTP')+13]
     all = f'{source_ip}, {date}, {time}, {request_type}, {request_status}'
     writer.writerow([all])
