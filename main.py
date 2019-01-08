from geoservice import GeoService
from timeit import timeit

key = '' # insert google key
params1 = {
	'address': 'santa cruz'
}

params2 = {
	'latlng': '80,20'
}

def timer(func, *args, **kwargs):
	res = []
	def wrapped():
		return res.append(func(*args, **kwargs))
	timeit(wrapped, number=3000)
	return res


geo = GeoService(key)
t = timer(geo.geocode, params1)


geolocation = geo.geolocate()


pass