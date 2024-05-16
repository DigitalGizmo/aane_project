from django.conf import settings
from django.db import models



# class CommonEditHistory(models.Model):
 
#     editor = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.PROTECT,
#     )    
#     created = models.DateTimeField(auto_now_add=True)
#     note = models.TextField(blank=True, default='')

#     class Meta:
#         abstract = True
