def format_record(rec):
    ans = ""
    fio = rec[0].strip()
    group = rec[1]
    gpa = rec[2]

    fio = fio.split()
    if len(fio) == 0 or len(group) == 0:
        return "TypeError"
    if not(0.0 <= gpa <= 5.0):
        return "ValueError"

    
    ans = ans + fio[0][0].upper() + fio[0][1:] + ' '
    for i in range(1, len(fio)):
        ans = ans + fio[i][0].upper() + '.'
    ans = ans + ', гр. ' + group + ', '
    gpa = "{:.2f}".format(gpa)
    ans += str(gpa)
    return ans

# вывод тест-кейсов
print()
print(("Иванов Иван Иванович", "BIVT-25", 4.6), '->', format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(("Петров Пётр", "IKBO-12", 5.0), '->', format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(("Петров Пётр Петрович", "IKBO-12", 5.0), '->', format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(("  сидорова  анна   сергеевна ", "ABB-01", 3.999), '->', format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(("   ", "BIVT-26", 4.45), '->', format_record(("   ", "BIVT-26", 4.45)))
print(("Sabirova adelina", "", 3.56), '->', format_record(("Sabirova adelina", "", 3.56)))
print(("sabirova adelina", "BIVT-26-6-1", 6.7), '->', format_record(("sabirova adelina", "BIVT-26-6-1", 6.7)))
print()