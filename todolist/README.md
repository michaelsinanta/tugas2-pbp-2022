# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django
Nama    : Michael Christlambert Sinanta\
NPM     : 2106750414\
Kelas   : PBP C\
Link Hasil Deploy : https://django-project-tugas2-2022.herokuapp.com/todolist/

### Apa kegunaan {% csrf_token %} pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
{% csrf_token %} pada elemen `<form>` berfungsi sebagai penanda bagi form bahwa token csrf berasal dari server. Token CSRF adalah token yang berisi nilai yang unik dan rahasia. Token ini dihasilkan oleh server dan dikirimkan ke klien serta disertakan dalam HTTP request. Saat permintaan request dibuat, sercer akan memvalidasi request tersebut dengan token yang diharapkan. Jika permintaan pada token salah, maka request tidak valid. Dengan token CSRF, maka hacker tidak dapat membuat request sembarangan pada aplikasi kita karena tidak dapat menentukan nilai token CSRF korbannya.\
Tanpa {% csrf_token %}, request pengguna tidak memiliki kode token yang menjaga form agar terlindungi dari serangan keamanan. Hal ini dapat menjadi celah bagi hacker untuk membuat HTTP request agar dapat melakukan aktivitas pada sistem dan data kita. Misalnya jika pada halaman create-task tidak ditambahkan csrf_token, maka hacker dapat menambahkan, menghapus, dan mengubah status task tanpa perlu menebak kode token. Hal ini tentu sangat berbahaya dan menyebabkan keamanan website kita terancam oleh hacker.

### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual. 
Iya, kita dapat membuat elemen `<form>` secara manual. Dengan generator {{ form.as_table }}, generator tersebut merupakan fasilitas dari Django Template Language untuk membuat form dalam tabel secara efektif dan lebih mudah. Namun, tentu saja elemen `<form>` dapat kita gunakan untuk menerima dan mengumpulkan data dari pengguna sehingga dapat kita gunakan secara manual.\
Gambaran besar bagaimana cara membuat `<form>` secara manual :
1. Pada template, buatlah tags `<form>` yang menggunakan method POST.
2. Tags `<form>` merujuk ke suatu route dan kita akan implementasikan pada views.py untuk meng-handle request tersebut.
3. Meletakkan semua komponen input dan button pada tags `<form>`.
4. Pada views.py, kita mendapatkan data input yang akan dimasukkan ke dalam form lalu kita akan memanipulasi (CRUD) resource pada database sesuai dengan parameter yang diberikan pada POST tersebut.

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. 
1. User meng-input data yang akan diterima oleh `<form>` dan akan diterima/di-trigger oleh input bertipe submit.
2. Setelah itu, views akan membaca request dari user dan mendapatkan parameter serta value dari request POST.
3. Input akan di-handle berdasarkan manipulasi (CRUD) yang telah diprogram pada views.py.
4. Data tersebut akan digunakan pada template sehingga dimasukkan pada context.
5. Selanjutnya, view akan me-return hasil render dengan template dan context tersebut.
6. Template akan menggunakan informasi dari context untuk ditampilkan kepada user.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat sebuah django-app bernama todolist dengan perintah python manage.py startapp todolist.
2. Membuka settings.py di folder project_django dan menambahkan aplikasi todolist ke dalam variabel INSTALLED_APPS untuk mendaftarkan django-app ke dalam proyek Django, sebagai berikut:
```python
    INSTALLED_APPS = [
    ..., 
    'todolist', 
    ]
```
3. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist dengan membuat sebuah berkas di dalam folder aplikasi todolist bernama urls.py untuk melakukan routing terhadap fungsi views lah kamu buat sehingga nantinya halaman HTML dapat ditampilkan lewat browser. Isi dari urls.py tersebut adalah sebagai berikut.
```python
    from django.urls import path
    from todolist.views import show_todolist

    app_name = 'todolist'

    urlpatterns = [
        path('', show_todolist, name='show_todolist'),
    ]
```
4. Mendaftarkan aplikasi todolist ke dalam urls.py yang ada pada folder project_django dengan menambahkan potongan kode berikut pada variabel urlpatterns.
```python
    path('todolist/', include('todolist.urls')),
```
5. Menambahkan data yang diperlukan pada models.py sebagai berikut :
```python
    from django.db import models
    from django.contrib.auth.models import User
 
    class Task(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateField(auto_now_add = True)
        title = models.CharField(max_length= 255)
        description = models.TextField()
        is_finished = models.BooleanField(default=False)
```
6. Menjalankan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal. 
7. Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
8. Membuat file forms.py dan memanipulasi class TaskForm sesuai kebutuhan input.
9. Mengimplementasikan fungsi untuk form registrasi, login, logout, membuat task baru, menghapus task, dan mengubah status task agar pengguna dapat menggunakan todolist pada views.py.  
10. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task pada todolist.html.
11. Membuat halaman form untuk pembuatan task dan data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task pada create_task.html. Lalu, membuat halaman untuk login pada login.html dan register user pada register.html.
12. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut:
```python
    from django.urls import path
    from todolist.views import show_todolist
    from todolist.views import create_task
    from todolist.views import register
    from todolist.views import login_user
    from todolist.views import logout_user
    from todolist.views import delete_task
    from todolist.views import toggle_status
    
    app_name = "todolist"
    
    urlpatterns = [
        path('', show_todolist, name = 'show_todolist'),
        path('create-task/', create_task, name = 'create_task'),
        path('register/', register, name = 'register'),
        path('login/', login_user, name = 'login_user'),
        path('logout/', logout_user, name = 'logout_user'),
        path('toggle-status/<int:id>', toggle_status, name = 'toggle_status'),
        path('delete-task/<int:id>', delete_task, name = 'delete_task'),
    ]
```
13. Selanjutnya, saya memanggil command git add ., git commit -m “pesan”, dan git push sehingga repositori saya dapat ter-update. Oleh karena pada tugas 2 kemarin saya sudah men-deploy websitenya, secara otomatis aplikasi todolist dapat diakses menggunakan link deploy tugas 2 yang lalu.
