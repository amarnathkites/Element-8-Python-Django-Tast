from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.



class Teacher_details(models.Model):
    first_name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    profile_pic = models.FileField(upload_to="teacher_pic",null=True)
    phone_number = models.CharField(max_length=255,null=True)
    room_no = models.CharField(max_length=255,null=True)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)
    status = models.BooleanField(null=True)

    @property
    def imageURL(self):
        try:

            try:
                import os
                url =  self.profile_pic.url
               
                print(url)
                data = os.path.isfile("./"+str(url))
                print(data)
                if data == True:
                
                    url = url
                else:
                    url = 'https://www.freeiconspng.com/thumbs/no-image-icon/no-image-icon-4.png'

                pass
            except:
                url = 'https://www.freeiconspng.com/thumbs/no-image-icon/no-image-icon-4.png'
                pass
            
        except:
            url = 'https://www.freeiconspng.com/thumbs/no-image-icon/no-image-icon-4.png'
        return url

class Teacher_subject_details(models.Model):
    teacher_id = models.ForeignKey(Teacher_details,related_name="tecaher_id",on_delete=models.CASCADE,null=True)
    subject_name = models.CharField(max_length=255,null=True)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=255,null=True)