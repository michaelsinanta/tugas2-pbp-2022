# Tugas 6: Javascript dan AJAX
Nama    : Michael Christlambert Sinanta\
NPM     : 2106750414\
Kelas   : PBP C\
Link Hasil Deploy : https://django-project-tugas2-2022.herokuapp.com/todolist/

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming. 
1. Asynchronous programming adalah pendekatan pemrograman yang tidak terikat pada input output (I/O) protocol. Dengan pemrograman Asynchronous, beberapa operasi dapat berjalan secara bersamaan tanpa perlu menunggu tugas lain selesai terlebih dahulu. Pekerjaan akan dilakukan tanpa harus terikat dengan proses lain sehingga program dapat berjalan independen. Asynchronous programming adalah arsitektur non-blocking di mana program tidak perlu memblokir eksekusi lebih lanjut saat satu atau lebih operasi berlangsung. 
2. Synchronous programming adalah pendekatan programming yang memiliki pendekatan yang lebih old style di mana pemrograman terikat pada input output (I/O) protocol. Synchronous programming adalah arsitektur blocking di mana suatu operasi akan dilakukan satu per satu dalam urutan. Saat satu operasi sedang diproses, instruksi lainnya akan diblokir. Setelah tugas pertama selesai, maka tugas berikutnya akan dipicu dan seterusnya.\
Selain itu, perbedaan lain antara asynchronous programming dengan synchronous programming adalah sebagai berikut :
- Asynchronous adalah multi-thread sehingga operasi berjalan secara pararel sedangkan synchronous adalah single-thread dimana satu operasi berjalan pada satu waktu.
- Asynchronous meningkatkan throughput karena beberapa operasi dapat berjalan secara bersamaan sedangkan synchronous lebih lambat.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini. 
Event-driven adalah suatu paradigma pemrograman dimana operasi dapat berjalan jika di-trigger/ditentukan dengan suatu event seperti keluaran atau tindakan pengguna untuk menanggapi event tersebut. Event dapat dipicu oleh pengguna seperti dengan meng-klik icon atau memasukkan teks. Subroutine yang merespon event disebut event handler. Event handler akan memastikan apakah pemrosesan sudah sesuai dan terjadi sebagai respons terhadap event yang memicunya.\
Contoh dari penerapan paradigma tersebut pada tugas ini adalah ketika pengguna menekan tombol “Tambah Task Baru”, maka program akan menyiapkan form. Setelah user mengisi form lalu menekan tombol “Tambah Task”, maka program akan menambahkan data baru sesuai input user.

### Jelaskan penerapan asynchronous programming pada AJAX.
Pada program JavaScript, kita perlu menambahkan `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>` pada bagian `<head>` sehingga fitur AJAX dapat dijalankan. Pada AJAX, asynchronous programming dilakukan saat mengirimkan request. Pada saat request diproses, request akan berjalan di “belakang” sehingga user dapat menjalankan operasi lain tanpa harus menunggu. AJAX akan menampung semua event dari pengguna dan kemudian akan diproses secara server-side. Hasil dari proses data akan memperbaharui halaman secara langsung dan user tidak perlu me-refresh halaman karena data akan langsung diperbaharui.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat view baru yang mengembalikan seluruh data task dalam bentuk JSON yaitu show_json dengan views.py sebagai berikut:
```Java
def show_json(request):
   data_todolist = Task.objects.filter(user = request.user)
   return HttpResponse(serializers.serialize("json", data_todolist), content_type="application/json")
```
2. Membuat path /todolist/json yang mengarah ke view yang baru kamu buat. 
```java
   path('json/', show_json, name = 'show_json'),
```
3. Lakukan pengambilan task menggunakan AJAX GET.
Menambahkan `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>` pada bagian `<head>`. Lalu menambahkan AJAX GET di dalamnya.
```java
$(document).ready(function(){
       $.get(window.location.href + "json/", function(data){
           for (i = 0; i < data.length; i++){
               getData(data[i]);
           }
    function getData(data){
           $("#todolist").append(
		#memasukkan hasil get ke dalam elemen HTML
	    }
	}
});
```
4. Untuk AJAX POST, saya membuat tombol Tambah Task Baru yang membuka sebuah modal dengan form untuk menambahkan task.
Membuat view baru untuk menambahkan task baru ke dalam database yaitu add_task yang berisi views.py sebagai berikut :
```java
@login_required(login_url='/todolist/login/')
@csrf_exempt
def add_task(request):
   if request.method == "POST":
       user = request.user
       title = request.POST.get("title")
       description = request.POST.get("description")
       new_task = Task(user = user, title = title, description = description)
       new_task.save()
       return JsonResponse({
           "pk" : new_task.pk, "fields": {
           "date" : new_task.date,
           "title" : new_task.title,
           "description" : new_task.description,
           "is_finished" : new_task.is_finished,
       }})
```
5. Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.
```java
   path('add/', add_task, name="add_task"),
```
6. Menghubungkan form yang telah dibuat di dalam modal kamu ke path /todolist/add
```java
    $("#new-task").submit(function(e){
        e.preventDefault();
        $.post(window.location.href + "add/", { title: $("#title").val(), description: $("#description").val(),
        }).done(function (data) {
            getCard(data);
            deleteCard(data);
            $("#title").val(""), $("#description").val("");
            document.getElementById("todolist").insertAdjacentHTML("beforebegin", $(`#${data.pk}-card`));
        });
    });
```
7. Selanjutnya, saya memanggil command git add ., git commit -m “pesan”, dan git push sehingga repositori saya dapat ter-update. Oleh karena pada tugas 2 kemarin saya sudah men-deploy websitenya, secara otomatis aplikasi todolist dapat diakses menggunakan link deploy tugas 2 yang lalu.