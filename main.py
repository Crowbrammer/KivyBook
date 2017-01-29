from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json

class AddLocationForm(BoxLayout):
	search_input = ObjectProperty()

	def search_location(self):
		search_template = "http://api.openweathermap.org/data/2.5/find?q={}&type=like&APPID=" + "e2c59545ea674f80ab4ce01138ef7b58"
		search_url = search_template.format(self.search_input.text)
		
		request = UrlRequest('http://api.openweathermap.org/data/2.5/weather?lat=34&lon=139&APPID=e2c59545ea674f80ab4ce01138ef7b58', self.found_location)

	def found_location(self, request, data):
		data = json.loads(data.decode()) if not isinstance(data, dict) else data
		print(data)
		cities = ["{} ({})".format(d['name'], d['sys']['country'])
			for d in data['list']]
		self.search_results.item_strings = cities
		print("\n".join(cities))
		
		
	def current_location(self):
		current_location_template = "api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=e2c59545ea674f80ab4ce01138ef7b58"
		coordinates = self.search_input.text.split(',') #Needs to remove spaces
		current_location_url = current_location_template.format(coordinates[0], coordinates[1])
		request = UrlRequest(current_location_url, self.found_location)
		

class WeatherApp(App):
	pass

if __name__ == '__main__':
	WeatherApp().run()