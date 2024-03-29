from django import template

register = template.Library()

@register.filter(name='is_in_cart')

def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    # print(keys)
    # print(product, cart)
    return False

@register.filter(name='cart_quantity')

def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    # print(keys)
    # print(product, cart)
    return 0