from django.urls import path
from.import views

urlpatterns = [
    path('product/',views.product,name='product'),
    path('add_product/',views.add_product,name='add_product'),
    path('edit_product/<int:id>',views.edit_product,name='edit_product'),
    # path('update_data/<int:id>/',views.update_data,name='update_data'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),

]