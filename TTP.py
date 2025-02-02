import sys
import time
import os

# Cores
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
END = "\033[0m"
Text_Strong = "\033[1m"
Text_StrongWithUnderline = "\033[4m"
Text_StrongEnd = "\033[0m"

# Função Calculadora
def Calculadora():
    print()
    msg = f"{CYAN}Calculadora{END}".center(50, "-")
    print(msg)
    print()
    print("1) Soma")
    print("2) Subtração")
    print("3) Multiplicação")
    print("4) Divisão")
    print("5) Sair")
    print()
    while True:
        cmd = input(f"<(TermoPY/{CYAN}Calculadora{END})> ")
        
        if cmd == "1":
            print()
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {num1 + num2}")
            print()
        
        elif cmd == "2":
            print()
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {num1 - num2}")
            print()
        
        elif cmd == "3":
            print()
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {num1 * num2}")
            print()
        
        elif cmd == "4":
            print()
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"Resultado: {num1 / num2}")
            print()
        
        elif cmd == "5":
            break
        
        else:
            print(f"{RED}Comando não reconhecido{END}")
            print()
# Função ToDoList
def ToDoList():
    print()
    msg = f"{CYAN}ListPY{END}".center(50, "-")
    print(msg)
    print()
    print("1) Adicionar tarefa")
    print("2) Remover tarefa")
    print("3) Listar tarefas")
    print("4) Salvar tarefas")
    print("5) Carregar tarefas")
    print("6) Sair")
    print()
    Datebase = []
    while True:
        cmd = input(f"<(TermoPY/{CYAN}ToDo-List{END})> ")
        
        if cmd == "1":
            print()
            task = input("Digite a tarefa: ")
            Datebase.append(task)
            print(f"{GREEN}Tarefa adicionada com sucesso {END}")
            print()
        
        elif cmd == "2":
            task = input("Digite a tarefa: ")
            if task not in Datebase:
                print(f"{RED}Tarefa não encontrada {END}")
                print()
                continue
            elif task in Datebase:
                Datebase.remove(task)
                print(f"{GREEN}Tarefa removida com sucesso {END}")
            else:
                print(f"{RED}Erro desconhecido {END}")    
            
            print()
        
        elif cmd == "3":
            print()
            print("Tarefas:")
            for i in Datebase:
                print(f"- {YELLOW}{i}{END}")
            print()
        
        elif cmd == "4":
            with open("Data/todolist.txt", "w") as f:
                for i in Datebase:
                    f.write(f"{i}\n")
            print(f"{GREEN}Tarefas salvas com sucesso{END}")
            print()
        
        elif cmd == "5":
            with open("Data/todolist.txt", "r") as f:
                # Carregar as tarefas dentro do array Datebase durante 
                Datebase = [i.strip() for i in f.readlines()] # Remove os espaços em branco
            print(f"{GREEN}Tarefas carregadas com sucesso{END}")
            print()
        
        elif cmd == "6":
            break
        
        elif cmd == "help":
            print()
            print("1) Adicionar tarefa")
            print("2) Remover tarefa")
            print("3) Listar tarefas")
            print("4) Salvar tarefas")
            print("5) Carregar tarefas")
            print("6) Sair")
            print()
        
        else:
            print(f"{RED}Comando não reconhecido{END}")
            print()
# Início do programa
def InicioPrograma():
    print()
    dado = f"{GREEN}Detalhes de software{END}".center(50, "-")
    print(dado)
    print()
    print(f"{Text_StrongWithUnderline}Nome:{END} Tools Terminal in Python (TTP)")
    print(f"{Text_StrongWithUnderline}Versão:{END} 1.1")
    print(f"{Text_StrongWithUnderline}Linguagem:{END} Python")
    print(f"{Text_StrongWithUnderline}Desenvolvedor:{END} Victor Alex Moreira Gouveia")
    print(f"{Text_StrongWithUnderline}GitHub:{END} https://github.com/Victor-Alex-Moreira-Gouveia")
    print(f"{Text_StrongWithUnderline}Licença:{END} MIT")
    print()

InicioPrograma()
mod1 = f" {CYAN}TerminalPY Versão 1.0{END} ".center(50, "-")
print(mod1)
print(f"{YELLOW}Digite 'help' para ver todos os comandos{END}")
print()

while True:
    cmd = input(f"<(TermoPY/{PURPLE}NULL{END})> ")
    cmd_formatado = cmd.lower()
    
    if cmd_formatado == "exit":
        sys.exit()
    
    elif cmd_formatado == "help":
        print(f"{CYAN}exit{END} - Saír do terminal")
        print(f"{CYAN}help{END} - Mostrar todos os comandos")
        print(f"{CYAN}time{END} - Mostrar a hora atual")
        print(f"{CYAN}list{END} - Lista todos os softwares instalados")
        print(f"{CYAN}clear{END} - Limpar a tela")
        print()
        
    elif cmd_formatado == "time":
        print(time.strftime("%H:%M:%S"))
        print()
    
    elif cmd_formatado == "list":
        print()
        print(f"1) To do list ({CYAN}ListPY{END})")
        print(f"2) Calculadora ({CYAN}CalcPY{END})")
        print()
    
    elif cmd_formatado == "clear":
        print("\n" * 100)
    
    # Programas
    
    elif cmd_formatado == "listpy":
        # Verifica se a pasta 'Data' existe e se não existir, cria a pasta
        if not os.path.exists("Data"):
            os.makedirs("Data")
        
        # Caso a pasta exista, verifica se o arquivo 'todolist.txt' existe e se não existir, cria o arquivo
        if os.path.exists("Data"):
            if not os.path.exists("Data/todolist.txt"):
                with open("Data/todolist.txt", "w") as f:
                    pass
        
        ToDoList()
    
    elif cmd_formatado == "calcpy":
        Calculadora()
    
    # Comandos de erro
    else:
        print(f"{RED}Comando não reconhecido", END)
        print(f"{YELLOW}Digite 'help' para ver todos os comandos{END}")