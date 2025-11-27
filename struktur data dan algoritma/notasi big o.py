import time

def factorial(n):
    if n < 0:
        return "Faktorial tidak didefinisikan untuk angka negatif"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def simple_benchmark_factorial(factorial_fn, targets):
    # Ukur waktu rata-rata menghitung faktorial untuk setiap target (satu kali panggil per target)
    total = 0.0
    for t in targets:
        start = time.perf_counter()
        factorial_fn(t)
        total += time.perf_counter() - start
    return total / len(targets)

# Bagian utama program
if __name__ == "__main__":
    # Contoh penggunaan kalkulator
    try:
        num = int(input("Masukkan angka positif untuk menghitung faktorial: "))
        print(f"Faktorial dari {num} adalah: {factorial(num)}")
    except ValueError:
        print("Input harus berupa angka bulat positif.")
    
    # Benchmark empiris
    print("\n--- Benchmark Empiris ---")
    targets = [5, 10, 50, 100, 500]  # Nilai n yang berbeda untuk diukur (sesuaikan jika perlu)
    avg_time = simple_benchmark_factorial(factorial, targets)
    print(f"Targets yang diukur: {targets}")
    print(f"Waktu rata-rata per faktorial: {avg_time:.6f} detik")
    print("Catatan: Waktu meningkat linear dengan n (sesuai O(n)), tapi untuk n kecil mungkin terlihat konstan karena overhead Python.")
