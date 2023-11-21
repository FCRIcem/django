from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
# Create your views here.
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect


def giris_yap(req):
    # İstek method'u kontrolü
    if req.method == 'POST':
        # POST isteği geldiyse, formdan email ve parola bilgilerini al
        email = req.POST.get('email')
        parola = req.POST.get('parola')
        
        # Kullanıcının girdiği bilgileri ekrana yazdır
        print(f"Email: {email}, Parola: {parola}")

        try:
            # Veritabanında kullanıcıyı email ile ara
            user = User.objects.get(email=email)
            
            # Eğer kullanıcı bulunursa ve parola doğruysa
            if user is not None and user.check_password(parola):
                # Doğrulama başarılı, kullanıcıyı oturum açtır ve kayıt sayfasına yönlendir
                print(f"Giriş başarılı: {user}")
                login(req, user)
                return redirect('kayit_ol')
            else:
                # Eğer kullanıcı bulunsa da parola yanlışsa
                print("Giriş başarısız: Parola yanlış")
                return render(req, 'giris_yap.html', {'hata': 'Kullanıcı adı veya parola yanlış'})
        except User.DoesNotExist:
            # Eğer kullanıcı bulunamazsa
            print("Giriş başarısız: Kullanıcı bulunamadı")
            return render(req, 'giris_yap.html', {'hata': 'Kullanıcı adı veya parola yanlış'})

    else:
        # GET isteği geldiyse, giriş sayfasını göster
        return render(req, 'giris_yap.html')




        





def kayit_ol(req):
    if req.method == 'POST':
        kullanici_adi = req.POST['kullanici_adi']
        email = req.POST['email']
        parola = req.POST['parola']
        parola_tekrar = req.POST['parola_tekrar']
        
        if parola == parola_tekrar:
            if User.objects.filter(username=kullanici_adi).exists():
                return render(req, 'kayit_ol.html', {"hata": "Kullanıcı adı kullanılıyor"})
            else:
                if User.objects.filter(email=email).exists():
                    return render(req, 'kayit_ol.html', {"hata": "E-mail kullanılıyor"})
                else:
                    user = User.objects.create_user(username=kullanici_adi, email=email, password=parola)
                    user.save()
                    return redirect('giris_yap')
        else:
            return render(req, 'kayit_ol.html', {"hata": "Parola uyuşmuyor"})
    else:
        return render(req, 'kayit_ol.html')








def cikis (req):
    logout(req)
    return redirect('giris_yap')