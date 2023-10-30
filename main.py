def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
 
#---------------------------------------------------------------------------

#Testes do Professor

# Teste para número de dois dígitos
def test_digital_root():
    assert digital_root(16) == 7
 
# Teste para número de três dígitos
def test_digital_root_three_digits():
    assert digital_root(942) == 6
 
# Teste para número de seis dígitos
def test_digital_root_six_digits():
    assert digital_root(132189) == 6
 
# Teste para número de seis dígitos
def test_digital_root_large_number():
    assert digital_root(493193) == 2
 
# Teste para número de um dígito
def test_digital_root_single_digit():
    assert digital_root(5) == 5
    
#Testes Criados

# Teste para número de dois dígitos
def test_digital_root_created():
    assert digital_root(24) == 6

# Teste para número de três dígitos
def test_digital_root_three_digits_created():
    assert digital_root(357) == 6 

# Teste para número de seis dígitos
def test_digital_root_six_digits_created():
    assert digital_root(987654) == 3  

# Teste para número de nove dígitos
def test_digital_root_large_number_created():
    assert digital_root(123456789) == 9  

# Teste para número de um dígito
def test_digital_root_single_digit_created():
    assert digital_root(8) == 8 
 
# Executando os testes
if __name__ == "__main__":
    test_digital_root()
    test_digital_root_three_digits()
    print("3 Digitos Passou!")
    test_digital_root_six_digits()
    print("6 Digitos Passou!")
    test_digital_root_large_number()
    print("Varios Digitos Passou!")
    test_digital_root_single_digit()
    print("Digito Unico Passou!")
    print("Todos os testes do professor passaram!")
    print("-------------------------------------------")
    test_digital_root_created()
    print("2 Digitos Criado Passou!")
    test_digital_root_three_digits_created()
    print("3 Digitos Criado Passou!")
    test_digital_root_six_digits_created()
    print("6 Digitos Criado Passou!")
    test_digital_root_large_number_created()
    print("Varios Digitos Criado Passou!")
    test_digital_root_single_digit_created()
    print("Digito Unico Criado Passou!")
    print("Todos os testes criados passaram!")
    

    