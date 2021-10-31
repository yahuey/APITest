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
    page_number = 2
    endpoint = f"{api_base_url}{endpoint_path}?{api_key}&query={new_keyword}&page={page_number}"
    req1 = requests.get(endpoint)
    # for troubleshooting purposes
    print(req1.status_code)
    # Saving the JSON data into a variable
    init_json = req1.text
    # Then saving the JSON data into a dictionary for easier navigation
    init_dict = json.loads(init_json)
    final_dict = init_dict["results"]
    final_dict
    # I have to stop here, but I am trying to get all of the pages here into one CSV form
    loop_dict = {}
    # loop_json = ""
    # if int(init_dict["total_pages"]) > page_number:
    #     count = int(init_dict["total_pages"])
    #     print("This is count " + str(count))
    #     for page_number in range(count):
    #         loop_endpoint = f"{api_base_url}{endpoint_path}?{api_key}&query={new_keyword}&page={page_number}"
    #         loop_req = requests.get(loop_endpoint)
    #         loop_json = loop_req.text
    #         loop_dict.update(loop_json)
    #         final_dict.update(loop_dict["results"])
    #         loop_dict.clear()
    #         loop_json = ""
    #         page_number += 1
    #     return final_dict
    # else:
    return final_dict

# Here we are looking at the results only for a cleaner search, then saving them as a csv format to be looked at.
def display_data(search_dict):
    df = pd.DataFrame(search_dict).rem
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
