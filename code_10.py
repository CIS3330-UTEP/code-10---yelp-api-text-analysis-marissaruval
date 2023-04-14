
from yelpapi import YelpAPI
import pandas as pd
import requests
import urllib.parse
import json
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

api_key = "puAjy7iKppGdQ1veYkj7j1CmoNmejmGS3mcRdHAQ0qQ4vrRvKH1zeWVf5fxeSC72IXjl9I6p_WYzq5jnnSgw4Gqgbhbb6FkmcyBmCnYkSRDFA097V89iufK7BSg2ZHYx"
yelp_api = YelpAPI(api_key)

search_food= "sushi"
search_location = "New York, NY"
search_sort_by = "rating" #best_match, rating, review_count, distance
search_limit = 20

search_results = yelp_api.search_query(term=search_food, location=search_location,  sort_by=search_sort_by, limit=search_limit)
print(search_results)

search_term = urllib.parse.quote_plus(search_food)
location = urllib.parse.quote_plus(search_location)
search_sort_by = "rating" 
search_limit = 20
url = f"https://api.yelp.com/v3/businesses/search?location={location}&term={search_term}&sort_by={search_sort_by}&limit={search_limit}"
headers = {
    "accept": "application/json",
    "Authorization": "Bearer puAjy7iKppGdQ1veYkj7j1CmoNmejmGS3mcRdHAQ0qQ4vrRvKH1zeWVf5fxeSC72IXjl9I6p_WYzq5jnnSgw4Gqgbhbb6FkmcyBmCnYkSRDFA097V89iufK7BSg2ZHYx"
}

response = requests.get(url, headers=headers)
response_json = json.loads(response.text)

print(response_json['businesses'])

print("\n")

result_df = pd.DataFrame.from_dict(response_json["businesses"])
print(result_df)
result_df.to_csv("requests_businesses_results.csv")

review_id = "domo-sushi-new-york"
reviews = yelp_api.reviews_query(id=review_id)
print(reviews)

for response in reviews["reviews"]:
    print(response['text'])

#tokens
for value in response['text']:
    token = nltk.word_tokenize(value)
    tag = nltk.pos_tag(token)
    print(tag)
    for t in tag:
        if t[1] =="JJ" or t[1] =="JJS" or t[1] == "NN":
            print(t[0])


analyer = SentimentIntensityAnalyzer()
for rev in response['text']:
    sen_score = analyer.polarity_scores(rev)
    print(rev)
    print(sen_score)

'''
new_text=[]
for tokens in tag:
    if tag[0] not in stopwords:
        print(tag[0])
        print(tag)
        new_text.append(tag[0])
print("\noriginal")
print(value)
print("\nnew")     
print()   
'''