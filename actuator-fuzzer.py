import requests
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed


def check_if_spring_boot_server(host):
    try:
        req = requests.get(host, timeout=5)
        if 'X-Application-Context' in req.headers and 'Apache-Coyote' in req.headers['X-Application-Context']:
            return True
        return False
    except requests.RequestException:
        print(f"Error connecting to {host}")
        return False


def fuzz_single_route(host, route):
    try:
        req = requests.get(f'{host}/{route.strip()}', timeout=5)
        if req.status_code == 200:
            return f'{host}/{route} is a valid url + path'
    except requests.RequestException:
        pass
    return None


def fuzz_spring_server(host, workers):
    if check_if_spring_boot_server(host):
        with ThreadPoolExecutor(max_workers=workers) as executor, open('routes.txt', 'r') as routes:
            futures = [executor.submit(fuzz_single_route, host, route) for route in routes]

            for future in as_completed(futures):
                result = future.result()
                if result:
                    print(result)
    else:
        print("Target is not a spring-boot resource")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fuzz a Spring Boot server.')
    parser.add_argument('host', type=str, help='The host to target.')
    parser.add_argument('--workers', type=int, default=10, help='Number of workers for multi-threading.')

    args = parser.parse_args()

    fuzz_spring_server(args.host, args.workers)
