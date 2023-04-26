from django.conf import settings
from django.conf.urls.static import static
from.import views
from django.urls import path
from django. contrib.auth import views as auth_view

from .forms import LoginForm, MyPasswordResetForm, MypasswordChangeForm, MySetPasswordForm

urlpatterns=[
    path('',views.home),
    path('places/<slug:val>',views.PlacesView.as_view(),name='place'),
    path('place-title/<val>', views.PlaceTitle.as_view(), name="place-title"),
    path('place-detail/<int:pk>', views.PlaceDetail.as_view(),name='place-detail'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
    path('bookingdetail/', views.BookingView.as_view(), name='bookingdetail'),
    path('bookingsuccessful/', views.bookingsuccessful, name='bookingsuccessful'),
    path('payment', views.payment, name='payment'),
    path('search', views.search, name='search'),

                #  login authentication

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html', authentication_form=LoginForm),name='login'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='changepassword.html',form_class=MypasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset-done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64><token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)