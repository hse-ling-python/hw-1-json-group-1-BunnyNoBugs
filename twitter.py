import json
from pprint import pprint
from collections import Counter
from string import punctuation
import re

twitter = []
for line in open('hw_3_twitter.json'):
    twitter.append(json.loads(line))
# print(len(twitter))

# ok = 0
# for tweet in twitter:
#     if len(tweet) > 1:
#         ok += 1
# print('{percent}% твитов составляют неудаленные записи'.format(percent=round(ok/len(twitter)*100, 2)))

# languages = []
# for tweet in twitter:
#     if len(tweet) > 1:
#         languages.append(tweet['lang'])
# languages = Counter(languages).most_common(10)
# print('Топ-10 самых популярных языков твитов: {most_popular}'.format(most_popular=' '.join([x[0] for x in languages])))

# users = []
# active_users = []
# for tweet in twitter:
#     if len(tweet) > 1:
#         user_id = (tweet['user']['id'])
#         if user_id in users and id not in active_users:
#             active_users.append(user_id)
#         users.append(user_id)
# print('{active_users_number} пользователей имеют больше одного твита'.format(active_users_number=len(active_users)))

# hashtags = []
# for tweet in twitter:
#     if len(tweet) > 1:
#         if tweet['entities']['hashtags']:
#             for hashtag in tweet['entities']['hashtags']:
#                 hashtags.append(hashtag['text'])
# print('Топ-20 самых популярных хэштегов: {top_twenty_hashtags}'.format(
#     top_twenty_hashtags=', '.join([x[0] for x in Counter(hashtags).most_common(20)])))

# preprocessed_twitter = []
# for tweet in twitter:
#     if len(tweet) > 1 and tweet['lang'] == 'en' and 'retweeted_status' not in tweet:
#         if tweet['truncated']:
#             preprocessed_twitter.append(
#                 [x.strip(punctuation) for x in tweet['extended_tweet']['full_text'].lower().split()])
#         else:
#             preprocessed_twitter.append([x.strip(punctuation) for x in tweet['text'].lower().split()])
# frequency_dictionary = Counter([word for tweet in preprocessed_twitter for word in tweet])
# print('Топ-10 самых частых слов в твитах на английском языке: {top_ten_words}'.format(
#     top_ten_words=', '.join([word[0] for word in frequency_dictionary.most_common(10)])))

# followers_numbers = []
# for tweet in twitter:
#     if len(tweet) > 1:
#         if not (tweet['user']['name'], tweet['user']['followers_count']) in followers_numbers:
#             followers_numbers.append((tweet['user']['name'], tweet['user']['followers_count']))
# followers_numbers.sort(key=lambda i: i[1], reverse=True)
# print('Топ-10 пользователей по количеству подписчиков: {top_ten_followers_numbers}'.format(
#     top_ten_followers_numbers=', '.join([followers_numbers[i][0] for i in range(10)])))

sources = []
for tweet in twitter:
    if len(tweet) > 1:
        sources.append(re.search('<.+?>(.+?)<.+>', tweet['source']).group(1))
sources = Counter(sources)
print('Топ-10 самых популярных источников твитов: {top_ten_sources}'.format(
    top_ten_sources=', '.join(source[0] for source in sources.most_common(10))))
