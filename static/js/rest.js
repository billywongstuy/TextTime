function init() {
  init_settings = {
    apiKey : "AIzaSyBlUVfPgmBlDKVRmjBaCNfoEqlpW0zoWhc",
    discoveryDocs : ["https://vision.googleapis.com/$discovery/rest?version=v1"],
    clientId : "texttime-151416",
    scope : "read-write"
  };
  return gapi.client.init(init_settings);
}

function load() {
  return gapi.client.load("https://vision.googleapis.com/$discovery/rest?version=v1");
}

function initAll() {
  init();
  load();
}

function processImage(imagePath) {
  visionRequest = {
    "requests" : [
      {
        "image" : {
          "content" : imageContent
        },
        "features" : [
          {
            "type" : enum(TEXT_DETECTION),
            "maxResults" : 5
          }
        ]
        //imageContext left out for now
      }
    ]
  };
  args = {
    path : "https://vision.googleapis.com/v1/images:annotate",
    method : "POST",
    body : visionRequest
  };
  return gapi.client.request(args);
}

function readFile() {
  if (this.files && this.files[0]) {
    var FR= new FileReader();
    FR.onload = function(e) {
      return e.target.result;
    };
    FR.readAsDataURL( this.files[0] );
  }
}
