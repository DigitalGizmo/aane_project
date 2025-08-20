from django.conf import settings
from django.db import models



class CommonEditHistory(models.Model):
 
    editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )    
    date_edited = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, default='')

    # @property
    # def active_users(self):
    #     return self.editor.filter(user__is_active=True)

    class Meta:
        abstract = True
