import re


def parse_email(email: str):
    email_pattern = re.compile(r'^[a-zA-Z0-9]{2,64}@[a-zA-Z]{2,64}\.[a-zA-Z0-9]{2,6}')
    if not email_pattern.match(email):
        raise ValueError(f'Wrong email: {email}')
    u, d = email.split('@')
    return {"username": u, "domain": d}


def test():
    emails = ['mcleod190@gmail.com', 'someone@geekbrains.ru','someone@geekbrainsru' ]
    [print(parse_email(email)) for email in emails]


if __name__ == '__main__':
    test()