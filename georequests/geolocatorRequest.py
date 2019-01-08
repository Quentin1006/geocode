from requests import Request

class GeolocatorRequest(Request):
	GEOLOC_API_URL_BASE = 'https://www.googleapis.com/geolocation/v1/geolocate'

	def __init__(self, params):
		if not params:
			raise ValueError("Please set some params to your request")

		super().__init__()

		self.method = 'POST'
		self.url = self.GEOLOC_API_URL_BASE
		self.params = dict(key=params['key'])
		self.json = params['json']



if __name__ == '__main__':
	pass