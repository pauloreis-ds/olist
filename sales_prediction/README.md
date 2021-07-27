## Sales Forecast

**Motivation! What's the context?**
- In 2017 Olist started to forecast its monthly sales based on the average revenue from 3 months before. But now the company
  wants to be able to predict future sales more accurately with a wider time range (3 months).

**Why?**
- To efficiently allocate resources for future projects, growth and manage its cash flow. 

**Who are the stakeholders?**
- The financial sector will use the forecast to the set operating budgets and to project cash flows.
- And the marketing team, who will have the opportunity to schedule promotions if it appears sales <br>
will be weak and will be able to better allocate budget among other marketing activities.

**What is the deliverable?**
- A dashboard with the information about the forecast.


> **ps: We will use the data to forecast the second quarter of 2018 and the third quarter will be our "production data".**

## Result

<p align="justify">
<strong>
In the beginning of this project, Olist moving average predictive model has been showing large errors,
even though it was getting lower. And for next Quarter, Olist needs a model with an error lower than 6.75%
(current moving average error).
</strong>
</p>

<img align="center" width="850" src="images/moving_average_baseline.png">

<p align="justify">
<strong>
The Project was successful, since We deacrease the error when predicting the sales from second quarter of 2018.
Now, Olist can forecast the 3rd quarter expecting an error of 5.7% above or below the real revenue value, instead of 6.7%.
And... Yes, after two months of trial the arima model has been showing to be a more accurate model.
</strong>
</p>

<img align="center" width="850" src="images/arima_vs_moving_average.png">

<p align="justify">
<strong>
</strong>
</p>

