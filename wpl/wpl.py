from re import sub


def convert(template, code):
    for command in template:
        code = sub(command, template[command], code)

    return code
