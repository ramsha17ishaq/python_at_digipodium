numbers = [200,500,300]
out = map(str,numbers)
print(set(out))

out = map(lambda i : i/10, numbers)
print(set(out))