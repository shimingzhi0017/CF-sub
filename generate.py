import requests

sources = {
    "移动优选": "https://github.com/DustinWin/BestCF/releases/latest/download/cmcc-ip.txt",
    "联通优选": "https://github.com/DustinWin/BestCF/releases/latest/download/cucc-ip.txt",
    "电信优选": "https://github.com/DustinWin/BestCF/releases/latest/download/ctcc-ip.txt",
    "CF优选域名": "https://github.com/DustinWin/BestCF/releases/latest/download/bestcf-domain.txt"
}

lines_out = ["proxies:"]

for group, url in sources.items():

    try:

        response = requests.get(url)

        lines = response.text.splitlines()

        count = 0

        for line in lines:

            line = line.strip()

            if not line:
                continue

            item = line.split("#")[0].split(",")[0].strip()

            count += 1

            proxy = f'''  - {{name: {group}{count}, server: {item}, port: 2083, type: vless, uuid: 3384c36c-4b66-45f5-9990-736943f4b90a, tls: true, skip-cert-verify: true, servername: shimingzhi0017.xyz, client-fingerprint: chrome, network: ws, ws-opts: {{path: /ABCD1234, headers: {{Host: shimingzhi0017.xyz}}}}, udp: true}}'''

            lines_out.append(proxy)

            if count >= 5:
                break

    except Exception as e:

        print(f"Error processing {group}: {e}")

with open("cf-proxies.yaml", "w", encoding="utf-8") as f:

    f.write("\n".join(lines_out))

print("生成完成")
