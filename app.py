from flask import Flask, render_template, make_response, request
import random

app = Flask(__name__)

def shuffle_options(questions):
    for question in questions:
        options = question['options']
        correct_answer = question['answer']
        random.shuffle(options)
        question['options'] = options
        question['answer'] = correct_answer
    return questions

questions_q = [
    {"question": "Para pedir que transmita mais devagar, usa-se:", "options": ["QRQ", "QRS", "QRU"], "answer": "QRS"},
    {"question": "'QTR' é utilizado para:", "options": ["Saber o horário exato", "Informar localização", "Pedir para desligar"], "answer": "Saber o horário exato"},
    {"question": "Quando se quer fazer uma ponte de comunicação, utiliza-se:", "options": ["QRU", "QRM", "QSP"], "answer": "QSP"},
    {"question": "O código 'QAR' significa:", "options": ["Está ocupado", "Desligar", "Qual horário"], "answer": "Desligar"},
    {"question": "Para perguntar se tem algo para comunicar, usa-se:", "options": ["QRU", "QSL", "QTH"], "answer": "QRU"},
    {"question": "'QTU' é utilizado para:", "options": ["Saber a distância", "Perguntar o horário de operação", "Confirmar mensagem"], "answer": "Perguntar o horário de operação"},
    {"question": "O código para perguntar sobre interferência humana é:", "options": ["QRN", "QRM", "QRU"], "answer": "QRM"},
    {"question": "Para saber a força do sinal, utiliza-se:", "options": ["QSA", "QSL", "QRM"], "answer": "QSA"},
    {"question": "'QRB' é usado para:", "options": ["Saber o nome", "Verificar o horário", "Saber a distância entre estações"], "answer": "Saber a distância entre estações"},
    {"question": "Para pedir que transmita mais rápido, usa-se:", "options": ["QRS", "QRQ", "QRL"], "answer": "QRQ"},
    {"question": "O código 'QTA' significa:", "options": ["Cancelar última mensagem", "Transmitir mais rápido", "Fazer ponte"], "answer": "Cancelar última mensagem"},
    {"question": "Para perguntar se alguém está ocupado, utiliza-se:", "options": ["QRV", "QRL", "QRU"], "answer": "QRL"},
    {"question": "'QTC' é usado para:", "options": ["Saber localização", "Perguntar sobre mensagens para enviar", "Confirmar recebimento"], "answer": "Perguntar sobre mensagens para enviar"},
    {"question": "O código 'QSN' significa:", "options": ["Fazer ponte", "Escutou-me", "Está ocupado"], "answer": "Escutou-me"},
    {"question": "Para saber que horas alguém saiu, usa-se:", "options": ["QTR", "QTN", "QTU"], "answer": "QTN"},
    {"question": "'TKS' é utilizado para:", "options": ["Desligar", "Obrigado", "Repetir mensagem"], "answer": "Obrigado"},
    {"question": "Para pedir repetição da última mensagem, usa-se:", "options": ["QSM", "QSN", "QSR"], "answer": "QSM"},
    {"question": "O código 'QRX' é usado para:", "options": ["Desligar comunicação", "Quando vai ligar novamente", "Está na escuta"], "answer": "Quando vai ligar novamente"},
    {"question": "'QRT' significa:", "options": ["Transmitir mais devagar", "Parar de transmitir/fora do ar", "Qual sua localização"], "answer": "Parar de transmitir/fora do ar"},
    {"question": "Para fazer um comunicado ou aviso, utiliza-se:", "options": ["QTC", "QSO", "QSP"], "answer": "QSO"},
    {"question": "O código 'QTH' é utilizado para:", "options": ["Perguntar o horário", "Solicitar endereço ou localização", "Pedir para desligar"], "answer": "Solicitar endereço ou localização"},
    {"question": "Quando alguém usa 'QRV', significa que:", "options": ["Está com interferência", "Quer saber o horário", "Está preparado/às ordens"], "answer": "Está preparado/às ordens"},
    {"question": "Para perguntar sobre interferência na comunicação, usa-se:", "options": ["QRN", "QSL", "QTR"], "answer": "QRN"},
    {"question": "O código 'QSJ' refere-se a:", "options": ["Viatura", "Dinheiro/pagamento", "Motorista"], "answer": "Dinheiro/pagamento"},
    {"question": "Para confirmar o recebimento de uma mensagem, utiliza-se:", "options": ["QRZ", "QRU", "QSL"], "answer": "QSL"},
    {"question": "O código 'QSD' é usado para identificar:", "options": ["Motorista", "Viatura", "Pagamento"], "answer": "Motorista"},
    {"question": "Quando se quer saber quem está chamando, utiliza-se:", "options": ["QTH", "QRZ", "QRU"], "answer": "QRZ"},
    {"question": "'QAP' significa:", "options": ["Desligar o rádio", "Está na escuta", "Qual seu nome"], "answer": "Está na escuta"},
    {"question": "Para saber o nome do operador ou indicativo da estação, usa-se:", "options": ["QRA", "QAP", "QTH"], "answer": "QRA"},
    {"question": "O código 'QSV' é utilizado para:", "options": ["Motorista", "Pagamento", "Viatura"], "answer": "Viatura"}
]

questions_j = [
    {"question": "O código 'J3' refere-se a:", "options": ["Abastecimento", "Troca de guarnição de serviço", "Refeição"], "answer": "Troca de guarnição de serviço"},
    {"question": "Quando uma guarnição informa 'J4', significa que:", "options": ["Está em deslocamento para ocorrência", "Está fazendo refeição", "Está em lavação de viatura"], "answer": "Está fazendo refeição"},
    {"question": "O código 'J5' é utilizado para informar:", "options": ["Abastecimento", "Banheiro", "Chegada na Base"], "answer": "Abastecimento"},
    {"question": "'J6' indica:", "options": ["Baixa mecânica da viatura", "Lavação ou limpeza de viatura", "Troca de guarnição"], "answer": "Lavação ou limpeza de viatura"},
    {"question": "Quando uma viatura está com problemas mecânicos, usa-se o código:", "options": ["J7", "J6", "J8"], "answer": "J7"},
    {"question": "O código 'J8' é utilizado para informar:", "options": ["Chegada ao local da ocorrência", "Banheiro", "Abastecimento"], "answer": "Banheiro"},
    {"question": "Quando uma guarnição está a caminho de uma ocorrência, utiliza-se:", "options": ["J10", "J11", "J9"], "answer": "J9"},
    {"question": "'J10' significa:", "options": ["Guarnição em deslocamento para ocorrência", "Chegada da guarnição ao local da ocorrência", "Guarnição em deslocamento para a Base"], "answer": "Chegada da guarnição ao local da ocorrência"},
    {"question": "O código 'J11' é usado para informar:", "options": ["Chegada da guarnição na Base", "Guarnição em deslocamento para a Base", "Chegada da guarnição ao local da ocorrência"], "answer": "Guarnição em deslocamento para a Base"},
    {"question": "'J12' indica:", "options": ["Guarnição em deslocamento para ocorrência", "Chegada da guarnição na Base", "Troca de guarnição de serviço"], "answer": "Chegada da guarnição na Base"}
]

questions_phonetic = [
    {"question": "No alfabeto fonético, a letra 'A' é representada por:", "options": ['ALFA','ÁBACO','ABAJUR'], "answer": 'ALFA'},
    {"question": "No alfabeto fonético, a letra 'B' é representada por:", "options": ['BRAVO','BRISA','BRUMA'], "answer": 'BRAVO'},
    {"question": "No alfabeto fonético, a letra 'C' é representada por:", "options": ['CHARLIE','CHARME','CHICOTE'], "answer": 'CHARLIE'},
    {"question": "No alfabeto fonético, a letra 'D' é representada por:", "options": ['DELTA','DADO','DEDO'], "answer": 'DELTA'},
    {"question": "No alfabeto fonético, a letra 'E' é representada por:", "options": ['ECO','ELEFANTE','EMA'], "answer": 'ECO'},
    {"question": "No alfabeto fonético, a letra 'F' é representada por:", "options": ['FOXTROT','FACA','FOGO'], "answer": 'FOXTROT'},
    {"question": "No alfabeto fonético, a letra 'G' é representada por:", "options": ['GOLF','GATO','GELO'], "answer": 'GOLF'},
    {"question": "No alfabeto fonético, a letra 'H' é representada por:", "options": ['HOTEL','HARPA','HÉLICE'], "answer": 'HOTEL'},
    {"question": "No alfabeto fonético, a letra 'I' é representada por:", "options": ['INDIA','ILHA','ÍMÃ'], "answer": 'INDIA'},
    {"question": "No alfabeto fonético, a letra 'J' é representada por:", "options": ['JULIET','JARRO','JOIA'], "answer": 'JULIET'},
    {"question": "No alfabeto fonético, a letra 'K' é representada por:", "options": ['KILO','KIWI','KETCHUP'], "answer": 'KILO'},
    {"question": "No alfabeto fonético, a letra 'L' é representada por:", "options": ['LIMA','LUA','LÁPIS'], "answer": 'LIMA'},
    {"question": "No alfabeto fonético, a letra 'M' é representada por:", "options": ['MIKE','MESA','MALA'], "answer": 'MIKE'},
    {"question": "No alfabeto fonético, a letra 'N' é representada por:", "options": ['NOVEMBER','NAVIO','NUVEM'], "answer": 'NOVEMBER'},
    {"question": "No alfabeto fonético, a letra 'O' é representada por:", "options": ['OSCAR','OVO','OURO'], "answer": 'OSCAR'},
    {"question": "No alfabeto fonético, a letra 'P' é representada por:", "options": ['PAPA','PATO','PENA'], "answer": 'PAPA'},
    {"question": "No alfabeto fonético, a letra 'Q' é representada por:", "options": ['QUEBEC','QUEIJO','QUIABO'], "answer": 'QUEBEC'},
    {"question": "No alfabeto fonético, a letra 'R' é representada por:", "options": ['ROMEU','RATO','REMO'], "answer": 'ROMEU'},
    {"question": "No alfabeto fonético, a letra 'S' é representada por:", "options": ['SIERRA','SACO','SELO'], "answer": 'SIERRA'},
    {"question": "No alfabeto fonético, a letra 'T' é representada por:", "options": ['TANGO','TELA','TUBO'], "answer": 'TANGO'},
    {"question": "No alfabeto fonético, a letra 'U' é representada por:", "options": ['UNIFORM','UVA','URSO'], "answer": 'UNIFORM'},
    {"question": "No alfabeto fonético, a letra 'V' é representada por:", "options": ['VICTOR','VACA','VELA'], "answer": 'VICTOR'},
    {"question": "No alfabeto fonético, a letra 'W' é representada por:", "options": ['WHISKEY','WAFER','WALKIE-TALKIE'], "answer": 'WHISKEY'},
    {"question": "No alfabeto fonético, a letra 'X' é representada por:", "options": ['X-RAY','XÍCARA','XADREZ'], "answer": 'X-RAY'},
    {"question": "No alfabeto fonético, a letra 'Y' é representada por:", "options": ['YANKEE','IOGA','IATE'], "answer": 'YANKEE'},
    {"question": "No alfabeto fonético, a letra 'Z' é representada por:", "options": ['ZULU','ZEBRA','ZÍPER'], "answer": 'ZULU'},
]

questions_all = questions_q + questions_j + questions_phonetic

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quiz/<quiz_type>")
def quiz(quiz_type):
    question_count = int(request.args.get('count', 5))  # Padrão para 5 se não for especificado
    
    if quiz_type == "q":
        questions = questions_q
        quiz_name = "Código Q"
    elif quiz_type == "j":
        questions = questions_j
        quiz_name = "Código J"
    elif quiz_type == "phonetic":
        questions = questions_phonetic
        quiz_name = "Alfabeto Fonético"
    elif quiz_type == "all":
        questions = questions_all
        quiz_name = "Quiz Completo"
    else:
        return "Quiz não encontrado", 404

    # Garante que não tentamos selecionar mais perguntas do que existem
    question_count = min(question_count, len(questions))
    
    selected_questions = random.sample(questions, question_count)
    shuffled_questions = shuffle_options(selected_questions)
    
    response = make_response(render_template("quiz.html", questions=shuffled_questions, quiz_type=quiz_type, quiz_name=quiz_name))
    response.headers['ngrok-skip-browser-warning'] = 'true'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
