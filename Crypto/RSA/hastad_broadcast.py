#!/usr/bin/env python3
import binascii

# find_mult_inv and nth_root stolen from stack overflow

def find_mult_inv(x, n):
    a = [0, 1]
    q = [None, None]
    r = [n, x]
    i = 1
    
    while r[i] > 1:
        i += 1
        r.append(r[i - 2] % r[i - 1])
        q.append(r[i - 2] // r[i - 1])
        a.append((a[i-2] - q[i] * a[i - 1]) % n)
    
    if r[i] == 1: return a[i]
    else: return None

def mul(l):
    m = 1
    for x in l:
        m *= x
    return m

def list_to_long(l):
    return [int(x, 16) for x in l]

def nth_root(x, n):
    # Start with some reasonable bounds around the nth root.
    upper_bound = 1
    while upper_bound ** n <= x:
        upper_bound *= 2
    lower_bound = upper_bound // 2
    # Keep searching for a better result as long as the bounds make sense.
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        mid_nth = mid ** n
        if lower_bound < mid and mid_nth < x:
            lower_bound = mid
        elif upper_bound > mid and mid_nth > x:
            upper_bound = mid
        else:
            # Found perfect nth root.
            return mid
    return mid + 1

# finds x for len(mod_list) modular congruences
def chinese_remainder_theorem(ct_list, mod_list):
    orig_msg = 0

    for ct, mod in zip(ct_list, mod_list):
        rem_mod_list = mod_list.copy()
        rem_mod_list.remove(mod)
        mul_res = mul(rem_mod_list)
        orig_msg += (ct * mul_res * find_mult_inv(mul_res, mod))

    return orig_msg % mul(mod_list)


# decrypts to some HTB flag
ct_list = [
    '536F9C0519E23A35D12DC8D860D0B19821B92CC11852549AFDFED8A196D955CB6604A53A637C6C39B8A5566CD47A1BF231CF68CF2618E1DE8D54577B7BB661CFD85921F3399A19A2382A37D1336D5E07891C4EA3524846875559358DD54BA217E8939BFB42F87F883089FE6C83CBC4A2DED874AD4E6F18FF691BBEE21E1A4471',
    'B..',
    '4..',
    '1..',
    '2..',
]

mod_list = []

ct_list = list_to_long(ct_list)
mod_list = list_to_long(mod_list)

orig_msg = chinese_remainder_theorem(ct_list, mod_list)

dec_msg = nth_root(orig_msg, len(mod_list))
print(dec_msg)
print(hex(dec_msg)[2:])
print(bytes.fromhex(hex(dec_msg)[2:]))
