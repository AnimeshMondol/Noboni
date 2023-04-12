from django.urls import path
from blog.views import(

	create_blog_view,
	detail_blog_view,
	edit_blog_view,
	create_comment_view,
	comment_view,
	create_doctor_blog_view,
	doctor_detail_blog_view,
	doctor_edit_blog_view,

)

app_name = 'blog'

urlpatterns = [
	path('create/', create_blog_view, name="create"),
	path('createblog/', create_doctor_blog_view, name="doctorblogcreate"),
	path('<slug>/', detail_blog_view, name='detail'),
	path('<slug>/detail', doctor_detail_blog_view, name='doctorblogdetail'),
	path('<slug>/', create_comment_view, name='comment'),
	path('<slug>/', comment_view, name='comments'),
	path('<slug>/edit', edit_blog_view, name='edit'),
	path('<slug>/editblog', doctor_edit_blog_view, name='doctorblogedit'),


]