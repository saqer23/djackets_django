from django.urls import path
from product import views

urlpatterns = [
    path('latser-products/',views.latestProductslist.as_view()),
    path('products/search',views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/',views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/',views.CategoryDetail.as_view()),
    path('catygorys/',views.latestCategory.as_view()),

]