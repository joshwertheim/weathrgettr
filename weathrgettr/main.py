import urllib2
import json

class Feed(object):
    """Feed object - Responsible for loading JSON data at given URL"""
    url = ""
    response_data = ""
    formatted_response_data = ""
    json_representation = ""

    def __init__(self, url):
        self.url = url

    def load_and_prepare(self):
        try:
            self.response_data = urllib2.urlopen(self.url)
        except:
            self.json_representation = "No data at URL."
            return
        self.formatted_response_data = json.load(self.response_data) 
        self.formatted_response_data = json.dumps(self.formatted_response_data, sort_keys=True, indent=4, separators=(',', ': ')) # pretty printed json file object data
        self.json_representation = json.loads(self.formatted_response_data)

    @property
    def get_representation(self):
        if self.json_representation == "No data at URL.":
            return False, self.json_representation
        else:
            return True, self.json_representation

class Location(object):
    """Location object - Responsible for holding required weather properties for each location"""




feed = Feed("http://api.wunderground.com/api/5b40e5dfadfc56e9/conditions/q/CA/San_Jose.json")
feed.load_and_prepare()
# print feed.formatted_response_data


