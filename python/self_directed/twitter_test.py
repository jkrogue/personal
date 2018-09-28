import twitter
import time

with open('twitter_info.txt') as f:
	twitter_info = f.read().split('\n')

print(twitter_info)
for each in twitter_info:
	print(each)
api = twitter.Api(consumer_key = twitter_info[0],
	consumer_secret = twitter_info[1],
	access_token_key = twitter_info[2],
	access_token_secret = twitter_info[3])

def to_string_time(struct_time):
	return "{}-{}-{}".format(struct_time.tm_year,str(struct_time.tm_mon).zfill(2),str(struct_time.tm_mday).zfill(2))

def search_all(term, start_time = "2015-01-01"):
	results = []
	end_time = to_string_time(time.gmtime())
	while True:
		curr_results = api.GetSearch(term = term,until=end_time,since=start_time)
		results += curr_results

		print(results[0])

		#If less than 15 results are returned than we must be done
		if len(curr_results) < 15:
			break

		#Update end_time to the time of the last returned tweet
		end_time = to_string_time(time.gmtime(results[14].created_at_in_seconds))
	return results

results = search_all(term = input("Search for: "), start_time = input("Enter start date (YYYY-MM-DD): "))

print(len(results))