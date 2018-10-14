from django.contrib import admin
from .models import (
	Extra_Footer_Contact,
	Extra_Footer_Head_1,
	Extra_Footer_Head_2,
	Extra_Footer_Head_3,
	Extra_Footer_Bottom_1,
	Extra_Footer_Bottom_2,
	Extra_Footer_Bottom_3,
	)

# Register your models here.

admin.site.register(Extra_Footer_Contact)
admin.site.register(Extra_Footer_Head_1)
admin.site.register(Extra_Footer_Head_2)
admin.site.register(Extra_Footer_Head_3)
admin.site.register(Extra_Footer_Bottom_1)
admin.site.register(Extra_Footer_Bottom_2)
admin.site.register(Extra_Footer_Bottom_3)
