def media(*num):
    if len(num) == 0:
        return 0 
    return sum(num) / len(num)

print(f"A media dos valores é: {media(3,5,7)}")