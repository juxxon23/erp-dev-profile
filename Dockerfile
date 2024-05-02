FROM python

WORKDIR /home/app

COPY . .

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]