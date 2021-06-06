from django.shortcuts import render, redirect
from . import servises
from .models import Product, Billing_Address
from .forms import Billing_AddressForm


def index(request):
    categories = servises.get_categories()
    sales = servises.get_sale()
    popular_product = Product.objects.all().filter(mini_category_id=4)
    brands = servises.get_brand()
    ctx = {
        "categories": categories,
        "sales": sales,
        "popular_product": popular_product,
        "brands": brands,
    }
    return render(request, 'fashion/index.html', ctx)


def shop(request):
    categories = servises.get_categories()
    mini_categories = servises.get_mini_categories()
    products = servises.get_products()
    brands = servises.get_brand()

    ctx = {
        "categories": categories,
        "mini_categories": mini_categories,
        "products": products,
        "brands": brands,

    }
    return render(request, 'fashion/shop.html', ctx)





def contact(request):
    return render(request, 'fashion/contact.html')


def blog(request):
    blogs = servises.get_blog()
    ctx = {
        "blogs": blogs
    }
    return render(request, 'fashion/blog.html', ctx)


def single_blog(request, blog_id):
    blogs = servises.get_blog()
    blog = servises.get_blog_by_id(blog_id=blog_id)
    ctx = {
        "blog": blog,
        "blogs": blogs
    }
    return render(request, 'fashion/single-blog.html', ctx)


def regular(request):
    regular = servises.get_regular()
    ctx = {
        "regular": regular
    }
    return render(request, 'fashion/regular-page.html', ctx)


def product_details(request, product_id):
    products_details = servises.get_product_details(product_id=product_id)
    print(products_details)
    ctx = {

        "products_details": products_details
    }
    return render(request, 'fashion/single-product-details.html', ctx)


def checkouts(request):
    modal = Billing_Address()
    form = Billing_AddressForm(request.POST or None, instance=modal)
    # order=
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
    return render(request, 'fashion/checkout.html')
