from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views





urlpatterns = [
    path('store/add-property/', views.add_property, name='add_property'),
    path('store/edit-property/<int:pk>/', views.edit_property, name='edit_property'),
    path('store/delete/<int:pk>/', views.delete_property, name='delete_property'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<pk>/', views.agent_profile, name='agent_profile'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
