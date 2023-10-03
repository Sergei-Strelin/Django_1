import logging

from django.http import HttpResponse

# from django.shortcuts import render


logger = logging.getLogger(__name__)

headers = {'Cache-Control': 'no-cache, must-revalidate',
           'Pragma': 'no-cache'}


def main(request):
    body = """
    <title>Главная страница</title>
    <body>
        <div>
            <h1>Главная страница</h1>
            <p>Содержимое главной страницы</p>
            <p>Перейдите на страницу: /sergey</p>
        </div>
        <footer>
            <div>
                <p>Copyright &copy;
                    <script type="text/javascript"> document.write(new Date().getFullYear());</script>
                    Communications Inc. Все права защищены.
                </p>
            </div>
        </footer>
    </body>
    """
    logger.info(f'Страница открыта: {body}')
    return HttpResponse(body, charset="utf-8", headers=headers)


def sergey(request):
    body = """
        <title>О себе</title>  
        <body>     
            <div>
                <h1>Стрелин Сергей Алексеевич</h1>
                <p>Мужчина, 37 лет, родился 08 июня 1986</p>
                <p>Перейдите на страницу: /main</p>
            </div>
            <footer>
                <div>
                    <p>Copyright &copy;
                        <script type="text/javascript"> document.write(new Date().getFullYear());</script>
                        Communications Inc. Все права защищены.
                    </p>
                </div>
            </footer>
        </body>
        """
    logger.info(f'Страница открыта: {body}')
    return HttpResponse(body, charset="utf-8", headers=headers)