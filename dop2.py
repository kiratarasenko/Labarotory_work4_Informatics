import yaml
import pickle
import json

with open("schedule.yaml", "r", encoding='utf-8') as my_file:
    schedule = yaml.load(my_file, Loader=yaml.FullLoader)

print(schedule)
with open("schedule_lab.bin", "wb") as f:
    pickle.dump(schedule, f, protocol=pickle.HIGHEST_PROTOCOL)

with open("schedule_lab.bin", "rb") as f:
    schedule_lab1 = pickle.load(f)


with open("schedule_lab.json", "w", encoding='utf-8') as fi:
    json.dump(schedule_lab1, fi, ensure_ascii=False)


