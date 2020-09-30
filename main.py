import json
import  requests
import  datetime
import psycopg2

postgresConnection    = psycopg2.connect( host="localhost",database="my",user="postgres",password="Anup@123")
cursor                = postgresConnection.cursor()
# name_Table            = "data_name"
# sqlCreateTable = "create table "+name_Table+" ( id SERIAL PRIMARY KEY, summary varchar(800));"
# cursor.execute(sqlCreateTable)
# postgresConnection.commit()


url = 'http://api.openweathermap.org/'
api_key = '271d1234d3f497eed5b1d80a07b3fcd1'
complete_url = url +  'data/2.5/weather?q=Yavatmal,india&appid=' + api_key
response = requests.get(complete_url)
x = response.json()
date_name = x['dt']
date_m = datetime.datetime.fromtimestamp(date_name)
current_day = date_m.strftime('%d')

num = int(current_day)
# num = 7
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            # msg ={ num : 'is not a prime number so no Date'}
            # print(json.dumps(msg))
            print('Date is not a prime number so no Date')
            cursor.execute("INSERT INTO data_name (id, summary) VALUES ( DEFAULT ,'Date is not a prime number so no Date')");
            postgresConnection.commit()
            break
    else:
        # msg = response.json()
        # print(json.dumps(msg))
        print(response.json())
else:
    # msg = {num : 'is not a prime number so no Date'}
    # print(json.dumps(msg))
    print('Date is not a prime number so no Date')
    cursor.execute("INSERT INTO data_name (id, summary) VALUES ( DEFAULT ,'Date is not a prime number so no Date')");
    postgresConnection.commit()





