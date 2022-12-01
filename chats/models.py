from django.db import models
from django.urls import reverse 


class Chats(models.Model):
    Title= models.TextField()
    Author= models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    body = models.TextField()
    Date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return reverse('details_view', args=[str(self.id)]) #helps output views effectively without misbehavng

class Comment(models.Model):
    post = models.ForeignKey(Chats,on_delete=models.CASCADE,related_name='comments')
    Author= models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']  #in support of the commentss database

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.Author)



