dataset_sessions = [
    {
        "session_id": 1,
        "turns": [
            {"question": "A partir de que horas posso fazer o check-in?", "ground_truth": "O check-in é permitido a partir das 14h."},
            {"question": "E se eu chegar de madrugada?", "ground_truth": "O serviço de recepção funciona, mas o check-in antecipado está sujeito à disponibilidade e a taxas de 30% a 50% do valor da diária."}
        ]
    },
    {
        "session_id": 2,
        "turns": [
            {"question": "Posso levar meu cachorro? Ele pesa 5kg.", "ground_truth": "Sim, o hotel recebe cães e gatos de pequeno porte até 10kg com uma tarifa Pet Fee de R$ 60 por estadia."},
            {"question": "Ele pode frequentar a piscina com as crianças?", "ground_truth": "Não, por normas da vigilância sanitária, os animais não podem ingressar nas áreas de piscina e restaurante."}
        ]
    },
    {
        "session_id": 3,
        "turns": [
            {"question": "Tem internet de alta velocidade no hotel?", "ground_truth": "Sim, oferecemos Wi-Fi gratuito de alta velocidade em todo o hotel. Há também a rede Premium paga."},
            {"question": "Qual é a senha da rede gratuita?", "ground_truth": "A senha para a rede padrão (HotelExample_Guest) é hotel1234."}
        ]
    },
    {
        "session_id": 4,
        "turns": [
            {"question": "O estacionamento é gratuito?", "ground_truth": "Não, o estacionamento e valet custam R$ 30,00 por diária."},
            {"question": "Vocês garantem que meu carro ficará na sombra?", "ground_truth": "As vagas cobertas e subterrâneas são disponibilizadas por ordem de chegada até que a lotação seja completada."}
        ]
    },
    {
        "session_id": 5,
        "turns": [
            {"question": "Quais são os horários do café da manhã?", "ground_truth": "O café da manhã é servido das 6h30 às 10h30."},
            {"question": "E se eu não tiver ele incluso no meu pacote, quanto pago?", "ground_truth": "Para quem não possui o café incluso na reserva, cobra-se uma taxa de R$ 55,00 por pessoa na portaria."}
        ]
    },
    {
        "session_id": 6,
        "turns": [
            {"question": "O hotel possui serviço gratuito de transporte do aeroporto?", "ground_truth": "Não há serviço gratuito. O hotel oferece serviço de transfer (van/carro) com tarifa adicional de R$ 80,00 por trecho."},
            {"question": "A que distância ele fica de vocês?", "ground_truth": "O aeroporto está a 12 km de distância do hotel (aproximadamente 25 minutos de carro)."}
        ]
    },
    {
        "session_id": 7,
        "turns": [
            {"question": "Posso fumar no quarto?", "ground_truth": "Não, o hotel é um ambiente livre de fumo e é expressamente proibido fumar em qualquer espaço coberto."},
            {"question": "Isso inclui cigarro eletrônico e vape?", "ground_truth": "Sim, é expressamente proibido o uso de qualquer tipo de fumo, inclusive cigarros eletrônicos, charutos ou cachimbos."}
        ]
    },
    {
        "session_id": 8,
        "turns": [
            {"question": "Qual a idade mínima para se hospedar sozinho?", "ground_truth": "Menores de 18 anos só podem se hospedar acompanhados dos pais ou responsáveis legais."},
            {"question": "E se o adolescente tiver autorização judicial?", "ground_truth": "Caso acompanhado de terceiros, exige-se autorização judicial ou por escrito dos responsáveis com firma reconhecida."}
        ]
    },
    {
        "session_id": 9,
        "turns": [
            {"question": "O que acontece se eu chegar para o check-in após as 18h?", "ground_truth": "As reservas são garantidas até as 18h. Em caso de ausência sem comunicação (No Show) a reserva pode ser cancelada e cobrada integralmente."},
            {"question": "Como posso garantir se eu for atrasar?", "ground_truth": "A reserva se mantém se houver garantia de no-show (ex: cartão de crédito ou depósito prévio fornecidos previamente)."}
        ]
    },
    {
        "session_id": 10,
        "turns": [
            {"question": "Quais documentos preciso apresentar no check-in?", "ground_truth": "É necessário apresentar um documento oficial de identidade com foto (RG, CNH ou Passaporte). O titular do cartão de crédito da reserva também deve estar presente."},
            {"question": "Vocês exigem caução nessa hora?", "ground_truth": "Sim, retemos uma garantia eletrônica (caução) de em média R$ 200,00 por dia."}
        ]
    },
    {
        "session_id": 11,
        "turns": [
            {"question": "Existe um horário de silêncio obrigatório no hotel?", "ground_truth": "Sim, o horário de silêncio absoluto vigora das 22h às 07h para garantir o bem-estar de todos."},
            {"question": "O que acontece se um hóspede fizer barulho alto nesse período?", "ground_truth": "Barulhos e conversas em tom alto implicarão em advertências ou multas."}
        ]
    },
    {
        "session_id": 12,
        "turns": [
            {"question": "O que acontece se for detectado cheiro de fumaça no meu quarto?", "ground_truth": "Caso seja percebido odor ou vestígio de tabaco, uma multa por limpeza extrema será lançada na conta do hóspede."},
            {"question": "Onde eu poderia fumar então?", "ground_truth": "Os fumantes deverão se dirigir aos locais especificamente designados nas áreas externas (se houver)."}
        ]
    },
    {
        "session_id": 13,
        "turns": [
            {"question": "Posso utilizar meu fogareiro elétrico no quarto?", "ground_truth": "Não é permitida a utilização de aparelhos de alto consumo, como fogareiros ou resistências, visando evitar riscos de incêndio."},
            {"question": "E se eu precisar ferver água?", "ground_truth": "Nós solicitamos que evite usar esses itens de alto consumo, você pode utilizar o frigobar ou o serviço de quarto 24h para bebidas quentes."}
        ]
    },
    {
        "session_id": 14,
        "turns": [
            {"question": "Qual a regra para consumo de bebidas alcoólicas?", "ground_truth": "O consumo de bebidas alcoólicas é permitido apenas para maiores de 18 anos, mediante apresentação de identificação."},
            {"question": "Vocês vendem isso de madrugada no quarto?", "ground_truth": "Sim, o serviço de quarto está disponível 24h e as cervejas artesanais ou garrafas de vinho podem ser solicitadas via Room Service."}
        ]
    },
    {
        "session_id": 15,
        "turns": [
            {"question": "O hotel se responsabiliza por valores deixados na mesa?", "ground_truth": "Não. O hotel recomenda o uso do cofre eletrônico do quarto e não se responsabiliza por valores ou dinheiro não armazenados nele."},
            {"question": "E se alguém da limpeza roubar?", "ground_truth": "A política de responsabilidade determina que valores expressivos devem estar no cofre, caso contrário não há passibilidade de indenização."}
        ]
    },
    {
        "session_id": 16,
        "turns": [
            {"question": "Onde ficam as rotas de evacuação de incêndio?", "ground_truth": "A rota de evacuação está localizada na porta de todos os quartos e nos corredores do prédio."},
            {"question": "Qual ramal eu ligo se houver fogo?", "ground_truth": "Em caso acidental, deve-se contatar imediatamente a recepção nos ramais específicos previstos de emergência (como o Ramal 0)."}
        ]
    },
    {
        "session_id": 17,
        "turns": [
            {"question": "Posso receber visitas no meu quarto à tarde?", "ground_truth": "Não. Visitantes não-hóspedes são permitidos apenas em áreas comuns (lobby, restaurante) e o acesso aos andares de quartos é restrito."},
            {"question": "Até que horas eles podem ficar nessas áreas comuns?", "ground_truth": "Os visitantes podem ficar nas áreas comuns das 08h até, no mais tardar, 22h."}
        ]
    },
    {
        "session_id": 18,
        "turns": [
            {"question": "Crianças podem usar a piscina sozinhas?", "ground_truth": "Não, as crianças deverão sempre estar acompanhadas por um adulto responsável ao utilizar a piscina."},
            {"question": "Bebês podem entrar com fraldas normais nela?", "ground_truth": "Não, bebês devem utilizar fraldas apropriadas flutuantes para mergulhos infantis."}
        ]
    },
    {
        "session_id": 19,
        "turns": [
            {"question": "Tem salva-vidas de plantão lá?", "ground_truth": "Não existe salva-vidas no local, portanto o uso da piscina é de responsabilidade exclusiva do hóspede."},
            {"question": "Qual o horário de funcionamento dela?", "ground_truth": "A piscina funciona todos os dias das 08h00 da manhã às 20h00."}
        ]
    },
    {
        "session_id": 20,
        "turns": [
            {"question": "Qual o horário de funcionamento da academia?", "ground_truth": "A academia (Fitness Center) funciona diariamente das 06h00 às 22h00."},
            {"question": "Adolescentes podem treinar lá?", "ground_truth": "O acesso à academia é restrito para menores de 16 anos, salvo acompanhamento formalizado pelos pais."}
        ]
    },
    {
        "session_id": 21,
        "turns": [
            {"question": "Posso almoçar no restaurante usando apenas roupa de banho?", "ground_truth": "Não, não é permitido o ingresso ou trânsito nos restaurantes sem camisas, em biquínis ou com os pés descalços."},
            {"question": "Que tipo de comida tem no almoço?", "ground_truth": "O almoço oferece pratos à la carte ou buffet executivo (saladas, carnes, massas, sobremesas) e funciona das 12h às 15h."}
        ]
    },
    {
        "session_id": 22,
        "turns": [
            {"question": "Como funciona o check-out tarde?", "ground_truth": "O late check-out até as 16h00 tem cobrança de 50% do valor da diária, dependendo da disponibilidade."},
            {"question": "Tem alguma regra que isenta essa taxa?", "ground_truth": "Hóspedes que integram o programa 'Viajante Vip Hotel' podem ganhar check-outs prorrogados gratuitos às 14h."}
        ]
    },
    {
        "session_id": 23,
        "turns": [
            {"question": "O hotel emite nota fiscal para minha empresa?", "ground_truth": "Sim, realizamos emissão fiscal contra empresas (B2B) perante faturamento quinzenal para clientes corporativos registrados."},
            {"question": "Preciso mandar algum e-mail pra isso?", "ground_truth": "Sim, a recepção exigirá seus dados corporativos completos durante o check-out ou via contato com nosso setor de faturamento."}
        ]
    },
    {
        "session_id": 24,
        "turns": [
            {"question": "Qual é a política sobre lavagem de roupas?", "ground_truth": "O hotel possui serviço de lavanderia (urgente) que custa R$ 50,00 por peça, entregando em até 6 horas."},
            {"question": "Esses serviços são cobrados na hora?", "ground_truth": "Não, serviços de lavanderia costumam ser lançados como 'consumo' e pagos sempre na saída do Check-Out."}
        ]
    },
    {
        "session_id": 25,
        "turns": [
            {"question": "Os quartos têm ar condicionado?", "ground_truth": "Sim, todos os quartos são equipados com Ar Condicionado Split silencioso."},
            {"question": "Qual a voltagem das tomadas deles?", "ground_truth": "A voltagem padrão nas acomodações do hotel é de 220v."}
        ]
    },
    {
        "session_id": 26,
        "turns": [
            {"question": "Posso agendar uma massagem?", "ground_truth": "Sim, oferecemos massagem relaxante com aromaterapia por R$ 150,00 a hora, mediante agendamento das 09h às 21h."},
            {"question": "Posso agendar pela recepção?", "ground_truth": "O agendamento é feito no próprio Spa, e terapias do SPA costumam ser lançadas na conta do quarto."}
        ]
    },
    {
        "session_id": 27,
        "turns": [
            {"question": "Quais passeios posso fazer na cidade?", "ground_truth": "O Concierge organiza City Tours, passeios de barco para ilhas, e roteiros ecológicos de jipe."},
            {"question": "Qual o valor do passeio de barco?", "ground_truth": "O passeio de barco custa R$ 200,00 por pessoa, dura 2h e ocorre na temporada (jun–set)."}
        ]
    },
    {
        "session_id": 28,
        "turns": [
            {"question": "O hotel fica no centro turístico?", "ground_truth": "O hotel tem fácil acesso aos atrativos. Os pontos turísticos mais próximos são o Museu Central (2 km) e o Parque Verde com pista de caminhada (1,2 km)."},
            {"question": "Qual aplicativo vocês recomendam usar pra ir lá?", "ground_truth": "Sugerimos o uso de Uber, 99 ou InDriver, com ponto de embarque na entrada principal."}
        ]
    },
    {
        "session_id": 29,
        "turns": [
            {"question": "Se eu esquecer meu carregador, acho outro perto?", "ground_truth": "Existem pontos comerciais, como um Shopping Center e Centro Financeiro a 5 km de distância."},
            {"question": "E farmácia?", "ground_truth": "Temos uma farmácia 24h a 500m (Rua das Palmeiras, 100)."}
        ]
    },
    {
        "session_id": 30,
        "turns": [
            {"question": "Vocês têm suíte presidencial?", "ground_truth": "Sim, a Suíte Presidencial custa a partir de R$ 1.200,00 por noite e inclui 2 ambientes e serviço de mordomo."},
            {"question": "Tem jacuzzi nela?", "ground_truth": "Sim, ela possui champanhe de boas-vindas, máquina de café expresso e jacuzzi privativa."}
        ]
    },
    {
        "session_id": 31,
        "turns": [
            {"question": "O hotel tem programa de sustentabilidade?", "ground_truth": "Sim, possuímos o programa 'Hotel Verde'. Para colaborar, as roupas de cama são trocadas a cada 3 dias."},
            {"question": "E as toalhas, como funcionam no programa?", "ground_truth": "Se desejar reutilizar suas toalhas, deixe-as penduradas no toalheiro. Toalhas no chão serão lavadas."}
        ]
    },
    {
        "session_id": 32,
        "turns": [
            {"question": "Qual ramal para chamar a limpeza?", "ground_truth": "Para serviços de limpeza ou arrumação, o hóspede deve discar o ramal 105."},
            {"question": "A que horas eles passam limpando?", "ground_truth": "A arrumação do quarto ocorre diariamente entre as 09h00 e 16h00."}
        ]
    },
    {
        "session_id": 33,
        "turns": [
            {"question": "Posso cancelar minha reserva de graça?", "ground_truth": "Para a Tarifa Flexível, cancelamentos são totalmente gratuitos se realizados com até 48 horas de antecedência ao check-in."},
            {"question": "E se a minha tarifa for não reembolsável?", "ground_truth": "Reservas promocionais não reembolsáveis não permitem cancelamento, reembolso ou alteração, e o valor integral será retido."}
        ]
    },
    {
        "session_id": 34,
        "turns": [
            {"question": "O wi-fi pega na piscina?", "ground_truth": "Sim, oferecemos Wi-Fi gratuito em todo o perímetro do hotel, incluindo piscinas, restaurantes e quartos."},
            {"question": "Tem alguma rede com internet mais rápida?", "ground_truth": "Sim, há a rede Premium (HotelExample_Premium) adquirida na recepção para quem precisa de banda larga dedicada."}
        ]
    },
    {
        "session_id": 35,
        "turns": [
            {"question": "Qual bandeira de cartão vocês aceitam?", "ground_truth": "Aceitamos Cartões Nacionais e Internacionais (Visa, Mastercard, American Express, Diners, Elo)."},
            {"question": "Aceitam Euro físico?", "ground_truth": "Não, o hotel aceita pagamentos apenas em moedas correntes físicas do Brasil (Real/BRL), além de cartões e PIX."}
        ]
    },
    {
        "session_id": 36,
        "turns": [
            {"question": "Perdi meu cartão-chave. Tem multa?", "ground_truth": "Sim, em caso de perda do cartão-chave, comunique a recepção e será cobrada uma taxa de substituição de R$ 20,00."},
            {"question": "Esse cartão abre a porta de tudo?", "ground_truth": "O cartão-chave é necessário para acesso aos quartos, elevadores e entrada nas dependências de lazer."}
        ]
    },
    {
        "session_id": 37,
        "turns": [
            {"question": "O hotel possui jantar temático?", "ground_truth": "Sim, temos Jantares Temáticos no restaurante por R$ 120,00 por pessoa, incluindo buffet completo."},
            {"question": "Quando é a noite de churrasco?", "ground_truth": "O Churrasco Fogo de Chão ocorre aos Sábados. Há também Frutos do Mar (Sexta) e Noite Italiana (Quinta)."}
        ]
    },
    {
        "session_id": 38,
        "turns": [
            {"question": "O hotel organiza casamentos?", "ground_truth": "Sim! Para reservas de grupos (acima de 5 quartos, como eventos corporativos ou casamentos) possuímos tarifas especiais."},
            {"question": "Com quem falo para bloquear os quartos?", "ground_truth": "Você terá um gerente de contas exclusivo. Envie as datas e a quantidade de pessoas para grupos@hotelexample.com.br."}
        ]
    },
    {
        "session_id": 39,
        "turns": [
            {"question": "Vocês disponibilizam cofre nos quartos?", "ground_truth": "Sim, todos os quartos são equipados com cofres eletrônicos."},
            {"question": "O que devo colocar neles?", "ground_truth": "Recomendamos que todo dinheiro ou valores expressivos sejam armazenados nele por questões de segurança e indenização."}
        ]
    },
    {
        "session_id": 40,
        "turns": [
            {"question": "O café da manhã tá incluído no quarto standard?", "ground_truth": "Sim, o Quarto Standard (R$ 350,00) tem café da manhã incluso, Wi-Fi e TV a cabo."},
            {"question": "Vocês têm cama extra infantil?", "ground_truth": "Camas extras para crianças custam R$ 120,00/noite, mas berços são gratuitos para menores de 2 anos."}
        ]
    },
    {
        "session_id": 41,
        "turns": [
            {"question": "Se eu chegar antes das 14h, posso ficar na piscina?", "ground_truth": "Sim. Caso chegue mais cedo, você pode guardar suas malas no nosso Maleiro de forma gratuita e utilizar a piscina ou restaurante."},
            {"question": "E tem como já entrar no quarto de manhã?", "ground_truth": "O Early check-in antes das 14h está sujeito à disponibilidade, com taxa de 30% a 50% do valor da diária."}
        ]
    },
    {
        "session_id": 42,
        "turns": [
            {"question": "Como conecto no wifi premium?", "ground_truth": "A Rede Premium de alta velocidade é a 'HotelExample_Premium' e os planos devem ser consultados na recepção."},
            {"question": "Ele pega na área de lazer também?", "ground_truth": "Sim, a conectividade do hotel abrange todos os quartos, áreas de lazer e espaços de eventos."}
        ]
    },
    {
        "session_id": 43,
        "turns": [
            {"question": "O restaurante abre na janta até tarde?", "ground_truth": "O restaurante funciona para o jantar até as 22h, e exige-se reserva prévia no caso de Jantar Temático."},
            {"question": "Se eu perder a hora, posso pedir algo no quarto?", "ground_truth": "Sim, o Serviço de Quarto (Room Service) está disponível 24 horas por dia com cardápio."}
        ]
    },
    {
        "session_id": 44,
        "turns": [
            {"question": "Vocês têm tomadas para carregar carros?", "ground_truth": "Sim, no estacionamento temos tomadas para carregamento de veículos elétricos (EVs)."},
            {"question": "Quanto custa para o valet guardar ele?", "ground_truth": "O serviço de estacionamento e valet custa R$ 30,00 por diária."}
        ]
    },
    {
        "session_id": 45,
        "turns": [
            {"question": "Criança acima de 7 anos paga a mais?", "ground_truth": "Sim, para cama extra de adulto ou criança acima de 7 anos é cobrada uma taxa de R$ 120,00 por noite."},
            {"question": "E bebê?", "ground_truth": "Para bebês, fornecemos berços gratuitos para menores de 2 anos, mediante disponibilidade."}
        ]
    },
    {
        "session_id": 46,
        "turns": [
            {"question": "O hotel tem programa de happy hour?", "ground_truth": "Sim, o Happy Hour ocorre no Bar do Lobby das 17h às 19h."},
            {"question": "O que servem lá?", "ground_truth": "Nesse horário, há descontos especiais em drinks selecionados."}
        ]
    },
    {
        "session_id": 47,
        "turns": [
            {"question": "O que é o programa Verde?", "ground_truth": "O 'Hotel Verde' é um programa de sustentabilidade onde as roupas de cama são trocadas a cada 3 dias e toalhas podem ser reutilizadas."},
            {"question": "Se eu jogar minha toalha no piso de propósito, o que ocorre?", "ground_truth": "Toalhas jogadas no chão indicam solicitação de troca e serão prontamente lavadas e substituídas por novas."}
        ]
    },
    {
        "session_id": 48,
        "turns": [
            {"question": "Vocês têm computadores pro hóspede?", "ground_truth": "Sim, o nosso Business Center oferece estações de trabalho, computadores e impressoras disponíveis 24h no térreo."},
            {"question": "Eu pego a senha do wifi premium com eles?", "ground_truth": "Você deve consultar os planos da rede Premium (HotelExample_Premium) diretamente na recepção."}
        ]
    },
    {
        "session_id": 49,
        "turns": [
            {"question": "Perdi meu relógio. Tem achados e perdidos?", "ground_truth": "Sim, se perder um objeto, entre em contato com a recepção ou o e-mail achadosperdidos@hotel.com."},
            {"question": "Quanto tempo vocês guardam as coisas lá?", "ground_truth": "Os itens esquecidos são guardados no hotel por um período de 30 dias."}
        ]
    },
    {
        "session_id": 50,
        "turns": [
            {"question": "O que acontece se eu levar multa por cheiro de cigarro?", "ground_truth": "A multa por odor de fumaça é lançada na sua conta, considerada como taxa adicional por limpeza extrema."},
            {"question": "Isso vale pro pátio externo também?", "ground_truth": "A proibição de fumo (incluindo cigarros eletrônicos) se aplica a qualquer espaço coberto do hotel, aposentos ou corredores. Nas áreas externas designadas, o fumo é permitido."}
        ]
    }
]

# Variável flat para compatibilidade com outros testes
dataset = [turn for s in dataset_sessions for turn in s['turns']]

