import json

import stripe

from config.settings import STRIPE_SECRETE_KEY, YOUR_DOMAIN

from item.models import Item

stripe.api_key = STRIPE_SECRETE_KEY


def create_checkout_session(item: Item) -> str:
    create_product(item)
    create_price(item)
    price = stripe.Price.list(product=str(item.pk)).get('data')[0].get('id')
    try:
        checkout_session = stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=[{"price": price, "quantity": 1}],
            mode="payment",
        )
        return checkout_session.get('id')

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
            product = {'exception product': str(e)}

    finally:

        return product


def create_price(item: Item):
    try:
        if len(stripe.Price.list(product=str(item.pk)).get("data")) == 0:
            stripe.Price.create(
                currency="usd",
                unit_amount=item.price,
                product=f"{item.pk}"
            )

    except stripe.error.InvalidRequestError as e:
        return str(e)
