def time_string(h,m,s):
    if s == "24":
        b = f"{h}:{m}"
    if s == "12":
        if h <= 12:
            b = f"{h}:{m}am"
        else:
            b = f"{h-12}:{m}pm"
    return b

print(time_string(19,38,'12'))