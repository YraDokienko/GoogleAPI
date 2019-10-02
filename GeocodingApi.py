import requests

API_ID = 'AIzaSyDChIbwkFxmKZvPS63ySo3Yktg3fVcj2vM'


class LocationApi():
    url = 'https://maps.googleapis.com/maps/api/geocode/json'

    def get_location(self, address=None, latlng=None):
        response = requests.get(self.url, {'key': API_ID, 'address': address, 'latlng': latlng, })
        return response.json()

    def get_coordinates_by_address(self, address):
        """Метод возвращает координаты локации по ЗАПРОСУ"""
        coordinates = self.get_location(address=address)
        print('Запрос по адрессу:  {}\nОтвет - Координаты:\n    lat = {}\n    lng = {}\n'.format
                     (coordinates['results'][0]['formatted_address'],
                      coordinates['results'][0]['geometry']['location']['lat'],
                      coordinates['results'][0]['geometry']['location']['lng']))

    def get_address_by_coordinates(self, *args):
        """Метод возвращат данные локации по координатам"""
        if type(args[0]) == list:
            lat = args[0][0]
            lng = args[0][1]
        else:
            lat = args[0]
            lng = args[1]
        address = self.get_location(latlng='{},{}'.format(lat, lng))
        print('Запрос по координатам: lat = {} lng = {}\nОтвет - Локация: {}\n'.format
              (lat, lng, address['results'][0]['formatted_address']))


location = LocationApi()
location.get_coordinates_by_address('Derybasivska Street, 23')
location.get_address_by_coordinates([46.483955, 30.737055])
location.get_address_by_coordinates(46.483955, 30.737055)

