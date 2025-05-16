from django.db import models


FOOD_TYPE_CHOICES = {
    "Canned": "Canned",
    "Packet": "Packet",
    "Meat": "Meat",
    "Frozen Meal": "Frozen Meal",
    "Sauce":"Sauce",
    "Pasta":"Pasta",
    "Drink Mix":"Drink Mix",
    "Cereal": "Cereal",
    "Cheese": "Cheese",
    "Lunch Meat": "Lunch Meat",
    "Drink": "Drink",




}
# Create your models here.
class FoodItem(models.Model):
  name = models.CharField(max_length=255)
  food_type = models.CharField(max_length=255, choices=FOOD_TYPE_CHOICES, default="Canned")
  amount_on_hand = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
      return self.name