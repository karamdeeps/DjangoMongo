from djongo import models


class User(models.Model):
    name = models.CharField(max_length=100)
    profession = models.TextField()
    salary = models.IntegerField()
    position = models.CharField(max_length=50)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    objects = models.DjongoManager()

    def __str__(self):
        return '%s' % self.id

    class Meta:
        # abstract = True
        db_table = 'user'


# class Company(models.Model):
#     _id = models.ObjectIdField()
#     user = models.EmbeddedField(
#         model_container=User,
#     )
#     position = models.CharField(max_length=50)
#     objects = models.DjongoManager()
