from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(('authentications.urls','authentications'), namespace = 'auth')),
    path('payment/', include(('payments.urls','payments'), namespace = 'pay')),
    path('cart/', include(('cart.urls', 'cart'), namespace = 'cart')),
    path('api-v1/', include(('api.urls','api'), namespace = 'api')),
    path('/', include(('products.urls', 'products'), namespace = 'products')),
 
]
