def snake_string(s):
    i = 1
    ss = ""
    while i < len(s):
        ss = ss + s[i]
        i += 4
    j = 0
    while j < len(s):
        ss = ss + s[j]
        j += 2
    k = 3
    while k < len(s):
        ss = ss + s[k]
        k += 4
    return ss

def snake_string_elegant(s):
    return s[1::4] + s[::2] + s[3::4]
if __name__ == "__main__":
    print(snake_string("Hello_World!")) # "e_lHloWrdlo"
    print(snake_string_elegant("Hello_World!"))
