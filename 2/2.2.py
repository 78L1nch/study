for R in range(1, 10):
    target = int(str(R) * 12)
    for xpust in range(10000, 100000):
        if target % xpust == 0:
            groxot = target // xpust
            if 100000 <= groxot <= 999999:
                s_xpust = str(xpust)
                s_groxot = str(groxot)
                if s_xpust[1] == str(R) and s_groxot[1] == str(R) and s_groxot[4] == str(R):
                    all_digits = set(s_xpust + s_groxot)
                    if len(all_digits) == 10:
                        print(f"XPУСТ = {xpust}")
                        print(f"ГРОХОТ = {groxot}")
                        print(f"РРРРРРРРРРРР = {target}")
                        exit()
print("Решение не найдено")