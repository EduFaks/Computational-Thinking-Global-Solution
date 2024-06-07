# Global Solution 2024
# Eduardo Fakiani, Fernanda Rocha Menon, Luiza Macena Dantas

# Função para simular a leitura de um sensor a partir de dados fictícios
def ler_sensor(dados, localizacao, tipo_sensor):
    return f"{tipo_sensor.capitalize()} em {localizacao}: {dados[localizacao][tipo_sensor]}"


# Função para pedir e validar a escolha do local pelo usuário
def escolher_local(locais):
    while True:
        print("Selecione um local para ver as leituras dos sensores:")
        for i, local in enumerate(locais, 1):
            print(f"{i}. {local}")
        print(f"{len(locais) + 1}. Ver média das temperaturas e umidades")

        escolha = input("\nDigite o número da opção desejada: ")

        if escolha.isdigit():
            escolha = int(escolha) - 1
            if 0 <= escolha <= len(locais):
                return escolha

        print("Escolha inválida. Tente novamente.\n")


# Função para exibir as leituras dos sensores para o local selecionado
def exibir_leituras(dados_sensores, local):
    print(f"\nLeituras para {local}:")
    for tipo in dados_sensores[local]:
        leitura = ler_sensor(dados_sensores, local, tipo)
        print(leitura)


# Função para calcular e exibir a média das temperaturas e umidades
def calcular_media(dados_sensores):
    soma_temperatura = 0
    soma_umidade = 0
    contagem = 0

    for local in dados_sensores:
        temperatura = int(dados_sensores[local]["temperatura"][:-2])
        umidade = int(dados_sensores[local]["umidade"][:-1])
        soma_temperatura += temperatura
        soma_umidade += umidade
        contagem += 1

    media_temperatura = soma_temperatura / contagem
    media_umidade = soma_umidade / contagem

    print(f"\nMédia das Temperaturas: {media_temperatura:.2f}°C")
    print(f"Média das Umidades: {media_umidade:.2f}%")


# Função principal para organizar o fluxo do programa
def main():
    # Dados fictícios para diferentes locais
    dados_sensores = {
        "Praia Azul": {"temperatura": "27°C", "umidade": "65%", "luminosidade": "210 lux"},
        "Praia do Sol": {"temperatura": "28°C", "umidade": "70%", "luminosidade": "220 lux"},
        "Praia do Norte": {"temperatura": "25°C", "umidade": "60%", "luminosidade": "200 lux"},
        "Mar Aberto": {"temperatura": "24°C", "umidade": "80%", "luminosidade": "150 lux"},
        "Recife Encantado": {"temperatura": "26°C", "umidade": "75%", "luminosidade": "230 lux"}
    }

    locais = list(dados_sensores.keys())

    while True:
        # Solicita que o usuário selecione um local válido ou a opção de ver a média
        escolha = escolher_local(locais)

        if escolha == len(locais):
            # Exibe a média das temperaturas e umidades
            calcular_media(dados_sensores)
        else:
            # Exibe as leituras dos sensores para o local selecionado
            local_selecionado = locais[escolha]
            exibir_leituras(dados_sensores, local_selecionado)

        # Pergunta se o usuário deseja fazer outra operação
        continuar = input("\nDeseja fazer outra operação? (s/n): ").strip().lower()
        if continuar != 's':
            break


# Executa a função principal
if __name__ == "__main__":
    main()
