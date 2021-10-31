# This will assist in the API getting
import requests
# We need to read JSON here to have clean data
import json
# This will help make the data look pretty for others to see
import pandas as pd

def get_query():
    print("What movie would you like to search?")
    keyword = input()
    return keyword

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

def movie_query(new_keyword):
    api_key = "api_key=b7fd41a703f1568133d18d5f5c46f262"
    api_base_url = "https://api.themoviedb.org/3"
    endpoint_path = f"/search/movie"
    # again creating an endpoint for the movies
    endpoint = f"{api_base_url}{endpoint_path}?{api_key}&query={new_keyword}&page=1"
    req1 = requests.get(endpoint)
    # for troubleshooting purposes
    print(req1.status_code)
    # Saving the JSON data into a variable
    init_json = req1.text
    # Then saving the JSON data into a dictionary for easier navigation
    init_dict = json.loads(init_json)
    # Showing the data row-by-row in this format
    for x, y in init_dict.items():
        print(x, y)
    # This is to get a specific ID that we need. I really wanted to test my knowledge of nested lists and dictionaries.
    return init_dict

# Here we are looking at the results only for a cleaner search, then saving them as a csv format to be looked at.
def display_data(search_dict):
    df = pd.DataFrame(search_dict["results"])
    file_export = df.to_csv()
    print(df)
    return file_export

# This is to run the program as a main for cleanliness sake. We're saving things too for our save as a search the person entered.
def main():
    user_keyword = get_query()
    clean_keyword = prepped_input(user_keyword)
    query_dict = movie_query(clean_keyword)
    export = display_data(query_dict)
    web = open(f"{user_keyword}.csv", "w")
    web.write(export)
    web.close()
# running the data through here. Just cleaner
main()
