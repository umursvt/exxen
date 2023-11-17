
import string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from requests import request
from django.contrib.auth import authenticate, login,logout


# Create your views here.

def userRegister(requests):
    if requests.method == 'POST':
        kullanici = requests.POST['kullanici']
        email=requests.POST['email']
        sifre=requests.POST['sifre']
        sifre2= requests.POST['sifre2']

        if kullanici != '' and email != '' and sifre != '':
            if sifre == sifre2:
                #HATALI GİRİŞLER
                if User.objects.filter(username = kullanici).exists():
                    messages.error(requests, 'Bu kullanıcı zaten mevcut')
                    return redirect('register')
                elif User.objects.filter(email = email).exists():
                    messages.error(requests, 'Bu email kullanımda')
                    return redirect('register')
                
                elif len(sifre) < 6:
                    messages.error(requests, 'Şifre en az 6 karakter olması gerekiyor.')
                    return redirect('register')
                elif kullanici in sifre:
                    messages.error(requests, 'Şifre ile kullanıcı adı benzer olamaz.')
                elif sifre[0] in string.ascii_lowercase:
                    messages.error(requests, 'Baş harfi büyük olmalı')
                else:
                    #HATA YOKSA GİRİŞE İZİN VERİR
                    user = User.objects.create_user(username=kullanici, password=sifre, email=email)
                    user.save()
                    messages.success(requests, 'Kullanıcı oluşturuldu.')
                    return redirect('index')
            else:
                messages.error(requests, 'Şifreler uyuşmuyor')
        else:
            messages.error(requests,'Tüm alanların doldurulması gerekiyor')
            return redirect('register')
            
    return render(requests,'register.html')

def user_login(requests):
    if requests.method == 'POST':
        kullanici=requests.POST['kullanici']
        sifre=requests.POST['sifre']

        user=authenticate(requests, username=kullanici, password=sifre)
        if user is not None:
            login(requests,user)
            messages.success(requests, 'Giriş yapıldı.')
            return redirect('index')
        else:
            messages.error(requests, 'Kullanıcı adı ve şifre hatalı')
            return redirect('login')
    return render(requests,'login.html')

def user_logout(requests):
    logout(requests)
    messages.success(requests,'Çıkış yapıldı')
    return redirect('index')    
            