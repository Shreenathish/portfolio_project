import tabula 
import pandas as pd


df = tabula.read_pdf(r'E:\portfolio_project\extracting_img\Adobe Scan 02-Oct-2024.pdf',pages =2)
dataframe = df[0]

dataframe.rename(columns={'Unnamed: 1':'Theory','Second Year':'Pratical','Unnamed: 2':'Internal'},inplace=True)
print(dataframe)
