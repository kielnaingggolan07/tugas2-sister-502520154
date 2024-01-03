import zmq
import time

context = zmq.Context()
client = context.socket(zmq.REQ)

# Menghubungkan ke server dengan pola Simple Pirate (load balancing)
client.connect("tcp://localhost:5555")  # Ganti alamat dan port sesuai server Anda

for i in range(5):
    try:
        # Kirim pesan ke server
        request = b"Hello from client"
        client.send(request)

        # Terima dan cetak balasan dari server
        reply = client.recv()
        print(f"Client menerima: {reply.decode()}")

        # Tambahkan sedikit jeda sebelum mengirim pesan berikutnya
        time.sleep(1)
    except KeyboardInterrupt:
        break

# Tutup koneksi ke server dan context ZeroMQ
client.close()
context.term()
