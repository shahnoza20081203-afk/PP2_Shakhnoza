import json
import os

# Получаем точный путь к папке task4, где лежит этот скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "sample-data.json")

try:
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Вывод таблицы
    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
    print(f"{'-'*50} {'-'*20}  {'-'*6}  {'-'*6}")

    imdata = data.get("imdata", [])

    for item in imdata:
        attributes = item.get("l1PhysIf", {}).get("attributes", {})

        dn = attributes.get("dn", "")
        descr = attributes.get("descr", "")
        speed = attributes.get("speed", "inherit")
        mtu = attributes.get("mtu", "")

        print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")

except FileNotFoundError:
    print(f"Файл не найден по пути: {json_path}")