# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django
Nama    : Michael Christlambert Sinanta\
NPM     : 2106750414\
Kelas   : PBP C\
Link Hasil Deploy : https://django-project-tugas2-2022.herokuapp.com/mywatchlist/

### Jelaskan perbedaan antara JSON, XML, dan HTML!
HTML atau HyperText Markup Language adalah markup language yang menggunakan argumen tag untuk menyatakan kode berupa elemen-elemen dan struktur konten yang harus diterjemahkan browser dan digunakan untuk membuat halaman website. HTML berfokus dalam penyajian dan formatting data. Ekstensi file HTML adalah .html.\
JSON atau JavaScript Object Notation adalah suatu format untuk menyimpan dan mentransfer data yang disajikan dalam bahasa JavaScript. JSON merepresentasikan data dengan struktur key dan value. JSON didukung semua browser dan data yang disimpan dalam bentuk array sehingga memudahkan dalam transfer data. Ukuran sintaksnya juga lebih kecil sehingga lebih ringan dan parsing data di server juga akan lebih cepat. Struktur JSON yang tidak memiliki tag membuat mudah untuk dibaca. Ekstensi file JSON adalah .json.\
XML atau Extensive Markup Language adalah suatu markup language yang digunakan untuk menyederhakan pertukaran dan penyimpanan data. Perbedaan antara HTML dan XML adalah HTML digunakan untuk menampilkan data dan XML digunakan untuk menyederhanakan pertukaran data. HTML bersifat case insensitive dan XML bersifat case sensitive. Berbeda dengan JSON, XML tidak mendukung tipe array. XML menyimpan data dalam format seperti tree pada HTML sehingga dari segi penyimpanan, XML menyimpan elemen secara terstruktur dan lebih mudah dibaca oleh mesin. Ekstensi file XML adalah .xml.

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Alasan kita memerlukan data delivery dalam pengimplementasian platform adalah karena dalam platform, terjadi pertukaran data antara klien/user dengan server. Format pertukaran data yang sering kita gunakan adalah HTML, XML, dan JSON. Kita membutuhkan data delivery untuk mengirim format-format data tersebut agar dapat dipahami komputer lain untuk berkomunikasi dan bertukar data satu sama lain.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat sebuah django-app bernama mywatchlist dengan perintah python manage.py startapp mywatchlist.
2. Membuka settings.py di folder project_django dan menambahkan aplikasi mywatchlist ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app ke dalam proyek Django, sebagai berikut:
```python
    INSTALLED_APPS = [
    ..., 
    'mywatchlist', 
    ]
```
3. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist dengan membuat sebuah berkas di dalam folder aplikasi mywatchlist bernama urls.py untuk melakukan routing terhadap fungsi views yang telah kamu buat sehingga nantinya halaman HTML dapat ditampilkan lewat browser. Isi dari urls.py tersebut adalah sebagai berikut:
```python
    from django.urls import path
    from mywatchlist.views import show_mywatchlist

    app_name = 'mywatchlist'

    urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    ]
```
4. Mendaftarkan aplikasi mywatchlist ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns.
```python
    path('mywatchlist/', include('mywatchlist.urls')),
```
5. Membuat sebuah model MyWatchList yang memiliki atribut watched, titile, rating, release_date, dan review. Pertama, saya membuka file models.py yang ada di folder mywatchlist dan menambahkan potongan kode berikut:
```python
    from django.db import models 
    from django.core.validators import MaxValueValidator, MinValueValidator 

    class MyWatchList(models.Model): 
    watched = models.BooleanField() 
    title = models.CharField(max_length=255) 
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    release_date = models.DateField() 
    review = models.TextField() 
```
6. Menjalankan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal. 
7. Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
8. Menambahkan minimal 10 data untuk objek MyWatchList dengan membuat sebuah folder bernama fixtures di dalam folder aplikasi mywatchlist dan membuat sebuah berkas bernama initial_mywatchlist_data.json yang berisi 10 data tersebut.
9. Menjalankan perintah python manage.py loaddata initial_mywatchlist_data.json untuk memasukkan data tersebut ke dalam database Django lokal.
10. Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format: 
* HTML
Membuat folder bernama templates di dalam folder aplikasi mywatchlist dan membuat berkas bernama mywatchlist.html yang isinya sebagai berikut:
```python
    {% extends 'base.html' %}
    
    {% block content %}
    
    <h1>Lab 1 Assignment PBP/PBD</h1>
    
    <h3>Name: </h3>
    <p>{{nama}}</p>
    
    <h3>Student ID: </h3>
    <p>{{studentId}}</p>
    
    <h3>Informasi: </h3>
    <p>{{fiturPesan}}</p>
    
    <table>
    <tr>
        <th>Watched</th>
        <th>Title</th>
        <th>Rating</th>
        <th>Release Date</th>
        <th>Review</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for watchlist in list_watchlist %}
        <tr>
            <td>{{watchlist.watched}}</td>
            <td>{{watchlist.title}}</td>
            <td>{{watchlist.rating}}</td>
            <td>{{watchlist.release_date}}</td>
            <td>{{watchlist.review}}</td>
        </tr>
    {% endfor %}
    </table>
    
    {% endblock content %}
```
Selanjutnya, pada views.py, saya menambahkan function show_html untuk menampilkan request pada website dengan menampilkan mywatchlist.html tersebut sebagai berikut: 
```python
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
```
Saya juga menerapkan fitur yang menampilkan pesan dengan aturan sebagai berikut: 
- Jika jumlah film yang sudah ditonton lebih banyak atau sama dengan jumlah film yang belum ditonton, tampilkan pesan "Selamat, kamu sudah banyak menonton!" dalam bentuk HTML 
- Jika jumlah film yang belum ditonton lebih banyak dari jumlah film yang sudah ditonton, tampilkan pesan "Wah, kamu masih sedikit menonton!" dalam bentuk HTML
* XML
Pada views.py, saya menambahkan function show_xml untuk menampilkan request pada website dengan menampilkan data dengan format XML tersebut sebagai berikut: 
```python
    def show_xml(request):
        data_mywatchlist = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("xml", data_mywatchlist), content_type="application/xml")
```
* JSON
Pada views.py, saya menambahkan function show_json untuk menampilkan request pada website dengan menampilkan data dengan format JSON tersebut sebagai berikut: 
```python
    def show_json(request):
        data_mywatchlist = MyWatchList.objects.all()
        return HttpResponse(serializers.serialize("json", data_mywatchlist), content_type="application/json")
```
11. Membuat routing sehingga data di atas dapat diakses melalui URL:
- http://localhost:8000/mywatchlist/html untuk mengakses mywatchlist dalam format HTML 
- http://localhost:8000/mywatchlist/xml untuk mengakses mywatchlist dalam format XML 
- http://localhost:8000/mywatchlist/json untuk mengakses mywatchlist dalam format JSON 
Caranya adalah pada urls.py, saya menambahkan urlpatterns sebagai berikut :
```python
    urlpatterns = [
        …
        path('html/', show_html, name='show_html'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        …
    ]
 ```
12. Selanjutnya, saya memanggil command git add ., git commit -m “pesan”, dan git push sehingga repositori saya dapat ter-update. Oleh karena pada tugas 2 kemarin saya sudah men-deploy websitenya, secara otomatis aplikasi mywatchlist dapat diakses menggunakan link deploy tugas 2 yang lalu. Namun, saya menambahkan pada web https://dashboard.heroku.com/apps/django-project-tugas2-2022 dengan memberikan command pada run console berupa perintah python manage.py loaddata initial_mywatchlist_data.json untuk memasukkan data tersebut ke dalam database Django pada link heroku saya.

### Screenshot Postman dari tiga URL
1. HTML ```[GET] http://localhost:8000/mywatchlist/html/```
![HTML](https://user-images.githubusercontent.com/97111982/191467111-3e2a81a8-1485-4267-8aa0-9268b5cfa906.png)
2. XML ```[GET] http://localhost:8000/mywatchlist/xml/```
![XML](https://user-images.githubusercontent.com/97111982/191466271-e136cc25-c729-40c4-9dc1-b00dd4ec7725.png)
3. JSON ```[GET] http://localhost:8000/mywatchlist/json/```
![JSON](https://user-images.githubusercontent.com/97111982/191467254-d6c33d50-dad6-488c-b2cd-1bbea8f1f21b.png)
<br>