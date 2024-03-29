from django.db import models


class State(models.Model):
    # slug = models.SlugField('short name', max_length=32, unique=True)
    abbr = models.CharField(max_length=4, default='MA')
    # note = models.TextField(blank=True, default='')   

    def __str__(self):
        return self.abbr

class Town(models.Model):
    state = models.ForeignKey('State', on_delete=models.PROTECT,
                              default=1)
    # slug = models.SlugField('short name', max_length=32, unique=True)
    title = models.CharField(max_length=64)
    # note = models.TextField(blank=True, default='')   

    def __str__(self):
        return self.title + ", " + self.state.abbr

    class Meta:
        ordering = ['title']  