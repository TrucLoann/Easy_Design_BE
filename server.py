
import time
import os
import random
import json
from flask import Flask, redirect
from payos import PayOS, ItemData, PaymentData
# Keep your PayOS key protected by including it by an environment variable
client_id = 'c4d60cd9-099c-4687-aad3-62541a7b0454'
api_key = "56d34944-99a3-4121-9656-7ec6da7e2c29"
checksum_key = "e3732b19b941ab3e9c5408c3d7b85d1ee4b293a1855bd1168d87c5fee86060d0"

payos = PayOS(client_id, api_key, checksum_key)

app = Flask(__name__, static_folder="public",static_url_path="",template_folder="public")

YOUR_DOMAIN = "http://localhost:3030"


@app.route("/create-payment-link", methods=["POST"])
def create_payment_link():
    try:
        item = ItemData(name="Design Template", quantity=1, price=20000)
        payment_data = PaymentData(
            orderCode=int(time.time()),
            amount=20000,
            description="Thanh toan don hang",
            items=[item],
            cancelUrl="https://easy-design.vercel.app/cancel.html",
            returnUrl="https://easy-design.vercel.app/success.html",
        )
        payment_link_response = payos.createPaymentLink(payment_data)
    except Exception as e:
        return str(e)

    return redirect(payment_link_response.checkoutUrl)


if __name__ == "__main__":
    app.run(port=3030)