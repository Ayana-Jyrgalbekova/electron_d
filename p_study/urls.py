from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import *
from p_study import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', main_page, name='main_page'),
    path('entrance/',  user_login, name='entrance'),
    path('timetable/', TimetableList.as_view(), name='timetable')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
