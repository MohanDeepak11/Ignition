import json

with open("view[1].json") as f:
    data = json.load(f)

print("Project Name:", data.get("name"))
