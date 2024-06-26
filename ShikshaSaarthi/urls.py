from django.conf import settings
from django.urls import include, path
from django.contrib import admin
# from home import urls as home_urls
from django.contrib.auth import views as auth_views
from users import views as user_views
from Resources import views as resources_views
from Resources import urls as resources_urls
from Resources import views as resources_views

app_name='ss'

urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/',user_views.register,name="register"),
    path('contact_us/',resources_views.index,name='contact_us'),
    path('contact_form_successfull/',resources_views.index2,name='contact_success'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    # # path('profile/',user_views.profile,name="profile"),
    path('',user_views.landing_page,name="home"),
    path('verification/',user_views.otp_verification,name='otp_verification'),
    path('resources/',include(resources_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

