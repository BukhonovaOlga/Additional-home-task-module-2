number = input("Введите число: ")

def find_divisors(number_):
    divisors_list = []
    for i in range(3, int(number_/2) + 1):
        if number_ % i == 0:
            divisors_list.append(i)
    divisors_list.append(number_)
    print(f'Делители числа {number_}: {divisors_list}.')
    return divisors_list

def find_pairs_for_divisor(divisor_):
    pairs_list = ""
    for i in range(1,  int(divisor_/2) + 1):
        if i != divisor_ - i:
            pairs_list += str(i)
            pairs_list += str(divisor_ - i)
    print(f'Пары для делителя {divisor_}: {pairs_list}.')
    return pairs_list

def find_pairs_for_number(number_):
    divisors_list = find_divisors(number_)
    pairs_list = ""
    for i in range(len(divisors_list)):
        pairs_list += find_pairs_for_divisor(divisors_list[i])
    return pairs_list

pairs_for_number_list = find_pairs_for_number(int(number))
print(f'Пары для числа {number}: {pairs_for_number_list}.')