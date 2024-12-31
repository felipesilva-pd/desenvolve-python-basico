def validar_cpf(cpf):
    """Valida um CPF fornecido no formato XXX.XXX.XXX-XX."""
    
    # Remove caracteres especiais e converte para uma lista de dígitos
    digitos = [int(d) for d in cpf if d.isdigit()]

    # Verifica se o CPF tem 11 dígitos
    if len(digitos) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum([(i + 2) * d for i, d in enumerate(reversed(digitos[:-2]))])
    resto = soma % 11
    digito1 = 11 - resto if resto > 1 else 0

    # Calcula o segundo dígito verificador
    soma = sum([(i + 2) * d for i, d in enumerate(reversed(digitos[:-1]))])
    resto = soma % 11
    digito2 = 11 - resto if resto > 1 else 0

    # Compara os dígitos verificadores calculados com os fornecidos
    return digito1 == digitos[-2] and digito2 == digitos[-1]

# Exemplo de uso:
cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
if validar_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")