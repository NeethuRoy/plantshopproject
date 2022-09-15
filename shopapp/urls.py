from.import views
from django.urls import path
app_name='shopapp'


urlpatterns = [
    path('', views.allPodCat, name='allPodCat'),
    path('<slug:c_slug>/',views.allPodCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail'),

]
