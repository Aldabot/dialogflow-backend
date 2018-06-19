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
Debugging using [ngrok](https://ngrok.com/)

```shell
$ ./ngrok http 8088
```
#### Dialogflow
Dialogflow's V2 API is being used.  
A POST request is sent to dialogflow-backend.  

Checkout [webhook requirements](https://dialogflow.com/) for more info.  
