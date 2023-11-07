import pika
import json
 
# Создаём подключение к серверу на локальном хосте
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
 
# Объявляем очередь y_true
channel.queue_declare(queue='y_true')
# Объявляем очередь y_pred
channel.queue_declare(queue='y_pred')
 
# Создаём функцию callback для обработки данных из очереди
def callback(ch, method, properties, body):
    print(f'Из очереди {method.routing_key} получено значение {json.loads(body)}')
 
# Извлекаем сообщение из очереди y_true
channel.basic_consume(
    queue='y_true',
    on_message_callback=callback,
    auto_ack=True
)
# Извлекаем сообщение из очереди y_pred
channel.basic_consume(
    queue='y_pred',
    on_message_callback=callback,
    auto_ack=True
)
 
# Запускаем режим ожидания прихода сообщений
print('...Ожидание сообщений, для выхода нажмите CTRL+C')
channel.start_consuming()