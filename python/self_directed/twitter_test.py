import twitter
import time

api = twitter.Api(consumer_key = "0GH7tu4IVadciAf0bmpY1oCE7",
	consumer_secret = "k6pI2XkczMXDYIiVGhojVMPnR3ivNsqEjBAgWD1SHjyLIO0Tw3",
	access_token_key = "788065625612521473-tobhL5J7VkpYUnVUCoYZr8pQA8M0HDu",
	access_token_secret = "EAUtppeePeOUILJ6mR18tx0MFaZsd9PmWriBgr1pth3kK")

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