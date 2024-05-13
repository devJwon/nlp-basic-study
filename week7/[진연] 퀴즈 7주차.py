for week in range(1, 51):
    file_name = f"{week}주차.txt"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"-{week} 주차 주간보고-\n")
        file.write("부서: \n")
        file.write("이름: \n")
        file.write("업무요약: \n")
