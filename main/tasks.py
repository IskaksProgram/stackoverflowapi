from django.core.mail import send_mail
from stackoverflowapi._celery import app

@app.task
def notify_user_task(email):
    send_mail(
        "Вы создали новый сапрос!", 
        "Спасибо за использоование нашего сайта!",
        "malimu1992@gmail.com"
        [email, ],
    )
    return  'sucess'





















