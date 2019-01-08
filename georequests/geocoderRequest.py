from requests import Request
import os.path


class GeocoderRequest(Request):
	GEOCODE_API_URL_BASE = 'https://maps.googleapis.com/maps/api/geocode/'

	def __init__(self, params):
		if not params:
			raise ValueError("Please set some params to your request")

		if self._isReverted(params):
			self._verifyReverseGeocoderRequest(params)
		else:
			self._verifyGeocoderRequest(params)

		if not 'output_format' in params:
			params['output_format'] = 'json'

		super().__init__()

		self.method = 'GET'
		self.url = os.path.join(self.GEOCODE_API_URL_BASE, params['output_format'])
		self.params = params


	def _isReverted(self, p):
		reverse = False
		if 'latlng' in p or 'placeid' in p:
			reverse = True

		return reverse

	def _verifyGeocoderRequest(self, p):
		if not 'address' in p and not 'components' in p:
			raise ValueError("Missing parameter address or components")


	def _verifyReverseGeocoderRequest(selfself, p):
		if not 'latlng' in p and not 'placeid' in p:
			raise ValueError("Missing parameter latlng or placeid")



if __name__ == '__main__':
	pass