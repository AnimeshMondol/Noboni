from django.urls import path

from store.views import(

	store,
	cart,
	checkout,
	updateItem,
	processOrder,

)

app_name = 'store'

urlpatterns = [
	#Leave as empty string for base url
	path('store/', store, name="store"),
	path('cart/', cart, name="cart"),
	path('checkout/', checkout, name="checkout"),
	path('update_item/', updateItem, name="update_item"),
	path('process_order/', processOrder, name="process_order"),

]