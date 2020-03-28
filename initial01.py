import numpy as np
import pandas as pd

# Sample objects with different PANDAS types
obj_dict = {}

obj_dict["0000"] = pd.Series([1 , np.nan, 6, "hello" , 4.25])
obj_dict["0001"] = pd.date_range('20190322', periods=6)
obj_dict["0002"] = pd.DataFrame(np.random.randn(6, 4), index=obj_dict["0001"] , columns=list('ABCD'))
obj_dict["0003"] = obj_dict["0002"].to_numpy()
obj_dict["0004"] = pd.read_csv("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")


for x in range(5):
    print("\u0332".join("OBJECT - "+str(x))) 
    print(obj_dict["000"+str(x)])
    print("\n")

obj_dict["0004"].head()
