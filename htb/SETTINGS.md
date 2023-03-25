Parret OS by Docker
--------

https://hub.docker.com/r/parrotsec/security

### 停止時にコンテナを削除する場合
  
```
sudo docker run --rm --name htb \
  --network host --cap-add=NET_ADMIN --device=/dev/net/tun \
  -ti -v $PWD/work:/work parrotsec/security
```

### コンテナを残す場合

```
sudo docker run --name htb \
  --network host --cap-add=NET_ADMIN --device=/dev/net/tun \
  -v $PWD/work:/work -ti parrotsec/security

### 停止
sudo docker stop htb

### 起動
sudo docker start htb

### bashでコンテナ操作
sudo docker exec -ti  htb bin/bash
```

### 特定ポートを開ける

```
sudo docker run --rm -p 8080:80 -ti parrotsec/security
```