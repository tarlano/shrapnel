# -*- Mode: Python -*-

import coro

from cys2n import Config, MODE, PROTOCOL
from coro.ssl.s2n import S2NSocket

from coro.log import NoFacility

LOG = NoFacility()

# EC doesn't work with s2n?
key = """-----BEGIN EC PARAMETERS-----
BggqhkjOPQMBBw==
-----END EC PARAMETERS-----
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIEjlUGmDtQ6knDdlAJSNkkBsrscdSAwCzwIIlf46CIgYoAoGCCqGSM49
AwEHoUQDQgAEmscdfOltpZJIAiDBfCXEIiG98Dhlqh6uUkj0+NkmE4WNrJpMDYD/
ZEcJ0pVEwjIZyAcb5Sl6tk4FuCkIfPmPRA==
-----END EC PRIVATE KEY-----
"""

crt = """-----BEGIN CERTIFICATE-----
MIICCDCCAbCgAwIBAgIJAPMOQCT1kfmpMAkGByqGSM49BAEwOzEUMBIGA1UEAxML
ZXhhbXBsZS5jb20xFjAUBgNVBAoTDUV4YW1wbGUsIEluYy4xCzAJBgNVBAYTAlVT
MB4XDTE1MDcxMTIxMDczOFoXDTE1MDgxMDIxMDczOFowOzEUMBIGA1UEAxMLZXhh
bXBsZS5jb20xFjAUBgNVBAoTDUV4YW1wbGUsIEluYy4xCzAJBgNVBAYTAlVTMFkw
EwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEmscdfOltpZJIAiDBfCXEIiG98Dhlqh6u
Ukj0+NkmE4WNrJpMDYD/ZEcJ0pVEwjIZyAcb5Sl6tk4FuCkIfPmPRKOBnTCBmjAd
BgNVHQ4EFgQUQR8Rw6gWKfmS8aag5pfjsNHblqMwawYDVR0jBGQwYoAUQR8Rw6gW
KfmS8aag5pfjsNHblqOhP6Q9MDsxFDASBgNVBAMTC2V4YW1wbGUuY29tMRYwFAYD
VQQKEw1FeGFtcGxlLCBJbmMuMQswCQYDVQQGEwJVU4IJAPMOQCT1kfmpMAwGA1Ud
EwQFMAMBAf8wCQYHKoZIzj0EAQNHADBEAiBXAW8xR517l9RbtvMt27lGGR8dcAcP
Tr9bHXvHzaDwLQIgAqbJQAkEhPdNZPzuxbtdTSMM1jijO+l+2hwJMScCpBM=
-----END CERTIFICATE-----
"""

key = """-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDbXarRaFWNbH7zt7qNLoTV02lEv5FyF0cOFuLXp2uSTpvlfQje
6CCJ4KvEE3cbRr3XReWn9TOLCidvnrIUZ61EpzJ0hNpRoAOb9zzHAxmxrvwRP+xz
KvR57bgsq44p7mZ97N453HFz54mIaLTsAR93qPP5Ao4z3kQi8IOKLP9UHQIDAQAB
AoGAJ4phsO9ShHRrCbkzWiFpdjVuQyMYr2z8tNBxQRf/btbWiO4ZvDwxKUkjDOvJ
S1RcAcKqm7S5/rTs2NTNGpp5g5HfqaqfnRvRTSUwrY9Y7qoouPn61KiDcBgghTL9
GH0v7pOvF0pOpaL/Q5jVv8tWjWXahtpmgHwsBIE44cavyc0CQQD7TfEvG+s17m+e
x0BZV98VpZ6mtP2oC0scgCn+GQ1ZNnhEfFawpY1gYxcQ2H7YP1xCNX0mHg52daum
+pdzXG/bAkEA33b0RzfUJa4Vu2QmuZD50lL6M13u1w60NkHtwQUghVC1BzNLktJs
uQRzHjrxHNy13RzpMWyYND1+Y+DpMwDpZwJAWyG6stC3DUm4JKYxCbU56wmybNX5
nnTp+h3oHINNOers1jkY3tpKWIfWl39LEHR5qnDnP2lq6T5mzxjUzzrYPQJBALjF
VfRxMCQ7zlJU3ERBoJ+M5r6EY9FEojPezaT1BU/WTOj4O/vZq/ZLvJf5apZP1LxQ
hGzOewdu9UvGk2wNy+8CQQDRsF/US06+PrSsWn0uiu+1Fy80PO5SoQmqNDL/olHw
61trvDaDJPIWzqxXuFwhVXZlTFlnaLxg3gAG+bMEqtSg
-----END RSA PRIVATE KEY-----
"""

crt = """-----BEGIN CERTIFICATE-----
MIICjzCCAfigAwIBAgIJAOFA3myvL0dJMA0GCSqGSIb3DQEBBQUAMDoxFDASBgNV
BAMTC2V4YW1wbGUuY29tMRUwEwYDVQQKEwxFeGFtcGxlLCBJbmMxCzAJBgNVBAYT
AlVTMB4XDTE1MDcxMTIxMjExOVoXDTE2MDcxMDIxMjExOVowOjEUMBIGA1UEAxML
ZXhhbXBsZS5jb20xFTATBgNVBAoTDEV4YW1wbGUsIEluYzELMAkGA1UEBhMCVVMw
gZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBANtdqtFoVY1sfvO3uo0uhNXTaUS/
kXIXRw4W4tena5JOm+V9CN7oIIngq8QTdxtGvddF5af1M4sKJ2+eshRnrUSnMnSE
2lGgA5v3PMcDGbGu/BE/7HMq9HntuCyrjinuZn3s3jnccXPniYhotOwBH3eo8/kC
jjPeRCLwg4os/1QdAgMBAAGjgZwwgZkwHQYDVR0OBBYEFIj+uemrlTyRZdHTwx8c
dvw6lXj+MGoGA1UdIwRjMGGAFIj+uemrlTyRZdHTwx8cdvw6lXj+oT6kPDA6MRQw
EgYDVQQDEwtleGFtcGxlLmNvbTEVMBMGA1UEChMMRXhhbXBsZSwgSW5jMQswCQYD
VQQGEwJVU4IJAOFA3myvL0dJMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQAD
gYEAIxmqzFn2JD4+Yp+wr2P+KiqCeP1NeNuDUsfqbx4p5xgM9fEMX3lnZsWeiCkX
2uv5idrZoUfBAkt1ao4xRAlRjc2TClwK7pNj3JKQQ0PdHVmPsJRQwxafcB1taXFS
14bcAwcAimx5zqYfMZho7tBUxpRd5vp6UVi1nR/9pIlZ7wE=
-----END CERTIFICATE-----
"""


cfg = Config()
cfg.add_cert_chain_and_key (crt, key)
cfg.set_protocol_preferences (['nork/1'])

def echo (conn):
    global rbytes, wbytes
    while 1:
        block = conn.recv (1024)
        if not block:
            break
        else:
            rbytes += len(block)
            conn.send (block)
            wbytes += len(block)

def serve (port):
    s = S2NSocket (cfg, mode=MODE.SERVER)
    s.bind (('', port))
    s.listen (10)
    while 1:
        conn, addr = s.accept()
        coro.spawn (echo, conn)

from coro.log import NoFacility
LOG = NoFacility()

rbytes = 0
wbytes = 0

def monitor (interval=10):
    global rbytes, wbytes
    while 1:
        r0, w0 = rbytes, wbytes
        coro.sleep_relative (interval)
        r = rbytes - r0
        w = wbytes - w0
        LOG ('throughput', r / interval, w / interval)

coro.spawn (serve, 7777)
coro.spawn (monitor)
coro.event_loop()
