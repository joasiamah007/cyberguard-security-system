# CYBERGUARD v1.0 - Personal Account Security Monitoring System

print("========================================")
print("            CYBERGUARD v1.0")
print("     PERSONAL SECURITY MONITORING SYSTEM")
print("========================================")
print()
print("Welcome, Security Analyst!")
print()
print("Your mission is to monitor account")
print("information and identify potential threats.")
print()
print("Starting security assessment...")
print()

#  User information collection
username = str(input("Enter username: "))
email = str(input("Enter email address: "))
password = str(input("Enter password: "))
age = int(input("Enter age: "))
ip_address = str(input("Enter IP address: "))
failed_attempts = int(input("Enter failed login attempts: "))
status_input = str(input("Is the account Active or Inactive? "))

# Convert account status to Boolean using if/else
if status_input == "Active" or status_input == "active" or status_input == "ACTIVE":
    is_active = True
    status_label = "ACTIVE"
else:
    is_active = False
    status_label = "INACTIVE"

# Demonstrate type() on collected values
print("Checked types -> username:", type(username), "| age:", type(age), "| failed_attempts:", type(failed_attempts), "| is_active:", type(is_active))
print()

# Feature 4: Password strength checker (based on length)
password_length = len(password)
if password_length < 8:
    password_assessment = "WEAK"
    password_message = "Weak password (fewer than 8 characters)."
else:
    if password_length < 12:
        password_assessment = "MODERATE"
        password_message = "Moderate password (8 to 11 characters)."
    else:
        password_assessment = "STRONG"
        password_message = "Strong password (12 or more characters)."

print("Password Check:", password_message)
print()

# Feature 3: Security threat detection
threat_line_1 = ""
threat_line_2 = ""
threat_line_3 = ""
threat_level = "LOW"
recommendation = "No immediate action required. Continue routine monitoring."

if failed_attempts == 0:
    threat_line_1 = "No failed login attempts detected."
else:
    if failed_attempts < 5:
        threat_line_1 = "[ALERT] Low security alert: 1 to 4 failed login attempts detected."
    else:
        threat_line_1 = "[CRITICAL] Multiple failed login attempts!"
        threat_line_2 = "[WARNING] Possible brute-force attack detected."
        threat_level = "HIGH"
        recommendation = "Investigate the login activity and secure the account immediately."

if is_active == False:
    threat_line_3 = "[INFO] Account access is currently disabled."
    if threat_level != "HIGH":
        threat_level = "MEDIUM"
        recommendation = "Account is inactive; verify whether access should remain disabled."
else:
    if failed_attempts < 5:
        threat_line_3 = "Account is active and no critical login threat detected."

# Feature 5: Security analyst report (never displays actual password)
print("========================================")
print("         CYBERGUARD SECURITY REPORT")
print("========================================")
print()
print("USER INFORMATION")
print("----------------------------------------")
print("Username:", username)
print("Email:", email)
print("Age:", age)
print("IP Address:", ip_address)
print("Account Status:", status_label)
print()
print("SECURITY ANALYSIS")
print("----------------------------------------")
print("Password Assessment:", password_assessment)
print("Failed Login Attempts:", failed_attempts)
print()
print("THREAT DETECTION")
print("----------------------------------------")
print(threat_line_1)
if threat_line_2 != "":
    print(threat_line_2)
if threat_line_3 != "":
    print(threat_line_3)
print()
print("FINAL SECURITY STATUS")
print("----------------------------------------")
print("THREAT LEVEL:", threat_level)
print()
print("RECOMMENDATION:")
print(recommendation)
print()
print("========================================")
print("         END OF SECURITY REPORT")
print("========================================")