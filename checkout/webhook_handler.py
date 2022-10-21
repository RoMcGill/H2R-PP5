from django.http import HttpResponse

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request


    def handle_event(self, event):

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.item_data
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping_details
        grand_total = round(intent.data.charges[0].amount/100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        try:

            order = Order.objects.get(
                full_name__iexact=shipping_details.name,
                email__iexact=shipping_details.email,
                phone_number__iexact=shipping_details.phone,
                country__iexact=shipping_details.country,
                postcode__iexact=shipping_details.postal_code,
                town_or_city__iexact=shipping_details.city,
                street_address1__iexact=shipping_details.line1,
                street_address2__iexact=shipping_details.line2,
                county__iexact=shipping_details.state,
            )
            order_exists = True
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS verified order already in database',
                status=200)
        except Order.DoesNotExist:
            try:

                order = Order.objects.create(
                    full_namect=shipping_details.name,
                    emailct=shipping_details.email,
                    phone_numberct=shipping_details.phone,
                    countryct=shipping_details.country,
                    postcodect=shipping_details.postal_code,
                    town_or_cityct=shipping_details.city,
                    street_address1ct=shipping_details.line1,
                    street_address2ct=shipping_details.line2,
                    county__=shipping_details.state,
                )

                for item_id, item_data in json.loads(cart)():
                    product = Brand_products.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook recieved: {event["type"]} | ERROR: {e}',
                    status=500)


        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):

        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)