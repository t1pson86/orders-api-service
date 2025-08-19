# Order Service (FastAPI)

A microservice for processing orders. Accepts requests to create/update orders and sends notifications to the RabbitMQ queue.

## 🛠 Technologies
- Python 3.10+
- FastAPI
- RabbitMQ (pika or aio-pika)
- FastStream

## 📦 Installation
1. Clone the repository:
    ```bash
   git clone https://github.com/t1pson86/order-service.git
     ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Interacting with other services
Sends messages to RabbitMQ in the following format:

```json
{
  "text": "order_name"
}
```

## 📌 Related repositories

[Notification Service (Aiogram)](https://github.com/t1pson86/telegram-notification-service) — receives events from RabbitMQ and sends notifications to Telegram.

<div align="center"> <sub>Built with ❤️ for professional FastAPI projects.</sub> </div>