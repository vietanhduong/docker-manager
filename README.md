# Docker Manager
This simple project help you manage docker containers by using `Docker Daemon APIs`

Todo
----
* [ ] Support view log container
* [ ] Support UI 
* [ ] Write `test`

Run
----
With `docker`:
```bash
$ docker run vietanhs0817/docker-manager --expose 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock
```
With `docker-compose`:
```yaml
version: "3.7"

services:
    manager:
      image: vietanhs0817/docker-manager
      ports:
        - 5000:5000
      volumes:
        - /var/run/docker.sock:/var/run/docker.sock
```
```bash
$ docker-compose up
```

**NOTE: For more details go to `GET localhost:5000/api HTTP/1.1`**
