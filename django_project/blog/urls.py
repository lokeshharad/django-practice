from django.urls import path
from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path("", views.home, name="blog-name"),
    path("about/", views.about, name="blog-about"),
]
