[![](https://images.microbadger.com/badges/image/goliasz/snowplow-webhook.svg)](https://microbadger.com/images/goliasz/snowplow-webhook "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/goliasz/snowplow-webhook.svg)](https://microbadger.com/images/goliasz/snowplow-webhook "Get your own version badge on microbadger.com")

# snowplow-webhook

Generic webhook based on python tracker

# Sample Docker RUN

```
$ docker run -d --name=spwh --hostname=spwh -p 0.0.0.0:5000:5000 -e SP_COLLECTOR_URI=example.com -e SP_COLLECTOR_PROTOCOL=https -e SP_COLLECTOR_PORT=443 -e SP_COLLECTOR_METHOD=post goliasz/snowplow-webhook
```

# Sample POST

```
curl -X POST http://localhost:5000/api/v1.0/sp --header "Content-Type:application/json" -d '{"i_app_id":"test","i_user_id":"user0","i_language":"en","i_ip":"127.0.0.1","i_user_agent":"bubu","test1":"test1"}'
```

# License
Apache License, Version 2.0
