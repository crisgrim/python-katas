def applydiscount(total):
    if total > 100:
        return total - (total * 0.1)
    else:
        return total


print(applydiscount(101))
print(applydiscount(100))
print(applydiscount(20))
