from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from user_message import views as user_message_views




urlpatterns = [
    path('messages/<int:id>/', user_message_views.AllMessages.as_view(), name='all_messages'),
    path('send_message/<int:id>/', user_message_views.CreateMessageView.as_view(), name='send_message'),
    path('delete_message', user_message_views.delete_message, name='delete_message'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





