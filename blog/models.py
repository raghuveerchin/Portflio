from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_data = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) < 100:
            return self.body
        else:
            return self.body[:100] + " ..."

    def pub_data_fmt(self):
        return self.pub_data.strftime("%b %e %Y")
        # return self.pub_data