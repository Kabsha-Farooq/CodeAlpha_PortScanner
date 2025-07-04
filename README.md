# CodeAlpha_PortScanner

## Port Scanner Tool - Cyber Security Internship Task 3

This is a basic port scanner script written in Python. It scans a target IP or domain for open TCP ports within a specified range.

### Technologies Used
- Python 3
- socket module (built-in)

### How It Works
- Takes a target IP address or domain as input
- Scans ports from 1 to 100 (can be increased)
- Prints which ports are open
- Uses socket connection to test availability

### Setup Instructions

1. No external libraries required.

2. Run the Script

```bash
python port_scanner.py
```

3. When prompted:

```bash
Enter target IP or domain: scanme.nmap.org
```

4. Output will show open ports, like:

```
Port 22 is OPEN
Port 80 is OPEN
```

Note: This script is for educational and ethical testing only. Do not use it for scanning unauthorized systems.

---

### Author

Kabsha Farooq  
LinkedIn: https://www.linkedin.com/in/kabsha-farooq-27218030a/

This project was completed as part of the CodeAlpha Cyber Security Internship.
