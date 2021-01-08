
# Wzor na pierwiastek n stopnia Newtona
# x_i+1 = 1/n ( (n-1) x_i + (A/x_i^(n-1)) ) )

def newton5(a, e=0.0001):
    x_i = 1
    while abs(x_i**5 - a) > e:
        x_i = 0.2 * ((4 * x_i) + (a / x_i**4))
    return x_i


a = int(input("Podaj dowolna liczbe dodatnia: "))

print(f"Pierwiastek piatego stopnia z {a} = {newton5(a)}\n")
print(a**(1/5))
