from bottle import run, route, run, get, post, template
from sys import argv
import json

images=["http://lh4.ggpht.com/U9JYgruXI7rIiZaojqKz39xtCEgp_lgaBRzwiMdoR8STEJDK291yW0R0OF0PvP1j16ULuLo22bBOI16PKw",
        "http://lh5.ggpht.com/5QHXbZ0SkRJiIxl7hKenRsPPXEa1xBSPJJ-UTnB_wreW5TgjH7iD13sxIjO8uyP1MCLHas_X7csmdVSI",
        "http://lh3.ggpht.com/WJg4Y0ou0O_wTPQh7om9zyJRnsc4xNOP4SBC3cL8804k57xKSdJRzxK4ERUVm0oxYb7CeSWzwK-HsFFjLg",
        "http://lh4.ggpht.com/8PoDv9ygWSY60M3ikEFmevlZYcPt8lFUmdZCPWOBoizDTkc72nu7B1_5sDUZ5JY5F32NacBK-sT9levn",
        "http://lh6.ggpht.com/z4mRATzB6KyDOeOR1OuYMLIJawOPWoaTAZbXhOJj8dYRz5k5ecO5Hri9LKzGJNq2KnA5vfQNrZnczGUvQw",
        "http://lh5.ggpht.com/z4qxXKRKhJUxn_cwh0Cdc87-gXQShqYJlnecIHOB7hFok1XMFFLv8IQlyuINiW-oyjUiWDNlB1oUIC_uLg"]

@get('/')
def index():
    return template('Index.html')

@get('/getImages')
def getImages():
    return json.dumps(images)

def main():
    run(host='0.0.0.0', port=argv[1])

if __name__=="__main__":
    main()