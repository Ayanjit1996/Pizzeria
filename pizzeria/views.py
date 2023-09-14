from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Order, Pizza
from .serializers import OrderSerializer
from .tasks import update_order_status

def set_default_order_placing_time():
    return timezone.now()

class Add_Pizza_order(APIView):
    def post(self, request):
        # Deserialize the request data using OrderSerializer
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():

            pizzas_data = request.data.get('pizzas', [])

            # Check if there is at least one pizza in the order
            if not pizzas_data:
                return Response({"error": "At least one pizza is required in the order"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Create the order instance
            order = serializer.save()

            # Get the pizza data from the request
            pizzas_data = request.data.get('pizzas', [])
            # Create and associate Pizza instances with the order
            for pizza_data in pizzas_data:
                # Access the pizza attributes from pizza_data
                pizzabase = pizza_data.get('pizzabase', '')
                cheese = pizza_data.get('cheese', '')
                toppings = pizza_data.get('toppings', [])

                # Print the values
                print(f'pizzabase: {pizzabase}, cheese: {cheese}, toppings: {toppings}')
                # Check if the sizes meet the required conditions
                if len(pizzabase) == 1 and len(cheese) == 1 and len(toppings) == 5:
                    # Create a new pizza order and assign the order instance
                    pizza_order = Pizza(order=order, pizzabase=pizzabase, cheese=cheese, toppings=toppings)
                    # Save the pizza order to the database
                    pizza_order.save()
                else:
                    # Debugging: Print a message
                    print("Invalid pizza data")

                    # Handle the case where the conditions are not met (e.g. return an error response)
                    return Response({"error": "Invalid pizza data"}, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CurrentOrderStatusView(APIView):
    def get(self, request):
        # Celery task
        update_order_status.delay()
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        # Extract only order_id and status from the serialized data
        result_data = [{'order_id': item['order_id'], 'status': item['status']} for item in serializer.data]
        return Response(result_data, status=status.HTTP_200_OK)


