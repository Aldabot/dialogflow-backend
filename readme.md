# Alda backend

This is the project containing Alda's webhook

## Website:
* Find out more at [alda.bot](https://alda.bot)

### Instructions
#### Deployment
Webhook deployment with [zappa](https://github.com/Miserlou/Zappa)

```shell
$ zappa init
$ zappa deploy
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
