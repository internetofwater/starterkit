# Installation

Installation takes 3 steps.

0. Server Requirements
1. Install docker
2. (Optional) Install caddy
3. Install GET-IT

## 0. Verify server requirements

Minimum requirements are:

- 16 GB RAM
- 4-core CPU
- 50GB disk space

## 1. Install docker and docker-compose

## 2. Install caddy

### 2.1 Install Go
```
sudo apt-get update
sudo apt-get -y upgrade
wget https://dl.google.com/go/go1.14.linux-amd64.tar.gz
sudo tar -xvf go1.14.linux-amd64.tar.gz
sudo mv go /usr/local
```

### 2.2 build Caddy from source
```
git clone -b v2 "https://github.com/caddyserver/caddy.git"
cd caddy/cmd/caddy/
go build
```

### 2.3 Install caddy binary you just built

```
sudo mv caddy /usr/bin/
caddy version
groupadd --system caddy
useradd --system \
	--gid caddy \
	--create-home \
	--home-dir /var/lib/caddy \
	--shell /usr/sbin/nologin \
	--comment "Caddy web server" \
	caddy
  
cd /etc/systemd/system
wget https://github.com/caddyserver/dist/blob/master/init/caddy.service

sudo systemctl daemon-reload
sudo systemctl enable caddy
sudo systemctl start caddy
systemctl status caddy
```
### 
