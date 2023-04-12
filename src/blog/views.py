from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from blog.models import BlogPost, Comment
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from account.models import Account

def create_blog_view(request):

	context = {}

	user = request.user

	if request.POST:
		form = CreateBlogPostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			obj = form.save(commit=False)
			author = Account.objects.filter(username=user.username).first()
			obj.author = author
			obj.save()
			return redirect('blogpost')
		else:
			context['form'] = form	

	else:			
		form = CreateBlogPostForm()
		context['form'] = form
	return render(request, "blog/create_blog.html", context)


def detail_blog_view(request, slug):

	context = {}

	blog_post = get_object_or_404(BlogPost, slug=slug)
	context['blog_post'] = blog_post

	return render(request, 'blog/detail_blog.html', context)	

def edit_blog_view(request, slug):

	context = {}

	user = request.user
	
	blog_post = get_object_or_404(BlogPost, slug=slug)
	
	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			blog_post = obj
			return redirect('blogpost')
		else:
			context['form'] = form	

	else:		
		form = UpdateBlogPostForm(
			initial = {
					"title": blog_post.title,
					"body": blog_post.body,
					"image": blog_post.image,
			}
		)
		context['form'] = form
		return render(request, 'blog/edit_blog.html', context)


def create_comment_view(request):

	context = {}

	user = request.user

	if request.POST:
		form = CreateCommentForm(request.POST or None)
		if form.is_valid():
			obj = form.save(commit=False)
			author = Account.objects.filter(username=user.username).first()
			obj.author = author
			obj.save()
			return redirect('comments')
		else:
			context['form'] = form	

	else:			
		form = CreateCommentForm()
		context['form'] = form
	return render(request, "blog/detail_blog.html", context)		


def comment_view(request):
	
	comment_post = get_object_or_404(Comment, slug=slug)
	context['comment_post'] = comment_post

	return render(request, 'blog/detail_blog.html', context)

 
def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ") # python install 2019 = [python, install, 2019]
	for q in queries:
		posts = BlogPost.objects.filter(
				Q(title__icontains=q) | 
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))


def create_doctor_blog_view(request):

	context = {}

	user = request.user

	if request.POST:
		form = CreateBlogPostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			obj = form.save(commit=False)
			author = Account.objects.filter(username=user.username).first()
			obj.author = author
			obj.save()
			return redirect('doctor_blogpost')
		else:
			context['form'] = form	

	else:			
		form = CreateBlogPostForm()
		context['form'] = form
	return render(request, "blog/doctor_create_blog.html", context)	


def doctor_detail_blog_view(request, slug):

	context = {}

	blog_post = get_object_or_404(BlogPost, slug=slug)
	context['blog_post'] = blog_post

	return render(request, 'blog/doctor_detail_blog.html', context)	


def doctor_edit_blog_view(request, slug):

	context = {}

	user = request.user
	
	blog_post = get_object_or_404(BlogPost, slug=slug)
	
	if request.POST:
		form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			blog_post = obj
			return redirect('doctor_blogpost')
		else:
			context['form'] = form	

	else:		
		form = UpdateBlogPostForm(
			initial = {
					"title": blog_post.title,
					"body": blog_post.body,
					"image": blog_post.image,
			}
		)
		context['form'] = form
		return render(request, 'blog/doctor_edit_blog.html', context)	



