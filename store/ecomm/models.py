from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  category= models.CharField(max_length=255, blank=True)
  price= models.DecimalField(max_digits=10, decimal_places=2)
  product_id=models.CharField(max_length=255)
  image=models.ImageField(upload_to ='uploads/', default="")
  
  def __str__(self):
        return str(self.name) + ": $" + str(self.price)

class Computer(models.Model):
  name = models.CharField(max_length=255)
  RAM= models.CharField(max_length=255)
  hard_drive= models.CharField(max_length=255) 
  CPU= models.CharField(max_length=255) 
  display= models.CharField(max_length=255)
  OS= models.CharField(max_length=255) 
  soundcard= models.CharField(max_length=255)
  price= models.DecimalField(max_digits=10, decimal_places=2)
  category= models.CharField(max_length=255, blank=True, default="")
  image=models.ImageField(upload_to ='uploads/', default="")
  def __str__(self):
        return str(self.name) + ": $" + str(self.price)
  

class Order(models.Model):
    order_num=models.CharField(max_length=255)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.order_num) + ": $" + str(self.total)
    

class OrderItem(models.Model):
    computer=models.IntegerField()
       # computer=models.ForeignKey(Computer, on_delete = models.CASCADE)
  #  order=models.ForeignKey(Order, on_delete = models.CASCADE, default="1")
    price= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self): 
        return str(self.computer) + ": $" + str(self.price)
   
    def set_price(self):
             self.price=self.computer.price


# declare a new model with a name "detailModel"
class DetailModel(models.Model):

	# fields of the model
	title = models.CharField(max_length = 200)
	description = models.TextField()

	# renames the instances of the model
	# with their title name
	def __str__(self):
		return self.title
