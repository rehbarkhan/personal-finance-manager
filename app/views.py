from django.shortcuts import render, redirect
from django.views import View
from .models import Expense, ExpenseYear
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import ExpenseForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        current_year = timezone.now().year
        expenses = Expense.objects.filter(date__year = current_year, User=request.user)
        expense_dict = dict()
        expense_dict['year'] = current_year
        months = ["jan",'feb','mar','apr','may','june','july','aug','spet','oct','nov','dec']
        for index in range(len(months)):
            total_credit = 0
            total_debit = 0
            month_index = index + 1
            for expense in expenses:
                if expense.transaction_type == 'debit' and expense.date.month == month_index:
                    total_debit += expense.sum
                if expense.transaction_type == 'credit' and expense.date.month == month_index:
                    total_credit += expense.sum
            expense_dict[months[index]] = total_credit - total_debit
        return render(request, 'app/index.html', expense_dict)

class LoginView(View):
    def get(self, request):
        return render(request, 'app/login.html', {})
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        auth_user = authenticate(request, username = email, password=password)
        if auth_user is not None:
            login(request, auth_user)
            return redirect('index')
        messages.error(request, "Your credential is wrong")
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        form = ProfileForm()
        return render(request, 'app/register.html', {'form':form})
    
    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            instance = form.save()
            user = User.objects.create(username=instance.email)
            password = '{}{}'.format(instance.contact, instance.date_of_birth.year)
            user.set_password(password)
            user.first_name = instance.first_name
            user.last_name = instance.last_name
            user.email = instance.email
            user.save()
            return render(request , 'app/register.html',{
                'success': True,
                'email': instance.email,
                'password': password    
            })
        return render(request, 'app/register.html', {'form':form})
    
class AddExpense(LoginRequiredMixin, View):
    def get(self, request):
        form = ExpenseForm()
        return render(request, 'app/add_expense.html', {'form':form})
    
    def post(self, request):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.User = request.user
            data.save()
            messages.success(request, 'Entry addedd successfully.')
        return redirect('add_expense')

class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')

class ExpenseReport(LoginRequiredMixin, View):
    def get(self, request):
        years = ExpenseYear.objects.filter(User=request.user)
        return render(request, 'app/expense_report.html', {'years':years})
    
    def post(self, request):
        if request.htmx:
            from time import sleep
            year = request.POST.get('year')
            month = request.POST.get('month')
            reports = Expense.objects.filter(User=request.user,date__year = year, date__month=month)
            credit_total = 0
            debit_total = 0 
            for report in reports:
                if report.transaction_type == 'credit':
                    credit_total += report.sum
                else:
                    debit_total += report.sum
            return render(request, 'app/partial/expense_report.html',{'reports':reports, 'credit_total':credit_total, "debit_total":debit_total})
        else:
            return redirect('report_expense')

class Profile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'app/profile.html', {})
    
    def post(self, request):
        if request.htmx:
            current_password = request.POST.get('current_password')
            new_password_first = request.POST.get('new_password_first')
            new_password_second = request.POST.get('new_password_second')

            # do some validateion
            User = request.user
            User.set_password(new_password_first)
            User.save()
            update_session_auth_hash(request=request, user=User)
            messages.success(request, 'Your Password chagned succesfully.')
            return render(request, 'app/partial/profile.html')
        else:
            return redirect('profile')