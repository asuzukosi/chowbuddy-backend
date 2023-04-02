from django.db import models
from restaurant.models import Dish, Restaurant
from customer.models import Customer
from delivery.models import Delivery, Deliverer
from typing import List
# Create your models here.

class DishOrder(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
class Meal(models.Model):
    dish_orders =  models.ManyToManyField(DishOrder)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    def calculate_total_price(self):
        total = 0.0
        for dish_order in self.dish_orders:
            total += dish_order.amount
        return total
class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    meal =  models.ForeignKey(Meal, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customers = models.ManyToManyField(Customer, related_name="meal_plans")
    next_interval = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

MEAL_ORDER_STATUSES = [["PENDING", "PENDING"], ["ACCEPTED", "ACCEPTED"], ["DELIVERED", "DELIVERED"]]
class MealOrder(models.Model):
    meal =  models.ForeignKey(Meal, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=MEAL_ORDER_STATUSES, default="PENDING")
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @staticmethod
    def getAllOrdersForCustomer(self, customerId):
        orders:List[MealOrder] = MealOrder.objects.all()
        customer = Customer.objects.get(id=customerId)
        filtered_orders = []
        for order in orders:
            if order.delivery.customer == customer:
                filtered_orders.append(order)
        return filtered_orders
    
    @staticmethod
    def getAllOrdersFromRestaurant(self, restaurantId):
        orders:List[MealOrder] = MealOrder.objects.all()
        restaurant = Restaurant.objects.get(id=restaurantId)
        filtered_orders = []
        for order in orders:
            if order.meal.restaurant == restaurant:
                filtered_orders.append(order)
        return filtered_orders

    @staticmethod
    def create_order(dishorders, restaurant, deliverer, customer):
        restaurant = Restaurant.objects.get(id=restaurant)
        meal:Meal = Meal.objects.create(restaurant=restaurant)
        deliverer = Deliverer.objects.get(id=deliverer)
        customer = Customer.objects.get(id=customer)
        
        for dishorder in dishorders:
            db_dishorder = DishOrder.objects.create(**dishorder)
            meal.dish_orders.add(db_dishorder)
        meal.save()
        delivery = Delivery.objects.create(deliverer=deliverer, restaurant=restaurant, customer=customer)
        order = MealOrder.objects.create(meal=meal, price=meal.calculate_total_price(), delivery=delivery)
        order.save()
        return order
