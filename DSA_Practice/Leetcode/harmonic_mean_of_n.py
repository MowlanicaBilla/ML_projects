def harmonic_mean_of_n(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_mean_of_n(n - 1))

print(harmonic_mean_of_n(2))

print(harmonic_mean_of_n(4))