from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Path ke WebDriver Chrome
chromedriver_path = "C:/Users/ahmad/Downloads/Compressed/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Mengatur opsi untuk Chrome
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Memulai WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

print('')
print('Pengujian Login Form - Aplikasi POS Kasir')
print('')
# URL halaman login
url = 'http://localhost/pos-kasir-php-master/login.php'
driver.get(url)

# Tunggu beberapa saat untuk memastikan halaman sudah dimuat
time.sleep(2)


def find_elements():
    """Mencari elemen input user, pass, dan tombol login."""
    username_input = driver.find_element(By.NAME, "user")
    password_input = driver.find_element(By.NAME, "pass")
    login_button = driver.find_element(By.NAME, "proses")
    return username_input, password_input, login_button


def handle_alert():
    """Memeriksa apakah alert muncul, dan mengembalikan teksnya."""
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()  # Menutup alert
        print(f"Alert detected: {alert_text}")
        return alert_text
    except NoAlertPresentException:
        return None


def verify_login(expected_result):
    """Memverifikasi hasil login berdasarkan ekspektasi."""
    alert_text = handle_alert()
    if expected_result == "gagal":
        if alert_text and "Login Gagal" in alert_text:
            return "Berhasil - Login gagal sesuai ekspektasi"
        else:
            return "Gagal - Login berhasil padahal seharusnya gagal"
    elif expected_result == "berhasil":
        if "index.php" in driver.current_url:  # Memeriksa apakah URL berubah ke halaman dashboard
            return "Berhasil - Login berhasil sesuai ekspektasi"
        else:
            return "Gagal - Login gagal padahal seharusnya berhasil"


# Skenario 1: Login
print('Skenario 1: Login')
username_input, password_input, login_button = find_elements()
username_input.clear()
password_input.clear()
username_input.send_keys("admin")  # Username benar
time.sleep(2)
password_input.send_keys("123")  # Password benar
login_button.click()
time.sleep(2)
print(f"{verify_login('berhasil')}")

time.sleep(5)

print('')

# Skenario 2: Masuk ke halaman Barang setelah login berhasil
print('Skenario 2: Masuk ke halaman Barang')
time.sleep(2)

data_master_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Data Master']]"))
)
data_master_button.click()
time.sleep(1)

# Klik submenu "Barang"
barang_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?page=barang']"))
)
barang_link.click()
time.sleep(3)

# Verifikasi apakah halaman Barang dimuat dengan benar
if "index.php?page=barang" in driver.current_url:
    print("Berhasil - Berhasil memasuki halaman Barang")
else:
    print("Gagal - Gagal memasuki halaman Barang")

print('')
print("Mulai Pengujian Pada Halaman Barang")
print('-'*255)
print('')

print('Skenario 3: Tambah Barang')

# Tunggu sampai tombol "Insert Data" muncul dan klik
insert_data_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@data-target='#myModal']"))
)
insert_data_button.click()

# Verifikasi apakah modal tambah barang muncul
try:
    tambah_barang_modal = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "myModal"))  # Ganti dengan ID modal jika berbeda
    )
    print("Berhasil - Form muncul setelah klik tombol 'Insert Data'")
except Exception as e:
    print(f"Gagal - Form tambah barang tidak muncul: {e}")
    driver.quit()  # Keluar jika modal tidak muncul
time.sleep(3)
# Isi form tambah barang
form_fields = {
    "kategori": "1",  # Pilih kategori (sesuaikan dengan nilai yang ada di database)
    "nama": "Barang Contoh",  # Nama Barang
    "merk": "Merk ABC",  # Merk Barang
    "beli": "10000",  # Harga Beli
    "jual": "15000",  # Harga Jual
    "satuan": "PCS",
    "stok": "20",  # Stok
}
time.sleep(3)
for field_name, field_value in form_fields.items():
    try:
        input_element = driver.find_element(By.NAME, field_name)
        if input_element.tag_name == "select":  # Jika elemen adalah dropdown
            from selenium.webdriver.support.ui import Select
            select = Select(input_element)
            select.select_by_value(field_value)
        else:  # Jika elemen adalah input teks
            input_element.clear()
            input_element.send_keys(field_value)
    except Exception as e:
        print(f"Field {field_name} tidak ditemukan: {e}")

# Klik tombol "Insert Data" untuk menyimpan data
submit_button = driver.find_element(By.ID, "tambah_barang")
submit_button.click()

# Tunggu beberapa saat untuk melihat hasil
time.sleep(3)

# Verifikasi apakah ada alert sukses
success_message = None
try:
    success_alert = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert-success')]/p"))
    )
    success_message = success_alert.text
except Exception:
    pass

if success_message and "Tambah Data Berhasil" in success_message:
    print("Berhasil - Barang berhasil ditambahkan")
else:
    print("Gagal - Barang tidak berhasil ditambahkan")
time.sleep(2)
print('')

# Skenario 4: Klik Sortir Barang Kurang
print("Skenario 4: Klik Sortir Barang Kurang")

# Tunggu tombol Sortir Stok Kurang muncul
sortir_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'index.php?page=barang&stok=yes')]"))
)

# Klik tombol Sortir Stok Kurang
sortir_button.click()
time.sleep(5)

# Verifikasi bahwa halaman berhasil menampilkan barang dengan stok kurang
if "stok=yes" in driver.current_url:
    print("Berhasil - Halaman Sortir Barang Kurang ditampilkan.")
else:
    print("Gagal - Halaman Sortir Barang Kurang tidak ditampilkan.")

print('')

# Skenario 5: Klik Tombol Refresh
print("Skenario 5: Klik Tombol Refresh")

# Tunggu tombol Refresh Data terlihat
refresh_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'index.php?page=barang') and @class='btn btn-success btn-md']"))
)

# Klik tombol Refresh Data
refresh_button.click()

WebDriverWait(driver, 10).until(
    EC.url_contains("index.php?page=barang")
)
time.sleep(3)

if "index.php?page=barang" in driver.current_url:
    print("Berhasil - Halaman berhasil direfresh.")
else:
    print("Gagal - Halaman tidak sesuai setelah refresh.")

print('')

# Fungsi Pencarian
print("Skenario 6: Fungsi Pencarian")
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
)

# Masukkan kata kunci "pulpen" ke dalam kolom search
search_input.clear()
search_input.send_keys("pulpen")
search_input.send_keys(Keys.RETURN)
time.sleep(3)
# Tunggu hasil pencarian muncul
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//table[@id='example1']//tbody/tr"))
)

# Ambil semua baris hasil pencarian
search_results = driver.find_elements(By.XPATH, "//table[@id='example1']//tbody/tr")

# Verifikasi apakah hasil pencarian relevan
for result in search_results:
    if "pulpen" not in result.text.lower():
        print("Error: Hasil pencarian tidak sesuai!")
        break
else:
    print("Berhasil - Semua hasil pencarian sesuai dengan kata kunci 'pulpen'.")

time.sleep(5)
print('')

# Skenario 7: Edit Data Barang
print("Skenario 7: Edit Data Barang")
# 1. Klik tombol Edit pada baris teratas
edit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "(//button[contains(text(), 'Edit')])[1]")  # Tombol Edit di baris pertama
    )
)
edit_button.click()

# Verifikasi URL setelah klik Edit
WebDriverWait(driver, 10).until(
    EC.url_contains("index.php?page=barang/edit&barang=")
)
current_url = driver.current_url
if "index.php?page=barang/edit&barang=" in current_url:
    print("Berhasil - Navigasi ke halaman edit.")
else:
    print("Gagal - Navigasi ke halaman edit.")
time.sleep(3)

# 2. Klik tombol Update Data
update_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Update Data')]"))
)
update_button.click()

# Verifikasi URL setelah klik Update Data
WebDriverWait(driver, 10).until(
    EC.url_contains("&success=edit-data")
)
if "&success=edit-data" in driver.current_url:
    print("Berhasil - Navigasi ke halaman sukses edit.")
else:
    print("Gagal - Navigasi ke halaman sukses edit.")
time.sleep(3)

# 3. Klik tombol Balik
balik_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'index.php?page=barang') and contains(text(), 'Balik')]"))
)
balik_button.click()

# Verifikasi URL setelah klik Balik
WebDriverWait(driver, 10).until(
    EC.url_to_be("http://localhost/pos-kasir-php-master/index.php?page=barang")
)
if driver.current_url == "http://localhost/pos-kasir-php-master/index.php?page=barang":
    print("Berhasil - Navigasi kembali ke halaman barang.")
else:
    print("Gagal - Navigasi kembali ke halaman barang.")
time.sleep(5)

print('')

# Skenario 8: Hapus Barang
print("Skenario 8: Hapus Barang")
delete_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@href, 'hapus.php?barang=hapus&id=')]/button[contains(text(), 'Hapus')]")
    )
)
delete_button.click()
time.sleep(2)
# 3. Verifikasi munculnya alert konfirmasi
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert

# Pastikan teks pada alert sesuai
if "Hapus Data barang ?" in alert.text:
    print("Berhasil - Konfirmasi hapus muncul.")
    alert.accept()  # Klik "OK" pada alert
else:
    print("Gagal - Konfirmasi hapus tidak sesuai.")
    alert.dismiss()  # Klik "Cancel" jika teks tidak sesuai
time.sleep(3)
success_alert = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'alert alert-danger')]//p[contains(text(), 'Hapus Data Berhasil !')]"))
)
if success_alert.is_displayed():
    print("Berhasil - Pesan konfirmasi penghapusan muncul, barang terhapus.")
else:
    print("Gagal - Pesan konfirmasi penghapusan tidak muncul.")
time.sleep(5)
print('')

# Skenario 9: Details Barang
print("Skenario 9: Details Barang")
details_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@href, 'index.php?page=barang/details&barang=')]/button[contains(text(), 'Details')]")
    )
)
details_button.click()

barang_id = driver.current_url.split("barang=")[-1]

WebDriverWait(driver, 10).until(
    EC.url_contains(f"index.php?page=barang/details&barang={barang_id}")
)

if driver.current_url == f"http://localhost/pos-kasir-php-master/index.php?page=barang/details&barang={barang_id}":
    print(f"Berhasil - Masuk ke halaman details untuk barang ID {barang_id}.")
else:
    print("Gagal - Navigasi ke halaman details.")
time.sleep(3)
balik_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'index.php?page=barang') and contains(text(), 'Balik')]"))
)
balik_button.click()
time.sleep(5)

print('')

# Skenario 10: Pagination
print("Skenario 10: Pagination")
# Daftar halaman yang ada di sidebar untuk diuji
# 1. Tunggu sampai elemen "Dashboard" muncul dan klik
dashboard_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Dashboard']]"))
)
dashboard_button.click()
time.sleep(1)

# Verifikasi bahwa halaman yang dimuat adalah halaman Dashboard
if driver.current_url == "http://localhost/pos-kasir-php-master/index.php":
    print("Halaman Dashboard berhasil dimuat.")
else:
    print("Halaman Dashboard gagal dimuat.")
time.sleep(3)

# 2. Tunggu sampai elemen "Data Master" muncul dan klik
data_master_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Data Master']]"))
)
data_master_button.click()
time.sleep(1)

# 3. Klik submenu "Barang"
barang_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?page=barang']"))
)
barang_link.click()

# Verifikasi URL halaman Barang
if driver.current_url == "http://localhost/pos-kasir-php-master/index.php?page=barang":
    print("Halaman Barang berhasil dimuat.")
else:
    print("Halaman Barang gagal dimuat.")
time.sleep(3)

data_master_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Data Master']]"))
)
data_master_button.click()
time.sleep(1)

# 4. Klik submenu "Kategori"
kategori_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?page=kategori']"))
)
kategori_link.click()

# Verifikasi URL halaman Kategori
if driver.current_url == "http://localhost/pos-kasir-php-master/index.php?page=kategori":
    print("Halaman Kategori berhasil dimuat.")
else:
    print("Halaman Kategori gagal dimuat.")
time.sleep(3)

# 5. Tunggu sampai elemen "Transaksi" muncul dan klik
transaksi_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Transaksi']]"))
)
transaksi_button.click()
time.sleep(1)

# 6. Klik submenu "Transaksi Jual"
transaksi_jual_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?page=jual']"))
)
transaksi_jual_link.click()

# Verifikasi URL halaman Transaksi Jual
if driver.current_url == "http://localhost/pos-kasir-php-master/index.php?page=jual":
    print("Halaman Transaksi Jual berhasil dimuat.")
else:
    print("Halaman Transaksi Jual gagal dimuat.")
time.sleep(3)

transaksi_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Transaksi']]"))
)
transaksi_button.click()
time.sleep(1)

# 7. Klik submenu "Laporan Penjualan"
laporan_penjualan_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?page=laporan']"))
)
laporan_penjualan_link.click()

# Verifikasi URL halaman Laporan Penjualan
if driver.current_url == "http://localhost/pos-kasir-php-master/index.php?page=laporan":
    print("Halaman Laporan Penjualan berhasil dimuat.")
else:
    print("Halaman Laporan Penjualan gagal dimuat.")
time.sleep(3)

# 8. Tunggu sampai elemen "Pengaturan Toko" muncul dan klik
pengaturan_toko_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Pengaturan Toko']]"))
)
pengaturan_toko_button.click()
time.sleep(1)

# Verifikasi URL halaman Pengaturan Toko
if driver.current_url == "http://localhost/pos-kasir-php-master/index.php?page=pengaturan":
    print("Halaman Pengaturan Toko berhasil dimuat.")
else:
    print("Halaman Pengaturan Toko gagal dimuat.")
time.sleep(3)

# Kembali kehalaman Barang
data_master_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[span[text()='Data Master']]"))
)
data_master_button.click()
time.sleep(1)

# 3. Klik submenu "Barang"
barang_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='index.php?page=barang']"))
)
barang_link.click()

print('')

# Skenario 11: Dropdown Jumlah Baris
print("Skenario 11: Dropdown Jumlah Baris")
# Tunggu sampai dropdown "Show entries" muncul
dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "example1_length"))
)
select = Select(dropdown)

# Dapatkan semua opsi dari dropdown
options = [option.text for option in select.options]

for value in options:
    # Pilih setiap opsi berdasarkan nilai
    print(f"  Mengubah dropdown menjadi: {value} entries")
    select.select_by_visible_text(value)
    time.sleep(2)  # Tunggu perubahan diterapkan

    # Verifikasi jumlah data yang ditampilkan
    rows = driver.find_elements(By.XPATH, "//table[@id='example1']/tbody/tr")
    print(f"  Jumlah baris yang ditampilkan: {len(rows)}")

    # Tambahkan log verifikasi
    if len(rows) <= int(value):
        print(f"  Dropdown '{value}' entries berfungsi dengan benar.\n")
    else:
        print(f"  Dropdown '{value}' entries tidak sesuai!\n")

time.sleep(5)
# Tutup browser
driver.quit()