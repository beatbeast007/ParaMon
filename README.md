
#  ParaMon


## Table of Contents 

- Introduction
- Features
- Installation
- Usage
- Options
- Examples
- Contributing
- License
## Introduction

ParaMon is a Python script designed to scan URLs and identify potential parameters present in the query string or HTML forms. It provides a convenient way to discover and verify parameters on websites, aiding in security testing and web application analysis.
## Features

- **URL Scanning:** Scan single or multiple URLs to identify potential parameters.
- **Parameter Extraction:** Use multiple heuristic techniques to extract parameters from query strings and HTML forms.
- **Parameter Verification:** Verify extracted parameters to distinguish true parameters from false positives.
- **Wordlist Support:** Optionally use a wordlist to filter parameters based on predefined keywords.
- **Output Saving:** Save scan results to a file for further analysis or documentation.
- **Multi threading:** Adjustable number of threads for concurrent processing.
- **Time delay:** Offers to set a custom time delay between requests, providing flexibility in adjusting scan speed.
- **Error Handling:** Handles errors gracefully, including failed URL fetching and verification errors.

## Installation

1. Clone the repository:

```bash
  git clone https://github.com/beatbeast007/ParaMon.git
```
2. Navigate to the project directory:
```bash
  cd ParaMon
```
3. Install dependencies:
```bash
  pip install -r requirements.txt
```
## Usage
To scan a URL:


```bash
  python paramon.py
```
Follow the prompts to enter the target URL, choose options, and view the scan results.
## Options

- **Number of Threads:** Choose the number of threads for concurrent scanning.
- **Wordlist Usage:** Specify whether to use a wordlist to filter parameters.
- **Output Saving:** Choose whether to save scan results to a file.
- **Custom Time Delay:** Set a custom time delay between scans.
## Examples

Scan a single URL:

![image](https://github.com/beatbeast007/ParaMon/assets/82287046/2faf7b52-e66f-44c0-86de-21eb3217114c)


Scan multiple URLs from a file:

![image](https://github.com/beatbeast007/ParaMon/assets/82287046/0be76dd9-c459-43a9-ad02-4d87c4bd30b3)


Scan with specific threads:

![image](https://github.com/beatbeast007/ParaMon/assets/82287046/d9100570-e7e2-48b6-8bfd-178a974a983a)


Scan using a wordlist:

![image](https://github.com/beatbeast007/ParaMon/assets/82287046/8c29ff65-90b6-4ee8-bc0f-bc8a5821a878)


Scan with specific time delay:

![image](https://github.com/beatbeast007/ParaMon/assets/82287046/24ac56e8-a362-4ce0-bdce-b6bee75d44e4)


Save output to a file:

![image](https://github.com/beatbeast007/ParaMon/assets/82287046/612c7edb-6da5-4291-83f7-effc5b20bb0f)


## Contributing

Contributions are welcome! If you'd like to contribute to ParaMon, please follow these steps:

1. Fork the repository.

2. Create a new branch (git checkout -b feature/your-feature-name).Make your changes.

3. Commit your changes (git commit -am 'Add new feature').

4. Push to the branch (git push origin feature/your-feature-name).

5. Create a new Pull Request.
## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/beatbeast007/ParaMon/blob/main/LICENSE) file for details
## 
Feel free to further customize this README.md as needed for your project!

