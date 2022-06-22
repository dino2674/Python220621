# DemoRE.py

import re
#print(dir(re))

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

#다중 라인 주석처리 :  ctrl + /
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

#검색 여부만 표시 (Match 는 완벽히 매칭이 되어야 함)
print(bool(re.search("ap", "this is apple")))
print(bool(re.match("ap", "this is apple")))

# 연도를 가져오는 경우
result = re.search("\d{4}", "올해는 2022년입니다.")
print(result.group())

# 우편 번호
result = re.search("\d{5}", "우리 동네는 52300입니다.")
print(result.group())