from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "shop"

    def __str__(self):
        return self.title


class Sale(models.Model):
    product_name = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    discount = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sale"

    def __str__(self):
        return self.product_name


class Category(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class Mini_Category(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "mini_category"

    def __str__(self):
        return self.name


class Brands(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "brands"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=1)
    discount = models.BooleanField(default=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    size = models.CharField(max_length=10, blank=False, null=False)
    color = models.CharField(max_length=50, blank=False, null=False)
    brands = models.ForeignKey(Brands, blank=False, null=True, on_delete=models.SET_NULL)
    mini_category = models.ForeignKey(Mini_Category, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name


class Billing_Address(models.Model):
    first_name = models.TextField(max_length=100, blank=False, null=False)
    last_name = models.TextField(max_length=100, blank=False, null=False)
    company_name = models.TextField(max_length=100, blank=False, null=False)
    country = models.TextField(max_length=30, blank=False, null=False)
    address = models.TextField(max_length=100, blank=False, null=False)
    postcode = models.CharField(max_length=30, blank=False, null=False)
    town_city = models.CharField(max_length=50, blank=False, null=False)
    province = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=40, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "billing_address"

    def __str__(self):
        return self.first_name


class Order(models.Model):
    products = models.JSONField(blank=False, null=False)
    all_price = models.IntegerField(blank=False, null=False, default=0)
    status = models.IntegerField(blank=False, null=False, default=1)
    payment_type = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order"

    def __str__(self):
        return self.products


class Blog(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "blog"

    def __str__(self):
        return self.title


class Regular(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "regular"

    def __str__(self):
        return self.title
