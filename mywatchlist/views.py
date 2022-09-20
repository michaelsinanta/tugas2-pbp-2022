from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    context = {
        'nama': 'Michael Christlambert Sinanta',
        'studentId': '2106750414',
    }
    return render(request, "mywatchlist_home.html", context)

def show_html(request):
    data_mywatchlist = MyWatchList.objects.all()
    
    #Fitur menampilkan pesan
    watchedMovie = 0
    notWatchedMovie = 0

    for movie in data_mywatchlist:
        if movie.watched:
            watchedMovie += 1
        else:
            notWatchedMovie += 1
    
    if (watchedMovie > notWatchedMovie):
        informasiPesan = "Selamat, kamu sudah banyak menonton!"
    else :
        informasiPesan = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_watchlist': data_mywatchlist,
        'nama': 'Michael Christlambert Sinanta',
        'studentId': '2106750414',
        'fiturPesan' : informasiPesan,
    }
    return render(request, "mywatchlist.html", context)

#Mengembalikan Data Berdasarkan ID dalam Bentuk XML
def show_xml(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

#Mengembalikan Data Berdasarkan ID dalam Bentuk XML
def show_json(request):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")

#Mengembalikan Data Berdasarkan ID dalam Bentuk XML
def show_xml_by_id(request, id):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")

#Mengembalikan Data Berdasarkan ID dalam Bentuk JSON
def show_json_by_id(request, id):
    data_mywatchlist = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")