brand  =[(1,0) , (7,5) ,(4,9) ,(3,2)]

sort_P = sorted(brand, key=lambda x:x[0])
sort_U = brand.sort(key=lambda x:x[1])

print(sort_P)