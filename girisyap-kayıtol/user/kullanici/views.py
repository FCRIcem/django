from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.
def giris_yap(req):
    if req.user.is_authenticated:
        return redirect('kayit_ol')
    if req.method == 'POST':
        kullanici_adi = req.POST['kullanici_adi']
        parola = req.POST['parola']
        
        user = authenticate(req, username=kullanici_adi, password=parola)
        if user is not None:
            login(req, user)
            return redirect('kayit_ol')
        else:
            return render(req, 'giris_yap.html', {'hata': 'Kullanıcı adı veya parola yanlış'})
    else:
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