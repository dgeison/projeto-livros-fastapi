import requests
import json

API_URL = "http://127.0.0.1:8000"


def tratar_resposta(resp: requests.Response):
    """Imprimir de forma amigável resposta da API."""
    try:
        data = resp.json()
    except ValueError:
        print(f"\nStatus: {resp.status_code}")
        print("Resposta sem JSON.")
        print(resp.text)
        return

    if resp.status_code >= 400:
        print(f"\n❌ Erro ({resp.status_code})")
    else:
        print(f"✅")
    print(json.dumps(data, indent=4, ensure_ascii=False))


def listar_livros():
    resp = requests.get(f"{API_URL}/livros")
    print("\n📚 Listar Livros:")
    tratar_resposta(resp)


def obter_livro():
    livro_uuid = input("🔍 UUID do livro: ").strip()
    resp = requests.get(f"{API_URL}/livros/{livro_uuid}")
    print("\n📖 Detalhes do Livro:")
    tratar_resposta(resp)


def adicionar_livro():
    print("\n✏️ Digite os dados do novo livro:")
    autor = input("👤 Autor: ")
    titulo = input("📕 Título: ")
    editora = input("🏢 Editora: ")
    ano = input("📅 Ano de publicação: ")

    payload = {
        "autor": autor,
        "titulo": titulo,
        "editora": editora,
        "ano": ano,
    }
    resp = requests.post(f"{API_URL}/livros", json=payload)
    print("\n➕ Livro adicionado:")
    tratar_resposta(resp)


def atualizar_livro():
    livro_uuid = input("🔍 UUID do livro a atualizar: ").strip()
    print("\n✏️ Digite os novos dados do livro:")
    autor = input("👤 Autor: ")
    titulo = input("📕 Título: ")
    editora = input("🏢 Editora: ")
    ano = input("📅 Ano de publicação: ")

    payload = {
        "autor": autor,
        "titulo": titulo,
        "editora": editora,
        "ano": ano,
    }
    resp = requests.put(f"{API_URL}/livros/{livro_uuid}", json=payload)
    print("\n🔄 Livro atualizado:")
    tratar_resposta(resp)


def atualizar_parcial():
    livro_uuid = input("🔍 UUID do livro a atualizar parcialmente: ").strip()
    print("\n✏️ Digite os dados a atualizar do livro:")
    autor = input("👤 Autor: ")
    titulo = input("📕 Título: ")
    editora = input("🏢 Editora: ")
    ano = input("📅 Ano de publicação: ")

    payload = {}

    if autor:
        payload["autor"] = autor
    if titulo:
        payload["titulo"] = titulo
    if editora:
        payload["editora"] = editora
    if ano:
        payload["ano"] = int(ano)

    resp = requests.patch(f"{API_URL}/livros/{livro_uuid}", json=payload)
    print("\n🔄 Livro atualizado com as novas informações:")
    tratar_resposta(resp)


def menu():
    while True:
        print("\n📚 === CLIENTE API DE LIVROS === 📚")
        print("1️⃣  Listar Livros")
        print("2️⃣  Obter livro por UUID")
        print("3️⃣  Adicionar livro")
        print("4️⃣  Atualizar livro")
        print("5️⃣  Atualizar novos dados do livro")
        print("0️⃣  Sair")

        opcao = input("\n🎯 Escolha a opção: ").strip()

        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            obter_livro()
        elif opcao == "3":
            adicionar_livro()
        elif opcao == "4":
            atualizar_livro()
        elif opcao == "5":
            atualizar_parcial()

        elif opcao == "0":
            print("\n👋 Encerrando cliente...")
            break


if __name__ == "__main__":
    menu()
