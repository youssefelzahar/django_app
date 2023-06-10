from django.db import models

class Female(models.Model):
    female_name=models.CharField(max_length=50)

       
    def __str__(self):
        return self.female_name
       

class Male(models.Model):
    male_name=models.CharField(max_length=50)
    girls=models.OneToOneField(Female,on_delete=models.CASCADE)    


    def __str__(self):
        return self.male_name
    

class Product(models.Model):
    product_name=models.CharField(max_length=50)
    def __str__(self):
        return self.product_name
    

class UserModels(models.Model):
    name=models.CharField(max_length=50)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
        

class Video(models.Model):
    video_name=models.CharField(max_length=50)
    def __str__(self):
        return self.video_name
    
    
class User(models.Model):
    name=models.CharField(max_length=50)
    watch=models.ManyToManyField(Video)
    def __str__(self):
        return self.name
    
class login(models.Model):
    user_name=models.CharField(max_length=50)    
    user_pasword=models.CharField(max_length=50)    

        
