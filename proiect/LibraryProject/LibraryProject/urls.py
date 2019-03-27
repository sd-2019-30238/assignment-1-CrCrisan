from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('books/', include('Books.urls'), name = "Books"),
    path('accounts/', include('Accounts.urls')),
    path('loan/', include('BookLoan.urls'), name = "BookLoan"),
]

urlpatterns += staticfiles_urlpatterns()

#for media
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)