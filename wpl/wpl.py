from re import sub


# Convert the code using a template {{{1 #
def convertCode(template: dict, code: str) -> str:
    for command in template:
        code = sub(command, template[command], code)

    return code
# 1}}} #
