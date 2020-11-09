FROM python:3.8-slim

LABEL DESCRIPTION="Pedigree file maker service"
LABEL VERSION="v0.0.1"

COPY rerunner/requirements.txt rerunner/README.md rerunner/setup.cfg rerunner/setup.py utils/wait-for-it.sh /rerunner/
COPY rerunner/app /rerunner/app/
WORKDIR /rerunner

RUN apt-get update &&                                   \
    apt-get upgrade -y &&                               \
    apt-get install -y python3-pip python3-setuptools   \
    python3-wheel curl ssh &&                           \
    pip install --no-cache-dir                          \
        --requirement requirements.txt                  \
         &&                                             \
    # clean up                                          \
    rm -rf /var/lib/apt/lists/*

ENV FLASK_APP="app"
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
