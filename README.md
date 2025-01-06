# Kelompok
<body>
    <table border="1">
        <tr>
            <th>Nama</th>
            <th>NIM</th>
            <th>Kelas</th>
            <th>Contribution</th>
        </tr>
        <tr>
            <td>Ahmad Syukron</td>
            <td>312110056</td>
            <td>TI.21.A.1</td>
            <td>Design User Interface (Front End, HTML dan CSS)</td>
        </tr>
        <tr>
            <td>Abid Husein</td>
            <td>312110031</td>
            <td>TI.21.A.1</td>
            <td>Rancangan Basis Data ERD</td>
        </tr>
        <tr>
            <td>Iman Setiawan</td>
            <td>312110219</td>
            <td>TI.21.A.1</td>
            <td>Publikasi Aplikasi (Web Hosting)</td>
        </tr>
        <tr>
        </tr>
    </table>
</body>
 
## Pembuatan Bersama
* Implementasi kode php menggunakan CodeIgniter 4
* Laporan (Dalam Bentuk toturial Lengkap dengan tahapan hasil eksekusi query) dalam bentuk:<p>
  + README.md
  + Video yang diyoutube

# Daftar Isi

- [Server DEMO](#server-demo)
  - [Video Penjelasan Aplikasi](#video-penjelasan-aplikasi)
- [Langkah Pembuatan](#langkah-pembuatan)
  - [Langkah 1: Install Codeigniter 4](#langkah-1-instal-codeigniter-4)
  - [Langkah 2: Create ERD](#langkah-2-create-erd)
  - [Langkah 3: Create the Database](#langkah-3-create-the-database)
  - [Langkah 4: Configuration](#langkah-4-configuration)
  - [Langkah 5: Create Model](#langkah-5-create-model)
  - [Langkah 6: Create Controller](#langkah-6-create-controller)
  - [Langkah 7: Create Views](#langkah-7-create-views)
  - [Langkah 8: Routes](#langkah-8-routes)
  - [Membuat Menu LOGIN](#membuat-menu-login)
- [Selesai](#terimakasih)


##  Server DEMO
Untuk mencoba aplikasi ini silahkan klik [DEMO](https://dinkadealer.site/) ini<p>
User/Password Admin Page:<p> 
- user: `admin2100`
- password: `Ganteng12345`
> Untuk menggunakan aplikasi ini ketik `git clone` paste code HTTPS.
> `composer install` lalu `composer update` untuk menginstall dan memperbaharui versi vendor<p>

### Video Penjelasan Aplikasi
[![Final video of fixing issues in your code in VS Code](https://img.youtube.com/vi/41PfBAvXD3U/maxresdefault.jpg)](https://www.youtube.com/watch?v=41PfBAvXD3U)


## Langkah Pembuatan
### Langkah 1: Instal CodeIgniter 4

Download dan install CodeIgniter 4 menggunakan Composer dengan cara 
```bash
composer create-project codeigniter4/appstarter jual-mobil -vvv
```
  - <b>create-project</b> adalah perintah untuk membuat proyek baru dengan composer;
  - <b>codeigniter4/appstarter</b> adalah file CI yang akan di-download;
  - <b>jual-mobil</b> adalah nama proyek yang akan kita buat;
  - <b>-vvv</b> berfungsi untuk melihat proses install lebih detail.<p>

Jika belum mempunyai composer anda bisa download di sini [Get Composer](https://getcomposer.org/download/) </p><br>

### Langkah 2: Create ERD

<br>


### Langkah 3: Create the Database
Buat database MySQL untuk aplikasi penjualan mobil, nama database `ci4`<p><br>

1. <b>Cars Table:</b>
    ```sql
    CREATE TABLE `cars` (
      `id` int(11) NOT NULL,
      `picture` varchar(255) NOT NULL,
      `name` varchar(255) NOT NULL,
      `type` varchar(255) NOT NULL,
      `description` varchar(255) DEFAULT NULL,
      `price` varchar(255) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ```
<br>


2. <b>Customers Table</b>
    ```sql
    CREATE TABLE `customers` (
      `id` int(11) NOT NULL,
      `name` varchar(255) NOT NULL,
      `phone_number` varchar(255) NOT NULL,
      `email` varchar(255) NOT NULL,
      `address` varchar(255) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ```
<br>


3. <b>Salesperson Table</b>
    ```sql
    CREATE TABLE `salesperson` (
      `id` int(11) NOT NULL,
      `name` varchar(255) NOT NULL,
      `phone_number` varchar(255) NOT NULL,
      `email` varchar(255) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ```
<br>


4. <b>Transaction Table</b>
    ```sql
    CREATE TABLE `transactions` (
      `id` int(11) NOT NULL,
      `customer_id` varchar(255) NOT NULL,
      `car_id` varchar(255) NOT NULL,
      `salesperson_id` varchar(255) NOT NULL,
      `price` varchar(255) NOT NULL,
      `created_at` datetime DEFAULT NULL,
      `updated_at` datetime DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    ```
<br>


5. <b>Users Table</b>
    ```sql
    CREATE TABLE `users` (
      `id` int(11) UNSIGNED NOT NULL,
      `email` varchar(255) NOT NULL,
      `username` varchar(30) DEFAULT NULL,
      `password_hash` varchar(255) NOT NULL,
      `reset_hash` varchar(255) DEFAULT NULL,
      `reset_at` datetime DEFAULT NULL,
      `reset_expires` datetime DEFAULT NULL,
      `activate_hash` varchar(255) DEFAULT NULL,
      `status` varchar(255) DEFAULT NULL,
      `status_message` varchar(255) DEFAULT NULL,
      `active` tinyint(1) NOT NULL DEFAULT 0,
      `force_pass_reset` tinyint(1) NOT NULL DEFAULT 0,
      `created_at` datetime DEFAULT NULL,
      `updated_at` datetime DEFAULT NULL,
      `deleted_at` datetime DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    ```
<br>



### Langkah 4: Configuration
<p>Buka file <b>app/Config/Database.php</b> dan konfigurasikan detail koneksi database Anda (misalnya, hostname, username, password, database name).</p>
<br>


### Langkah 5: Create Model
Buat model file <b>app/Models/</b><p>
Disini model yang kita buat ada `CarModel.php`, `CustomerModel.php`, `SalesPersonModel.php`, dan `TransactionModel.php`<p>

* <b>CarModel.php</b>
    ```php
    <?php

    namespace App\Models;

    use CodeIgniter\Model;

    class CarModel extends Model
    {
        protected $table = 'cars';
        protected $primaryKey = 'id';
        protected $allowedFields = ['name', 'type', 'price', 'picture', 'description'];

        public function search($keyword)
        {
            return $this->like('name', $keyword)->findAll();
        }
    }
    ```
<br>


* <b>CustomerModel.php</b>
    ```php
    <?php

    namespace App\Models;

    use CodeIgniter\Model;

    class CustomerModel extends Model
    {
        protected $table = 'customers';
        protected $primaryKey = 'id';
        protected $allowedFields = ['name', 'phone_number', 'email', 'address'];
        public function search($keyword)
        {
            return $this->like('name', $keyword)->findAll();
        }
    }
    ```        
<br>


* <b>SalesPersonModel.php</b>
    ```php
    <?php
    namespace App\Models;
    use CodeIgniter\Model;
    class SalesPersonModel extends Model
    {
        protected $table = 'salesperson';
        protected $primaryKey = 'id';
        protected $allowedFields = ['name', 'phone_number', 'email'];

        public function search($keyword)
        {
            return $this->like('name', $keyword)->findAll();
        }
    }
    ```     
<br>


* <b>TransactionModel.php</b>
    ```php
    <?php

    namespace App\Models;

    use CodeIgniter\Model;

    class TransactionModel extends Model
    {
        protected $table = 'transactions';
        protected $primaryKey = 'id';
        protected $allowedFields = ['customer_id', 'car_id', 'salesperson_id', 'price'];
        protected $useTimestamps = true; // Enable automatic timestamps

        protected $createdField = 'created_at'; // Specify the created_at field name
        protected $updatedField = 'updated_at'; // Specify the updated_at field name

        public function search($keyword)
        {
            return $this->like('customer_id', $keyword)->findAll();
        }
    }
    ```
<br>



### Langkah 6: Create Controller
Buat Controller file <b>app/Controllers/</b><p>
Disini model yang kita buat ada `CarsController.php`, `CustomerController.php`, `DashboardController.php`, `SalesPersonController.php`, `Home.php`, `Pages.php`, `UserPageController.php`, dan `TransactionController.php`<p>

* <b>CarsController.php</b>
    ```php
    <?php

    namespace App\Controllers;

    use App\Models\CarModel;
    use CodeIgniter\Controller;

    class CarsController extends Controller
    {
        public function index()
        {
            $carModel = new CarModel();
            $data = [
                'title' => 'Cars List',
                'cars' => $carModel->findAll()
                
            ];

            return view('cars/index', $data);
        }

        public function create()
        {
            $data = [
                'title' => 'Input New Cars'
            ];
            return view('cars/create', $data);
        }

        public function store()
        {

            $filepicture = $this->request->getFile('picture');
            $filepicture->move('car_img');
            $namepicture = $filepicture->getName();

            $carModel = new CarModel();
            $carData = [
                'name' => $this->request->getPost('name'),
                'type' => $this->request->getPost('type'),
                'picture' => $namepicture,
                'description' => $this->request->getPost('description'),
                'price' => $this->request->getPost('price'),
            ];

            $carModel->insert($carData);

            return redirect()->to('/car');
        }

        public function edit($id)
        {
            $carModel = new CarModel();
            $data = [
                'title' => 'Edit Cars',
                'car' => $carModel->find($id)
                
            ];
            return view('cars/edit', $data);
        }

        public function update($id)
        {
            $carModel = new CarModel();
            $carData = [
                'name' => $this->request->getPost('name'),
                'type' => $this->request->getPost('type'),
                'price' => $this->request->getPost('price'),
                'description' => $this->request->getPost('description'),
                'price' => $this->request->getPost('price'),
            ];


            $carModel->update($id, $carData);

            return redirect()->to('/car');
        }

        public function delete($id)
        {
            $carModel = new CarModel();
            $carModel->delete($id);

            return redirect()->to('/car');
        }

        public function find()
        {
            $keyword = $this->request->getPost('keyword');
            $carModel = new CarModel();

            $data = [
                'title' => 'Edit Sales Person',
                'cars' => $carModel->search($keyword)
            ];

            return view('cars/index', $data);
        }
    }
    ```
<br>


* <b>CustomerController.php</b>
    ```php
    <?php

    namespace App\Controllers;

    use App\Models\CustomerModel;
    use CodeIgniter\Controller;

    class CustomerController extends Controller
    {
        public function index()
        {
            $customerModel = new CustomerModel();
            $data = [
                'title' => 'Customer List',
                'customers' => $customerModel->findAll()
                
            ];

            return view('customer/index', $data);
        }

        public function create()
        {
            $data = [
                'title' => 'Tambah Customer'
            ];
            return view('customer/create', $data);
        }

        public function store()
        {
            $customerModel = new CustomerModel();

            $data = [
                
                'name' => $this->request->getVar('name'),
                'phone_number' => $this->request->getVar('phone_number'),
                'email' => $this->request->getVar('email'),
                'address' => $this->request->getVar('address')
            ];

            $customerModel->insert($data);

            return redirect()->to('/customer');
        }

        public function edit($id)
        {
            $customerModel = new CustomerModel();
            $data['customer'] = $customerModel->find($id);

            $data = [
                'title' => 'Edit Customer',
                'customer' => $customerModel->find($id)
                
            ];

            return view('customer/edit', $data);
        }

        public function update($id)
        {
            $customerModel = new CustomerModel();

            $data = [
                'name' => $this->request->getVar('name'),
                'phone_number' => $this->request->getVar('phone_number'),
                'email' => $this->request->getVar('email'),
                'address' => $this->request->getVar('address')
            ];

            $customerModel->update($id, $data);

            return redirect()->to('/customer');
        }

        public function delete($id)
        {
            $customerModel = new CustomerModel();
            $customerModel->delete($id);

            return redirect()->to('/customer');
            
        }

        public function find()
        {
            $keyword = $this->request->getPost('keyword');
            $customerModel = new CustomerModel();

            $data = [
                'title' => 'Edit Customer',
                'customers' => $customerModel->search($keyword)
            ];

            return view('customer/index', $data);
        }

    }
    ```
<br>


* <b>DashboardController.php</b>
    ```php
    <?php

    namespace App\Controllers;

    use App\Models\TransactionModel;
    use CodeIgniter\Controller;

    class DashboardController extends Controller
    {
        public function index()
        {
            $transactionModel = new TransactionModel();
            $transactions = $transactionModel->findAll();

            $data['prices'] = [];
            $data['dates'] = [];
            $data['title'] = 'Dasboard';

            foreach ($transactions as $transaction) {
                $data['prices'][] = $transaction['price'];
                $data['dates'][] = $transaction['created_at'];
            }

            return view('sales/dashboard', $data);
        }
    }
    ```
<br>


* <b>SalesPersonController.php</b>
    ```php
    <?php

    namespace App\Controllers;

    use App\Models\SalesPersonModel;
    use CodeIgniter\Controller;

    class SalesPersonController extends Controller
    {

        protected $salesPersonModel;

        public function __construct()
        {
            $this->salesPersonModel = new SalesPersonModel();
        }
        public function index()
        {
            $model = new SalesPersonModel();
            $data = [
                'title' => 'Sales Person List',
                'agents' => $model->findAll()
                
            ];

            return view('sales-person/index', $data);
        }

        public function create()
        {
            $data = [
                'title' => 'Add Sales Person',
                
            ];
            return view('sales-person/create', $data);
        }

        public function store()
        {
            $model = new SalesPersonModel();

            $agentData = [
                'name' => $this->request->getVar('name'),
                'phone_number' => $this->request->getVar('phone_number'),
                'email' => $this->request->getVar('email')
            ];

            $model->insert($agentData);

            return redirect()->to('/sales-person');
        }

        public function edit($id)
        {
            $model = new SalesPersonModel();
            $data = [
                'title' => 'Edit Sales Person',
                'salesperson' => $model->find($id)
                
            ];

            return view('sales-person/edit', $data);
        }

        public function update($id)
        {
            $model = new SalesPersonModel();

            $agentData = [
                'name' => $this->request->getVar('name'),
                'phone_number' => $this->request->getVar('phone_number'),
                'email' => $this->request->getVar('email')
            ];

            $model->update($id, $agentData);

            return redirect()->to('/sales-person');
        }

        public function delete($id)
        {
            $model = new SalesPersonModel();
            $model->delete($id);

            return redirect()->to('/sales-person');
        }

        public function find()
        {
            $keyword = $this->request->getPost('keyword');
            $salesPersonModel = new SalesPersonModel();

            $data = [
                'title' => 'Edit Sales Person',
                'agents' => $salesPersonModel->search($keyword)
            ];

            return view('sales-person/index', $data);
        }
        
    }

    ```
<br>


* <b>Home.php</b>
    ```php
    <?php

    namespace App\Controllers;

    class Home extends BaseController
    {
        public function index()
        {
            return view('welcome_message');
        }
    }
    ```
<br>


* <b>Pages.php</b>
    ```php
    <?php

    namespace App\Controllers;

    class Pages extends BaseController
    {
        public function home()
        {
            $data = [
                'title' => 'Home Page'
            ];
            echo view('Pages/home', $data);

        }
        public function about()
        { 
            $data = [
                'title' => 'About'
            ];
            echo view('Pages/About', $data);
        }

        public function contact()
        { 
            $data = [
                'title' => 'Contact Us',
                'alamat' => [
                    [
                        'tipe' => 'Rumah',
                        'alamat' => 'Jalan Bosih',
                        'kota' => 'Bekasi'
                    ],
                    [
                        'tipe' => 'Kantor',
                        'alamat' => 'Jalan Kota',
                        'kota' => 'Jakarta'
                    ]
                ]
            ];
            echo view('Pages/contact', $data);
        }


    }
    ```
<br>


* <b>UserPageController.php</b>
    ```php
    <?php

    namespace App\Controllers;

    use App\Models\CarModel;

    class UserPageController extends BaseController
    {
        public function index()
        {


            $carModel = new CarModel();
            // Retrieve car data from the database

            $randomPictures = $carModel
                ->select('picture')
                ->orderBy('RAND()')
                ->limit(5)
                ->findAll();

            $cars = $carModel->findAll();

            // Pass the car data to the view
            $data = [
                'cars' => $cars,
                'title' => 'Dinka Dealer',
                'randomPictures' => array_slice($randomPictures, 0, 5),
            ];
            echo view('user/home', $data);
        }

        public function vehicle()
        {

            $carModel = new CarModel();
            $data = [
                'title' => 'Vehicle List',
                'cars' => $carModel->findAll()
            ];

            echo view('user/vehicle', $data);
        }
    }
    ```
<br>


* <b>TransactionController.php</b>
    ```php
    <?php

    namespace App\Controllers;

    use App\Models\CustomerModel;
    use App\Models\CarModel;
    use App\Models\SalesPersonModel;
    use App\Models\TransactionModel;

    class TransactionController extends BaseController
    {
        protected $customerModel;
        protected $carModel;
        protected $salesPersonModel;

        public function __construct()
        {
            $this->customerModel = new CustomerModel();
            $this->carModel = new CarModel();
            $this->salesPersonModel = new SalesPersonModel();
        }

        // Display a list of transactions
        public function index()
        {
            // Assuming you have a TransactionModel.php model, retrieve all transactions
            $transactionModel = new TransactionModel();


            $data = [
                'title' => 'Transaction',
                'transactions' => $transactionModel->findAll()
                
            ];

            return view('transaction/index', $data);
        }

        // Display the create transaction form
        public function create()
        {
            $data['title'] = 'Create Transaction';
            $data['customers'] = $this->customerModel->findAll();
            $data['cars'] = $this->carModel->findAll();
            $data['salespersons'] = $this->salesPersonModel->findAll();
        

            return view('transaction/create', $data);
        }

        // Store the newly created transaction
        public function store()
        {
            // Get the input data
            $customerId = $this->request->getPost('customer_id');
            $carId = $this->request->getPost('car_id');
            $salespersonId = $this->request->getPost('salesperson_id');
            $price = $this->request->getPost('price');
        
            // Store the transaction in the database (you need to create the transaction model)
            $transactionData = [
                'customer_id' => $customerId,
                'car_id' => $carId,
                'salesperson_id' => $salespersonId,
                'price' => $price
            ];
        
            // Assuming you have a TransactionModel.php model, create a new instance and save the data
            $transactionModel = new TransactionModel();
            $transactionModel->insert($transactionData);
        
            // Redirect to the transaction list page or show a success message
            return redirect()->to('/transaction')->with('success', 'Transaction created successfully.');
        }

        // Display the edit transaction form
        public function edit($id)
        {
            $transactionModel = new TransactionModel();
            $data['title'] = 'Edit Data';
            $data['transaction'] = $transactionModel->find($id);
            $data['customers'] = $this->customerModel->findAll();
            $data['cars'] = $this->carModel->findAll();
            $data['salespersons'] = $this->salesPersonModel->findAll();

            return view('transaction/edit', $data);
        }

        // Update the existing transaction
        public function update($id)
        {
            // Get the input data
            $customerId = $this->request->getPost('customer_id');
            $carId = $this->request->getPost('car_id');
            $salespersonId = $this->request->getPost('salesperson_id');
            $price = $this->request->getPost('price');

            // Update the transaction in the database
            $transactionData = [
                'customer_id' => $customerId,
                'car_id' => $carId,
                'salesperson_id' => $salespersonId,
                'price' => $price
            ];

            // Assuming you have a TransactionModel.php model, update the transaction data
            $transactionModel = new TransactionModel();
            $transactionModel->update($id, $transactionData);

            // Redirect to the transaction list page or show a success message
            return redirect()->to('/transaction')->with('success', 'Transaction updated successfully.');
        }

        // Delete a transaction
        public function delete($id)
        {
            // Assuming you have a TransactionModel.php model, delete the transaction
            $transactionModel = new TransactionModel();
            $transactionModel->delete($id);

            // Redirect to the transaction list page or show a success message
            return redirect()->to('/transaction')->with('success', 'Transaction deleted successfully.');
        }

        public function index2()
        {
            $transactionModel = new TransactionModel();

            // Get total sales
            $totalSales = $transactionModel->selectSum('price')->get()->getRowArray()['price'];

            // Calculate profit (10% of total sales)
            $profit = $totalSales * 0.1;

            // Get transactions for the selected month
            $selectedMonth = $this->request->getGet('month');
            $transactions = $transactionModel->where('MONTH(created_at)', $selectedMonth)->findAll();

            // Pass the data to the view
            $data = [
                'totalSales' => $totalSales,
                'profit' => $profit,
                'transactions' => $transactions,
                'title' => 'asd'
            ];

            return view('sales/dashboard', $data);
        }
        public function find()
        {
            $keyword = $this->request->getPost('keyword');
            $transactionModel = new TransactionModel();

            $data = [
                'title' => 'Edit Sales Person',
                'transactions' => $transactionModel->search($keyword)
            ];

            return view('transaction/index', $data);
        }
    }
    ```
<br>



### Langkah 7: Create Views
* Buat folder `app/Views/cars` dan buat file ini:<p>

  + <b>create.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>
    <br>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1>Input New Cars</h1>

                <form method="post" action="/car/store" enctype="multipart/form-data">


                    <div class="row mb-3">
                        <label for="name" class="col-sm-2 form-label">Name:</label>
                        <div class="col-sm-5">
                            <input type="text" name="name" id="name" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="type" class="col-sm-2 form-label">Tipe</label>
                        <div class="col-sm-5">
                            <input type="type" name="type" id="type" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="picture" class="col-sm-2 form-label">Image</label>
                        <div class="col-sm-5">
                            <input class="form-control" type="file" id="picture" name="picture" required>

                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="description" class="col-sm-2 form-label">Description</label>
                        <div class="col-sm-5">
                            <textarea name="description" id="description" class="form-control" required></textarea>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="price" class="col-sm-2 form-label">Price</label>
                        <div class="col-sm-5">
                            <input type="number" name="price" id="price" class="form-control" required oninput="formatCurrency(this)">
                            <div id="currency-display" class="form-control" style="border: none; pointer-events: none;"></div>
                        </div>
                        <div class="col-sm-5">
                        </div>
                    </div>

                    <script>
                        function formatCurrency(input) {
                            const price = input.value;
                            const formattedPrice = new Intl.NumberFormat('id-ID', {
                                style: 'currency',
                                currency: 'IDR'
                            }).format(price);
                            document.getElementById('currency-display').innerText = formattedPrice;
                        }
                    </script>



                    <button type="submit" class="btn btn-primary">Add Cars</button>
                </form>
            </div>
        </div>
    </div>

    <?= $this->endSection(); ?>
    ```
<br>


  + <b>edit.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>
    <br>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1>Edit Cars Data</h1>
                <form method="post" action="/car/update/<?= $car['id']; ?>" enctype="multipart/form-data">
                    <div class="row mb-3">
                        <label for="name" class="form-label col-sm-2">Name</label>
                        <div class="col-sm-5">
                            <input type="text" name="name" id="name" value="<?= $car['name']; ?>" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="type" class="form-label col-sm-2">Type</label>
                        <div class="col-sm-5">
                            <input type="type" name="type" id="type" value="<?= $car['type']; ?>" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="description" class="col-sm-2 form-label">Description</label>
                        <div class="col-sm-5">
                            <textarea name="description" id="description" class="form-control" required><?= $car['description']; ?></textarea>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="price" class="form-label col-sm-2">Price</label>
                        <div class="col-sm-5">
                            <input type="type" name="price" id="price" value="<?= $car['price']; ?>" class="form-control" required>
                        </div>
                    </div>

                    <button type="submit" class="btn btn-primary">Update Cars</button>
                </form>


            </div>
        </div>
    </div>

    <?= $this->endSection(); ?>
    ```
<br>


  + <b>index.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>

    <div class="container">
        <br>
        <div class="d-flex justify-content-center">
            <h1>Cars List</h1>
        </div>


        <div class="d-flex justify-content-between">
            <a class="btn btn-success" href="/car/create">Add New Cars</a>
            <form action="/car/find" method="post">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search by name" name="keyword">
                    <div class="input-group-append">
                        <button class="btn btn-info" type="submit">Search</button>
                        <a class="btn btn-info" href="/car" role="button">Reset</a>
                    </div>
                </div>
            </form>
        </div>

        <?php if (session()->has('success')) : ?>
            <div class="alert alert-success"><?= session('success') ?></div>
        <?php endif; ?>

        <table class="table">
            <thead>
                <tr class="text-center">
                    <th>No</th>
                    <th>Name</th>
                    <th>Picture</th>
                    <th>Type</th>
                    <th>Description</th>
                    <th>Price</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($cars as $index => $customer) : ?>
                    <tr class="text-center">
                        <td tyle="white-space: nowrap;"><?= $index + 1; ?></td>
                        <td tyle="white-space: nowrap;"><?= $customer['name']; ?></td>
                        <td tyle="white-space: nowrap;">

                            <img class="img-fluid" src="/car_img/<?= $customer['picture']; ?>" alt="Car Picture" width="250px">

                        </td>
                        <td tyle="white-space: nowrap;"><?= $customer['type']; ?></td>
                        <td><?= $customer['description']; ?></td>

                        <td style="white-space: nowrap;">Rp <?= number_format($customer['price'], 0, ',', '.'); ?></td>


                        <td style="white-space: nowrap;">
                            <a href="/car/edit/<?= $customer['id']; ?>" class="btn btn-warning">Edit</a>
                            <a href="/car/delete/<?= $customer['id']; ?>" class="btn btn-danger">Delete</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>

    <?= $this->endSection(); ?>
    ```
<br>


* Buat folder `app/Views/customer` dan buat file ini:<p>

  + <b>create.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>
    <br>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1>Add New Customer</h1>

                <form method="post" action="/customer/store">


                    <div class="row mb-3">
                        <label for="name" class="col-sm-2 form-label">Name:</label>
                        <div class="col-sm-5">
                            <input type="text" name="name" id="name" class="form-control" required>
                        </div>
                    </div>




                    <div class="row mb-3">
                        <label for="phone_number" class="col-sm-2 form-label">Phone Number:</label>
                        <div class="col-sm-5">
                            <input type="text" name="phone_number" id="phone_number" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="email" class="col-sm-2 form-label">Email:</label>
                        <div class="col-sm-5">
                            <input type="email" name="email" id="email" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="address" class="col-sm-2 form-label">Address:</label>
                        <div class="col-sm-5">
                            <textarea name="address" id="address" class="form-control" required></textarea>
                        </div>
                    </div>

                    <button type="submit" class="btn btn-primary">Add Customer</button>
                </form>
            </div>
        </div>
    </div>


    <?= $this->endSection(); ?>
    ```
<br>


  + <b>edit.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>
    <br>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1>Edit Customers</h1>
                <form method="post" action="/customer/update/<?= $customer['id']; ?>">
                    <div class="row mb-3">
                        <label for="name" class="form-label col-sm-2">Name:</label>
                        <div class="col-sm-5">
                        <input type="text" name="name" id="name" value="<?= $customer['name']; ?>" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="phone_number" class="form-label col-sm-2">Phone Number:</label>
                        <div class="col-sm-5">
                        <input type="text" name="phone_number" id="phone_number" value="<?= $customer['phone_number']; ?>" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="email" class="form-label col-sm-2">Email:</label>
                        <div class="col-sm-5">
                        <input type="email" name="email" id="email" value="<?= $customer['email']; ?>" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="address" class="form-label col-sm-2">Address:</label>
                        <div class="col-sm-5">
                        <textarea name="address" id="address" class="form-control" required><?= $customer['address']; ?></textarea>
                        </div>
                    </div>

                    <button type="submit" class="btn btn-primary">Update Customer</button>
                </form>

            </div>
        </div>
    </div>

    <?= $this->endSection(); ?>
    ```
<br>


  + <b>index.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>

    <div class="container">


        <br>
        <div class="d-flex justify-content-center">
            <h1>Customer List</h1>
        </div>

        
        <div class="d-flex justify-content-between">
        <a class="btn btn-success" href="/customer/create">Add New Customer</a>
            <form action="/customer/find" method="post">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search by name" name="keyword">
                    <div class="input-group-append">
                        <button class="btn btn-info" type="submit">Search</button>
                        <a class="btn btn-info" href="/customer" role="button">Reset</a>
                    </div>
                </div>
            </form>
        </div>

        <?php if (session()->has('success')) : ?>
            <div class="alert alert-success"><?= session('success') ?></div>
        <?php endif; ?>

        <table class="table">
            <thead>
                <tr>
                    <th>No</th>
                    <th>Name</th>
                    <th>Phone Number</th>
                    <th>Email</th>
                    <th>Address</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($customers as $index => $customer) : ?>
                    <tr>
                        <td><?= $index + 1; ?></td>
                        <td><?= $customer['name']; ?></td>
                        <td><?= $customer['phone_number']; ?></td>
                        <td><?= $customer['email']; ?></td>
                        <td><?= $customer['address']; ?></td>
                        <td>
                            <a href="/customer/edit/<?= $customer['id']; ?>" class="btn btn-warning">Edit</a>
                            <a href="/customer/delete/<?= $customer['id']; ?>" class="btn btn-danger">Delete</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>

        </table>




    </div>
    <?= $this->endSection(); ?>
    ```
<br>


* Buat folder `app/Views/Layout` dan buat file ini:<p>

  + <b>footer.php</b>
    ```php
        <!-- Optional JavaScript; choose one of the two! -->

        <!-- Option 1: Bootstrap Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

        <!-- Option 2: Separate Popper and Bootstrap JS -->
        <!--
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
        -->
      </body>
    </html>
    ```
<br>


  + <b>navbar.php</b>
    ```php
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">

            <div class="container">
                <a class="navbar-brand" href="/">Dinka Dealer</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="/sales">Dashboard</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/sales-person">Sales Person</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/customer">Customer</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/car">Cars</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/transaction">Transaction</a>
                        </li>
                        
                    </ul>
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" href="/">Home Page</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="logout">Logout</a>
                        </li>
                    </ul>

                </div>
            </div>
            
    </nav>
    ```
<br>


  + <b>templete.php</b>
    ```php
    <!doctype html>
    <html lang="en">

    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

        <!-- My CSS -->
        <link rel="stylesheet" href="/style.css">

        <title> <?= $title; ?> </title>
    </head>

    <body>

        <?= $this->include('Layout/navbar') ?>

        <?= $this->renderSection('content') ?>

        <!-- Optional JavaScript; choose one of the two! -->

        <!-- Option 1: Bootstrap Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

        <!-- Option 2: Separate Popper and Bootstrap JS -->
        <!--
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
        -->
    </body>

    </html>
    ```
<br>


* Buat folder `app/Views/Pages` dan buat file ini:<p>

  + <b>about.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>

    <div class="container">
    <h1>Iman Setiawan</h1>
    <h5>Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci, libero. Officiis, impedit, vel commodi assumenda, magnam deserunt non veritatis sunt ducimus modi fugiat sapiente repellendus fugit? Odio facere atque quo.</h2>
    </div>

    <?= $this->endSection(); ?>
    ```
<br>


  + <b>contact.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>

    <?= $this->section('content'); ?>

    <div class="container">
        <div class="row">
            <div class="col">
                <h1>Contact Us</h1>
                <?php foreach ($alamat as $a) : ?>
                    <ul>
                        <li><?= $a['tipe']; ?></li>
                        <li><?= $a['alamat']; ?></li>
                        <li><?= $a['kota']; ?></li>
                    </ul>
                <?php endforeach; ?>
            </div>
        </div>
    </div>

    <?= $this->endSection(); ?>
    ```
<br>


  + <b>home.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>

    <div class="container">
    <h1>Dashbore</h1>


    <?= $this->endSection(); ?>
    ```
<br>


* Buat folder `app/Views/sales` dan buat file ini:<p>

  + <b>dashboard.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>
    <div class="container">

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <br>
        <div>
            <h1 class="row justify-content-center">Dashboard</h1>
        </div>
        <h4>Sales Graph</h4>
        <button class="btn btn-primary" onclick="showGraph(3)">Last 3 Days</button>
        <button class="btn btn-primary" onclick="showGraph(7)">Last 7 Days</button>
        <button class="btn btn-primary" onclick="showGraph(30)">Last 30 Days</button>
        <button class="btn btn-primary" onclick="showGraph(365)">Last 1 Year</button>

        <canvas id="chart"></canvas>


        <div class="container">
            <div class="row mt-4">
                <div class="col">
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>Duration</th>
                                <th>Total Sales</th>
                                <th>Profit Margin</th>
                                <th>Total Profit</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Last 3 Days</td>
                                <td id="totalSales3Days">-</td>
                                <td>15%</td>
                                <td id="totalProfit3Days">-</td>
                            </tr>
                            <tr>
                                <td>Last 7 Days</td>
                                <td id="totalSales7Days">-</td>
                                <td>15%</td>
                                <td id="totalProfit7Days">-</td>
                            </tr>
                            <tr>
                                <td>Last 30 Days</td>
                                <td id="totalSales30Days">-</td>
                                <td>15%</td>
                                <td id="totalProfit30Days">-</td>
                            </tr>
                        </tbody>
                    </table>

                </div>
            </div>
        </div>

        <script>
            // Retrieve the data passed from the controller
            var prices = <?php echo json_encode($prices); ?>;
            var dates = <?php echo json_encode($dates); ?>;

            // Format the dates without the time
            var formattedDates = dates.map(function(date) {
                var dateObj = new Date(date);
                return dateObj.toLocaleDateString(); // Format date to local string without time
            });

            // Format the value to Indonesian Rupiah currency format
            function formatCurrency(value) {
                return new Intl.NumberFormat('id-ID', {
                    style: 'currency',
                    currency: 'IDR'
                }).format(value);
            }

            // Calculate total sales for each duration
            function calculateTotalSales(prices) {
                var total = prices.reduce(function(sum, price) {
                    var priceValue = parseFloat(price.replace(/[^\d.-]/g, ''));
                    return sum + priceValue;
                }, 0);
                return total;
            }

            // Calculate total profit for each duration (15% of total sales)
            function calculateTotalProfit(totalSales) {
                var profit = (totalSales * 0.15).toFixed(0);
                return formatCurrency(profit);
            }

            // Calculate total sales for each duration
            var totalSales3Days = calculateTotalSales(prices.slice(-3));
            var totalSales7Days = calculateTotalSales(prices.slice(-7));
            var totalSales30Days = calculateTotalSales(prices.slice(-30));

            // Update the table with the formatted total sales values
            document.getElementById("totalSales3Days").textContent = formatCurrency(totalSales3Days);
            document.getElementById("totalSales7Days").textContent = formatCurrency(totalSales7Days);
            document.getElementById("totalSales30Days").textContent = formatCurrency(totalSales30Days);

            // Update the table with the calculated total profit values
            document.getElementById("totalProfit3Days").textContent = calculateTotalProfit(totalSales3Days);
            document.getElementById("totalProfit7Days").textContent = calculateTotalProfit(totalSales7Days);
            document.getElementById("totalProfit30Days").textContent = calculateTotalProfit(totalSales30Days);

            // Create a chart using Chart.js
            var ctx = document.getElementById('chart').getContext('2d');
            var chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: formattedDates, // Use the formatted dates without time
                    datasets: [{
                        label: 'Sales',
                        data: prices,
                        backgroundColor: 'rgba(0, 123, 255, 0.2)',
                        borderColor: 'rgba(0, 123, 255, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Sales Transaction',
                            position: 'top',
                            align: 'center',
                            font: {
                                size: 16
                            }
                        }
                    },
                    scales: {
                        x: {
                            display: true,
                            reverse: false, // Display latest day on the right side
                            title: {
                                display: true,
                                text: 'Date'
                            },
                            animation: {
                                from: "right" // Start the animation from the right
                            }
                        },
                        y: {
                            display: true,
                            title: {
                                display: true,
                                text: 'Sales'
                            }
                        }
                    },
                    tooltips: {
                        callbacks: {
                            label: function(context) {
                                var label = context.dataset.label || '';
                                var value = context.dataset.data[context.dataIndex];
                                return label + ': ' + formatCurrency(value);
                            }
                        }
                    }
                }
            });

            function showGraph(days) {
                // Update the chart data based on the selected number of days
                var filteredPrices = prices.slice(-days);
                var filteredDates = formattedDates.slice(-days);

                chart.data.labels = filteredDates;
                chart.data.datasets[0].data = filteredPrices;
                chart.update();

                // Update the table with total sales and total profit values
                var totalSales = calculateTotalSales(filteredPrices);
                var totalProfit = calculateTotalProfit(totalSales);

                if (days === 3) {
                    document.getElementById("totalSales3Days").textContent = formatCurrency(totalSales);
                    document.getElementById("totalProfit3Days").textContent = totalProfit;
                } else if (days === 7) {
                    document.getElementById("totalSales7Days").textContent = formatCurrency(totalSales);
                    document.getElementById("totalProfit7Days").textContent = totalProfit;
                } else if (days === 30) {
                    document.getElementById("totalSales30Days").textContent = formatCurrency(totalSales);
                    document.getElementById("totalProfit30Days").textContent = totalProfit;
                }
            }
        </script>

    </div>
    <?= $this->endSection(); ?>
    ```
<br>


* Buat folder `app/Views/sales-person` dan buat file ini:<p>

  + <b>create.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>
    <br>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1>Add New Sales Person</h1>

                <form method="post" action="/sales-person/store">


                    <div class="row mb-3">
                        <label for="name" class="col-sm-2 form-label">Name:</label>
                        <div class="col-sm-5">
                            <input type="text" name="name" id="name" class="form-control" required>
                        </div>
                    </div>


                    <div class="row mb-3">
                        <label for="phone_number" class="col-sm-2 form-label">Phone Number:</label>
                        <div class="col-sm-5">
                            <input type="text" name="phone_number" id="phone_number" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="email" class="col-sm-2 form-label">Email:</label>
                        <div class="col-sm-5">
                            <input type="email" name="email" id="email" class="form-control" required>
                        </div>
                    </div>

                    <button type="submit" class="btn btn-primary">Add Customer</button>
                </form>
            </div>
        </div>
    </div>


    <?= $this->endSection(); ?>
    ```
<br>


  + <b>edit.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>
    <br>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1>Edit Sales Person</h1>
                <form method="post" action="/sales-person/update/<?= $salesperson['id']; ?>">

                    
                    <div class="row mb-3">
                        <label for="name" class="form-label col-sm-2">Name:</label>
                        <div class="col-sm-5">
                        <input type="text" name="name" id="name" value="<?= $salesperson['name']; ?>" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="phone_number" class="form-label col-sm-2">Phone Number:</label>
                        <div class="col-sm-5">
                        <input type="text" name="phone_number" id="phone_number" value="<?= $salesperson['phone_number']; ?>" class="form-control" required>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <label for="email" class="form-label col-sm-2">Email:</label>
                        <div class="col-sm-5">
                        <input type="email" name="email" id="email" value="<?= $salesperson['email']; ?>" class="form-control" required>
                        </div>
                    </div>


                    <button type="submit" class="btn btn-primary">Update sales person</button>
                </form>

            </div>
        </div>
    </div>

    <?= $this->endSection(); ?>
    ```
<br>


  + <b>index.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>

    <div class="container">
        <br>
        <div class="d-flex justify-content-center">
            <h1>Sales Person List</h1>
        </div>


        <div class="d-flex justify-content-between">
            <a class="btn btn-success" href="/sales-person/create">Add New Sales Person</a>
            <form action="/sales-person/find" method="post">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search by name" name="keyword">
                    <div class="input-group-append">
                        <button class="btn btn-info" type="submit">Search</button>
                        <a class="btn btn-info ml-2" href="/sales-person" role="button">Reset</a>
                    </div>
                </div>
            </form>
        </div>

        <?php if (session()->has('success')) : ?>
            <div class="alert alert-success"><?= session('success') ?></div>
        <?php endif; ?>

        <table class="table">
            <thead>
                <tr>
                    <th>No</th>
                    <th>Name</th>
                    <th>Phone Number</th>
                    <th>Email</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($agents as $index => $customer) : ?>
                    <tr>
                        <td><?= $index + 1; ?></td>
                        <td><?= $customer['name']; ?></td>
                        <td><?= $customer['phone_number']; ?></td>
                        <td><?= $customer['email']; ?></td>
                        <td>
                            <a href="/sales-person/edit/<?= $customer['id']; ?>" class="btn btn-warning">Edit</a>
                            <a href="/sales-person/delete/<?= $customer['id']; ?>" class="btn btn-danger">Delete</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>

    <?= $this->endSection(); ?>
    ```
<br>


* Buat folder `app/Views/transaction` dan buat file ini:<p>

  + <b>create.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>
    <br>
    <div class="container">

        <!-- Display the create transaction form -->
        <h2>Create Transaction</h2>

        <?php if (session()->has('error')) : ?>
            <div class="alert alert-danger"><?= session('error') ?></div>
        <?php endif; ?>

        <form method="post" action="/transaction/store" class="my-4">


            <div class="row mb-3">
                <label for="customer_id" class="col-sm-2 form-label">Customer:</label>
                <div class="col-sm-5">
                    <select name="customer_id" id="customer_id" class="form-select" required>
                        <option value="" disabled selected>Select a customer</option> <!-- Placeholder option -->
                        <?php foreach ($customers as $customer) : ?>
                            <option value="<?= $customer['name'] ?>"><?= $customer['name'] ?></option>
                        <?php endforeach; ?>
                    </select>
                </div>
            </div>
            <div class="row mb-3">
                <label for="car_id" class="col-sm-2 form-label">Car:</label>
                <div class="col-sm-5">
                    <select name="car_id" id="car_id" class="form-select" required>
                        <option value="" disabled selected>Select a car</option> <!-- Placeholder option -->
                        <?php foreach ($cars as $car) : ?>
                            <option value="<?= $car['name'] ?>" data-price="<?= $car['price'] ?>"><?= $car['name'] ?></option>
                        <?php endforeach; ?>
                    </select>
                </div>
            </div>
            <div class="row mb-3">
                <label for="salesperson_id" class="col-sm-2 form-label">Salesperson:</label>
                <div class="col-sm-5">
                    <select name="salesperson_id" id="salesperson_id" class="form-select" required>
                        <option value="" disabled selected>Select a salesperson</option> <!-- Placeholder option -->
                        <?php foreach ($salespersons as $salesperson) : ?>
                            <option value="<?= $salesperson['name'] ?>"><?= $salesperson['name'] ?></option>
                        <?php endforeach; ?>
                    </select>
                </div>
            </div>
            <div class="row mb-3">
                <label for="price" class="col-sm-2 form-label">Price:</label>
                <div class="col-sm-5">
                    <input type="text" name="price" id="price" class="form-control" readonly>
                </div>
            </div>
            <div id="priceInIDR" class="row mb-3">
                <label for="priceIDR" class="col-sm-2 form-label"></label>
                <div class="col-sm-5">
                    <input type="text" id="priceIDR" class="form-control" readonly>
                </div>
            </div>
            <button type="submit" class="btn btn-primary">Create Transaction</button>
            <a class="btn btn-warning" href="/transaction">Back to Transaction List</a>


        </form>

        <script>
            // Get the customer selection element
            var customerSelect = document.getElementById('customer_id');

            // Get the car selection element
            var carSelect = document.getElementById('car_id');

            // Get the salesperson selection element
            var salespersonSelect = document.getElementById('salesperson_id');

            // Get the price input element
            var priceInput = document.getElementById('price');

            // Get the price in Indonesian currency element
            var priceIDRInput = document.getElementById('priceIDR');

            // Add event listener to the car selection
            carSelect.addEventListener('change', function() {
                // Get the selected car option
                var selectedCarOption = carSelect.options[carSelect.selectedIndex];

                // Get the price from the selected car option's data attribute
                var price = selectedCarOption.getAttribute('data-price');

                // Update the price input value
                priceInput.value = price;

                // Convert the price to Indonesian currency format
                var priceIDR = formatPriceToIDR(price);

                // Update the price in Indonesian currency input value
                priceIDRInput.value = priceIDR;
            });

            // Set the initial price based on the default selected car
            var defaultCarOption = carSelect.options[carSelect.selectedIndex];
            var defaultPrice = defaultCarOption.getAttribute('data-price');
            priceInput.value = defaultPrice;

            // Convert the price to Indonesian currency format
            var defaultPriceIDR = formatPriceToIDR(defaultPrice);

            // Set the initial price in Indonesian currency
            priceIDRInput.value = defaultPriceIDR;

            // Function to format price to Indonesian currency format
            function formatPriceToIDR(price) {
                var formatter = new Intl.NumberFormat('id-ID', {
                    style: 'currency',
                    currency: 'IDR',
                });
                return formatter.format(price);
            }
        </script>
    </div>

    <?= $this->endSection(); ?>
    ```
<br>


  + <b>edit.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>
    <br>
    <div class="container">

        <!-- Display the edit transaction form -->
        <h2>Edit Transaction</h2>
        <br>
        <?php if (session()->has('error')) : ?>
            <div class="alert alert-danger"><?= session('error') ?></div>
        <?php endif; ?>

        <form method="post" action="/transaction/update/<?= $transaction['id'] ?>">

            <div class="row mb-3">
                <label for="id" class="form-label col-sm-2">Transaction ID:</label>
                <div class="col-sm-5">
                    <input type="text" name="id" id="id" value="<?= $transaction['id'] ?>" readonly class="form-control">
                </div>
            </div>



            <div class="row mb-3">
                <label for="customer_id" class="form-label col-sm-2">Customer:</label>
                <div class="col-sm-5">
                    <select name="customer_id" id="customer_id" class="form-select">
                        <?php foreach ($customers as $customer) : ?>
                            <option value="<?= $customer['name'] ?>" <?= ($customer['id'] == $transaction['customer_id']) ? 'selected' : '' ?>>
                                <?= $customer['name'] ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>
            </div>
            <div class="row mb-3">
                <label for="car_id" class="form-label col-sm-2">Car:</label>
                <div class="col-sm-5">
                    <select name="car_id" id="car_id" class="form-select">
                        <?php foreach ($cars as $car) : ?>
                            <option value="<?= $car['name'] ?>" data-price="<?= $car['price'] ?>" <?= ($car['id'] == $transaction['car_id']) ? 'selected' : '' ?>>
                                <?= $car['name'] ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>
            </div>
            <div class="row mb-3">
                <label for="salesperson_id" class="form-label col-sm-2">Salesperson:</label>
                <div class="col-sm-5">
                    <select name="salesperson_id" id="salesperson_id" class="form-select">
                        <?php foreach ($salespersons as $salesperson) : ?>
                            <option value="<?= $salesperson['name'] ?>" <?= ($salesperson['id'] == $transaction['salesperson_id']) ? 'selected' : '' ?>>
                                <?= $salesperson['name'] ?>
                            </option>
                        <?php endforeach; ?>
                    </select>
                </div>
            </div>
            <div class="row mb-3">
                <label for="price" class="form-label col-sm-2">Price:</label>
                <div class="col-sm-5">
                    <input type="text" name="price" id="price" value="<?= $transaction['price'] ?>" readonly class="form-control">
                </div>
            </div>

            <button type="submit" class="btn btn-primary">Update Transaction</button>
            <a class="btn btn-warning" href="/transaction">Cancel</a>
        </form>

        <script>
            // Get the car select element
            const carSelect = document.getElementById('car_id');
            // Get the price input element
            const priceInput = document.getElementById('price');

            // Function to update the price based on the selected car
            function updatePrice() {
                // Get the selected car option
                const selectedCar = carSelect.options[carSelect.selectedIndex];
                // Get the price value from the selected car option's data attribute
                const carPrice = selectedCar.dataset.price;
                // Set the price input value to the selected car's price
                priceInput.value = carPrice;
            }

            // Add event listener to the car select element
            carSelect.addEventListener('change', updatePrice);

            // Call the updatePrice function initially to set the initial price
            updatePrice();
        </script>
        <br>

    </div>

    <?= $this->endSection(); ?>
    ```
<br>


  + <b>index.php</b>
    ```php
    <?= $this->extend('Layout/template'); ?>
    <?= $this->section('content'); ?>

    <div class="container">

        <br>
        <div class="d-flex justify-content-center">
            <h1>Transaction</h1>
        </div>

        <!-- Display the transaction list -->

        <div class="d-flex justify-content-between">
            <a class="btn btn-success" href="/transaction/create">Create New Transaction</a>
            <form action="/transaction/find" method="post">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search by name" name="keyword">
                    <div class="input-group-append">
                        <button class="btn btn-info" type="submit">Search</button>
                        <a class="btn btn-info" href="/transaction" role="button">Reset</a>
                    </div>
                </div>
            </form>
        </div>

        <?php if (session()->has('success')) : ?>
            <div class="alert alert-success"><?= session('success') ?></div>
        <?php endif; ?>

        <table class="table">
            <thead>
                <tr>
                    <th>No</th>
                    <th>ID</th>
                    <th>Customer</th>
                    <th>Car</th>
                    <th>Salesperson</th>
                    <th>Price</th>
                    <th>Created At</th>
                    <th>Updated At</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <?php
                $counter = 1;
                foreach ($transactions as $transaction) : ?>
                    <tr>
                        <td><?= $counter++ ?></td>
                        <td><?= $transaction['id'] ?></td>
                        <td><?= $transaction['customer_id'] ?></td>
                        <td><?= $transaction['car_id'] ?></td>
                        <td><?= $transaction['salesperson_id'] ?></td>
                        <td style="white-space: nowrap;">Rp <?= number_format($transaction['price'], 0, ',', '.'); ?></td>
                        <td style="white-space: nowrap;"><?= date('Y-m-d', strtotime($transaction['created_at'])) ?></td>
                        <td style="white-space: nowrap;"><?= date('Y-m-d', strtotime($transaction['updated_at'])) ?></td>
                        <td style="white-space: nowrap;">
                            <a href="/transaction/edit/<?= $transaction['id'] ?>" class="btn btn-warning">Edit</a>
                            <a href="/transaction/delete/<?= $transaction['id'] ?>" class="btn btn-danger">Delete</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>


    </div>
    <?= $this->endSection(); ?>
    ```
<br>


* Buat folder `app/Views/user` dan buat file ini:<p>

  + <b>home.php</b>
    ```php
    <?= $this->extend('user/template'); ?>
    <?= $this->section('content'); ?>


    <!-- Start slides -->
    <div id="slides" class="cover-slides">
        <ul class="slides-container">

            <?php foreach ($randomPictures as $picture) : ?>
                <li class="text-center">
                    <img src="car_img/<?= $picture['picture']; ?>" alt="">
                    <div class="container">
                        <div class="row">
                            <div class="col-md-12">
                                <h1 class="m-b-20"><strong>Dinka Dealer</strong></h1>
                                <p class="m-b-40">
                                    Temukan dealer mobil terbaik di kota Anda di Dealer Mobil Terpercaya. Kami menawarkan beragam pilihan mobil baru dan bekas dengan kualitas terbaik serta harga yang kompetitif. Dengan pengalaman puluhan tahun dalam industri otomotif, kami bangga menjadi mitra terpercaya bagi pelanggan kami.
                                </p>
                            </div>
                        </div>
                    </div>
                </li>
            <?php endforeach; ?>




        </ul>
        <div class="slides-navigation">
            <a href="#" class="next"> <i class="fa fa-angle-right" aria-hidden="true"></i></a>
            <a href="#" class="prev"> <i class="fa fa-angle-left" aria-hidden="true"></i></a>
        </div>
    </div>
    <!-- End slides -->

    <!-- Start About -->
    <div class="about-section-box">
        <div class="container">
            <div class="row">
                <div class="text-center">
                    <div class="inner-column">
                        <h1>Dinka Dealer</h1>
                        <br>
                        <h2>
                            Temukan dealer mobil terbaik di kota Anda di Dealer Mobil Terpercaya. Kami menawarkan beragam pilihan mobil baru dan bekas dengan kualitas terbaik serta harga yang kompetitif. Dengan pengalaman puluhan tahun dalam industri otomotif, kami bangga menjadi mitra terpercaya bagi pelanggan kami.
                        </h2>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
    <!-- End About -->

    <!-- Start Gallery -->
    <div class="gallery-box">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-12">
                    <div class="heading-title text-center">
                        <h2>Gallery</h2>
                        <p></p>
                    </div>
                </div>
            </div>
            <div class="tz-gallery">
                <div class="row">
                    <?php
                    $counter = 0;
                    foreach ($cars as $car) :
                        if ($counter >= 16) {
                            break; // exit the loop when 16 images are displayed
                        }
                    ?>
                        <div class="col-sm-5 col-md-3 col-lg-3">
                            <a class="lightbox" href="car_img/<?= $car['picture']; ?>">
                                <img class="img-fluid" src="car_img/<?= $car['picture']; ?>" alt="Gallery Images">
                            </a>
                        </div>
                    <?php
                        $counter++;
                    endforeach;
                    ?>
                </div>

            </div>
        </div>
        <!-- End Gallery -->
        <?= $this->endSection(); ?>
    ```
<br>


  + <b>navbar.php</b>
    ```php
    <header class="top-navbar">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="/">Dinka Dealer</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="/">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="/vehicle">Cars</a>
                        </li>

                    </ul>
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" href="/sales">Admin Page</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>
    ```
<br>


  + <b>template.php</b>
    ```php
    <!doctype html>
    <html lang="en">

    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Bootstrap CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <!-- Site CSS -->
        <link rel="stylesheet" href="css/style.css">
        <!-- Responsive CSS -->
        <link rel="stylesheet" href="css/responsive.css">
        <!-- Custom CSS -->
        <link rel="stylesheet" href="css/custom.css">

        <title> <?= $title; ?> </title>

    </head>

    <body>

        <?= $this->include('user/navbar') ?>

        <?= $this->renderSection('content') ?>


    <div class="sticky-bottom">
            <!-- Start Contact info -->
            <div class="contact-imfo-box">
                <div class="container">
                    <div class="row">
                        <div class="col-md-4">
                            <i class="fa fa-volume-control-phone"></i>
                            <div class="overflow-hidden">
                                <h4>Nomor Telepon</h4>
                                <p class="lead">
                                    021 544-112-441
                                </p>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <i class="fa fa-envelope"></i>
                            <div class="overflow-hidden">
                                <h4>Email</h4>
                                <p class="lead">
                                    sales@dealermakmur.com
                                </p>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <i class="fa fa-map-marker"></i>
                            <div class="overflow-hidden">
                                <h4>Lokasi</h4>
                                <p class="lead">
                                    Jawa Barat, Kab.Bekasi, Cikarang.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- End Contact info -->



            <!-- Start Footer -->
            <footer class="footer-area ">
                <div class="copyright">
                    <div class="container">
                        <div class="row">
                            <div class="col-lg-12">
                                <p class="company-name">Kelompok 2 - TI.21 &copy; 2023
                            </div>
                        </div>
                    </div>
                </div>
            </footer>
        </footer>
    </div>
        <!-- End Footer -->

        <!-- Optional JavaScript; choose one of the two! -->

        <!-- Option 1: Bootstrap Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
        <!-- Option 2: Separate Popper and Bootstrap JS -->
        <!--
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
        -->
        <!-- ALL JS FILES -->
        <script src="js/jquery-3.2.1.min.js"></script>
        <script src="js/popper.min.js"></script>
        <script src="js/bootstrap.min.js"></script>

        <!-- ALL PLUGINS -->
        <script src="js/jquery.superslides.min.js"></script>
        <script src="js/images-loded.min.js"></script>
        <script src="js/isotope.min.js"></script>
        <script src="js/baguetteBox.min.js"></script>
        <script src="js/form-validator.min.js"></script>
        <script src="js/contact-form-script.js"></script>
        <script src="js/custom.js"></script>
    </body>

    </html>
    ```
<br>

  + <b>vehicle.php</b>
    ```php
    <?= $this->extend('user/template'); ?>
    <?= $this->section('content'); ?>
    <br>
    <br>
    <br>
    <div class="container">
        <h1>Vehicle List</h1>
        <div class="row mb-5">
            <?php foreach ($cars as $cars) : ?>

                <div class="my-3 col-md-4">
                    <div class="card">
                        <img src="car_img/<?= $cars['picture']; ?>" class="card-img-top img-fluid"  alt="..." height="">
                        <div class="card-body">
                            <h9 class="card-title text-left"><?= $cars['type']; ?></h9>
                            <h2 class="card-title"><?= $cars['name']; ?></h2>
                            <p class="card-text"><?= $cars['description']; ?></p>
                            <a href="#" class="btn btn-sm btn-success">Rp. <?= $cars['price']; ?></a>
                        </div>
                    </div>
                </div>
            <?php endforeach; ?>
        </div>
    </div>

    <?= $this->endSection(); ?>
    ```
<br>

### Langkah 8: Routes
buka `app/Config/Routes.php` file dan tambahkan routes:<p>
  ```php
  $routes->get('/home', 'Pages::home');


  // User Routes
  $routes->get('/', 'UserPageController::index');
  $routes->get('/vehicle', 'UserPageController::vehicle');



  // Customer Routes
  $routes->get('/customer', 'CustomerController::index');
  $routes->get('/customer/create', 'CustomerController::create');
  $routes->post('/customer/store', 'CustomerController::store');
  $routes->get('/customer/edit/(:any)', 'CustomerController::edit/$1');
  $routes->post('/customer/update/(:any)', 'CustomerController::update/$1');
  $routes->get('/customer/delete/(:any)', 'CustomerController::delete/$1');
  $routes->post('/customer/find', 'CustomerController::find');


  // Cars Routes
  $routes->get('/car', 'CarsController::index');
  $routes->get('/car/create', 'CarsController::create');
  $routes->post('/car/store', 'CarsController::store');
  $routes->get('/car/edit/(:any)', 'CarsController::edit/$1');
  $routes->post('/car/update/(:any)', 'CarsController::update/$1');
  $routes->get('/car/delete/(:any)', 'CarsController::delete/$1');
  $routes->post('/car/find', 'CarsController::find');

  // Agent Routes
  $routes->get('/sales-person', 'SalesPersonController::index');
  $routes->get('/sales-person/create', 'SalesPersonController::create');
  $routes->post('/sales-person/store', 'SalesPersonController::store');
  $routes->get('/sales-person/edit/(:any)', 'SalesPersonController::edit/$1');
  $routes->post('/sales-person/update/(:any)', 'SalesPersonController::update/$1');
  $routes->get('/sales-person/delete/(:any)', 'SalesPersonController::delete/$1');
  $routes->get('/sales-person/search', 'SalesPersonController::search/$1');
  $routes->post('/sales-person/find', 'SalesPersonController::find');




  // Transaction Routes
  $routes->get('/transaction', 'TransactionController::index');
  $routes->get('/transaction/create', 'TransactionController::create');
  $routes->post('/transaction/store', 'TransactionController::store');
  $routes->get('/transaction/edit/(:any)', 'TransactionController::edit/$1');
  $routes->post('/transaction/update/(:any)', 'TransactionController::update/$1');
  $routes->get('/transaction/delete/(:any)', 'TransactionController::delete/$1');
  $routes->post('/transaction/find', 'TransactionController::find');

  // Sales Routes
  // $routes->get('/sales', 'TransactionController::index2');

  // Sales Routes
  $routes->get('/sales', 'DashboardController::index');

  ```

  <br>

  ### Membuat Menu LOGIN
  Untuk membuat menu Login Kita menggunkan library dari [myth-auth](https://github.com/lonnieezell/myth-auth) <p>

  * Langkah-Langkah
    + copy 
    ```php
      composer require myth/auth
    ```
    + Configuration
      1. Edit <b>app/Config/Validation.php</b><p>
      `use Myth\Auth\Authentication\Passwords\ValidationRules;`<p>
      2. untuk bagian ruleset<p>
      `ValidationRules::class,`<p>
      3. Setelah itu migrasikan database di terminal<p>
      ```php 
      php spark migrate -all
      ```
    + Restricting by Route
      kemudian edit dibagian `application/Config/Filters.php` dibagian `aliases`<p>
      ```php
        'login'      => \Myth\Auth\Filters\LoginFilter::class,
        'role'       => \Myth\Auth\Filters\RoleFilter::class,
        'permission' => \Myth\Auth\Filters\PermissionFilter::class,
      ```
      kita disini menggunkan fitur filters untuk melock login bagian admin saja
      ```php
        public filters = [
        'login' => ['before' => ['account/*']],
        ];
      ```
  
<br>

# TERIMAKASIH
Itu saja dari penjelasan kami. Untuk ke atas silahkan naik rocket ini:<P>
[![](asset/giphy.gif)](#daftar-isi)

