FROM python:3.13
WORKDIR /OSpy
COPY ./TTP.py /OSpy
CMD [ "python", "./TTP.py" ]
