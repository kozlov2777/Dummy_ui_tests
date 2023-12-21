FROM mcr.microsoft.com/playwright/python:v1.40.0-focal

WORKDIR /Dummy_ui_tests

COPY . /Dummy_ui_tests

RUN pip install -r requirements.txt


CMD ["pytest", "--reruns", "5", "--alluredir=allure-results"]
