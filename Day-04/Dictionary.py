info = {
     "name": "ashu",
     "cgpa": 7.2,
     "subject":["math","science"]
}

#dictionary method
dict_keys = list(info.keys())
print(dict_keys)

dict_vals = list(info.values())
print(dict_vals)

print(info.get("cgpa2"))

info.update(
     {
          "city":"delhi"
     }
)
print(info)

info["cgpa"] = 9.8
print(info["cgpa"])


print(type(info))