from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from users.layoff_prediction_model.predict import predict
from django.http import JsonResponse
from .models import LayoffPrediction
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm, LayoffPredictionForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
import requests


def home(request):
    print("I am in home page")
    api_key = '3990d862d59f4135a4fe98c8e02bea7b'
    url = f'https://newsapi.org/v2/everything?q=layoff&apiKey={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json().get('articles', [])
    else:
        articles = []

    article_groups = [articles[i:i + 3] for i in range(0, len(articles), 3)]

    return render(request, 'users/home.html', {'article_groups': article_groups})

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)

            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)
    
class CustomAdminLoginView(LoginView):
    form_class = LoginForm
    template_name = 'users/adminlogin.html' 


    ADMIN_USERNAME = 'workifyadmin'
    ADMIN_PASSWORD = 'shivam1001'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')


        if username != self.ADMIN_USERNAME or password != self.ADMIN_PASSWORD:
            form.add_error(None, "Invalid credentials for admin login.")
            return self.form_invalid(form)


        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)

            self.request.session.set_expiry(0)
            self.request.session.modified = True

            return HttpResponseRedirect(self.get_success_url())
        else:
            form.add_error(None, "Invalid credentials.")
            return self.form_invalid(form)

    def get_success_url(self):
        
        return reverse_lazy('users-admindashboard')

 
class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/admindashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      
        predictions = LayoffPrediction.objects.all()
        context['predictions'] = predictions
        return context


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
@login_required
def layoff_prediction_form(request):
    prediction_instance = None

    try:
        prediction_instance = LayoffPrediction.objects.get(user=request.user)
    except LayoffPrediction.DoesNotExist:
        pass
    
    if request.method == 'POST':
        form = LayoffPredictionForm(request.POST, instance=prediction_instance)
        if form.is_valid(): 
            data = form.cleaned_data

            formatted_data = {
                'Age': int(data.get('age')),
                'EducationField': int(data.get('education_field')),
                'JobRole': int(data.get('job_role')),
                'Department': int(data.get('department')),
                'Industry': int(data.get('industry')),
                'Stage': int(data.get('stage')),
                'Education': int(data.get('education')),
                'Funds_Raised(m)': float(data.get('funds_raised')),
                'PerformanceRating': int(data.get('performance_rating')),
                'JobSatisfaction': int(data.get('job_satisfaction')),
                'JobInvolvement': int(data.get('job_involvement')),
                'YearsAtCompany': int(data.get('years_at_company')),
                'YearsInCurrentRole': int(data.get('years_in_current_role')),
                'YearsWithCurrManager': int(data.get('years_with_curr_manager')),
                'MonthlyIncome': int(data.get('monthly_income')),
                'NumCompaniesWorked': int(data.get('num_companies_worked')),
                'Gender': int(data.get('gender')),
            }

            try:
                prediction, feature_importance, recommendations = predict(formatted_data)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)  
            
            formdata = form.save(commit=False) 
            formdata.user = request.user       
            formdata.prediction_percentage = prediction  
            formdata.save()

            return JsonResponse({
                'prediction': f"{prediction:.2f}",
                'feature_importance': feature_importance,
                'recommendations': recommendations
            })
        
        return JsonResponse({'error': 'Form is invalid. Please check your input.'}, status=400)
    
    else:
        form = LayoffPredictionForm(instance=prediction_instance)
    
    return render(request, 'users/layoff_prediction_form.html', {'form': form})



def success_view(request):
    return render(request, 'users/success.html')

