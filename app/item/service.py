import json

import stripe

from config.settings import STRIPE_SECRETE_KEY, YOUR_DOMAIN

from item.models import Item

stripe.api_key = STRIPE_SECRETE_KEY

def create_checkout_session(item: Item):
    product = create_product(item)
    price = create_price(item).get('data')[0]

    try:
        checkout_session = stripe.checkout.Session.create(
          success_url="https://example.com/success",
          line_items=[{"price": price.get('id'), "quantity": 1}],
          mode="payment",
        )

        return checkout_session

    except Exception as e:
        return str(e)


def create_product(item: Item) -> dict:
    product = None

    try:
        product = stripe.Product.retrieve(id=str(item.pk))

    except stripe.error.InvalidRequestError as e:
        if e.http_status == 404:
            product = stripe.Product.create(id=str(item.pk), name=item.name, description=item.description)

        else:
            product = {'exception': str(e)}

    finally:
        return product

def create_price(item: Item) -> dict:
    price = None

    try:
        if len(stripe.Price.list(product=item.pk)) > 0:
            price = stripe.Price.list(product=item.pk)

        else:
            price = stripe.Price.create(
                currency="usd",
                unit_amount_decimal=item.price,
                product_data={"id": item.pk, "name": item.name},
            )

    except stripe.error.InvalidRequestError as e:
        price = {'exception': str(e)}

    finally:
        return price
