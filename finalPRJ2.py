import requests
from bs4 import BeautifulSoup
import mysql.connector
import re

cnx = mysql.connector.connect(user='root', password='123',
                              host='127.0.0.1',
                              database='cardata')
cursor = cnx.cursor()
urlList = ['https://www.truecar.com/used-cars-for-sale/listings/lexus/?page=%d&sort[]=best_match',
           'https://www.truecar.com/used-cars-for-sale/listings/mazda/?page=%d&sort[]=best_match',
           'https://www.truecar.com/used-cars-for-sale/listings/hyundai/?page=%d&sort[]=best_match',
           'https://www.truecar.com/used-cars-for-sale/listings/mercedes-benz/?page=%d&sort[]=best_match',
           'https://www.truecar.com/used-cars-for-sale/listings/kia/?page=%d&sort[]=best_match',
           'https://www.truecar.com/used-cars-for-sale/listings/volkswagen/?page=%d&sort[]=best_match',
           'https://www.truecar.com/used-cars-for-sale/listings/toyota/?page=%d&sort[]=best_match',
           'https://www.truecar.com/used-cars-for-sale/listings/mitsubishi/?page=%d&sort[]=best_match']
for k in range(len(urlList)):
        for j in range(1,21):
            pageText = requests.get((urlList[k])%(j))
            soup = BeautifulSoup(pageText.text,'html.parser')
            names = soup.find_all('span', attrs = {'class':'vehicle-header-make-model text-truncate'})
            models = soup.find_all('div', attrs = {'data-test':'vehicleCardTrim'})
            productYears = soup.find_all('span', attrs = {'class':'vehicle-card-year font-size-1'})
            traveleds = soup.find_all('div', attrs = {'data-test':'vehicleMileage'})
            cities = soup.find_all('div', attrs = {'data-qa':'Location'})
            prices = soup.find_all('div', attrs = {'data-test':'vehicleCardPricingBlockPrice'})
            for i in range(len(names)):
                info = "INSERT INTO dataf(name, model, productYear, traveled, city, price) VAlUES (%s, %s, %s, %s, %s, %s)"
                values = (names[i].text, models[i].text, productYears[i].text, traveleds[i].text, cities[i].text, prices[i].text)
                cursor.execute(info, values)
                cnx.commit()



# create table dataf(name varchar(500), model varchar(500), productYear varchar(500), traveled varchar(500), city varchar(500), price varchar(500));create table dataf(name varchar(500), model varchar(500), productYear varchar(500), traveled varchar(500), city varchar(500), price varchar(500));

# cursor = cnx.cursor()
# query = 'SELECT * FROM dataf;'
# cursor.execute(query)
# print(list(cursor))