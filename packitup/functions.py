# importing requests package
import requests	

def ESGNews():
	
	# ESG news api
	# following query parameters are used
	# source, sortBy and apiKey
	url = ('https://newsapi.org/v2/everything?'
       'q=ESG&'
       'language=en&'
       'from=2022-08-20&'
       'sortBy=relevancy&'
       'apiKey=bcc83430e9964c40ab973b1012bd82cb')
	    
	# fetching data in json format
	response = requests.get(url)
	open_ESG_page = response.json()

	# getting all articles in a string article
	article = open_ESG_page["articles"]

	# empty list which will
	# contain all trending news
	results = []
	
	for ar in article:
		results.append(ar["title"])
		results.append(ar["description"])
		results.append(ar["source"])
		results.append(ar["url"])
	
	for i in range(len(results)):
		
		# printing all trending news
		print(i + 1, results[i])

# Driver Code
if __name__ == '__main__':
	
	# function call
	ESGNews()
