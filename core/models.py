from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import os
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextUploadingField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')  

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.image:
            try:
                # OPEN THE IMAGE TO VERIFY
                img = Image.open(self.image)
                img.verify()
                img = Image.open(self.image)

                # CONVERT IMAGE TO RGB IF NEEDED
                if img.mode in ("RGBA", "LA", "P"):
                    img = img.convert("RGB")

                # CALCULATE THE NEW DIMENSION OF THE IMAGE TO MAINTAIN ASPECT RATIO
                new_width = 800
                original_width, original_height = img.size
                new_height = int((new_width / original_width) * original_height)

                # RESIZE THE IMAGE
                img = img.resize((new_width, new_height), Image.LANCZOS)

                # PREPARE THE IMAGE FOR SAVING
                temp_img = BytesIO()

                # SAVE THE IMAGE AS JPEG
                img.save(temp_img, format="JPEG", quality=70, optimize=True)
                temp_img.seek(0)

                # CHANGE THE FILE EXTENSION TO .JPG
                original_name, extension = os.path.splitext(self.image.name)
                new_filename = f"{original_name}.jpg"

                # SAVE THE IMAGE AS BYTEIO OBJECT TO THE IMAGE FIELD WITH NEW FILENAME
                self.image.save(new_filename, ContentFile(temp_img.read()), save=False)

            except (IOError, SyntaxError) as e:
                raise ValueError(f"The uploaded file is not a valid image. -- {e}")

        super().save(*args, **kwargs)






    
class Order(models.Model):
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.transaction_id


