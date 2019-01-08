from requests.adapters import HTTPAdapter
from georequests.geocoderRequest import GeocoderRequest
from georequests.geolocatorRequest import GeolocatorRequest
import json



# check status to see if all went well,
# status: OK --> good
# status: OVER_QUERY_LIMIT --> limit exceeded

# maximum de requetes par jour est de 2500

class GeoService:
	TIMEOUT = 10

	def __init__(self, _key):
		self._request = None
		if _key:
			self._key = _key
		else:
			raise ValueError('No key provided')

	def _get(self, *p):
		params = p[0] if len(p) > 0 else {}

		# on transforme notre requete en PreparedRequest
		prepped = self._request.prepare()
		self._request = None
		response = HTTPAdapter().send(prepped, timeout=self.TIMEOUT)
		return json.loads(response)

	def setKey(self, new_key):
		if isinstance(new_key, str):
			self.key = new_key
		else:
			raise TypeError('key must be a string')

	def geocode(self, p):
		p['key'] = self._key
		self._request = GeocoderRequest(p)
		return self._get(p)

	def geolocate(self, *p):
		p = {'json': p, 'key': self._key}
		self._request = GeolocatorRequest(p)
		return self._get(p)

	@staticmethod
	def buildLatLng(lat, lng):
		return '{}, {}'.format(lat, lng)


if __name__ == '__main__':
	pass