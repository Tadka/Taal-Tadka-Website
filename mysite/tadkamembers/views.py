from django.http import HttpResponse
from tadkamembers.models import UserProfile
from django.template import Context,loader
# Create your views here.

def memberpage(request):
	member_list = UserProfile.objects.all().order_by('user__first_name')
	t = loader.get_template('members.html')
	c = Context({
		'member_list': member_list
	})
	return HttpResponse(t.render(c))
