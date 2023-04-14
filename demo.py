from yelpapi import YelpAPI
import pandas as pd
api_key = "puAjy7iKppGdQ1veYkj7j1CmoNmejmGS3mcRdHAQ0qQ4vrRvKH1zeWVf5fxeSC72IXjl9I6p_WYzq5jnnSgw4Gqgbhbb6FkmcyBmCnYkSRDFA097V89iufK7BSg2ZHYx"

yelp_api = YelpAPI(api_key)

#search_query
search_term = "pizza"
search_location = "Chicago, IL"
search_sort_by = "rating" #best_match, rating, review_count, distance
search_limit = 20

search_results = yelp_api.search_query( term=search_term ,location=search_location , sort_by=search_sort_by , limit=search_limit)
print(search_results)

for buisness in search_results["businesses"]:
    print(buisness["name"])
    print(buisness["alias"])
    print("\n")

result_df = pd.DataFrame.from_dict(search_results['businesses'])
print(result_df['alias'])
#result_df.to_csv('inclass_yelpapi.csv')
id_for_reviews = 'montis-chicago'

#reviews query
reviews_result = yelp_api.reviews_query(id=id_for_reviews)
print(reviews_result)

for review in reviews_result['reviews']:
    print(review)
    print("\n\n")

reviews_df = pd.DataFrame.from_dict(reviews_result['reviews'])
print(reviews_df['text'])

reviews_df.to_csv(f"{id_for_reviews}_reviews_")