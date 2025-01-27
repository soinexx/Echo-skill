import json
from scenarios import handle_dialog

def handle_request(event, context):
    """
    Основная функция, которую вызывает Яндекс.Cloud Function.
    :param event: dict, входящие данные (JSON) от Яндекс Диалогов.
    :param context: объект с данными окружения Cloud Functions.
    :return: dict, ответ для Яндекс Диалогов.
    """
    # Здесь "event" — это тот самый JSON, который Алиса передаёт навыку.
    # 1. Извлекаем данные запроса
    request = event.get('request', {})
    session = event.get('session', {})
    state = event.get('state', {})
    
    # 2. Вызываем функцию из сценария, которая вернёт нам готовый ответ
    response_body = handle_dialog(request, session, state)

    # 3. Возвращаем JSON-ответ
    return response_body

def handler(event, context):
    """
    Обёртка для удобства:
    в Яндекс.Cloud Function в настройках entrypoint указываем my_skill.main.handler
    """
    return handle_request(event, context)