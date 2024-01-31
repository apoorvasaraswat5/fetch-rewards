import uuid
from math import ceil


def generate_unique_id():
    """
    Generates unique ID for the receipt
    :return: unique ID
    """
    uuid_key = str(uuid.uuid4())
    return uuid_key


def calculate_points(data):
    """
    Calculates points against the receipt data based
    on some business rules
    :param data: receipt data
    :return: points
    """
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
    """
    One point for every alphanumeric character in the retailer name
    """
    points = 0
    for c in retailer_name:
        if c.isalnum():
            points += 1
    return points


def get_points_on_total(total):
    """
    50 points if the total is a round dollar amount with no cents.
    25 points if the total is a multiple of 0.25.
    """
    points = 0
    if float(total).is_integer():
        points += 50

    if float(total)%0.25 == 0:
        points += 25
    return points


def get_points_on_items(items):
    """
    5 points for every two items on the receipt.
    If the trimmed length of the item description is a multiple of 3,
    multiply the price by 0.2 and round up to the nearest integer.
    The result is the number of points earned.
    """
    points = 0
    points += (len(items)//2)*5

    for item in items:
        desc = item.get("shortDescription").strip()
        if len(desc)%3 == 0:
            updated_price = ceil(float(item["price"]) * 0.2)
            points += updated_price
    return points


def get_points_on_date_and_time(purchase_date,purchase_time):
    """
    6 points if the day in the purchase date is odd.
    10 points if the time of purchase is after 2:00pm and before 4:00pm.
    """
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
