def linearSearchProduct(productList, targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
products = ["kavitha", "karthi", "kavitha", "nisha", "kavitha", "kavitha"]
target = "kavitha"
target2 = 'red'
result = linearSearchProduct(products, target)
print(result);