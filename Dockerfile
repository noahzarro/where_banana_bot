FROM python:3.10
ADD main.py /
ADD arial.ttf /
ADD template.jpg /
ADD Ubuntu-Bold.ttf /
ADD requirements.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ] 