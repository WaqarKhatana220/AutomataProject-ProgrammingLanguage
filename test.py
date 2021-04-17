# FOR (INT i = 0; i < 2; i++)
# {
# FOR (INT j = 0; j <= 1; j = j + 1)
# {
# FOR (INT k = 0; k <= 1; k++)
# {
# PRINT(“(”, i, “,”, j, “,”, k, “)”)
# }
# }
# }

for i in range (0, 2):
    for j in range (0,1):
        for k in range (0,1):
            print("(", i, ",", j, ",", k, ")")