import threading
import requests
import json

def check_url(url, result_list):
    try:
        response = requests.get(url)
        result = {
            "url": url,
            "is_ok": response.ok,
            "status_code": response.status_code if response.ok else None
        }
    except requests.RequestException:
        result = {
            "url": url,
            "is_ok": False,
            "status_code": None
        }

    result_list.append(result)

def main():
    # Чтение URL-адресов из файла
    with open("links.txt", "r") as file:
        urls = file.read().splitlines()

    # Создание списка для хранения результатов
    results = []

    # Создание и запуск потоков
    threads = []
    for url in urls:
        thread = threading.Thread(target=check_url, args=(url, results))
        threads.append(thread)
        thread.start()

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Сохранение результатов в файл JSON
    with open("results.json", "w") as json_file:
        json.dump(results, json_file, indent=2)

if __name__ == "__main__":
    main()