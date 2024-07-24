import machine
import time
import dht

# Inisialisasi pin untuk sensor DHT22
dht_pin = machine.Pin(5)  # Ganti dengan pin yang sesuai
sensor = dht.DHT22(dht_pin)

while True:
    try:
        sensor.measure()
        suhu = sensor.temperature()
        kelembapan = sensor.humidity()
        print('Suhu: {:.2f}°C'.format(suhu))
        print('Kelembapan: {:.2f}%'.format(kelembapan))
    except OSError as e:
        print('Gagal membaca sensor.')

    time.sleep(2)  # Delay sebelum membaca data lagi

