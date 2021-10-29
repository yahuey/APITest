# This will assist in the API getting
import requests
# We need to read JSON here to have clean data
import json
# This will help make the data look pretty for others to see
import pandas

print("What keyword would you like to search?")
keyword = input()


# This is a function to allow us to use multiple words
def prepped_input(keyword):
# we break up the string here
    thest = keyword.split()
# create a variable for the prepped string
    final_string = ""
    added_material = "%20"
    if len(thest) > 1:
        for word in thest:
            final_string += word + added_material
        return final_string
    else:
        return keyword

new_keyword = prepped_input(keyword)
# variable here because in case of need to change API, it's only in one place
api_key = "api_key=b7fd41a703f1568133d18d5f5c46f262"
api_base_url = "https://api.themoviedb.org/3"
endpoint_path = f"/search/keyword"
# again creating an endpoint for the movies
endpoint = f"{api_base_url}{endpoint_path}?{api_key}&query={new_keyword}&page=1"
req1 = requests.get(endpoint)
# for troubleshooting purposes
print(req1.status_code)
# Saving the JSON data into a variable
res_dogs_json = req1.text
# Then saving the JSON data into a dictionary for easier navigation
res_dogs_dict = json.loads(res_dogs_json)
# Showing the data row-by-row in this format
for x, y in res_dogs_dict.items():
    print(x, y)
# This is to get a specific ID that we need. I really wanted to test my knowledge of nested lists and dictionaries.
print(res_dogs_dict["results"][0])
