import todoist

def addProject(s):
	api = todoist.TodoistAPI(access_token)
	project = api.projects.add(s[0])
	id = project.id
	api.commit()
	index = 1
	
	while index < len(s):
		item = api.items.add(s[index],id)
	api.commit()
	
	
	

