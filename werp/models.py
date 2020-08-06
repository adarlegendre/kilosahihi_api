from django.db import models

class FarmReturnOfficers(models.Model):
    name = models.CharField(max_length=49)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    id_no = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    region = models.CharField(max_length=50)
    zone = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    account_no =models.CharField(max_length=20)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Farm Return Officers"

class Farmers(models.Model):
    name  = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=19)
    id_no = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    zone =models.CharField(max_length=20)
    distro_date =models.CharField(max_length=20)
    account_no = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    def __str__ (self):
        return self.name
    class Meta:
        verbose_name_plural = "Farmers"

class Farms(models.Model):
     name = models.CharField(max_length=50)
     region = models.CharField(max_length=50)
     zone = models.CharField(max_length=50)
     def __str__ (self):
        return self.name
     class Meta:
        verbose_name_plural = "Farms"

class FarmProduce(models.Model):
     name = models.CharField(max_length=20)
     desc= models.CharField(max_length=50)
     status = models.CharField(max_length=10)
     def __str__ (self):
        return self.name
     class Meta:
        verbose_name_plural = "Farm Produce"


class Transactions(models.Model):
     farmer = models.ForeignKey(Farmers,on_delete=models.CASCADE)
     fro = models.ForeignKey(FarmReturnOfficers,on_delete=models.CASCADE)
     farm =  models.ForeignKey(Farms,on_delete=models.CASCADE)
     date = models.DateField()
     weight = models.CharField(max_length=5)
     produce =  models.ForeignKey(FarmProduce,on_delete=models.CASCADE)
     status = models.CharField(max_length=10)

     def __str__ (self):
        return self.name
     class Meta:
        verbose_name_plural = "Transactions"

