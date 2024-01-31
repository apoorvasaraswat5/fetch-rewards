import uuid
from math import ceil

def generate_unique_id():
    # unique ID for the receipt
    uuid_key =  str(uuid.uuid4())
    return uuid_key


def calculate_points(data):
    points = 0

    retailer_name = data.get("retailer","")
    items = data.get("items",[])
    total = float(data.get("total",0))
    purchase_date = data.get("purchaseDate")
    purchase_time = data.get("purchaseTime")

    points += get_points_on_retailer_name(retailer_name)
    points += get_points_on_total(total)
    points += get_points_on_items(items)
    points += get_points_on_date_and_time(purchase_date,purchase_time)
    return points


def get_points_on_retailer_name(retailer_name):
    points = 0
    for c in retailer_name:
        if c.isalnum():
            points += 1
    return points


def get_points_on_total(total):
    points = 0
    if float(total).is_integer():
        points += 50

    if float(total)%0.25 == 0:
        points += 25
    return points


def get_points_on_items(items):
    points = 0
    points += (len(items)//2)*5

    for item in items:
        desc = item.get("shortDescription").strip()
        if len(desc)%3 == 0:
            updated_price = ceil(float(item["price"]) * 0.2)
            points += updated_price
    return points


def get_points_on_date_and_time(purchase_date,purchase_time):
    points = 0
    date_tokens = purchase_date.split("-")
    day = int(date_tokens[2])
    if day%2 != 0:
        points += 6
    time_tokens = purchase_time.split(":")
    hour = time_tokens[0]
    if hour>="14" and hour<"16":
        points += 10
    return points
