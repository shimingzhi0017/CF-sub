import requests

sources = {

    "移动优选": "https://raw.githubusercontent.com/DustinWin/BestCF/main/cmcc-ip.txt",

    "联通优选": "https://raw.githubusercontent.com/DustinWin/BestCF/main/cucc-ip.txt",

    "电信优选": "https://raw.githubusercontent.com/DustinWin/BestCF/main/ctcc-ip.txt",

    "CF优选域名": "https://raw.githubusercontent.com/DustinWin/BestCF/main/bestcf-domain.txt"
}

yaml = "proxies:\n\n"

for group, url in sources.items():

    try:

        data = requests.get(url).text.strip().split("\n")

        data = data[:5]

        for i, item in enumerate(data, start=1):

            yaml += f'''
  - name: {group}{i}

    type: vless

    server: {item}

    port: 2083

    uuid: 3384c36c-4b66-45f5-9990-736943f4b90a

    network: ws

    tls: true

    udp: true

    skip-cert-verify: true

    servername: shimingzhi0017.xyz

    client-fingerprint: chrome

    ws-opts:

      path: /ABCD1234

      headers:
        Host: shimingzhi0017.xyz

'''

    except Exception as e:

        print(e)

open("cf-proxies.yaml", "w", encoding="utf-8").write(yaml)

print("生成完成")
