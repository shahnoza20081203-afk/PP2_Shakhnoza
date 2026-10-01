import json
import os
import re


def parse_receipt(file_name="raw.txt"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    product_pattern = r"\d+\.\n([^\n]+(?:\n[^\n]+)?)\n(?=\d+,\d{3}\s*x)"
    products_raw = re.findall(product_pattern, content)
    product_names = [p.replace("\n", " ").strip() for p in products_raw]

    item_prices = re.findall(r"Стоимость\n([\d\s]+,\d{2})", content)
    all_prices = re.findall(r"[\d\s]+,\d{2}", content)

    total_match = re.search(r"ИТОГО:\n([\d\s]+,\d{2})", content)
    total_amount = total_match.group(1).strip() if total_match else None

    datetime_match = re.search(
        r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})", content
    )
    date = datetime_match.group(1) if datetime_match else None
    time = datetime_match.group(2) if datetime_match else None

    payment_method_match = re.search(
        r"(Банковская карта|Наличные):", content, re.IGNORECASE
    )
    payment_method = (
        payment_method_match.group(1) if payment_method_match else "Не найден"
    )

    structured_data = {
        "date": date,
        "time": time,
        "payment_method": payment_method,
        "total_amount": total_amount,
        "products_count": len(product_names),
        "products": product_names,
        "item_prices": [p.strip() for p in item_prices],
        "all_prices": [p.strip() for p in all_prices],
    }

    return structured_data


if __name__ == "__main__":
    result = parse_receipt("raw.txt")

    print(json.dumps(result, ensure_ascii=False, indent=4))