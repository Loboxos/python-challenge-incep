import requests

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"

    @classmethod
    def is_hot_in_pehuajo(cls):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={cls.LAT}&lon={cls.LON}&appid={cls.API_KEY}&units=metric"
        try:
            response = requests.get(url)
            data=response.json()
            response.raise_for_status()
            temp_act = data['main']['temp']
            print(f"la temperatura actual es : {temp_act}")
            return temp_act > 28
        except (requests.RequestException,KeyError )as e:
            print(f"error : {e}")
            return False
print(GeoAPI.is_hot_in_pehuajo())