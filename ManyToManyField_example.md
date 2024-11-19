# models.py: `ManyToManyField` example

## Modify models.py

```python
from django.db import models

# Create your models here.
class Pizza(models.Model):
    """Create pizza.objects and connect it with multiple topping."""
    name = models.CharField(max_length=200)
    # 'models.ManyToManyField': Connect a multiple pizzas with multiple toppings.
    toppings = models.ManyToManyField("Topping")

    def __str__(self) -> str:
        return self.name

class Topping(models.Model):
    """Create topping.objects."""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
```

# Create a pizza with multiple toppings using the Django shell:

The below shell syntax is particularly useful because:

1. It won't create duplicate pizzas or toppings
2. It's more efficient as it uses `get_or_create`
3. It provides clear output of what was created
4. It can be safely run multiple times

```python
# Start Django shell
python manage.py shell

# More robust version with error checking
from your_app_name.models import Pizza, Topping

# Create pizza if it doesn't exist
supreme, created = Pizza.objects.get_or_create(name="Supreme")

# List of toppings we want
topping_names = ["Pepperoni", "Mushrooms", "Onions", "Bell Peppers", "Sausage"]

# Create toppings if they don't exist and add them to pizza
for topping_name in topping_names:
    topping, created = Topping.objects.get_or_create(name=topping_name)
    supreme.toppings.add(topping)

# Print the result
print(f"Pizza '{supreme.name}' has the following toppings:")
for topping in supreme.toppings.all():
    print(f"- {topping.name}")
```

# Find all pizzas that have a specific topping using the Django shell:

```python
# Start Django shell
python manage.py shell

# Import models
from your_app_name.models import Pizza, Topping

# Method 1: Get pizzas with a specific topping using the topping object
pepperoni = Topping.objects.get(name="Pepperoni")
pizzas_with_pepperoni = Pizza.objects.filter(toppings=pepperoni)

# Print results
print(f"\nPizzas with {pepperoni.name}:")
for pizza in pizzas_with_pepperoni:
    print(f"- {pizza.name}")

# Method 2: Get pizzas with a specific topping using the topping name
pizzas_with_mushrooms = Pizza.objects.filter(toppings__name="Mushrooms")
print("\nPizzas with Mushrooms:")
for pizza in pizzas_with_mushrooms:
    print(f"- {pizza.name}")

# Method 3: Get pizzas and their toppings in a single query (more efficient)
pizzas_with_toppings = Pizza.objects.filter(
    toppings__name="Pepperoni"
).prefetch_related('toppings')

print("\nPizzas with Pepperoni and their toppings:")
for pizza in pizzas_with_toppings:
    print(f"\n{pizza.name} has toppings:")
    for topping in pizza.toppings.all():
        print(f"- {topping.name}")

# Method 4: Find pizzas with multiple specific toppings
pizzas_with_both = Pizza.objects.filter(
    toppings__name__in=["Pepperoni", "Mushrooms"]
).distinct()  # distinct() is needed to avoid duplicate pizzas

print("\nPizzas with both Pepperoni AND Mushrooms:")
for pizza in pizzas_with_both:
    print(f"- {pizza.name}")
```

Each method has its uses:

- Method 1 is good when you already have a topping object
- Method 2 is simpler when you just know the topping name
- Method 3 is more efficient when you need to access the toppings later
- Method 4 is useful for finding pizzas with multiple specific toppings
- The complex example is great for analysis and statistics

Remember that `prefetch_related` is useful for performance when you need to access the related objects (like toppings) later in your code, as it reduces the number of database queries.
