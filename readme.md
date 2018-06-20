# Alda backend

Repository containing Alda's dailogflow webhook

## Website:
* Find out more at [alda.bot](https://alda.bot)

### Requirements
```shell
python -V
```
Python3.6
```shell
pip -V pip
```
pip 9.0.1  

```shell
$ pip install -r requirements.txt
```
### Deployment
#### Zappa
Webhook deployment to AWS lambda using [zappa](https://github.com/Miserlou/Zappa). Simpler than [serverless](https://serverless.com/) although it does not support different serverless architectures.  

##### First time deployment  
1. Set up AWS configuration profile
```shell
pip install awscli --upgrade --user
aws configure
```
2. Set up zappa configuration profile

```shell
$ pip install zappa
$ zappa init
$ zappa deploy
```

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
