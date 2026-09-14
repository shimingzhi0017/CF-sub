import requests

sources = {
    "移动优选": "https://github.com/DustinWin/BestCF/releases/latest/download/cmcc-ip.txt",
    "联通优选": "https://github.com/DustinWin/BestCF/releases/latest/download/cucc-ip.txt",
    "电信优选": "https://github.com/DustinWin/BestCF/releases/latest/download/ctcc-ip.txt",
    "CF优选域名": "https://github.com/DustinWin/BestCF/releases/latest/download/bestcf-domain.txt"
}

yaml_content = "proxies:\n"

for group, url in sources.items():

    try:

        response = requests.get(url)

        lines = response.text.splitlines()

        count = 0

        for line in lines:

            line = line.strip()

            if not line:
                continue

            # 去掉 # 后面的备注
            item = line.split("#")[0].split(",")[0].strip()

            count += 1

            yaml_content += f"""
  - name: {group}{count}
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
"""

            if count >= 5:
                break

    except Exception as e:

        print(f"Error processing {group}: {e}")

with open("cf-proxies.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_content)

print("生成完成")
