#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.DataFrame
revenue_growth_factor = 0.18
EBITDA_margin_rate = 0.45
tax_rate = - 0.21
capital_expenditures_rate = - 0.03
working_capital_increase_rate = - 0.06
EDBITA_exit_multiple = 32.7
discount_factor = 0.94

index = pd.date_range('2021', periods=12, freq='Y')
print(index)


# In[3]:


df=pd.DataFrame(index=index, columns=['revenue'])
df


# In[4]:


df['revenue'][0]=222
df


# In[5]:


for i in range(1, len(df)):
    df['revenue'][i] = df['revenue'][0] * (1 + revenue_growth_factor) ** (i)

df


# In[6]:


df['EBITDA'] = df.revenue * EBITDA_margin_rate
df


# In[7]:


df['taxes'] = df.EBITDA * tax_rate
df


# In[8]:


df['capital_expenditures'] = df.revenue * capital_expenditures_rate
df


# In[9]:


df['working_capital'] = df.revenue * working_capital_increase_rate
df


# In[10]:


df['cash_flow'] = df['EBITDA'] + df['taxes'] + df['capital_expenditures'] + df['working_capital']
df


# In[11]:


df['discount_factor'] = [(discount_factor ** i) for i in range(len(df))]
df


# In[12]:


df['Present_Value_of_Future_Cash_flow'] = df['cash_flow'] * df['discount_factor']
df


# In[13]:


last_EBITDA = df.EBITDA[-1]
last_EBITDA 


# In[18]:


terminal_value = EDBITA_exit_multiple * df.EBITDA[-1]
terminal_value
present_value_of_projected_fcf = df.Present_Value_of_Future_Cash_flow[1:-1].sum()
present_value_of_projected_fcf
present_value_of_terminal_value = terminal_value * df.discount_factor[-2]
present_value_of_terminal_value


# In[19]:


statement = f"""
Our projected Present Value of Projected Future Cash Flows are: {present_value_of_projected_fcf:.2f}.

We are providing revenue guidance in 2032 to be: {df.loc["2032", "revenue"].values[0]:.2f}

With an estimated EBITDA around: {df.loc["2032", "EBITDA"][0]:.2f}.

The terminal value a this time given a multiple of {EDBITA_exit_multiple:.2f} and the above EBITDA for 2030, would equal: {present_value_of_terminal_value:.2f}.

"""
print(statement)


# In[ ]:




