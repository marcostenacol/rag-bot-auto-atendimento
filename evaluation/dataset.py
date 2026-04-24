dataset = [
    {
        "question": "A partir de que horas posso fazer o check-in?",
        "ground_truth": "O check-in é permitido a partir das 14h."
    },
    {
        "question": "Posso levar meu cachorro? Ele pesa 5kg.",
        "ground_truth": "Sim, o hotel recebe cães e gatos de pequeno porte até 10kg. É aplicada uma tarifa Pet Fee de R$ 60 por estadia."
    },
    {
        "question": "Tem internet de alta velocidade no hotel?",
        "ground_truth": "Sim, oferecemos Wi-Fi gratuito de alta velocidade em todo o hotel. Para quem precisa de mais banda, há a rede Premium paga."
    },
    {
        "question": "O estacionamento é gratuito?",
        "ground_truth": "Não, o estacionamento e valet custam R$ 30,00 por diária."
    },
    {
        "question": "Quais são os horários do café da manhã?",
        "ground_truth": "O café da manhã é servido das 6h30 às 10h30."
    },
    {
        "question": "O hotel possui serviço gratuito de transporte em helicóptero do aeroporto?",
        "ground_truth": "Não há informações sobre serviço de helicóptero nos documentos. O hotel oferece serviço de transfer (van/carro) com tarifa adicional."
    },
    {
        "question": "Posso fumar no quarto?",
        "ground_truth": "Não, o hotel é um ambiente livre de fumo e é expressamente proibido fumar em qualquer espaço coberto, incluindo os quartos."
    },
    {
        "question": "Qual a idade mínima para se hospedar sozinho no hotel?",
        "ground_truth": "Menores de 18 anos só podem se hospedar acompanhados dos pais ou responsáveis legais, conforme o ECA (Lei nº 8.069/1990)."
    },
    {
        "question": "O que acontece se eu chegar para o check-in após as 18h sem avisar?",
        "ground_truth": "As reservas são garantidas até as 18h da data de início, salvo se houver garantia de no-show (depósito prévio ou cartão). Informe sempre eventuais atrasos."
    },
    {
        "question": "Quais documentos preciso apresentar no momento do check-in?",
        "ground_truth": "É necessário apresentar um documento oficial de identidade com foto (RG, CNH ou Passaporte) e o titular do cartão de crédito da reserva deve estar presente."
    },
    {
        "question": "Existe um horário de silêncio obrigatório no hotel?",
        "ground_truth": "Sim, o horário de silêncio absoluto vigora das 22h às 07h para garantir o bem-estar de todos os hóspedes."
    },
    {
        "question": "Posso usar cigarro eletrônico (vape) nas áreas internas?",
        "ground_truth": "Não, é expressamente proibido o fumo (inclusive cigarros eletrônicos) em qualquer espaço coberto do hotel, aposentos ou corredores."
    },
    {
        "question": "O que acontece se for detectado cheiro de fumaça no meu quarto?",
        "ground_truth": "Caso seja percebido odor ou vestígio de tabaco, uma multa por limpeza extrema será lançada na conta do hóspede."
    },
    {
        "question": "Posso utilizar meu próprio fogareiro ou resistência para ferver água no quarto?",
        "ground_truth": "Não é permitida a utilização de aparelhos de alto consumo, como fogareiros ou resistências, visando evitar riscos de incêndio."
    },
    {
        "question": "Qual a regra para consumo de bebidas alcoólicas no hotel?",
        "ground_truth": "O consumo de bebidas alcoólicas é permitido apenas para maiores de 18 anos, mediante apresentação de identificação."
    },
    {
        "question": "O hotel se responsabiliza por valores ou dinheiro deixados fora do cofre?",
        "ground_truth": "Não. O hotel recomenda o uso do cofre eletrônico do quarto e não se responsabiliza por valores não armazenados corretamente."
    },
    {
        "question": "Onde posso encontrar as instruções de evacuação em caso de emergência?",
        "ground_truth": "A rota de evacuação está localizada na porta de todos os quartos e nos corredores do prédio."
    },
    {
        "question": "Posso receber visitas de amigos não-hóspedes no meu quarto?",
        "ground_truth": "Não. Visitantes são permitidos apenas em áreas comuns (lobby, restaurante) das 08h às 22h. O acesso aos andares de quartos é restrito."
    },
    {
        "question": "As crianças podem usar a piscina sozinhas?",
        "ground_truth": "Não, as crianças deverão sempre estar acompanhadas por um adulto responsável ao utilizar a piscina."
    },
    {
        "question": "Bebês podem usar a piscina com fraldas comuns?",
        "ground_truth": "Não, bebês devem utilizar fraldas apropriadas flutuantes para mergulhos infantis na piscina."
    },
    {
        "question": "O hotel possui salva-vidas na piscina?",
        "ground_truth": "Não existe salva-vidas no local, portanto o uso da piscina é de responsabilidade exclusiva do hóspede."
    },
    {
        "question": "Qual o horário de funcionamento da academia (Fitness Center)?",
        "ground_truth": "A academia funciona diariamente das 06h00 às 22h00."
    },
    {
        "question": "Qual a idade mínima para frequentar a academia sem acompanhamento?",
        "ground_truth": "O acesso à academia é restrito para menores de 16 anos, salvo acompanhamento formalizado pelos pais."
    },
    {
        "question": "É permitido entrar no restaurante usando apenas roupas de banho?",
        "ground_truth": "Não, não é permitido o ingresso ou trânsito nos restaurantes sem camisas, em biquínis ou com os pés descalços."
    },
    {
        "question": "Por que é cobrada uma caução no check-in e qual o valor?",
        "ground_truth": "A caução é de aproximadamente R$ 200,00 por dia e serve como garantia para despesas extras ou danos, sendo reembolsada no check-out."
    },
    {
        "question": "Quais bandeiras de cartão de crédito o hotel aceita?",
        "ground_truth": "Aceitamos Visa, Mastercard, American Express, Diners, Elo e também pagamentos via PIX ou dinheiro (BRL)."
    },
    {
        "question": "Sou uma empresa, posso solicitar faturamento da nota fiscal?",
        "ground_truth": "Sim, o hotel realiza faturamento quinzenal para empresas cadastradas ou mediante depósitos antecipados."
    },
    {
        "question": "Quais são as regras para trânsito de animais (pets) no hotel?",
        "ground_truth": "Os pets devem portar carteira de vacinação atualizada e trafegar obrigatoriamente presos em guias ou coleiras pelo pátio."
    },
    {
        "question": "O pet pode frequentar o ambiente da piscina ou restaurante?",
        "ground_truth": "Não, por normas da vigilância sanitária, os animais não podem ingressar nas áreas de piscina e restaurante."
    },
    {
        "question": "O hotel garante vaga coberta no estacionamento?",
        "ground_truth": "As vagas cobertas e subterrâneas são disponibilizadas por ordem de chegada até que a lotação seja completada."
    },
    {
        "question": "Como funciona o 'Programa Viajante Vip Hotel'?",
        "ground_truth": "Hóspedes com mais de 3 estadias anuais ganham benefícios como upgrade de categoria, mimos de boas-vindas ou check-out tardio gratuito."
    },
    {
        "question": "Quais tipos de passeios o Concierge pode organizar?",
        "ground_truth": "O Concierge organiza City Tours, passeios de barco para ilhas, roteiros ecológicos de jipe e agendamento de terapias de Spa."
    },
    {
        "question": "O uso da academia tem alguma taxa extra?",
        "ground_truth": "Não, o Fitness Center possui entrada livre de taxas para os hóspedes do hotel."
    },
    {
        "question": "Existe alguma multa por perda do cartão-chave do quarto?",
        "ground_truth": "Sim, em caso de perda do cartão-chave, é cobrada uma taxa de substituição de R$ 20,00."
    },
    {
        "question": "Qual a distância entre o hotel e o aeroporto mais próximo?",
        "ground_truth": "O hotel está localizado a 12 km de distância do aeroporto, o que leva aproximadamente 25 minutos de carro."
    },
    {
        "question": "O hotel sugere algum aplicativo específico para transporte?",
        "ground_truth": "Sugerimos o uso de Uber, 99 ou InDriver, com ponto de embarque na entrada principal sob a marquise."
    },
    {
        "question": "O hotel oferece serviço de manobrista (Valet)?",
        "ground_truth": "Sim, dispomos de uma equipe de manobristas (Valet) para acomodar os veículos dos hóspedes."
    },
    {
        "question": "Até que horas o restaurante funciona para o jantar?",
        "ground_truth": "O restaurante funciona para o jantar até as 22h."
    },
    {
        "question": "O hotel aceita pagamentos em Dólar ou Euro?",
        "ground_truth": "O hotel aceita pagamentos em moedas correntes físicas do Brasil (Real/BRL), além de cartões e PIX."
    },
    {
        "question": "Como funciona a política de sustentabilidade em relação às toalhas?",
        "ground_truth": "Hóspedes que desejam participar do programa 'Hotel Verde' podem reutilizar toalhas deixando-as penduradas no toalheiro."
    },
    {
        "question": "Qual o ramal para entrar em contato com a equipe de limpeza?",
        "ground_truth": "Para serviços de limpeza ou arrumação, o hóspede deve discar o ramal 105."
    },
    {
        "question": "O serviço de quarto (Room Service) funciona de madrugada?",
        "ground_truth": "Sim, o serviço de quarto está disponível 24 horas por dia com cardápio acessível no quarto ou via app."
    },
    {
        "question": "O Wi-Fi abrange as áreas de lazer como a piscina?",
        "ground_truth": "Sim, oferecemos Wi-Fi gratuito em todo o perímetro do hotel, incluindo piscinas, restaurantes e quartos."
    },
    {
        "question": "O que devo fazer se tiver problemas com a conexão de internet?",
        "ground_truth": "O suporte para conexão Wi-Fi está disponível 24 horas por dia através da recepção."
    },
    {
        "question": "É possível fazer o check-out após as 12h?",
        "ground_truth": "Sim, dependendo da disponibilidade, mas está sujeito a taxas de 'late check-out'. Consulte a recepção."
    },
    {
        "question": "O café da manhã é cobrado para quem não tem reserva com pensão completa?",
        "ground_truth": "Para quem não possui o café incluso na reserva, cobra-se uma taxa de R$ 55,00 por pessoa na portaria."
    },
    {
        "question": "O hotel fica perto de algum museu?",
        "ground_truth": "Sim, o Museu Central está localizado a apenas 2 km do hotel."
    },
    {
        "question": "Quanto custa o serviço de lavanderia urgente?",
        "ground_truth": "A lavanderia urgente custa R$ 50,00 por peça, com entrega em até 6 horas (Seg-Sáb até 18h)."
    },
    {
        "question": "Quais são os principais pontos turísticos perto do hotel?",
        "ground_truth": "Os pontos turísticos mais próximos são o Museu Central (2 km) e o Parque Verde com pista de caminhada (1,2 km)."
    },
    {
        "question": "Posso contratar uma massagem relaxante no hotel?",
        "ground_truth": "Sim, oferecemos massagem relaxante com aromaterapia por R$ 150,00 a hora, mediante agendamento das 09h às 21h."
    }
]
