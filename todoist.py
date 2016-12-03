import todoist, urllib2, json

def addProject(s):
	api = todoist.TodoistAPI(access_token)
	project = api.projects.add(s[0])
	id = project.id
	api.commit()
	index = 1
	
	while index < len(s):
		item = api.items.add(s[index],id)
	api.commit()
	
	
	
def getToken(id,secret,code):
	u = urllib.open
	root = "https://todoist.com/oauth/access_token"
	url = root + "?client_id=" + id + "&client_secret=" + secret + "&code=" + code
	
	
	
query = {
		client_id: "08036ba1ba6f47e4ac6a04882ae53787",
		client_secret: "3be5d79578a94267aaaa3c11ade9d6b7",
		code: rCode,
	}
	
	var root = "https://todoist.com/oauth/access_token"
	var url = root + "?client_id=" + query.client_id + "&client_secret=" + query.client_secret + "&code=" + query.code

