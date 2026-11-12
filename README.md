# Vulnerability Assessment of Web Applications (Week 5 - Task 2)

## Overview
This repository contains the deliverables for **Week 5 - Task 2** of the Cyber Security Internship. The assessment focuses on identifying, exploiting (Proof-of-Concept), and documenting common OWASP Top 10 web vulnerabilities—specifically SQL Injection (SQLi), Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF)—on a controlled test environment.

## Repository Structure
* `docs/Web_Vulnerability_Assessment_Report.md` - Complete vulnerability assessment report with severity ratings, impact analysis, and remediation steps.
* `poc/exploits_and_payloads.txt` - Proof-of-Concept (PoC) payloads, HTTP requests, and reproduction steps for each finding.
* `scripts/header_security_check.py` - Python script to audit missing HTTP security headers on target web applications.

## Tools & Environment Used
* **Target Application:** OWASP Juice Shop / DVWA (Localhost Lab)
* **Scanning & Interception:** OWASP ZAP, Burp Suite Community Edition
* **Scripting:** Python 3 (`requests` library)
