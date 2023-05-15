import pandas as pd
import openpyxl 

read_excel=pd.read_excel("C:/Users/RnD Workstation/Documents/CostReview/0512/BPAPAC_0512.xlsx", sheet_name="FL_BPA")
extract_data=read_excel.drop(["Model"],axis=1)
extract_data.index=extract_data["Tool"]
extract_data=extract_data.drop(["Tool"],axis=1)
print(extract_data)

#column_list
column_list=list(extract_data.columns)

# column json file format
column_json=str({"columns":column_list}).replace("{",'').replace("}",'').replace("'",'"').replace('nan','"nan"')
print("")
print(column_json+","+"")

#index_list
extract_data=extract_data.T
value1=list(extract_data["F3U8CNU3W.ABWEUUS"].round(1))
value2=list(extract_data["F3P2CYUAW.ABWEUUS"].round(1))
value3=list(extract_data["F3P2CYUAT.ASSEUUS"].round(1))
value4=list(extract_data["F3P2CYUBW.ABWEUUS"].round(1))
value5=list(extract_data["F3P2CYUBE.ABLEUUS"].round(1))

# data,index json file format
data_json=str({"F3U8CNU3W.ABWEUUS":value1,
               "F3P2CYUAW.ABWEUUS":value2, 
               "F3P2CYUAT.ASSEUUS":value3,
               "F3P2CYUBW.ABWEUUS":value4,
               "F3P2CYUBE.ABLEUUS":value5}).replace("{",'').replace("}",'').replace("'",'"').replace('nan','"nan"')
print(","+data_json)

# #index_list
# for i in range(len(extract_data.index)):
#     if i==len(extract_data.index)-1:
#         aa='"'+str(extract_data.index[i])+'":'+str(extract_data.iloc[i].tolist())
#     else:
#         aa='"'+str(extract_data.index[i])+'":'+str(extract_data.iloc[i].tolist())+","
#     print(aa)

# # value1=list(read_excel["vs BOM"].round(1))
# # value2=list(read_excel["PO Price Change"].round(1))
# # value3=list(read_excel["Substitute Change"].round(1))
# # value4=list(read_excel["PO + Substitute"].round(1))


# data,index json file format
# data_json=str({"vs BOM":value1,
#                "PO Price Change":value2, 
#                "Substitute Change":value3,
#                "PO + Substitute":value4}).replace("{",'').replace("}",'').replace("'",'"').replace('nan','"nan"')
# print(","+data_json)



