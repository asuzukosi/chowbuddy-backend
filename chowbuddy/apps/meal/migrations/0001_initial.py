# Generated by Django 4.1.7 on 2023-04-12 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('delivery', '0001_initial'),
        ('restaurant', '0003_alter_dish_restaurant'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.dish')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_orders', models.ManyToManyField(to='meal.dishorder')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('next_interval', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customers', models.ManyToManyField(related_name='meal_plans', to='customer.customer')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal.meal')),
            ],
        ),
        migrations.CreateModel(
            name='MealOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[['PENDING', 'PENDING'], ['ACCEPTED', 'ACCEPTED'], ['DELIVERED', 'DELIVERED']], default='PENDING', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.delivery')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal.meal')),
            ],
        ),
    ]
