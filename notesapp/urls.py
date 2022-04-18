from django.urls import path

from .views import NotesList, NotesDetail,NotesCreate,NotesUpdate,NotesDelete

urlpatterns = [
    path('', NotesList.as_view(), name='note'),
    path('note/<int:pk>/',NotesDetail.as_view(),name='note'),
    path('create-note/',NotesCreate.as_view(),name='note-create'),
    path('note-update/<int:pk>/',NotesUpdate.as_view(),name='note-update'),
    path('note-delete/<int:pk>/',NotesDelete.as_view(),name='note-delete'),
]
