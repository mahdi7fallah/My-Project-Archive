import mysql.connector
import requests
import re


print("Downloading Web URL ...")
url = requests.get('https://www.digikala.com/search/category-mobile-phone/?brand[0]=18&brand[1]=82&has_selling_stock=1&attribute[A202][0]=292&sortby=20')
print("Link Downloaded.\n")

re_text = r'data-title-en=\"((\w+)\s*(.*)\s*([DS].*)SIM\s*(\d*)GB.*)\".*\s*.*\s*.*price\":(\d*)'
re_text_img = r'data-title-en=\"((\w+)\s*(.*)\s*([DS].*)SIM\s*(\d*)GB.*)\".*\s*.*\s*.*price\":(\d*).*\s*.*\s*.*\s*.*\s*.*\s*.*\s*.*\s*.*\s.*<\w*\s*\w*=\"(.*)"'

phone_info = re.findall(re_text_img,url.text)

db_address = 'localhost'
db_port = 3306
db_user = 'root'
db_Password = '********'
db_name = 'Python_Projects'
db_table_name = 'Phone_info_Samsung_Huawei'
db_table_key = "Full, Brand, Model, SIM, Storage, Price, Image"

try:
    print("Connecting To Database ...")
    my_db = mysql.connector.connect(host=db_address, user=db_user, password=db_Password, database=db_name, port=db_port)
    cs = my_db.cursor()
    print("Connected.\n")
except IOError as e:
    print("ERROR !!!")
    print(e)

print("Inserting Data To Database ...")
for i in phone_info:
    cs.execute("INSERT INTO {}({}) VALUE('{}', '{}', '{}', '{}', {}, {}, '{}');"
    .format(db_table_name, db_table_key, i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
print("Data Inserted.\n")
my_db.commit()

my_db.close()
print(("Finish.\nClose."))
