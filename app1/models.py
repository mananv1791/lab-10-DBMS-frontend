# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    cus_name = models.CharField(max_length=500)
    cus_id = models.CharField(primary_key=True, max_length=500)
    cus_address = models.CharField(max_length=500)
    cus_mobile = models.CharField(max_length=500)
    cus_email = models.CharField(max_length=500)

    def __str__(self):
        return self.cus_name

    def returnAll(self):
        return [self.cus_id, self.cus_name, self.cus_address, self.cus_mobile, self.cus_email]

    def returnHeading(self):
        return ["Customer ID", "Customer Name", "Customer Address", "Customer Mobile", "Customer Email"]

    class Meta:
        db_table = 'customer'


class HasProRaw(models.Model):
    prod = models.OneToOneField('Product', models.DO_NOTHING, primary_key=True)
    raw = models.ForeignKey('RawMaterial', models.DO_NOTHING)

    def __str__(self):
        return self.raw

    def returnAll(self):
        return [self.prod, self.raw]

    def returnHeading(self):
        return ["Product", "Raw"]

    class Meta:

        db_table = 'has_pro_raw'
        


class Login(models.Model):
    login_id = models.CharField(primary_key=True, max_length=500)
    login_username = models.CharField(max_length=500)
    user_password = models.CharField(max_length=500)
    user = models.ForeignKey('User', models.DO_NOTHING)

    def __str__(self):
        return self.login_username

    def returnAll(self):
        return [self.login_id, self.login_username, self.user]

    def returnHeading(self):
        return ["Login ID", "Login Username", "User"]

    class Meta:

        db_table = 'login'


class Product(models.Model):
    prod_id = models.CharField(primary_key=True, max_length=500)
    prod_name = models.CharField(max_length=500)
    prod_cost_price = models.IntegerField()
    prod_sell_price = models.IntegerField()
    prod_qty = models.IntegerField()

    def __str__(self):
        return self.prod_name

    def returnAll(self):
        return [self.prod_id, self.prod_name, self.prod_cost_price, self.prod_sell_price, self.prod_qty]

    def returnHeading(self):
        return ["Product ID", "Product Name", "Product Cost Price", "Product Sell Price", "Product Quantity"]

    class Meta:
        db_table = 'product'


class RaisedIssue(models.Model):
    reason = models.CharField(max_length=500)
    sales_id = models.CharField(max_length=500)
    qty = models.IntegerField()
    raised_id = models.CharField(primary_key=True, max_length=500)
    cus = models.ForeignKey(Customer, models.DO_NOTHING)
    prod = models.ForeignKey(Product, models.DO_NOTHING)
    total_amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.sales_id

    def returnAll(self):
        return [self.reason, self.sales_id, self.qty, self.raised_id, self.cus, self.prod, self.total_amount]

    def returnHeading(self):
        return ["Reason", "Sales ID", "Quantity", "Raised ID", "Customer", "Product", "Total Amount"]

    class Meta:

        db_table = 'raised_issue'


class RawMaterial(models.Model):
    raw_id = models.CharField(primary_key=True, max_length=500)
    raw_name = models.CharField(max_length=500)
    sup = models.ForeignKey('Supplier', models.DO_NOTHING)

    def __str__(self):
        return self.raw_id

    def returnAll(self):
        return [self.raw_id, self.raw_name, self.sup]

    def returnHeading(self):
        return ["Raw ID", "Raw Name", "Supplier"]

    class Meta:

        db_table = 'raw_material'


class Roles(models.Model):
    role_id = models.CharField(primary_key=True, max_length=500)
    role_name = models.CharField(max_length=500)
    user = models.ForeignKey('User', models.DO_NOTHING)

    def __str__(self):
        return self.role_name

    def returnAll(self):
        return [self.role_id, self.role_name, self.user]

    def returnHeading(self):
        return ["Role ID", "Role Name", "User"]

    class Meta:

        db_table = 'roles'


class RolesRoleDesc(models.Model):
    role_desc = models.CharField(primary_key=True, max_length=500)
    role = models.ForeignKey(Roles, models.DO_NOTHING)

    def __str__(self):
        return self.role_desc

    def returnAll(self):
        return [self.role, self.role_desc]

    def returnHeading(self):
        return ["Role", "Role Description"]

    class Meta:

        db_table = 'roles_role_desc'
        unique_together = (('role_desc', 'role'),)


class Sales(models.Model):
    cus_id = models.CharField(max_length=500)
    prod = models.ForeignKey(Product, models.DO_NOTHING)
    qty = models.IntegerField()
    sales_id = models.CharField(primary_key=True, max_length=500)
    user = models.ForeignKey('User', models.DO_NOTHING)
    profit = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.cus_id

    def returnAll(self):
        return [self.cus_id, self.prod, self.qty, self.sales_id, self.user, self.profit]

    def returnHeading(self):
        return ["Customer ID", "Product", "Quantity", "Sales ID", "User", "Profit"]

    class Meta:

        db_table = 'sales'


class Supplier(models.Model):
    sup_id = models.CharField(primary_key=True, max_length=500)
    company_name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    mob_no = models.CharField(max_length=500)

    def __str__(self):
        return self.sup_id

    def returnAll(self):
        return [self.sup_id, self.company_name, self.location, self.mob_no]

    def returnHeading(self):
        return ["Supplier ID", "Company Name", "Location", "Mobile Number"]

    class Meta:

        db_table = 'supplier'


class User(models.Model):
    user_name = models.CharField(max_length=500)
    user_id = models.CharField(primary_key=True, max_length=500)
    user_email = models.CharField(max_length=500)
    user_mob = models.CharField(max_length=500)

    def __str__(self):
        return self.user_name

    def returnAll(self):
        return [self.user_name, self.user_id, self.user_email, self.user_mob]

    def returnHeading(self):
        return ["Username", "User ID", "User Email", "User Mobile"]

    class Meta:
        db_table = 'user'
