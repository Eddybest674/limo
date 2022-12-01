from msilib.schema import ListView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import*
from django.urls import reverse_lazy


class Homepage(ListView):
    model=Chats
    template_name="chats/home.html"
    
class Detailview(DetailView):
    model=Chats
    template_name= "chats/details.html" 
    
    
class Createpost(LoginRequiredMixin,CreateView):
    model=Chats
    template_name= "chats/create.html"
    fields = ('Title', 'body') # this works with the form function below.
    login_url = 'login'
    
    def form_valid(self, form): # This enables a user create post and the name is attached as the author without manually selecting it.
        form.instance.Author = self.request.user
        return super().form_valid(form)
    

class Editpost(LoginRequiredMixin, UpdateView):
    model= Chats
    template_name= 'chats/edit.html'
    fields = ['Title','body'] #we only want the title and body to be editable
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs): # only the author can edit post.
        obj = self.get_object()
        if obj.Author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class Deletepost(LoginRequiredMixin, DeleteView):
    model=Chats
    template_name= 'chats/delete.html'
    success_url = reverse_lazy('home') #We use reverse_lazy as opposed to just reverse so that it won’t execute the URLredirect until our view has finished deleting the blog post.
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs): # only author can delete post with this.
        obj = self.get_object()
        if obj.Author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class Details(DetailView):
    model= Chats
    template_name= 'chats/details.html'
    

class About(ListView):
    model= Chats
    template_name='chats/index.html'

class Contact(ListView):
    model= Chats
    template_name='chats/contacts.html'

class Privacy(ListView):
    model= Chats
    template_name='chats/index.html'



# Create your views here.
