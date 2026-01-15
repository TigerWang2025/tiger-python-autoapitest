from string import Template
dic = {"name": "Jack"}
st = "Hello , ${name}"

print(Template(st).substitute(dic))