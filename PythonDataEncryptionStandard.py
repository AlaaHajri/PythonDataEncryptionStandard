##########################################################################################################################
print("#################################################################################################################")
print("                                             Calcul de la clé Ki")
print("#################################################################################################################")
##########################################################################################################################
#Clé initial de block de 64 bits:
#cleprincipal64 = "1234567812345678123456781234567812345678123456781034567810345678"
cleprincipal64 = "0100100101000101010011110100011001001001010101000010001100110001"
print("Cle64/Clé Principal = ", cleprincipal64, "de longeur ", len(cleprincipal64),"bit")

########################################################################################################################
# on coupe la cleprincipal64 dans une list1 de 8bit
list1 = []
for i in range(8):
    list1.append(cleprincipal64[8*i:8*(i+1)])
print("la liste avant de enlever le 8eme bit: ")
print(' '.join(list1))
list1string = ''.join(list1)
########################################################################################################################
# ici on a enlever le 8eme caractere de chaque bloque de la liste et on l'enregistre sur une list2
list2 = []
for i in range(8):
    list2.append(list1[i][0:-1])

print("la liste aprés de enlever le 8eme bit: ")
print(' '.join(list2))
list2string = ''.join(list2)
print("Cle56/Clé Racine = ", list2string, "de longeur ", len(list2string),"bit")

##########################################################################################################################
print("#################################################################################################################")
print("                                             Permutation PC-1")
print("#################################################################################################################")
#crée une liste de permutation PC-1

list3 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
clepermute = [cleprincipal64[i-1] for i in list3]
clepermute = ''.join(clepermute)
print("Clé avant permutation =",cleprincipal64)
print("Clé aprés permutation =",clepermute)
print("Longeur de la clé avant permutation =", len(cleprincipal64),"bit")
print("Longeur de la clé aprés permutation =", len(clepermute),"bit")

#print("longuer list PC-1:", len(list3))
#maintenant on vas crée une nouvelle clé de 56bit avec la permutation
# on déclare une nouvelle list vide appélle list4 dans la quelle on vas enregistrer les permutations qu'on a fait

# on crée un liste de cleprincipal64 en seul caractére #list 4
#for x in range(len(list3)):
##########################################################################################################################
print("#################################################################################################################")
print("                                             Décalage circulaire à gauche ")
print("#################################################################################################################")
##########################################################################################################################
#on coupe la clé en 2 partie de 28 bits
print("cl  =",clepermute, "avec longuer de",len(clepermute),"bit")

C0 = str(clepermute[0:28])
D0 = str(clepermute[28::])
print("C0  =",C0, "longueur", len(str(C0)))
print("D0  =",D0, "longueur", len(str(D0)))

#C0 = 0022222233333333444444445555
#D0 = 8888888877777777666666665555
#########1 2 3 4 5 6 7 8 9 10   11  12  13  14  15  16
#########1 1 2 2 2 2 2 2 1 2    2   2   2   2   2   1
listk = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1] # longeur len = 16

for y in range(len(listk)):
    if y == 0:
        C1_save = C0[:listk[y]]
        C1 = C0[y + 1::] + C1_save
        print("C1  =", C1)

        D1_save = D0[:listk[y]]
        D1 = D0[y + 1::] + D1_save
        print("D1  =", D1)
    elif y == 1:
        C2_save = C1[:listk[y]]
        C2 = C1[y::] + C2_save
        print("C2  =", C2)

        D2_save = D1[:listk[y]]
        D2 = D1[y::] + D2_save
        print("D2  =", D2)
    elif y == 2:
        C3_save = C2[:listk[y]]
        C3 = C2[y::] + C3_save
        print("C3  =", C3, "len", len(C3))

        D3_save = D2[:listk[y]]
        D3 = D2[y::] + D3_save
        print("D3  =", D3, "len", len(D3))
    elif y == 3:
        C4_save = C3[:listk[y]]
        C4 = C3[listk[y]::] + C4_save
        print("C4  =", C4, len(C4))
        #print(C4_save)

        D4_save = D3[:listk[y]]
        D4 = D3[listk[y]::] + D4_save
        print("D4  =", D4, len(D4))
        #print(D4_save)
    elif y == 4:
        C5_save = C4[:listk[y]]
        C5 = C4[listk[y]::] + C5_save
        print("C5  =", C5)

        D5_save = D4[:listk[y]]
        D5 = D4[listk[y]::] + D5_save
        print("D5  =", D5)
    elif y == 5:
        C6_save = C5[:listk[y]]
        C6 = C5[listk[y]::] + C6_save
        print("C6  =", C6)

        D6_save = D5[:listk[y]]
        D6 = D5[listk[y]::] + D6_save
        print("D6  =", D6)
    elif y == 6:
        C7_save = C6[:listk[y]]
        C7 = C6[listk[y]::] + C7_save
        print("C7  =", C7)

        D7_save = D6[:listk[y]]
        D7 = D6[listk[y]::] + D7_save
        print("D7  =", D7)
    elif y == 7:
        C8_save = C7[:listk[y]]
        C8 = C7[listk[y]::] + C8_save
        print("C8  =", C8)

        D8_save = D7[:listk[y]]
        D8 = D7[listk[y]::] + D8_save
        print("D8  =", D8)
    elif y == 8:
        C9_save = C8[:listk[y]]
        C9 = C8[listk[y]::] + C9_save
        print("C9  =", C9)

        D9_save = D8[:listk[y]]
        D9 = D8[listk[y]::] + D9_save
        print("D9  =", D9)
    elif y == 9:
        C10_save = C9[:listk[y]]
        C10 = C9[listk[y]::] + C10_save
        print("C10 =", C10)

        D10_save = D9[:listk[y]]
        D10 = D9[listk[y]::] + D10_save
        print("D10 =", D10)
    elif y == 10:
        C11_save = C10[:listk[y]]
        C11 = C10[listk[y]::] + C11_save
        print("C11 =", C11)

        D11_save = D10[:listk[y]]
        D11 = D10[listk[y]::] + D11_save
        print("D11 =", D11)
    elif y == 11:
        C12_save = C11[:listk[y]]
        C12 = C11[listk[y]::] + C12_save
        print("C12 =", C12)

        D12_save = D11[:listk[y]]
        D12 = D11[listk[y]::] + D12_save
        print("D12 =", D12)
    elif y == 12:
        C13_save = C12[:listk[y]]
        C13 = C12[listk[y]::] + C13_save
        print("C13 =", C13)

        D13_save = D12[:listk[y]]
        D13 = D12[listk[y]::] + D13_save
        print("D13 =", D13)
    elif y == 13:
        C14_save = C13[:listk[y]]
        C14 = C13[listk[y]::] + C14_save
        print("C14 =", C14)

        D14_save = D13[:listk[y]]
        D14 = D13[listk[y]::] + D14_save
        print("D14 =", D14)
    elif y == 14:
        C15_save = C14[:listk[y]]
        C15 = C14[listk[y]::] + C15_save
        print("C15 =", C15)

        D15_save = D14[:listk[y]]
        D15 = D14[listk[y]::] + D15_save
        print("D15 =", D15)
    elif y == 15:
        C16_save = C15[:listk[y]]
        C16 = C15[listk[y]::] + C16_save
        print("C16 =", C16)

        D16_save = D15[:listk[y]]
        D16 = D15[listk[y]::] + D16_save
        print("D16 =", D16)
##########################################################################################################################
print("#################################################################################################################")
print("                                             Permutation : PC-2")
print("#################################################################################################################")
##########################################################################################################################
list4 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

for i in range(1, 17):
    C = 'C' + str(i)
    D = 'D' + str(i)
    key = 'key' + str(i)
    exec(f"{C}{D} = {C} + {D}")
    exec(f"print(\"{C}{D} =\", {C}{D})")
    exec(f"{key} = [{C}{D}[j-1] for j in list4]")
    exec(f"{key} = ''.join({key})")
    exec(f"print(\"{key} =\", {key})")
