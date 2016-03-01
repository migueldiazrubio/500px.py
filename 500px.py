import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-term", "--term", help="Palabra de busqueda", type=str)
parser.add_argument("-size", "--size", help="Tamaño de las imagenes", type=str)
parser.add_argument("-results", "--results", help="Numero de resultados", type=str)
parser.add_argument("-path", "--path", help="Directorio para las descargas", type=str)
args = parser.parse_args()

term = args.term
size = args.size
results = args.results
path = args.path

if args.term and args.size and args.results and args.path:

    consumer_key = "PON_AQUI_TU_CONSUMER_KEY"
    photos_search_endpoint = "https://api.500px.com/v1/photos/search?"

    url = photos_search_endpoint + "consumer_key=" + consumer_key + "&term=" + term + "&image_size=" + size + "&rpp=" + results + "&exclude=Nude"

    response = requests.get(url)

    json = response.json()
    photos = json["photos"]

    count = 1

    for photo in photos:

        filename = "image" + str(count) + ".jpg"
        try:
            os.mkdir(path)
        except Exception:
            pass

        photo_data = requests.get(photo["image_url"], stream=True)
        if photo_data.status_code == 200:
            with open(os.path.join(path, filename), "wb") as myfile:
                for chunk in photo_data.iter_content(1024):
                    myfile.write(chunk)
                myfile.close()
        print(photo["image_url"])
        count += 1

else:

    parser.error("Debe indicar los siguientes parametros:\n- term: con el criterio de busqueda\n- size: con el tamaño de las imagenes (100, 200, 440, 600, 1080, 1600, 2048)\n- results: con el numero de imagenes a recuperar\n- path: Directorio para las descargas")
