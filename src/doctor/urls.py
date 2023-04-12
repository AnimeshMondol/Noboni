from django.urls import path
from doctor.views import(

	create_doctor_info_view,
	detail_doctor_info_view,
	edit_doctor_info_view,

)

app_name = 'doctor'

urlpatterns = [
	path('create/', create_doctor_info_view, name="create"),
	path('<slug>/', detail_doctor_info_view, name='detail'),
	path('<slug>/edit', edit_doctor_info_view, name='edit'),


]