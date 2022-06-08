@echo off

call %~dp0.repose3\Scripts\activate

cd %~dp0\Education_02_Telegram Bot

set TOKEN=5404436374:AAFwSx1GU7GQGPAG-sLjtyJ1zxhcOoVVv2c

python ibot.py

pause