#!/usr/bin/env python
# coding: utf-8

# First Dataquest Project
# ===================
# 
# ## Learning how to use a Jupyter Notebook
# 
# *The content below was a meta-exercise from the 'Python Fundamentals' course on how to work with Jupyter Notebooks.*

# ### Loading Data
# 
# The cell below illustrates how to load data from a csv file into python:
# 
# 1. Point the open() function to the path of your file, which returns a file object
# 2. Import the reader() function from the 'csv' library
# 3. Feed the file object into the reader() function, which returns a reader object that iterates through lines of the csv
# 4. Feed the reader object into a list, which makes a list of lists, each corresponding to a row in the csv file
# 5. Slice into the first 4 rows of the data to preview its contents

# In[1]:


opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
data = list(read_file)
data[:3]


# ### About the data
# 
# The data above was obtained from the public Kaggle dataset [Mobile App Store](https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps/), which is a snapshot from 2017 of the details 7000+ apps on the iOS App Store. See the data dictionary below:
# 
# |Column Name       |Description                                    |
# |------------------|-----------------------------------------------|
# |'id'              |App ID                                         |
# |'track_name'      |App Name                                       |
# |'size_bytes'      |Size (in Bytes)                                |
# |'currency'        |Currency Type                                  |
# |'price'           |Price amount                                   |
# |'rating_count_tot'|User Rating counts (for all version)           |
# |'rating_count_ver'|User Rating counts (for current version)       |
# |'user_rating'     |Average User Rating value (for all version)    |
# |'user_rating_ver' |Average User Rating value (for current version)|
# |'ver'             |Latest version code                            |
# |'cont_rating'     |Content Rating                                 |
# |'prime_genre'     |Primary Genre                                  |
# |'sup_devices.num' |Number of supporting devices                   |
# |'ipadSc_urls.num' |Number of screenshots showed for display       |
# |'lang.num'        |Number of supported languages                  |
# |'vpp_lic'         |Vpp Device Based Licensing Enabled             |
