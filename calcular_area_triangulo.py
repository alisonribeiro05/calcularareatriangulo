import math
def calcular_area_triangulo(a, b, c):

    p = (a + b + c) / 2

    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area
def verificar_e_calcular_triangulo():

    print("--- Verificador de Triângulo e Calculador de Área ---")

    try:
        a = int(input("Digite o valor do lado A (inteiro e positivo): "))
        b = int(input("Digite o valor do lado B (inteiro e positivo): "))
        c = int(input("Digite o valor do lado C (inteiro e positivo): "))
    except ValueError:
        print("\nERRO: Certifique-se de digitar apenas números inteiros.")
        return
    if a <= 0 or b <= 0 or c <= 0:
        print("\nERRO: Todos os valores devem ser inteiros e positivos.")
        return
    condicao_a = (a < b + c)  # Lado A deve ser menor que a soma de B e C
    condicao_b = (b < a + c)  # Lado B deve ser menor que a soma de A e C
    condicao_c = (c < a + b)  # Lado C deve ser menor que a soma de A e B

    if condicao_a and condicao_b and condicao_c:
        area = calcular_area_triangulo(a, b, c)
        print(f"Os valores {a}, {b} e {c} **FORMAM UM TRIÂNGULO**.")
        print(f"   A área deste triângulo é: **{area:.2f}** (aproximadamente)")
    else:
        # 4. SAÍDA SE NÃO FOR TRIÂNGULO

        print(f" Os valores {a}, {b} e {c} **NÃO FORMAM UM TRIÂNGULO**.")
        # É solicitado escrever os valores lidos neste caso
        print(f"   Valores lidos: A={a}, B={b}, C={c}.")
if __name__ == "__main__":
    verificar_e_calcular_triangulo()
