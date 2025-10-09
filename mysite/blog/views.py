from django.shortcuts import render


# Create your views here.
def post_list(request):
	"""Render the blog post list template at the site root."""
	return render(request, 'blog/post_list.html')
