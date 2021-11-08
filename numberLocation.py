#import phonenumbers
#from myNumber import number
import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers import PhoneNumberType
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import numpy as np
import pandas as pd
import folium
import webbrowser
import time


Key = '813978e32347461bb2d53b777a9545e2'
print('Enter Phone number to see past locations: ')
number=input('**')
phonenumber = phonenumbers.parse(number)
print(f'{number}')
print(type(number))
print(f'{phonenumber}')
print(type(phonenumber))
time.sleep(5)

yourLocation = geocoder.description_for_number(phonenumber, 'en')
Region = geocoder.description_for_number(phonenumber, 'en')
isValid = phonenumbers.is_valid_number(phonenumber)
# Checking possibility of a number
isPossible = phonenumbers.is_possible_number(phonenumber)
serviceProvider = carrier.name_for_number(phonenumber, 'en')
#sserviceProvider = phonenumbers.parse(phonenumber)


print(f'[LOCATION] {yourLocation}')
time.sleep(1)
print(f'[REGION] {Region}')
time.sleep(1)
print(f'[VALID] {isValid}')
time.sleep(1)
print(f'[Is Possible?] {isPossible}')
time.sleep(1)
print(f'[SERVICE-PROVIDER?] {serviceProvider}')
time.sleep(1)




numNum2 = phonenumbers.parse(number)

#print(f'[SERVICEPROVIDER] {serviceProvider}')
##print('*' * 100)

######################
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
print('Query;', query)
print('Results;', results)

#for x in range(len(results)):     ### ---> DEBUGGING - TO VIEW ARRAY BEFORE CONVER TO DF
    #print(f'{results[x]} \n', 'x' * 100)
#print(type(query)) #<- debug purpose
#print(type(results)) #<-debug purpose
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(f'[COORDINATES] {lat} , {lng}\n')
df = pd.DataFrame(results)
print('*' * 100)
print(f'[EXPORT] ..saved as coordinates.txt {df.head(2)}')
df.to_csv(r'\coordinates.csv', index = False)
#########################
myMap = folium.Map(location = [lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup = yourLocation).add_to(myMap)
myMap.save('eyespy.html')
print(f'[MAP]** saved to eyespy.html')
#file:///Users/macbook/Documents/CS/PROJECT/phone_number/eyespy.html

#pd.read_html(myMap.save('eyespy.html'))
webbrowser.open('eyespy.html')
webbrowser.open('/Users/macbook/Documents/CS/PROJECT/phone_number/eyespy.html')
