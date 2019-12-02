# Piaware-python   
 Python script to acquire, view, filter, sort and manipulate ADSB data from piaware/dump1090-fa   

# Requires geopy  
To install geopy   
```   
pip3 install geopy   
```    

# Example usage   
```   
import piaware   

papy=piaware.piawarepython()  

getdata=papy.adsbdata()

# Sort flights by flight code in ascending order.
sorteddata=papy.adsbdatasort(getdata,"flight","asc")

# Filter flights within 5-10 nautical miles radius from ADSB receiver
filtereddata,filteredaircrafts=papy.adsbdatafilter(getdata,"distance",5,10)

print("")    
print("ADSB DATA")   
print("")  
print(getdata)   
print("")  
print("")  
print("SORTED DATA")  
print("")  
print(sorteddata)  
print("")  
print("")  
print("FILTERED DATA")   
print("")  
print(filtereddata)   
print("")   
print("")  
print(filteredaircrafts)   
print("")   
print("")
```   

# Sorting keys/options  
"flight"      - to sort by flight codes
"squawk"      - to sort by squawk code  
"distance"    - to sort by aircraft distance from receiver  
"alt_baro"    - to sort by aircraft altitude  
"gs"          - to sort by aircraft speed  
"mag_heading" - to sort by aircraft heading  
"messages"    - to sort by number of messages  

Use "asc" to sort list in ascending order and "dec" to sort list in descending order  


# Filtering keys/options   
"distance"    - to filter data by distance  
"alt_baro"    - to filter by aircraft altitude  
"gs"          - to filter by aircraft speed  
"mag_heading" - to filter by aircraft heading  
"messages"    - to filter by number of messages  
