from re import sub


# Convert the code using a template {{{1 #
def convertCode(template: dict, code: str) -> str:
    for command in template:
        code = sub(command, template[command], code)

    return code
# 1}}} #


# Find the language from file header {{{1 #
def findLanguage(code: str) -> str:
    lang = code.splitlines()[0]
    lang = lang.replace('# ', '')

    return lang
# 1}}} #
