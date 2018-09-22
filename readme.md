# Alda backend

This is the project containing Alda's dialogflow webhook.

## Website:
* Find out more at [alda.bot](https://alda.bot)

## Development Steps
1. Activate Virtual Environment
```
source venv/bin/activate
```
2. Install requirements if required
```
pip install -r requirements.txt
```
3. Start application
```
python main.py
```
4. Make the app url public by using [ngrok](https://ngrok.com/)
```
$ ./ngrok http 8088
```
5. Make changes and debug when required

6. Deploy by using [zappa](https://github.com/Miserlou/Zappa)
```
$ zappa init
$ zappa deploy
```
