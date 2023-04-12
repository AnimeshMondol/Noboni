from django import forms

from blog.models import DoctorInfo

class CreateDoctorInfoForm(forms.ModelForm):

	class Meta:
		model = DoctorInfo
		fields = ['name', 'specialist', 'lcno', 'address', 'phone', 'email', 'image']


class UpdateBlogPostForm(forms.ModelForm):

	class Meta:
		model = DoctorInfo
		fields = ['name', 'specialist', 'lcno', 'address', 'phone', 'email', 'image']

	def save(self, commit=True):
		doctor_info = self.instance
		doctor_info.name = self.cleaned_data['name']
		doctor_info.specialist = self.cleaned_data['specialist']
		doctor_info.lcno = self.cleaned_data['lcno']
		doctor_info.address = self.cleaned_data['address']
		doctor_info.phone = self.cleaned_data['phone']
		doctor_info.email = self.cleaned_data['email']

		if self.cleaned_data['image']:
			doctor_info.image = self.cleaned_data['image']

		if commit:
			doctor_info.save()
		return doctor_info			
