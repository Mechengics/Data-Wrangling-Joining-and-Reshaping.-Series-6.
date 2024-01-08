#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Data Wrangling: Join, Combine, and Reshape


# In[2]:


#This chapter is designed to focus on tools to help combine, join and rearrange data.


# In[19]:


#Hierarchical Indexing
import pandas as pd
import numpy as np
import random
data1=pd.Series(np.random.uniform(size=8),
               index=[["a","a","a","b","b","b","c","c"],
               [1,2,3,1,2,3,1,2]])
data1


# In[20]:


#This is called as multi index. I think in the previous course we had said we will learn multi index in the comming lessons. 


# In[21]:


#This multi index has particularly two labels. The outer labels contains the alphabetical index. 
#You can also slice both outer and inner index.
#for this you can try the following. 
data1["b":"c"]


# In[22]:


#want to deal with the inner index also?
#you can proceed as 
data1.loc[["a","b"],1]


# In[23]:


#You can see that only the sepcified inner index is selected in this case.


# In[24]:


#Herarchical indexing is useful in rehsaping the data into pivot table. 
#For this you should use the unstack expression.
data1.unstack()


# In[ ]:


#This method of unstack is more detailed explained in reshaping and pivoting.


# In[26]:


#In case of the data frame you can use the expression. 
frame1=pd.DataFrame(np.arange(12).reshape((4,3)),
                   index=[["a","a","b","b"], [1,2,1,2]],
                   columns=[["A","A","B"],["C","C","C"]])
frame1


# In[27]:


#You can see how the given data frame is multindexed in the given example
#The A column contains two categories C and C and B contains only one category that is C
#Also the a index contains two sub index that is 1 and 2, and b also contains two sub index 1 and 2.


# In[34]:


#you can also give the index name of the data frame. 
frame1.index.names=["string","integer"]
frame1.columns.names=["alpha1","alpha2"]
frame1


# In[36]:


frame1.index.nlevels#this gives the levels of index. There are two levels here so the output is 2.


# In[38]:


#you can also swap levels in the given dataframe
frame1.swaplevel("string","integer")# the swap level swaps the value of string and integer


# In[42]:


#you can also sort the index, specifying the level using sort_index expression.
frame1.sort_index(level=0)
#you can observe the level is sorted now.


# In[41]:


#you can perform both the actions at the same time. In case of specifying the name of levels everytime you can also use integer analogy to do so. 
frame1.swaplevel(0,1).sort_index(level=0)


# In[43]:


#when we conduct this sort index expression we can observe that, the sorting of the index removes the repeated data values from the integer format.


# In[47]:


#Summary Statistics by level. 
#want to conduct statistical operations by level on the data.
frame1.groupby(level="integer").sum()


# In[48]:


frame1.groupby(level="alpha1", axis="columns").sum()


# In[49]:


frame1["A"]


# In[50]:


#Some times you want to split the data frame and create a seperate data frame. This sepereate has seperate columns which you can use as the index for the further processing of the data.
frame2=pd.DataFrame({"one":range(7),"two":range(7,0,-1),"c":["one","one","two","one","three","three","one"],
                     "d":[0,1,2,0,1,2,3]})
frame2


# In[51]:


frame3=frame2.set_index(["c","d"])
frame3


# In[53]:


#By defeault the columns you have specified will drop from the tabular data. 
#if you don't want to do this you can specify the drop attribute to be false. 
frame4=frame2.set_index(["c","d"], drop=False)
frame4


# In[55]:


#the command reset index is just opposite to the command set index. 
#it helps you to bring the index back in the data frame, and the new index will be the integers that starts from the zero. 
frame3.reset_index()


# In[56]:


#Remember of the column is already present in the data frame than this method doesnot work. 
#It indicates the error specifying that the column is already present in the given data frame.


# In[ ]:


###Combining and Merging Datsets.###


# In[57]:


#pandas.merge
#If you want the intersection of the data sets than you can use the operation called as pandas merge
#use pandas.merge


# In[60]:


frame5=pd.DataFrame({"match": ["b","a","b","a"],
                    "data1":pd.Series(range(4), dtype="Int64")})
frame6=pd.DataFrame({"match":["b","b","a","c"],
                    "data2":pd.Series(range(4), dtype="Int64")})
frame5


# In[61]:


frame6


# In[62]:


#you can use the merge command to merge these two dataframes in a single one. 


# In[65]:


pd.merge(frame6, frame5)


# In[66]:


#You can see that the data is merged and the values are assigned similarly.
#Value c which was present in frame6 is automatically dropped from the list. So it is better to call it as the intersection.
#But if the frame5 was shorter than frame 6 but contained the same keys, the largest dataframe is taken into consideration and in addition to that, the values of the shorter dataframe are autmatically analyzed and filled.
#This may sound a bit cray but, you can try it and see the outcome.
#The matching between two data frame is automatically done by the same column that is match.
#It is essential to specify the matching column as per the demand.
#For doing this you can use the on method.


# In[67]:


pd.merge(frame5, frame6, on="match")


# In[68]:


#say you have different column names and still you want to join the datas you can use the left_on and right_on method to join the columns. 
#I will use the previous data frame and make the correction on them and demonstrate the result. 
frame7=pd.DataFrame({"match1": ["b","a","b","a"],#match is made match1 to have different columns
                    "data1":pd.Series(range(4), dtype="Int64")})
frame8=pd.DataFrame({"match":["b","b","a","c"],
                    "data2":pd.Series(range(4), dtype="Int64")})
frame7


# In[69]:


frame8


# In[73]:


#now in order to merge dataframe with the same column, this time the pandas doesnot do this on own so we have to specify them left_on and right_on
pd.merge(frame7,frame8, left_on="match1",right_on="match")


# In[76]:


#Well maybe you want to do the union instead of the intersection, you cn specify the method using how and give the result outer, 
pd.merge(frame7,frame8, left_on="match1", right_on="match", how="outer")


# In[77]:


#you can see the section c which is not present in frame7 is given a null definition.


# In[ ]:


#The method how has various methods
#inner: Used the key combination used in both tables. 
#right: use all key combinations found on the righ of the table
#outer: uses all key combinations observed in both tabes.


# In[4]:


import pandas as pd
import numpy as np
dataframe1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "b"],
                        "data1": pd.Series(range(6), dtype="Int64")})

dataframe2 = pd.DataFrame({"key": ["a", "b", "a", "b", "d"],
                     "data2": pd.Series(range(5), dtype="Int64")})
pd.merge(dataframe1, dataframe2, on="key", how="left")


# In[5]:


pd.merge(dataframe1, dataframe2, on="key", how="right")


# In[ ]:


#Difference between the method right and left. 
#right: means that all the rows on the right should be included and those rows whose keys match should be also included. If the rows of 1 are not included in 2 than null values are kept.
#left: means that all the rows on the left should be included and those rows whose keys match should be also included. If the rows of left are not present in right than null values are kept.


# In[6]:


#inner and outer: inner joins only those rows that are common in both data frames.
#and outer joins the all the rows and gives null values to the rows which don't contain the specified element.


# In[ ]:


#sort: helps to sort the merged data. 


# In[16]:


#Merging of Index
left1=pd.DataFrame({'key':['a','b','c','a','c','b'],'values':range(6)})
right1=pd.DataFrame({'group_val':[3,5]},index=['a','b'])
pd.merge(left1,right1, left_on='key',right_index=True)


# In[17]:


left1


# In[18]:


right1


# In[19]:


#If you want to see the union of these dataframes than you can pass the how argument.
pd.merge(left1,right1, left_on='key', right_index=True, how="outer")
#you can see that now we have extracted the union from the given data.


# In[20]:


#you can also join the dataframe using the join expression
left1.join(right1, how="outer")


# In[21]:


#this join method is used to join multiple dataframes having overlapping index, but not overlapping columns. 
#you can also join, multiple dataframes using this method
#in order to do this you can function as, if there was another dataframe called as df2 than you can join them as
#left1.join([right1, df2])
#for union or intersection you can specify as the following
#left1.join([right1, df2], join="outer")


# In[22]:


#Concatenation
#Array method of concatenation. 
#you can concatenate the arrays using the method pd.concat, this method enables you concatenate.
#say we have array1
arr=np.arange(12).reshape((3,4))
np.concatenate([arr,arr], axis=1)


# In[23]:


#you can see in the result that, the arrays are concatenated on the basis of the columns if you press axis=0 it will be done on the basis of rows. That means there will be 6 rows in the axis.


# In[24]:


#not ony arrays you can also concatenate series using this method
s1 = pd.Series([0, 1], index=["a", "b"], dtype="Int64")

s2 = pd.Series([2, 3, 4], index=["c", "d", "e"], dtype="Int64")

s3 = pd.Series([5, 6], index=["f", "g"], dtype="Int64")


# In[25]:


pd.concat([s1,s2,s3])


# In[26]:


#if we use axis="columns", than we can use this method to create a dataframe. 


# In[27]:


pd.concat([s1,s2,s3], axis="columns")


# In[31]:


#By doing this you are getting the union of the series if you want to create the intersection you can operate them as:
s4=pd.concat([s1,s3])
pd.concat([s1,s4], axis="columns", join="inner")


# In[32]:


s4


# In[34]:


#you can see that the resulting concatenated series is not indentifiable on the basis of which has come from first and which from the second series to solve this issue you can use the expression as
s5=pd.concat([s1,s4], keys=["key1","key2"])
s5


# In[35]:


#you can clearly se the two datas that is s1 and s4 combining here in this new leveled seires.


# In[37]:


#Want to create a dataframe using this series we can proceed as follows:
s5.unstack()
#you can see more clearly what data is present in the form of key 1, key 2 and what is not present in there.


# In[38]:


#This same logic applies for the dataframe
concat1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=["a", "b", "c"],
                    columns=["one", "two"])

concat2 = pd.DataFrame(3 + np.arange(4).reshape(2, 2), index=["a", "c"],
                      columns=["three", "four"])
pd.concat([concat1, concat2], axis="columns",keys=["level1","level2"])


# In[42]:


#here we are using axis as columns to solve the issue of the column or row method, 
#those values that are not present in both of the dataframes are mentioned as null values.
pd.concat([concat1, concat2], ignore_index=True)
#This ignore index commands used here functions to remove the index of the newly created dataframe. 


# In[ ]:


#verify_integrity:Check new axis in concatinated object for duplictes and raise and exceptionif so; by default (False), allows duplicates.


# In[43]:


#Combining Data with Overlap:
a = pd.Series([np.nan, 2.5, 0.0, 3.5, 4.5, np.nan],
             index=["f", "e", "d", "c", "b", "a"])
b = pd.Series([0., np.nan, 2., np.nan, np.nan, 5.],
                 index=["a", "b", "c", "d", "e", "f"])
np.where(pd.isna(a),b,a)


# In[ ]:


#where means that if null is present in the a series, than select elements from b
#if not null than a is selected.
#to use the wehre method, we should know that the length should be equal.


# In[45]:


#in pandas you can use combine_first to conduct the same operation.
a.combine_first(b)
#in this method it is not necessary that the series should of same length.


# In[48]:


#Reshaping and Pivoting
stack=pd.DataFrame(np.arange(6).reshape((2,3)),
                   index=pd.Index(["a","b"], name="state"),
                   columns=pd.Index(["one","two","three"], name="number"))


# In[50]:


#stack brings the columns as indexes
r1=stack.stack()
r1


# In[51]:


#you can unstack the data using the unstack method
r1.unstack()


# In[52]:


#you can unstack different levels
r1.unstack(level="state")


# In[54]:


#if the values are not present than null values is presented. 
#When you stack the unstacked data the null values are automatically dropped
#When the dropna is set to false than the null values are not removed.
test1=pd.concat([s1,s2],keys=["one","two"])
test1


# In[56]:


test1.unstack()


# In[57]:


test1.unstack().stack()


# In[58]:


#here the null values are automatically dropped.
#if you want to set this to false
test1.unstack().stack(dropna=False)


# In[63]:


#REMEMBER 
#the level that is defined while unstacking rests as the lower level
#you can also name the index to stack and unstack.


# In[64]:


###Pivot Tables###
import pandas as pd
import numpy as np
new=pd.read_csv("C:\\Users\\user\\Desktop\\athlete_events.csv")
new.head()


# In[65]:


#you can extract this table from kaggle, this is the record of names of olympians who had practiced in the events.


# In[67]:


#Want to see what was the average height of olympic athlets. 
new["Height"].mean()


# In[72]:


#want to caluate the average mean of height in each year you can try as
new.groupby('Year')['Height'].mean()


# In[74]:


#want to know the average height of teams at each distinct year. 
#for this we can pivot table
new.pivot_table(index="Year", columns="Sport", values="Height")


# In[75]:


#pivot table if not specified a special method always calcualtes the average of the given data.
#want to view the tallest sprots height in each year. 
new.pivot_table(index="Year", columns="Sport", values="Height",aggfunc=["max"])


# In[76]:


#want to calculate mean and maximum values at the same time you can use the method.
new.pivot_table(index="Year", columns="Sport", values="Height",aggfunc=["max","mean"])


# In[77]:


#Here we got two columns having levels of columns. And this is how you use the pivot tables.


# In[ ]:


#If you have made this far by learning all the series. Hat's off to your consistency
#Regards
#Mechengics.
#Ankit Sangroula

