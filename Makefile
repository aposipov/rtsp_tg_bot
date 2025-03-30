IMAGE_NAME = rtsp_tg_bot
CONT_NAME = rtsptg_cont

all:
		@echo "build and run"

build:
		docker build -t ${IMAGE_NAME} .

run:	build
		docker run --name ${CONT_NAME} -v $(PWD)/core_bot/data:/bot/data \
		-d --restart=unless-stopped ${IMAGE_NAME}

stop:
		docker stop ${CONT_NAME}

rm:
		docker container rm ${CONT_NAME}
		docker image rm ${IMAGE_NAME}:latest

rmi:
		docker image rm ${IMAGE_NAME}:latest

restart: stop rm run

clean: stop rm

start:
		python3 core_bot/main.py

test:
		pytest -v
