import random

def run_quiz(questions):
    score = 0
    
    for question, options, correct_option in questions:
        print("\n" + question)
        
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        
        user_answer = get_user_answer(len(options))
        
        if user_answer == correct_option:
            print("Correto!\n")
            score += 1
        else:
            print(f"Incorreto! A resposta correta era a opção {correct_option}: {options[correct_option-1]}\n")
    
    print(f"Fim do quiz! Sua pontuação final é: {score}/{len(questions)}")

def get_user_answer(num_options):
    while True:
        try:
            user_input = int(input(f"Escolha uma opção (1-{num_options}): "))
            if 1 <= user_input <= num_options:
                return user_input
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

# Defina suas perguntas, opções de resposta e respostas corretas
quiz_questions = [
    ("Qual é a capital do Brasil?", ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"], 1),
    ("Quantos planetas existem em nosso sistema solar?", ["7", "8", "9", "10"], 2),
    ("Quem escreveu 'Dom Quixote'?", ["Miguel de Cervantes", "William Shakespeare", "Jane Austen", "Fyodor Dostoevsky"], 1),
    # Adicione mais perguntas conforme desejado
]

# Embaralhe as perguntas para tornar o quiz mais interessante
random.shuffle(quiz_questions)

# Execute o quiz com as perguntas definidas
run_quiz(quiz_questions)
