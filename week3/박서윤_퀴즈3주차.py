sites = input("https:// 포함 사이트 주소 입력: ")

domain_body = sites.split("//")[1].split(".")[0]
pwd = domain_body[:3]+str(len(domain_body))+str(domain_body.count("e"))+"!"

print(f"{sites}의 권장 비번은 {pwd}입니다")