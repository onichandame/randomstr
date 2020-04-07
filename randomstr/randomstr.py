def randomstr(readable=False, capitalization=False, length=10, charset='alphanumeric'):
    from rstr import rstr
    from string import digits, ascii_lowercase, ascii_uppercase
    chars = ''
    if capitalization:
        ascii_lowercase = ''
    if charset == 'alphanumeric':
        chars = digits + ascii_lowercase + ascii_uppercase
    elif charset == 'alphabetic':
        chars= ascii_lowercase + ascii_uppercase
    elif charset == 'numeric':
        chars = digits
    elif charset == 'hex':
        chars = digits + ascii_lowercase[:6]
    else:
        chars = charset
    if readable:
        for c in '0Oil':
            chars = chars.replace(c, '')
    return rstr(chars, length)
