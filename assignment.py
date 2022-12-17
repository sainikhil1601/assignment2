import pandas as pd
inp1 = pd.Series([12, 14, 16, 18, 20])
inp2 = pd.Series([10, 12, 14, 16, 18])
print(inp1,inp2)
output = inp1 + inp2
print("Add o/p:",output)
output = inp1-inp2
print("Sub o/p:",output)
output = inp1*inp2
print("Mul o/p:",output)
output = inp1//inp2
print("Floor div o/p:",output)
output = inp1/inp2
print("Div o/p:",output)
output = inp1%inp2
print("Mod o/p:",output)