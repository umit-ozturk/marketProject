from functools import partial
from products.models import Product
from categories.models import Category
from companies.models import Company
from django.db.models import Count


def int_or_default(value, default=None):
    try:
        return abs(int(value))
    except (ValueError, TypeError):
        return default


int_or_zero = partial(int_or_default, default=0)


def get_category_name():
    cat_ids = Product.objects.values_list('category', flat=True)
    category_names = Category.objects.filter(pk__in=cat_ids).annotate(cat_prod=Count('product'))
    return category_names


def get_company_name():
    com_ids = Product.objects.values_list('company', flat=True)
    company_names = Company.objects.filter(pk__in=com_ids).annotate(com_prod=Count('company'))
    return company_names
