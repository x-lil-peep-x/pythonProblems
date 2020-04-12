# SUmar digitos de una sequencia de numeros IZI

while True:
    try:
        n = int(input())
        sequence_sum = (n - 1) * ((1 + (n - 1)) / 2)
        sequence_sum *= 2
        while n > 1:
            sequence_sum += n % 10
            n /= 10

        print(int(sequence_sum))
    except:
        break
