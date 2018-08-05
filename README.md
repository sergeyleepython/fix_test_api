API testing
=========
Tests and tests results for https://reqres.in/

## REQUIREMENTS
Python 3.6

Python dependencies:
* pytest==3.7.1
* allure-pytest==2.5.0
* requests==2.19.1
* requests-toolbelt==0.8.0

Allure tool (https://docs.qameta.io/allure/2.0/)

## LAUNCHING
py.test -s -v --testing-stand=DEV

py.test --alluredir reports

allure serve reports


