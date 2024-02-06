import requests
import sys


# Найти объект по координатам.
def reverse_geocode(ll):
    geocoder_request_template = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={ll}&format=json"

    # Выполняем запрос к геокодеру, анализируем ответ.
    geocoder_request = geocoder_request_template.format(**locals())
    response = requests.get(geocoder_request)

    if not response:
        raise RuntimeError(
            """Ошибка выполнения запроса:
            {request}
            Http статус: {status} ({reason})""".format(
                request=geocoder_request, status=response.status_code, reason=response.reason))

    # Преобразуем ответ в json-объект
    json_response = response.json()

    # Получаем первый топоним из ответа геокодера.
    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"] if features else None



def download_map(ll=None, map_type='map', zoom=15, add_params=None, size=450):
    params = {
        'll': ll,
        'l': map_type,
        'z': zoom,
        'size': f'{size},{size}' 
    }
    map_req = f"http://static-maps.yandex.ru/1.x"
    print(map_req)

    if add_params:
        map_req += '&' + add_params

    response = requests.get(map_req, params)

    if not response:
        print('Ошибка выполнения запроса')
        sys.exit(1)

    map_file = 'map.png'
    try:
        with open(map_file, mode='wb') as file:
            file.write(response.content)
    except IOError as ex:
        print('Ошибка при записи в файл', ex)
        sys.exit(2)

