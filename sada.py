def menu_principal():
    print("Menu:")
    print("Escolha uma das opçoes:")
    print("0. Regras da torre ")
    print("1. retirar uma peça de lugar")
    print("2. Colocar uma peça em outro disco")
    print("3. Mostrar o disco que você está segurando")
    print("4. Imprimir as torres")
    print("5. Sair")



def main():
    while True:
        menu_principal()

        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
           retirar_peca()
        elif opcao == "2":
            colocar_peca()
        elif opcao == "3":
            Mostrar_discosegurando()
        elif opcao == "4":
            imprimir_torres()  
        elif opcao == "5":
            sys.exit()
        elif opcao == "0":
            regras_torre()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


print("batata")        