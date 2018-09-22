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
$ zappa update
```

### Requirements
```shell
python -V
```
Python 3.6
```shell
pip -V pip
```
pip 9.0.1  

### Append
#### Zappa
Webhook deployment to AWS lambda using [zappa](https://github.com/Miserlou/Zappa). Simpler than [serverless](https://serverless.com/) although no support for different serverless architectures.  

##### First time deployment  
1. Set up AWS configuration profile
```shell
pip install awscli --upgrade --user
aws configure
```
Introduce AWS keys

2. Set up zappa configuration profile
```shell
$ pip install zappa
$ zappa init
$ zappa deploy
```
Introduce deployment characteristics

##### Later updates
```shell
zappa update dev
```
#### Debugging
##### Flask
[Flask](http://flask.pocoo.org/) is the framework used for the API deployment.  

If process not closed properly by using <kbd>Ctrl</kbd> + <kbd>C</kbd>  
1. Locate the process running on that port:
```shell
fuser 8088/tcp
```
2. Kill the process:
```shell
fuser -k 8088/tcp
```

##### Ngrok
Debugging using [ngrok](https://ngrok.com/)
```shell
$ ./ngrok http 8088
```
#### Dialogflow
The NLP is done by Dialogflow.  

In particular, Dialogflow's V2 API is being used.  
A POST request is sent to dialogflow-backend.  

Checkout [webhook requirements](https://dialogflow.com/) for more info.
