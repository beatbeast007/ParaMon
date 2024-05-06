import os
import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time

print("""
\033[91m██████╗  █████╗ ██████╗  █████╗ ███╗   ███╗ ██████╗ ███╗   ██╗\033[91m
\033[91m██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗ ████║██╔═══██╗████╗  ██║\033[91m
\033[91m██████╔╝███████║██████╔╝███████║██╔████╔██║██║   ██║██╔██╗ ██║\033[91m
\033[91m██╔═══╝ ██╔══██║██╔══██╗██╔══██║██║╚██╔╝██║██║   ██║██║╚██╗██║\033[91m
\033[91m██║     ██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║╚██████╔╝██║ ╚████║\033[91m
\033[91m╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\033[91m

\033[35mv1.0 \033[0m 𝙈𝙖𝙙𝙚 𝙬𝙞𝙩𝙝 ❤️ 𝙗𝙮\033[91m 𝘽𝙀𝘼𝙎𝙏\033[91m 

""")

THREADS = 2

def extract_parameters(url, wordlist=None):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text

            # Extract parameters using multiple heuristic techniques
            regex_patterns = [
                # Standard query parameters
                r'[?&]([a-zA-Z0-9_-]+)=[^&]+',
                # Parameters within JavaScript code
                r'(?<=\?|\&)([a-zA-Z0-9_-]+)\s*:\s*\'[^&]+\'',
                # Parameters within HTML form actions
                r'<form [^>]*action=[\'"]?[^\'"\s>]+[\'"]?[^>]*>',
                r'name=["\']?([a-zA-Z0-9_-]+)["\']?',
            ]

            parameters = set()
            for pattern in regex_patterns:
                matches = re.findall(pattern, html_content)
                parameters.update(matches)

            # Filter out blocked keywords and results containing <form action=
            parameters = {param for param in parameters if "viewport" not in param.lower()}
            parameters = {param for param in parameters if not param.startswith("<form ")}

            # If wordlist is provided, filter parameters based on wordlist
            if wordlist:
                parameters = {param for param in parameters if param in wordlist}

            # Print potential parameters
            if parameters:
                result = []
                result.append("\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8mPotential parameters found on the website:\033[0m")
                for param in parameters:
                    result.append(param)
                result.append("\n\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8mVerifying parameters...\033[0m")
                with ThreadPoolExecutor(max_workers=THREADS) as executor:
                    futures = [executor.submit(verify_parameter, url, param) for param in parameters]
                    for future in futures:
                        result.append(future.result())
                return result
            else:
                return ["\033[91m\033[1m(+)\033[0m No parameters found on the website."]
        else:
            return [f"\033[91m\033[1m(+)\033[0m Failed to fetch URL. Status code: {response.status_code}"]
    except Exception as e:
        return [f"\033[91m\033[1m(+)\033[0m An error occurred: {str(e)}"]

def verify_parameter(base_url, param):
    try:
        url = base_url + "?" + param
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            # You can add more verification logic here based on the HTML content
            # For simplicity, let's just check if the word "error" appears in the HTML content
            if "error" not in html_content.lower():
                return f"Verified: \033[94m{param}\033[0m is a true parameter"
            else:
                return f"\033[91mFalse Positive: {param} is not a true parameter\033[0m"
        else:
            return f"Failed to fetch URL {url}. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred while verifying parameter {param}: {str(e)}"

def main():
    url = prompt_for_url()
    urls = []
    if os.path.isfile(url):
        urls = read_urls_from_file(url)
    else:
        urls.append(url)

    for url in urls:
        print(f"\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8m\033[1mScanning URL: {url}\033[0m")

        THREADS = prompt_for_threads()
        USE_WORDLIST = prompt_for_wordlist()
        wordlist = None
        if USE_WORDLIST:
            wordlist_file = input("\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8m\033[1mEnter the path to the wordlist file:\033[0m ")
            if os.path.isfile(wordlist_file):
                with open(wordlist_file, 'r') as f:
                    wordlist = set(f.read().splitlines())
            else:
                print("\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8m\033[1mInvalid file path. Using default parameter extraction method.\033[0m")
        
        SAVE_OUTPUT = prompt_for_output()
        if SAVE_OUTPUT:
            default_output_path = f"URL_{urlparse(url).netloc}.txt"
            output_file = input("\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8m\033[1mEnter the path to save the output file (Press Enter to save here): \033[0m")
            if not output_file:
                output_file = default_output_path

        DELAY = prompt_for_delay()

        scan_results = extract_parameters(url, wordlist)
        for line in scan_results:
            if "Verified:" in line:
                param, status = line.split(" is ")
                print(f"\033[94m{param}\033[0m is {status}")
            else:
                print(line)
        
        if SAVE_OUTPUT:
            with open(output_file, 'w') as f:
                for line in scan_results:
                    f.write(line + "\n")
            print(f"\033[1m\033[92mResult saved in the '{output_file}' file.\033[0m")

        time.sleep(DELAY)

def prompt_for_url():
    return input("\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8m\033[1mEnter the target URL or mention the file name containing URLs:\033[0m ")

def prompt_for_threads():
    threads = input("\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8m\033[1mEnter the number of threads (1 to 10 / def 2):\033[0m ")
    return int(threads) if threads else 2

def prompt_for_wordlist():
    use_wordlist = input("\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8m\033[1mDo you want to use a wordlist? (y/N):\033[0m ").lower()
    return use_wordlist == 'y'

def prompt_for_output():
    save_output = input("\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8m\033[1mDo you want to save the output to a file? (y/N):\033[0m ").lower()
    return save_output == 'y'

def prompt_for_delay():
    custom_delay = input("\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8m\033[1mDo you want to set a custom time delay? (1 to 20 / def 2):\033[0m ").lower()
    if custom_delay == 'y':
        delay = input("\033[91m\033[1m(+)\033[0m \033[38;2;101;254;8m\033[1mEnter the custom time delay in seconds (1-20): \033[0m")
        return int(delay) if delay.isdigit() and 1 <= int(delay) <= 20 else 2
    else:
        return 2

def read_urls_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
            return [url.strip() for url in urls]
    except Exception as e:
        print(f"An error occurred while reading URLs from file: {str(e)}")
        return []


if __name__ == "__main__":
    main()
