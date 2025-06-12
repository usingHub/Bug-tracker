from django.urls import path
from .views import (
    SignUpView, BugListView, BugDetailView,
    BugCreateView, BugUpdateView, BugDeleteView
)

app_name = 'bugtracker'

urlpatterns = [
    path('', BugListView.as_view(), name='bug_list'),  # default home view
    path('signup/', SignUpView.as_view(), name='signup'),
    path('dashboard/', BugListView.as_view(), name='dashboard'),  # optional
    path('<int:pk>/', BugDetailView.as_view(), name='bug_detail'),
    path('create/', BugCreateView.as_view(), name='bug_create'),
    path('<int:pk>/update/', BugUpdateView.as_view(), name='bug_update'),
    path('<int:pk>/delete/', BugDeleteView.as_view(), name='bug_delete'),
    
]
