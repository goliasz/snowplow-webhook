
# snowplow-webhook

## Sample Docker RUN

```
$ docker run -d --name=spwh --hostname=spwh -p 0.0.0.0:5000:5000 -e SP_COLLECTOR_URI=rbox24.com -e SP_COLLECTOR_PROTOCOL=https -e SP_COLLECTOR_PORT=444 -e SP_COLLECTOR_METHOD=post goliasz/snowplow-webhook
```

# License
Apache License, Version 2.0
