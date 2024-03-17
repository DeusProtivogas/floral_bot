
from floralshop_bot.models import Bouquet, Order

def save_order(order):
    bouquet = Bouquet.objects.filter(name=order['bouquet_name']).first()

    client = Order.objects.get_or_create(
        name=order["name"],
        address=order["address"],
        time=order["time"],
        date=order["date"],
        bouquet=bouquet,
    )

    print(client)
    return client


def get_bouquets_list():
    bouquets = list(Bouquet.objects.order_by('occasion'))

    return bouquets
