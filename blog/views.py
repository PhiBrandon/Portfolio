from django.shortcuts import render
from .models import Post, projects
from django.utils import timezone
from django.views import View
from blog.forms import contactForm

# Create your views here.
def post_list(request):
	posts = Post.objects.order_by('-date')[:3]
	return render(request, 'blog/post_list.html', {'post': posts})

def app_display(request):
	template_name = 'blog/portfolio.html'
	context = {'list': projects.objects.all()}
	return render(request, template_name, context)

def about(request):
	return render(request, 'blog/about.html')

def contact(request):
	if request.method == 'POST':
		form = contactForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			name = form.cleaned_data['name']


		args = {'form': form, 'email': email, 'name': name}
		return render(request, 'blog/contact_me.html',args)
	else:
		form = contactForm()
		
		return render(request, 'blog/contact_me.html', {'form': form})

def article(request, tid):
	payload = Post.objects.filter(pk=tid)
	return render(request, 'blog/article.html',{'payload':payload})


