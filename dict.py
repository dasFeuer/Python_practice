# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
#   "England": "London"
# }
# # country_capitals["Italy"] = "Rome"
# # del country_capitals["Canada"]


# # country_capitals.clear()
# print(country_capitals)

# print(country_capitals["Germany"]) 
# print(country_capitals["England"]) 

country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}

for country in country_capitals:
    print(country)

print()

for country in country_capitals:
    capital = country_capitals[country]
    print(capital)

country_capitals = {"England": "London", "Italy": "Rome"}

print(len(country_capitals))   

numbers = {10: "ten", 20: "twenty", 30: "thirty"}

print(len(numbers))            

countries = {}

print(len(countries))   


file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

print(".pdf" in file_types)       
print(".mp3" in file_types)       
print(".mp3" not in file_types)   