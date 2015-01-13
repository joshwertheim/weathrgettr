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
    """Location object - Responsible for saving weather properties for each location"""

    def __init__(self, location_name, temp_f, temp_c, temp_full, weather_desc, observation_time):
        self.location_name = location_name
        self.temp_f = temp_f
        self.temp_c = temp_c
        self.temp_full = temp_full
        self.weather_desc = weather_desc
        self.observation_time = observation_time

    def print_string_representation(self):
        print self.location_name
        print self.temp_full
        print self.weather_desc
        print self.observation_time

def main():
    feed = Feed("http://api.wunderground.com/api/5b40e5dfadfc56e9/conditions/q/CA/San_Jose.json")
    feed.load_and_prepare()

    info = feed.get_representation[1]
    current = info.get("current_observation")

    full = current.get("display_location").get("full")
    temp_f = current.get("temp_f")
    temp_c = current.get("temp_c")
    weather = current.get("weather")
    temperature_string = current.get("temperature_string")
    obs_time = current.get("observation_time")

    location = Location(full, temp_f, temp_c, temperature_string, weather, obs_time)
    location.print_string_representation()

    # print current
    # print feed.formatted_response_data

if __name__ == "__main__":
    main()




