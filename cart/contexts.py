from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from dishes.models import Dish

def cart_contents(request):

    cart_items = []
    total = 0
    dish_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            dish = get_object_or_404(Dish, pk=item_id)
            total += item_data * dish.price
            dish_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'dish': dish,
            })
        else:
            dish = get_object_or_404(Dish, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * dish.price
                dish_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'dish': dish,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
 
    grand_total = delivery + total
    context = {
        'cart_items': cart_items,
        'total': total,
        'dish_count': dish_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
