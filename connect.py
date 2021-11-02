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
    page_number = 1
    endpoint = f"{api_base_url}{endpoint_path}?{api_key}&query={new_keyword}&page={page_number}"
    req1 = requests.get(endpoint)
    # for troubleshooting purposes
    print(req1.status_code)
    # Saving the JSON data into a variable
    init_json = req1.text
    # Then saving the JSON data into a dictionary for easier navigation
    init_dict = json.loads(init_json)
    final_dict = {}
  # I have to stop here, but I am trying to get all of the pages here into one CSV form
    if int(init_dict["total_pages"]) > page_number:
        count = int(init_dict["total_pages"])
        print("This is count " + str(count))
        dict_stuff = []
        trans_dict = {}
        for x in range(count):
            loop_endpoint = f"{api_base_url}{endpoint_path}?{api_key}&query={new_keyword}&page={x + 1}"
            loop_req = requests.get(loop_endpoint)
            loop_json = loop_req.text
            loop_dict = json.loads(loop_json)
            loop_json = ""
            loop_req  = ""
            trans_dict = loop_dict
            dict_stuff.append(trans_dict.get("results"))
            # final_dict.update({"results": "deez nuts"})
            # final_dict.update({"results": dict_stuff.append(trans_dict.get("results"))})
            trans_dict.clear()
        final_dict.update({"results": dict_stuff})
        return final_dict["results"]
    else:
        return init_dict["results"]

# Here we are looking at the results only for a cleaner search, then saving them as a csv format to be looked at.
def display_data(search_list):
    length = len(search_list)
    new_table = pd.DataFrame()
 # this looks at the length of the list, if it's large we will need to get all the data manageable.
    if length > 1:
        print("the if is running")
        for x in range(length):
            df = pd.DataFrame(search_list[x], columns=['adult', 'backdrop_path', 'genre_ids', 'id', 'original_language',
                                                    'original_title', 'overview', 'popularity', 'poster_path',
                                                    'release_date', 'title', 'video', 'vote_average', 'vote_count'])
            print(df)
            new_table = new_table.append(df)
        file_export = new_table.to_csv()
        return file_export
    else:
        df = pd.DataFrame(search_list[0], columns=['adult', 'backdrop_path','genre_ids', 'id', 'original_language',
                                                   'original_title', 'overview', 'popularity', 'poster_path',
                                                   'release_date', 'title', 'video', 'vote_average', 'vote_count'])
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
