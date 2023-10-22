from django.shortcuts import get_object_or_404, render,redirect
from .models import *
# Create your views here.

def index(request, baslik_id):
    kategori=QuizBaslik.objects.all()
    baslik = get_object_or_404(QuizBaslik, pk=baslik_id)
    sorular = QuizSorulari.objects.filter(baslik=baslik)
    context = {'baslik': baslik, 'sorular': sorular,'kategori':kategori,}
    return render(request, 'quiz/layout.html', context)


def sonuc(request,baslik_id):
    if request.method == 'POST':
        baslik = get_object_or_404(QuizBaslik, pk=baslik_id)
        dogru_sayisi = 0
        yanlis_sayisi = 0

        for soru in QuizSorulari.objects.filter(baslik=baslik):
            cevap = request.POST.get('soru_' + str(soru.id))
            if cevap == soru.dogru_secenek:
                dogru_sayisi += 1
            else:
                yanlis_sayisi += 1

        return render(request, 'quiz/sonuc.html', {'dogru_sayisi': dogru_sayisi, 'yanlis_sayisi': yanlis_sayisi})
    else:
        return redirect('quiz/layout.html')