from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . views import BakeryView, BakeryMainView, OrderView

urlpatterns = [
        path('', BakeryMainView.as_view(), name='index'),
        path('category/<int:category_id>/', BakeryView.as_view(), name='category'),
        path('create', views.create, name='create'),
        path('order', OrderView.as_view(), name='bakery_order'),
        path('search', views.search_view, name='search_view'),
        path('bakery/<int:pk>', views.BakeryDetailView.as_view(), name='bakery_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




