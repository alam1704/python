prompt = "Give me an integer: "
def get_int():
    return int(input(prompt)) 
x = get_int()
y = get_int()
def calc_hcf (a,b):
    if b==0:
        return a
    else:
        return calc_hcf(b, a%b)
print(calc_hcf(x,y))