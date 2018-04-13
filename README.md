# Cow's Calving Prediction
BABY on the way
<br/>
<br/>

# Dataset
The dataset contains data of 1043 pregnant cows.<br/>
For each cow, the data is recorded every 2 hours (i.e. 1 period).<br/>
About 75% of the cows have 120 periods of data recorded (i.e. 10 days) before calving.<br/>
In the original file, each row of data represent a single period.<br/>
In the contatenated file, each row is a time-consequential piece of data of n consecutive periods, with the label y in the last column.
The label represent the closest period of the time interval to calving.<br/>
Different n size is provided in seperated files of "win_n", which n = 3, 6, 12.
<br/>
<br/>

# Run<br/>
1. Install pre-request<br/>
Python 3.3+<br/>
Xgboost<br/>
http://xgboost.readthedocs.io/en/latest/build.html<br/>
SK-learn<br/>
http://scikit-learn.org/stable/install.html<br/>
SK-learn imbalanced-learn<br/>
http://contrib.scikit-learn.org/imbalanced-learn/stable/index.html<br/>
Jupyter notebook is highly-recommended for step-by-step observation.<br/>


2. Get started<br/>
Unzip the contatenated data in the repo<br/>
Open Cow_Alarm_boundary.ipynb in jupyter notebook<br/>
Run!


