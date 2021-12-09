irany = input()
def fordulj_orajarasi_iranyba(irany):
    if(irany == "É"):
        return "K"
    elif(irany == "K"):
        return "D"
    elif(irany == "D"):
        return "NY"
    elif(irany == "NY"):
        return "É"
print(fordulj_orajarasi_iranyba(irany))
