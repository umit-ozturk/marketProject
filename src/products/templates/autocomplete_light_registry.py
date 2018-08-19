import autocomplete_light
from .models import Product

# This will generate a PersonAutocomplete class
autocomplete_light.register(Product,
    # Just like in ModelAdmin.search_fields
    search_fields=['^slug',],
    # This will actually html attribute data-placeholder which will set
    # javascript attribute widget.autocomplete.placeholder.
    autocomplete_js_attributes={'placeholder': 'Other model name ?',},
)