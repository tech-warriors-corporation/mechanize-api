try:
    app = __import__("app").app
except Exception as error:
    print(error)

try:
    app = __import__("__main__").app
except Exception as error:
    print(error)
