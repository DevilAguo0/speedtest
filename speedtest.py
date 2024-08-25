# speedtest_script.py

import subprocess
import json

def run_speedtest():
    try:
        # 执行 speedtest-cli 命令并获取 JSON 输出
        result = subprocess.run(['speedtest', '--json'], capture_output=True, text=True, check=True)
        # 解析 JSON 数据
        data = json.loads(result.stdout)
        
        # 提取并打印结果
        print(f"Download Speed: {data['download'] / 1_000_000:.2f} Mbps")
        print(f"Upload Speed: {data['upload'] / 1_000_000:.2f} Mbps")
        print(f"Latency: {data['latency']} ms")
        print(f"Server: {data['server']['name']}, {data['server']['location']}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running speedtest-cli: {e}")
    except json.JSONDecodeError as e:
        print(f"Failed to parse speedtest-cli output: {e}")

if __name__ == "__main__":
    run_speedtest()
