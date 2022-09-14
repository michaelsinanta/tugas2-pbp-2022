# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django
Nama    : Michael Christlambert Sinanta\
NPM     : 2106750414\
Kelas   : PBP C\
Link Repository : https://django-project-tugas2-2022.herokuapp.com/
## Diagram
Berikut adalah bagan yang berisi request client ke web aplikasi berbasis Django:
![BaganMVT](https://user-images.githubusercontent.com/97111982/190168532-2a3693c0-eba4-4f51-8c18-eab31e1f160d.png)

### Jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

Ketika user memberikan URL di laman pencarian, browser akan melakukan HTTP request yang user berikan ke dalam server Django dan Django akan mencocokan url yang diminta dengan url yang didefinisikan pada urls.py / parsing sesuai dengan urlspattern yang cocok. Bila tidak ditemukan, maka Django akan memanggil halaman error dengan kode 404.\
Jika sudah sesuai, urls.py akan meneruskan permintaan ke views.py. Views.py akan bertugas sebagai penengah dimana ia akan menggunakan berkas html (template) untuk mengatur dan memetakan tampilan web serta menggunakan models.py untuk melakukan query terhadap database dan dapat memanggil, menulis, maupun menghapus objek/data apa saja yang ingin digunakan nantinya.\
Fungsi view akan mengembalikan response berupa berkas html. Setelah permintaan selesai diproses, hasil dari berkas html tersebut akan dirender dan menampilkan konten data pada halaman web untuk klien/user. 
<br> 
### Mengapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita menggunakan virtual environment sebagai wadah virtual yang dapat membantu kita dalam mengatur dependecies dan library yang dibutuhkan dalam project sehingga tidak terpisah satu sama lain. Virtual environment dapat mengontrol masing-masing python package dengan versi yang kita inginkan dan mencegah konflik antar satu program dengan program lainnya.\
Kita tetap bisa membuat aplikasi web berbasis Django walaupun tidak memakai virtual environment. Namun, hal ini tidak direkomendasikan karena jika kita membiarkan dependencies diinstal secara global, kita dapat menyebabkan overwrite package saat development project kita nantinya dan berpotensti menciptakan konflik antar project.

### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

**I. Langkah 1** 

1. Django-app sudah tersedia yaitu bernama katalog sehingga kita bisa langsung dapat menggunakannya. Pada settings.py di folder project_django, aplikasi katalog juga sudah terdaftar dalam variabel INSTALLED_APPS.

2. CatalogItem model sudah tersedia di models.py. Selanjutnya, kita membuat fungsi show_katalog pada views.py. Saya melengkapi dictionary show_katalog dengan nama dan NPM saya.
        from django.shortcuts import render
        from katalog.models import CatalogItem

        def show_katalog(request):
            data_katalog = CatalogItem.objects.all()
            context = {
                'list_katalog': data_katalog,
                'nama': 'Michael Christlambert Sinanta',
                'studentId': "2106750414"
            }
            return render(request, "katalog.html", context)

3. Mendaftarkan aplikasi katalog ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns. 
        
        path('katalog/', include('katalog.urls')),

**II. Langkah 2**\
Melakukan routing terhadap fungsi views yang telah kamu buat sehingga nantinya halaman HTML dapat ditampilkan lewat browser dengan menambahkan nama aplikasi dan urlpatterns dari urls.py pada folder katalog sebagai berikut.\
    
        from katalog.views import show_katalog

        app_name = 'katalog'

        urlpatterns = [
            path('', show_katalog, name='show_katalog'),
        ]

**III. Langkah 3**\
Mengatur berkas katalog.html dan memetakan data yang diteruskan dari fungsi show_katalog serta mengiterasi list_katalog dengan template sebagai berikut :

        {% extends 'base.html' %}
        
        {% block content %}

        <h1>Lab 1 Assignment PBP/PBD</h1>

        <h5>Name: </h5>
        <p>{{nama}}</p>

        <h5>Student ID: </h5>
        <p>{{studentId}}</p>

        <table>
        <tr>
        <th>Item Name</th>
        <th>Item Price</th>
        <th>Item Stock</th>
        <th>Rating</th>
        <th>Description</th>
        <th>Item URL</th>
        </tr>
        {% comment %} Add the data below this line {% endcomment %}
        {% for katalog in list_katalog %}
        <tr>
            <td>{{katalog.item_name}}</td>
            <td>{{katalog.item_price}}</td>
            <td>{{katalog.description}}</td>
            <td>{{katalog.item_stock}}</td>
            <td>{{katalog.rating}}</td>
            <td>{{katalog.item_url}}</td>
        </tr>
        {% endfor %}
        </table>

        {% endblock content %}


**IV. Langkah 4**\
Saya membuat aplikasi baru pada Heroku dan mengambil nama aplikasi serta API Key. Selanjutnya, saya menambahkan secrets pada github repository tugas 2 dengan variabel sebagai berikut :\
HEROKU_API_KEY: <VALUE_API_KEY_ANDA>\
HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU_ANDA>\
Selanjutnya, saya menunggu sampai berhasil ter-deploy dan website berhasil terbentuk. 
