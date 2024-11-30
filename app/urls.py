from django.urls import path
from .views import IndexView, LoginView, RegisterView, AddExpense, Logout, ExpenseReport, Profile

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('expense/add/', AddExpense.as_view(), name='add_expense'),
    path('expense/report/', ExpenseReport.as_view(), name='report_expense')
]