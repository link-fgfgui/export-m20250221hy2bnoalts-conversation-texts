import json
import pythonmonkey as pm
from pprint import pp
js_code = open('Avatar.js', 'r', encoding='utf-8').read()
pm.eval(js_code)
avatar_raw = list(pm.globalThis._avatar)
texts = json.loads(open("m20250221hy2bnoalts-zh-cn.json",
                   'r', encoding='utf-8').read())
texts = {i: texts[i] for i in texts if "car_egg" in i}
avatar = {str(int(i["_id"])): i["Name"] for i in avatar_raw}
avatar.update(json.loads(
    open("avatar_add.json", "r", encoding='utf-8').read()))
# pp(avatar)
# quit()
# print(avatar)
# print(len(avatar))
conversationIdsPairTemp = {}
for key in texts:
    key_slice = key.split('_')
    conversationId = key_slice[2]
    avatarId = key_slice[3]

    if conversationId == "play":
        print(
            f"开拓者 与 {avatar[avatarId]} |\n\t{avatar[avatarId]}: {texts[key]}")
    else:
        if conversationId in conversationIdsPairTemp.keys():
            print(
                f"{avatar[avatarId]} 与 {avatar[conversationIdsPairTemp[conversationId]["id"]]} |")
            print(
                f"\t{avatar[conversationIdsPairTemp[conversationId]["id"]]}: {conversationIdsPairTemp[conversationId]["text"]}")
            print(f"\t{avatar[avatarId]}: {texts[key]}")
        else:
            conversationIdsPairTemp[conversationId] = {
                "text": texts[key], "id": avatarId}
