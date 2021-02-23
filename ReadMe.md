**Crypto Tracking Twitter Bot**

This is my code for a Twitter bot that tweets out current exchange volumes hourly,
and current cryptocurrency prices with their percent change vs their "opening price" (price at midnight) every 15 minutes.
It also tracks Elon Musk's Twitter to see if any of his tweets mention a certain 
crypto asset. If it does, the bot will tweet out a link of that certain crypto's stock on Coindesk so one can monitor
its price fluctuation and to see how much he influences the price. 

In order to keep this bot up and running 24/7 I built a Docker Image with my code and then deployed
the image on an Amazon AWS EC2 VM instance.


**API's Used**

[Tweepy](https://www.coinapi.io/)                                       
[CoinAPI](https://docs.coinapi.io/#md-docs)
