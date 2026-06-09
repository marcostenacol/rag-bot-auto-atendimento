from flask import Blueprint, request, jsonify
from libs.evo import EvoAPI
from bot.aiBot import AIBot
from bot.detectIntention import IntentionDetector
from bot.reservation.flow import handle_reservation_flow
from app.services.userService import get_user_by_contact, create_user
from app.services.messageHistoryService import get_last_messages_by_user, save_message
from app.services.preReservationStepService import get_active_pre_reservation_step

evo = EvoAPI()
ai_bot = AIBot()
intention = IntentionDetector()


webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/chatbot/webhook', methods=['POST'])
@webhook_bp.route('/chatbot/webhook/', methods=['POST'])
def webhook():
    data = request.json

    data_payload = data.get('data') if data else None
    if not data_payload:
        return jsonify({'status': 'failed', 'message': 'Dados Vazios.'}), 200

    remotejid = data_payload.get('key', {}).get('remoteJid')
    if not remotejid or '@' not in remotejid:
        return jsonify({'status': 'failed', 'message': 'remoteJid inválido.'}), 200

    received_message = data_payload.get('message', {}).get('conversation')
    if not received_message:
        return jsonify({'status': 'success', 'message': 'Mensagem não-texto ignorada.'}), 200

    instance = data.get('instance', {})
    apikey = data.get('apikey', {})
    received_number = remotejid.split("@")[0]
    sender_type = remotejid.split("@")[1]

    if sender_type in ['g.us', 'status@broadcast']:
        return jsonify({'status': 'success', 'message': 'Mensagem de grupo/status ignorada.'}), 200

    user = get_user_by_contact(received_number)

    if not user:
        user = create_user(name = data.get('data', {}).get('pushName', ''), contact = received_number)

    try:
        step = get_active_pre_reservation_step(user.id)
        if step:
            message = handle_reservation_flow(user, received_message)
        else:
            intention_type = intention.detect(received_message)
            if intention_type == "pre_reserva":
                message = handle_reservation_flow(user, received_message)
            else:
                history_messages = get_last_messages_by_user(user.id)
                message = ai_bot.invoke(
                    history_messages=history_messages,
                    question=received_message
                )

        evo.send_message(instance=instance,
                             apikey=apikey,
                             sender_number=received_number,
                             message=message)

        save_message(user_id = user.id, message=received_message, response = message)
    except Exception as e:
        print(f"[!] Erro ao processar a mensagem do usuário {received_number}: {e}")
        fallback_message = "Desculpe, tivemos um problema ao processar sua mensagem. Por favor, tente novamente em instantes."
        try:
            evo.send_message(instance=instance,
                                 apikey=apikey,
                                 sender_number=received_number,
                                 message=fallback_message)
        except Exception as send_error:
            print(f"[!] Falha ao enviar mensagem de fallback: {send_error}")
        return jsonify({'status': 'failed', 'message': 'Erro interno tratado.'}), 200

    return jsonify({'status': 'success'}), 200