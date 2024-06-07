## Generic
This is a hackathon hosted by PeakAI, Manchester. There are 3 tasks that are marked. The main data science project is end-to-end forecasting project.

## What is forecasting?
It deals with uncertainty (it bad, something you cannot control). Forecasting is the art of passing judgment on the likehood. Prediction deals with estimating an outcome from unseen data, typically with no time acpect.
Forecasting requires time aspect (you are trying to say what's going to happen in the future). Making forecasting is easy, but making a good forecasting is hard.
It needs lots of data to create a relative good forecast. Some things are just random. You need to have a very good understandung if the factors which contribute.

Example: Time sun cimes up in the morning; Weather forecast (hard, sometime inaccurate).

The way you split the train/test data is really important. 

# data analysis:

we found the products that generateed the highest sales and profit. This was matched via product subcategory. We then analysed the top performing products, then we analyse sales and profit. 

how effective are promotional campaigns:

to find the effectiveness of the promotional campaigns, we first binarised the discounts into 0 and 1 - with 0 being the no discount and 1 being there is a discount. We then aggreagted the data by month. We then did a linear regression and found thatt there was a strong correlation between frequency of promos in a month vs the sales and profit. 

# forecasting

we did a general fbprophet forecast. We also did multiple prophets for each subcategory. We did time series train test split. 






