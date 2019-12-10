# Docker Manager
This simple project help you manage docker containers by using `Docker Daemon APIs`

Todo
----
* [x] Support events change
* [x] Support view log container
* [ ] Support UI 
* [ ] Write `test`
* [x] Support view log `TTY` container
* [x] Inspect container 

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

Kubernetes
----
Just for fun. You can try my config :)

```yaml
apiVersion: apps/v1beta1
kind: Deployment
metadata:
 name: docker-manager
 labels:
   app: docker-manager
spec:
 replicas: 1
 template:
    metadata:
      labels:
        app: docker-manager
    spec:
      containers:
      - name: docker-manager
        image: vietanhs0817/docker-manager:latest
        ports:
          - containerPort: 5000
        volumeMounts:
        - name: dockersock
          mountPath: "/var/run/docker.sock"
      volumes:
      - name: dockersock
        hostPath:
          path: /var/run/docker.sock
---
kind: Service
apiVersion: v1
metadata:
  name: docker-manager-service
spec:
  ports:
    - name: http
      port: 5000
  selector:
    app: docker-manager
```

**NOTE: For more details go to `GET localhost:5000/api HTTP/1.1`**
