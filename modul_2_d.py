# Слишком древний шифр
# n = [3:20] = result and n%(i+j)==0


def generate_password(n):
    if n < 3 or n > 20:
        return "Число должно быть в диапазоне от 3 до 20."
    password = ""
    pas_list = []
    for i in range(1, n):
        for j in range(i + 1, n):
            pas_list_sum = i + j
            if n % pas_list_sum == 0:
                pas_list.append((i, j))
    for i, j in pas_list:
        password += str(i) + str(j)
    return password

n = int(input("Введите число от 3 до 20: "))
result = generate_password(n)
print("Нужный пароль:", result)
