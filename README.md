# honeygain-claim-honeypot
Automatically claim the daily honeypot  
There is a crontab that will run the included python script at 10pm.

## Environment Variables

|Name           |Value           |Optional |
|---------------|----------------|---------|
|JWT_TOKEN      |Your token      |No       |
|DISCORD_WEBHOOK|Your webhook url|Yes      |

## Example
docker run --name honeygain-daily -d  -e JWT_TOKEN=<-!your token!-> -e DISCORD_WEBHOOK=<-!channel webhook!-> arnesteinbach/honeygain-claim-honeypot

[https://hub.docker.com/r/arnesteinbach/honeygain-claim-honeypot](https://hub.docker.com/r/arnesteinbach/honeygain-claim-honeypot)
