from django.http import HttpResponse
from blog.models import Post
from django.template import Context,loader
# Create your views here.

def index(request):
    latest_blog_list = Post.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('index.html')
    c = Context({
        'latest_blog_list': latest_blog_list
    })
    return HttpResponse(t.render(c))
