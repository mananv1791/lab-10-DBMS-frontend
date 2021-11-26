from django.contrib import admin
from .models import Customer, User, HasProRaw, Login, Product, RaisedIssue, RawMaterial, Roles, RolesRoleDesc, Sales, Supplier


admin.site.register(Customer)
admin.site.register(User)
admin.site.register(Login)
admin.site.register(Product)
admin.site.register(RaisedIssue)
admin.site.register(RawMaterial)
admin.site.register(Roles)
admin.site.register(Sales)
admin.site.register(Supplier)
