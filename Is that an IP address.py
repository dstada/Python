"""Is That an IP Address?

Given a string as input, create a program to evaluate whether or not it is a valid IPv4 address.

A valid IP address should be in the form of: a.b.c.d where a, b, c and d are integer values ranging from 0 to 255 inclusive.

For example:
127.0.0.1 - valid
127.255.255.255 - valid
257.0.0.1 - invalid
255a.0.0.1 - invalid
127.0.0.0.1 - invalid
"""

import socket

ip = input("Give IP:")


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False
    return True


if is_valid_ipv4_address(ip) is False:
    print("Not a valid IP")
else:
    print("Valid IP")

# -----------------------------------------------------------------------

def check_ip(ip):
    try:
        parts = ip.split('.')
        # Must be four parts and all parts 0-255
        return len(parts) == 4 and all(0 <= int(part) < 256 for part in parts)
    except ValueError:
        return False    # Not convertible to integer
    except (AttributeError, TypeError):
        return False    # No string


if check_ip(ip) is False:
    print("Not valid")
else:
    print("Valid")





