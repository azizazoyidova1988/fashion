from django.db import connection
from contextlib import closing

def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from category""")
        categories = dict_fetchall(cursor)
        return categories


def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from products """)
        products = dict_fetchall(cursor)
        return products


def get_sale():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from sale """)
        sales = dict_fetchall(cursor)
        return sales

def get_mini_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select mini_category.*, category.name as c_name from mini_category
            inner join category on mini_category.category_id = category.id """)
        mini_categories = dict_fetchall(cursor)
        return mini_categories

def get_product_details(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select products.*, brands.name as b_name from products
            inner join brands on products.brands_id = brands.id 
            where products.id =  %s""",[product_id])
        mini_categories = dict_fetchone(cursor)
        return mini_categories


def get_blog():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from blog """)
        blog = dict_fetchall(cursor)
        return blog

def get_blog_by_id(blog_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from blog where blog.id = %s """,
                       [blog_id])
        blogs = dict_fetchone(cursor)
        return blogs


def get_regular():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from regular """)
        regulars = dict_fetchall(cursor)
        return regulars

def get_brand():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from brands """)
        brands = dict_fetchall(cursor)
        return brands

# def get_shop():
#     with closing(connection.cursor()) as cursor:
#         cursor.execute("""select * from shop """)
#         shop = dict_fetchall(cursor)
#         return shop






def get_order():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from  max_way_order """)
        orders = dict_fetchall(cursor)
    return orders


def get_category_by_id(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from  max_way_category 
                 where id = %s""", [pk])
        status = dict_fetchone(cursor)
    return status


def get_categories_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from max_way_category""")
        categories = dict_fetchall(cursor)
    return categories



def get_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from max_way_product""")
        products = dict_fetchall(cursor)
    return products




def get_categories_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  count(max_way_product.id),max_way_category.name ,max_way_product.category_id 
        FROM max_way_category LEFT JOIN max_way_product
		ON max_way_product.category_id=max_way_category.id
		GROUP BY max_way_product.category_id,max_way_category.name 
        ORDER BY COUNT(max_way_product.id) DESC""")
        categories=dict_fetchall(cursor)
        return categories

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))