from django.contrib import admin
from django.urls import include, path

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/records/', include('records.urls')),  # 替换为你的应用名称
]
