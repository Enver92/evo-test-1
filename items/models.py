from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=68)

    def __str__(self):
        return self.name


# class AbstractItem(models.Model):
#     name = models.CharField(max_length=48)
#     manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL)
#     description = models.TextField(max_length=500, help_text='Enter a description of an item')
#     image = models.ForeignKey('ItemImage', on_delete=models.SET_NULL)
#     number_of_clicks = models.PositiveIntegerField(default=0)


class Category(models.Model):
    """
    Model representing an item category (e.g. Fridge, TV).
    """
    category = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category


class Item(models.Model):
    name = models.CharField(max_length=48, default='Item')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True)
    item_image = models.ForeignKey('ItemImage', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=500, help_text='Enter a description of an item', blank=True, null=True)
    number_of_clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} by {}".format(self.category, self.manufacturer)

    # def add_click(self):
    #     self.number_of_clicks += 1

    class Meta:
        ordering = ["-number_of_clicks"]


class ItemImage(models.Model):
    image = models.ImageField(upload_to='items_images/')
    image_category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Photo of a {} #{}".format(self.image_category, self.id)
