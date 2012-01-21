from django.http import HttpResponse
from setlist.models import Song
from django.template import Context, loader

# Create your views here.

def music(request):
	set_list = Song.objects.all().order_by('-importance')
	t = loader.get_template('music.html')
	c = Context({
		'set_list': set_list
	})
	return HttpResponse(t.render(c))
