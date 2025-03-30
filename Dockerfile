FROM python:3.12

WORKDIR /bot

COPY core_bot .

RUN rm -rf /etc/localtime &&  \
    ln -s /usr/share/zoneinfo/Asia/Vladivostok /etc/localtime && \
    echo "Asia/Vladivostok" > /etc/timezone

RUN apt update && apt install -y ffmpeg

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py" ]