from wpl.wpl import findLanguage, convertCode
import wpl.langs
import sys


def main():
    file = sys.argv[1]
    with open(file, 'r+') as f:
        code = f.read()
    lanugage = findLanguage(code)
    lanugage = eval(f"wpl.langs.{lanugage}")
    code = convertCode(lanugage, code)
    exec(code)


if __name__ == "__main__":
    main()
