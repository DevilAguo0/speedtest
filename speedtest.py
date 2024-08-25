import subprocess
import json
import datetime

def run_speedtest():
    try:
        result = subprocess.run(['speedtest', '--json'], capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        print(f"Download Speed: {data['download'] / 1_000_000:.2f} Mbps")
        print(f"Upload Speed: {data['upload'] / 1_000_000:.2f} Mbps")
        print(f"Latency: {data['latency']} ms")
        print(f"Server: {data['server']['name']}, {data['server']['location']}")
    except Exception as e:
        print(f"Speedtest error: {e}")

def run_iperf3(server_ip, duration):
    try:
        result = subprocess.run(['iperf3', '-c', server_ip, '-t', str(duration)], capture_output=True, text=True, check=True)
        print(result.stdout)
    except Exception as e:
        print(f"iPerf3 error: {e}")

def run_mtr(target):
    try:
        result = subprocess.run(['mtr', '--report', '--report-cycles', '1', target], capture_output=True, text=True, check=True)
        print(result.stdout)
    except Exception as e:
        print(f"MTR error: {e}")

def monitor_bandwidth():
    try:
        subprocess.run(['bmon'], check=True)
    except Exception as e:
        print(f"bmon error: {e}")

def log_results(filename, data):
    with open(filename, 'a') as file:
        file.write(f"{datetime.datetime.now()}: {data}\n")

if __name__ == "__main__":
    # Run tests
    run_speedtest()
    run_iperf3('server_ip_here', 10)  # Replace with actual server IP and duration
    run_mtr('target_ip_here')  # Replace with actual target IP
    monitor_bandwidth()  # Real-time monitoring

    # Example of logging
    log_results('test_results.log', 'Example log entry')
