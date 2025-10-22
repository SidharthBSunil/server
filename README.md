# server


server.py old program


serverwithgui.py it new program designed in today


```bash

sudo mkdir -p --mode=0755 /usr/share/keyrings
`````
```bash
curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null
`````

```bash
echo 'deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared any main' | sudo tee /etc/apt/sources.list.d/cloudflared.list
`````
```bash
sudo apt update && sudo apt install cloudflared -y
`````
