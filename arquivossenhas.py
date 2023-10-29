import os
import json
from cryptography.fernet import Fernet

def carregar_arquivo_senhas(arquivo_senhas, chave):
    if os.path.exists(arquivo_senhas):
        with open(arquivo_senhas, 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = Fernet(chave).decrypt(encrypted_data)
            return json.loads(decrypted_data)
    else:
        return {}


def salvar_arquivo_senhas(arquivo_senhas, senhas, chave):
    data = json.dumps(senhas)
    encrypted_data = Fernet(chave).encrypt(data.encode())
    with open(arquivo_senhas, 'wb') as file:
        file.write(encrypted_data)


def main():
    arquivo_senhas = "senhas.dat"
    chave = Fernet.generate_key()
    senhas = carregar_arquivo_senhas(arquivo_senhas, chave)

    while True:
        print("Gerenciador de Senhas")
        print("1. Adicionar senha")
        print("2. Recuperar senha")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_conta = input("Nome da conta: ")
            senha_conta = input("Senha: ")
            senhas[nome_conta] = senha_conta
            salvar_arquivo_senhas(arquivo_senhas, senhas, chave)
            print(f"Senha para {nome_conta} adicionada com sucesso!")
        elif escolha == "2":
            nome_conta = input("Nome da conta: ")
            if nome_conta in senhas:
                print(f"Senha para {nome_conta}: {senhas[nome_conta]}")
            else:
                print(f"Senha para {nome_conta} não encontrada.")
        elif escolha == "3":
            break
        else:
            print("Escolha uma opção válida.")

if __name__ == "__main__":
    main()
