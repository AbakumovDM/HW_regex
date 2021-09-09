import csv
import re
phone_patten = r"(\+7|8)?\s*\(*(\d{3})\)*[\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s]*\(*(доб\.)*[\s]*(\d+)*[\)]*"
phone_sub = r"+7(\2)\3-\4-\5 \6\7"

with open("phonebook_raw.csv", encoding='utf8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def main(contact_list: list):
  new_list = list()
  for item in contact_list:
    mod_list = ' '.join(item[:3]).split((' '))
    res = [mod_list[0], mod_list[1], mod_list[2], item[3], item[4], re.sub(phone_patten, phone_sub, item[5]), item[6]]
    new_list.append(res)
  return union(new_list)

def union(new_list: list):
  res_list = list()
  for item in new_list:
    last_name = item[0]
    first_name = item[1]
    for new_item in new_list:
      new_last_name = new_item[0]
      new_first_name = new_item[1]
      if last_name == new_last_name and first_name == new_first_name:
        if item[2] == "": item[2] = new_item[2]
        if item[3] == "": item[3] = new_item[3]
        if item[4] == "": item[4] = new_item[4]
        if item[5] == "": item[5] = new_item[5]
        if item[6] == "": item[6] = new_item[6]
    if item not in res_list:
      res_list.append(item)
  return res_list

with open("phonebook.csv", "w", encoding='utf8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(main(contacts_list))
