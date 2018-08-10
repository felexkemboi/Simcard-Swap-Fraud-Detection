<h1 align="center"> Sim Card Swap Fraud Detection</h1>

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a7e80990559246c9b3e98782a42c241f)](https://www.codacy.com/project/syombuamadona/Sim-Card-Fraud-Detection./dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Madonahs/Sim-Card-Fraud-Detection.&amp;utm_campaign=Badge_Grade_Dashboard)

With an upsurge in cybercrimes related to Sim Card Swap fraud in developing countries, making fraud detection is a top priority. If we are able to estimate whether someone is going to commit Sim Card Fraud we can surely try to prevent it earlier. 


## Intro

Predicting the likelihood of Sim Card Swap Fraud Occurrence.
* **Analysis, Time series and prediction**
* **Train and test the data samples**
* **Normalize and summarize the data**

### Mode
Develop

### Implementations

* **Define Problem**
* **Prepare Data**
* **Evaluate Algorithms**
* **Improve Results**
* **Present Results**

### Usage

Sim Card Swap Fraud Detection.

### Model

* **Logistic Regression.** Logistic regression is the appropriate regression analysis to conduct when the dependent variable is dichotomous (binary). Like all regression analyses, the logistic regression is a predictive analysis.


## Data

### Sample Dataset

There can be many factors as to why someone would want to swap his/her sim card, I will just use few. The swap will be represented by 
```1``` and 
```0``` will represent not swapped. I created this data for this exercise.

Sample Output Representation: 

Swap | Not Swapped|
|------ |------:|
|1 | 0|

* **Sample Fake Data taken from Nairobi, Kenya constituencies**
Data is not given in this case so I decided to create my own, I will identify Locations here and not use the Location since we can have many customers living in the same Location.  

ID| Location                  | Age           | Subscriber Complaints   | Monthly Payments KSH |  Contacts |Swap Agent |
| ------------- | -------------         |:--------------------: | ----------------: | ---------------:| ---------------:| ---------------:|
|1|EastLeigh              |30                     | 3            |1200               |20| 0|
|2|Buru Buru              |18                     | 2          |60               |10 | 1|
|3|Donholm                |60                     | 1            |180               |44| 0|
|4|Lavington              |25                     | 2            |200               |30|0|
|5|Kileleshwa             |30                     | 2           |300               |10|1|
|6|Kitusuru               |45                     | 1            |900               |55|0|
|7|EastLeigh              |50                     | 3            |120               |20| 0|
|8|Buru Buru              |78                     | 1          |60               |10 | 1|
|9|Donholm                |26                     | 1            |180               |44| 0|
|10|Dagoretti            |23                     | 2            |200               |30|0|
|11|Kasarani             |33                     | 2            |300               |10|1|
|12|Kitusuru               |45                     | 1            |1200               |55|0|
|13|Umoja I              |30                     |2             |800               |100| 0|
|14|Pumwani              |33                     | 6           |60               |90 | 1|
|15|Umoja II              |26                     | 1            |180               |44| 0|
|16|Ngara            |23                     | 2            |2000               |30|0|
|17|Kariokor              |33                     | 2            |3000               |10|1|
|18|Mihang'o             |45                     | 1            |1200               |55|0|
|19|Makadara             |66                     |1              |50               |100| 0|
|20|Dandora Area III            |78                     | 1           |60               |10 | 1|
|21|Roysambu              |26                     | 1            |180               |44| 0|
|22|Mutu-ini            |23                     | 2           |2000               |30|0|
|23|Kilimani              |33                     | 2            |300               |10|1|
|24|Ruai             |45                     | 1           |1200               |55|0|
|25|Ridgeways            |66                     |1              |50               |100| 0|
|26|Riruta             |78                     | 1           |60               |10 | 1|
|27|Donholm              |26                     | 1           |180               |44| 0|
|28|Dandora Area IV          |23                     | 2            |200               |30|0|
|29|Bahati             |33                     | 2          |3000               |10|1|
|30|Karura              |45                     | 1            |1200               |55|0|



### Data Modeling 
Sample:
![data modelling](https://user-images.githubusercontent.com/11560987/43804440-aa75f892-9a61-11e8-9d0c-e5201c2cfd3d.PNG)

### Experiments
![swap_fraud](https://user-images.githubusercontent.com/11560987/43934745-60242a14-9c16-11e8-9fe9-97de48961f1e.png)

## Results
```0.625``` Not very bad since the data is Random.

### Training

### Testing
![accuracy](https://user-images.githubusercontent.com/11560987/43936810-fbcb2d2e-9c1f-11e8-87d4-7309bac805ac.png)





 Copyright [2018] [Madona Syombua]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
