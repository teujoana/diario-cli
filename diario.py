# diario.py

import os
from datetime import datetime

DATA_FILE = "diario.txt"

def adicionar_entrada():
    print("\n🔹 Nova entrada no diário")
    texto = input("Escreva sua anotação: ")
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{data_hora}] {texto}\n")
    print("✅ Anotação salva!\n")

def listar_entradas():
    print("\n📚 Entradas no diário:")
    if not os.path.exists(DATA_FILE):
        print("Ainda não há entradas.")
        return
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        print(f.read())

def apagar_entradas():
    confirm = input("⚠️ Tem certeza que deseja apagar tudo? (s/n): ")
    if confirm.lower() == 's':
        open(DATA_FILE, "w").close()
        print("🗑️ Todas as entradas foram apagadas.\n")
    else:
        print("❌ Ação cancelada.\n")

def menu():
    while True:
        print("=== Diário de Bordo CLI ===")
        print("1. Adicionar entrada")
        print("2. Listar entradas")
        print("3. Apagar tudo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_entrada()
        elif opcao == "2":
            listar_entradas()
        elif opcao == "3":
            apagar_entradas()
        elif opcao == "4":
            print("Até mais! 💚")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()
