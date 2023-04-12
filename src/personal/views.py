from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from blog.views import get_blog_queryset
from blog.models import BlogPost

BLOG_POSTS_PER_PAGE = 5

def home_screen_view(request):
	print(request.headers)
	return render(request, "base.html", {})

def index_view(request):
	print(request.headers)
	return render(request, "index.html", {})

def userprofile_view(request):
	print(request.headers)
	return render(request, "userprofile.html", {})	

def blogpost_view(request):
	
	context = {}

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

	blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)



	# Pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	try:
		blog_posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

	context['blog_posts'] = blog_posts

	return render(request, "personal/bpost.html", context)	

def doctor_index_view(request):
	print(request.headers)
	return render(request, "doctor_index.html", {})	

def doctor_blogpost_view(request):
	
	context = {}

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

	blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)



	# Pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	try:
		blog_posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

	context['blog_posts'] = blog_posts

	return render(request, "personal/docbpost.html", context)	

def doc_profile_view(request):
	print(request.headers)
	return render(request, "doctorprofile.html", {})	

def covid_view(request):
	print(request.headers)
	return render(request, "covid.html", {})

def product_view(request):
	print(request.headers)
	return render(request, "product.html", {})	