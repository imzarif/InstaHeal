from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
import Bloglist.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
    path('blog', Bloglist.views.allblogs, name='allblogs'),
    path('<int:blog_id>', Bloglist.views.detail, name='detail'),
    path('cart/', include('shopping_cart.urls', namespace='shopping_cart'))
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)