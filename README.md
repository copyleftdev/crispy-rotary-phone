
# Spring Boot Fuzzing Tool(crispy-rotary-phone)

A simple yet efficient tool for fuzzing Spring Boot servers to discover valid routes. This tool first checks if the target host is a Spring Boot server and then proceeds to fuzz it using the routes provided in a file.

## Features
- Detection of Spring Boot servers using specific HTTP headers.
- Multi-threading support for faster fuzzing.
- Command Line Interface for easy usage.

## Prerequisites
- Python 3
- `requests` library (You can install it using `pip install requests`)

## Usage

1. First, clone the repository or download the script.
2. Make sure you have a `routes.txt` file with potential routes, one per line.
3. Run the script using the following command:

```bash
python script_name.py <TARGET_HOST> --workers <WORKER_COUNT>
```

Replace `script_name.py` with the actual name of the script. `<TARGET_HOST>` should be the host you want to target, and `<WORKER_COUNT>` is the number of threads/workers you want to utilize (default is 10).

Example:
```bash
python spring_fuzzer.py http://example.com --workers 15
```

## Important Notes
- Always ensure you have proper authorization before fuzzing a server. Unauthorized scanning and fuzzing might be illegal and unethical.
- Adjust the number of workers based on your machine's capabilities and network conditions. Using an extremely high number of workers might lead to false negatives due to rate limiting or other issues.

## Contribution
Feel free to contribute to this project by submitting pull requests or issues.

## License
This project is open-source. Please ensure you respect all legal and ethical guidelines when using or modifying it.
