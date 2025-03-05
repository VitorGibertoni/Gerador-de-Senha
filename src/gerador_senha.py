import random
import string
import pyperclip

# Função para gerar uma senha aleatória
def generate_password(length=12, uppercase=True, numbers=True, symbols=True):
    # Inicializa a lista de caracteres com as letras minúsculas
    characters = string.ascii_lowercase
    
    # Adiciona letras maiúsculas, se solicitado
    if uppercase:
        characters += string.ascii_uppercase
    # Adiciona números, se solicitado
    if numbers:
        characters += string.digits
    # Adiciona símbolos, se solicitado
    if symbols:
        characters += string.punctuation
    
    # Gera a senha aleatória com o comprimento especificado
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Solicita ao usuário o comprimento da senha
    length = int(input("Digite o comprimento da senha (12 caracteres recomendado): "))
    # Pergunta ao usuário se deseja incluir letras maiúsculas
    include_uppercase = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    # Pergunta ao usuário se deseja incluir números
    include_numbers = input("Incluir números? (s/n): ").lower() == 's'
    # Pergunta ao usuário se deseja incluir símbolos
    include_symbols = input("Incluir símbolos? (s/n): ").lower() == 's'
    
    # Gera a senha com as preferências do usuário
    generated_password = generate_password(length, include_uppercase, include_numbers, include_symbols)
    # Exibe a senha gerada
    print(f"Sua senha gerada é: {generated_password}")

    # Pergunta ao usuário se deseja copiar a senha para a área de transferência
    copy = input("Deseja copiar a senha para a área de transferência? (s/n): ").lower()
    if copy == 's':
        # Copia a senha para a área de transferência
        pyperclip.copy(generated_password)
        print("⚡ Senha copiada para a área de transferência! Use Ctrl+V para colar.")
    else:
        # Finaliza o programa caso o usuário não queira copiar a senha
        print("Programa Finalizado")
