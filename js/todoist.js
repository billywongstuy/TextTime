function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}


function main() {
	
	query = {
		client_id: "08036ba1ba6f47e4ac6a04882ae53787",
		state: "3be5d79578a94267aaaa3c11ade9d6b7",
		scope: ["data:read_write", "task:add"],
		redirect_uri: "urn:ietf:wg:oauth:2.0:oob",
	}
	
	
	var main = "https://todoist.com/oauth/authorize?"
	var url = main + "client_id=" + query.client_id + "&scope=" + query.scope + "&state=" + query.state;

	
	window.location.href = url;
	

}