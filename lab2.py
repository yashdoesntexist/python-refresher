from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# Create a small dataset:
df = pd.DataFrame([
  [1,1,1,0],   # Basket 1
  [0,1,0,1],   # Basket 2
  [1,1,1,1],   # Basket 3
], columns=['milk','bread','eggs','butter'])

frequentItemset = apriori(df, use_colnames= True) # min_support defaults to 0.5 no need to explicitly mention that
association = association_rules(frequentItemset, metric='lift', min_threshold=1.0)

print(frequentItemset)
print()
print(association[['antecedents','consequents','support','confidence','lift']])
print()


