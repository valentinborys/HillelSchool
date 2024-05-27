import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params)
photos = response.json()
print(photos)

if 'photos' in photos:
    for idx, photo in enumerate(photos['photos']):
        img_url = photo['img_src']

        img_response = requests.get(img_url)

        if img_response.status_code == 200:
            file_name = f"mars_photo{idx + 1}.jpg"

            with open(file_name, 'wb') as file:
                file.write(img_response.content)

            print(f"Збережено {file_name}")
        else:
            print(f"Помилка при скачуванні фото {img_url}")

else:
    print("Фото не знайдено")