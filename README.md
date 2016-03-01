# 500px.py
Un script de consola escrito en python para descargar imágenes masivamente del servicio 500px pudiendo indicar la palabra clave, así como la calidad de las mismas.

## Configurar el script

1. Accede a [http://500px.com/settings/applications]()
2. Crea una nueva app desde el menú **Register your application**.
3. Teclea "http://www.500px.com" o cualquier otra en los campos **Application URL**, **Callback URL**, **JavaScript SDK Callback URL** y **Support URL**
4. Una vez creada la app, puedes consultar el **Consumer Key** en el apartado **"See application details"**.
5. Abre el fichero **500px.py** en tu editor favorito
6. Modifica la siguiente linea para incluir la información que acabas de generar para tu app

```python
    consumer_key = "PON_AQUI_TU_CONSUMER_KEY"
```

## Utilizar el script

Un ejemplo de llamada sería el siguiente:

```python
    python3 500px.py -term "Dogs" -size 2048 -results 10 -path images
```

Para más información sobre los diferentes tamaños que pueden informarse en el campo **size**, se puede acceder a la siguiente dirección [https://github.com/500px/api-documentation/blob/master/basics/formats_and_terms.md]().
