from django.urls import path
# from note_api import views
# from note_api.views import NoteListView
from .views import NoteListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'index', NoteListView, basename='note')

urlpatterns = router.urls

# urlpatterns = [
#      path('index/', NoteListView.as_view(), name='index'),
#      path('index/', NoteListView.as_view(), name='index'),
    
# ]