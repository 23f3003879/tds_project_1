---
title: "Graded assignment 6"
topic_id: 169283
slug: "graded-assignment-6"
original_url: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283
downloaded_at: "2025-06-18T16:55:25.731077"
---

### Post #1 by Jivraj Singh Shekhawat on 2025-03-06T13:48:39.245Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/1

Please post any questions related to
[Graded Assignment 6 - Data Analysis](https://seek.onlinedegree.iitm.ac.in/courses/ns_25t1_se2002?id=25&type=assignment&tab=courses&unitId=23)

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline
2025-03-15T18:30:00Z

---

### Post #2 by Jivraj Singh Shekhawat on 2025-03-06T13:49:29.690Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/2

---

### Post #3 by Lovepreet Singh on 2025-03-02T11:45:12.668Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/3

The answer choices for questions 1 and 2 in graded assignment 6 are quite confusing. Both questions are single-select, yet three out of the four options are correct in each case. I’m unsure whether to choose one of the correct options or if the question is actually asking for the incorrect one. Could someone please clarify?

[@carlton](/u/carlton)

---

### Post #4 by Sarang Tambe on 2025-03-02T11:57:04.636Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/4

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

I have similar concern

For Q1, I used the following code:

print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = kk['price_retention'].corr(kk[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

And got the following output:

Pearson correlation for Karnataka between price retention and column
	Mileage (km/l)            : 0.03
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.04

Whereas options are below where none of them are correct.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fa9a2e601c94da84cbd25c406235d1009b204c.png)

> **Image Description**: The image shows a set of radio buttons with associated text labels. One radio button is selected. The labels are: 'Mileage: 0.95', 'AvgDistance: -0.05' (selected), 'Mileage: 0.21', and 'EngineCapacity: 0.17'. The labels appear to represent data features and their associated values, possibly representing coefficients or weights in a model.
image281×219 9.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fa9a2e601c94da84cbd25c406235d1009b204c.png)

Whereas for Q2 (Punjab and Yamaha) I used the following code:

print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') & (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = pb['price_retention'].corr(pb[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

and got the following answers:

Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l)            : 0.24
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.08

The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/51b03d00c3e962e6c4fc7fc64930a23e82500006.png)

> **Image Description**: The image shows a selection of radio button options, each labeled with a feature name and a numerical value. The options are: 'Mileage: 0.95', 'AvgDistance: -0.06', 'Mileage: 0.24' (selected), and 'EngineCapacity: -0.08'. The feature names seem relevant to a dataset about vehicles.
image278×216 9.19 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/51b03d00c3e962e6c4fc7fc64930a23e82500006.png)

---

### Post #5 by Carlton D'Silva on 2025-03-04T10:11:22.975Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/5

[@24f2006061](/u/24f2006061)
 We are looking into it. We will update based on our analysis. Thanks for letting us know.

Kind regards

---

### Post #6 by Abhinav on 2025-03-03T18:06:51.395Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/6

I used a python script to get the solution to quesiton 1 of week 6 graded assignment. It matches three options. Is this a bug or like we then need to analyze using the pearson coefficient to determine which option is the correct one

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630_2_690x131.png)

> **Image Description**: The image shows a multiple-choice question about the factors influencing motorcycle resale value in Delhi. The question asks to evaluate the impact of mileage, average daily distance traveled, and engine capacity on price retention for Yamaha motorcycles using the Pearson Correlation Coefficient. The student has selected "EngineCapacity: 0.13" as the answer.
image1383×263 25 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630.png)

---

### Post #7 by Wasim Ansari on 2025-03-07T17:12:28.199Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/7

Dear Sirs, Can we have some response on these issues related particularly to the questions 1 and 2 of Graded Assignment 6. It looks like multiple options are correct in the given options. Any guidance or hint, on how to arrive at the right answer will be helpful. Thanks and regards.
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

---

### Post #8 by Shashannk on 2025-03-08T15:17:03.743Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/8

Yeah…Even I am facing the same issue. Out of the 4 options provided, 3 options are correct in my case both for Q1 & Q2, but both these questions are single-choice questions. Kindly look into it and help us out
[@carlton](/u/carlton)
 !

---

### Post #9 by RAJ K BOOPATHI on 2025-03-10T07:56:14.493Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/9

I guess for both Q1 & Q2, we need to find the option that is having stronger correlation (positive/negative). Please correct me if I am wrong.

---

### Post #10 by Pradeep Mondal on 2025-03-11T06:42:12.463Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/10

Any updates on these? I am too facing the same issue.

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

---

### Post #11 by Udipth on 2025-03-11T17:42:32.616Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/11

In GA6 for first 2 questions 3 out of 4 options are correct. Even the question is not clearly asking anything. Kindly suggest are we supposed to select the wrong one

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04_2_690x190.png)

> **Image Description**: The image shows a multiple-choice question related to data analysis. The question asks about the impact of mileage, average daily distance, and engine capacity on motorcycle price retention in Maharashtra, India, using the Pearson Correlation Coefficient. The task is to evaluate which factor has the most influence based on the given correlation values. The options are "AvgDistance: 0.09", "Mileage: 0.95", "EngineCapacity: -0.02", and "Mileage: 0.12", with the option "Mileage: 0.95" selected.
image2083×575 47.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04.png)

---

### Post #12 by Shashannk on 2025-03-12T03:42:05.053Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/12

Kindly update us regarding the status of Q1 & Q2
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #13 by LAKSHAY on 2025-03-12T11:29:04.042Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/13

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

[@Saransh_Saini](/u/saransh_saini)

Dear TDS Team,

There are multiple issues in Graded Assignment 6 that require urgent attention:

Questions 1 and 2, along with their options, are ambiguous.

In Questions 3 and 4, I am unable to obtain an exact answer that matches any of the given options, despite trying multiple approaches, including the Excel regression method and other models in a Google Colab file.

The data for Question 10 is missing. I attempted to run the shapefile in QGIS, but it resulted in an error. Additionally, I searched for the shapefile of New York roads on official websites, but their servers are currently under maintenance.

The assignment deadline is approaching, but these issues remain unresolved. Kindly look into this matter at the earliest and provide a resolution as soon as possible.

Thank you for your support.

---

### Post #14 by Pradeep Mondal on 2025-03-12T13:30:00.912Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/14

Yes, there are no specifics in Q1 to Q4 and are quite ambiguous.

For instance:

forecast the 2027 resale value of the Hero - HF Deluxe in Gujarat, using historical data.

but is this talking about the average resale value as no input features are specified?

---

### Post #15 by LAKSHAY on 2025-03-12T14:11:15.210Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/15

Let’s wait for their response.

I submitted nearby option for Q3 and Q4

---

### Post #16 by Vivek Rekha Ashoka on 2025-03-12T14:36:43.739Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/16

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

[@Saransh_Saini](/u/saransh_saini)

Can you please provide any update ASAP as the deadline for this GA coincides with Quiz 2. With many ambiguities unresolved it’s hard to solve this and study for Quiz 2 (and do offline college work even though that’s not your problem).

Thanks

---

### Post #17 by Jivraj Singh Shekhawat on 2025-03-13T09:47:03.906Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/17

Hi
@all

Question intends you to select most correlated one.

Select option which is absolute highest.

---

### Post #18 by M v Sunil on 2025-03-14T14:30:12.725Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/18

[@Jivraj](/u/jivraj)
  - Can you please check answer choices for Q7 for GA6 where no choices are matching with the answer. The answer is coming to around 11.5 kms which is 11500 meters.

Q.A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction : (26.5596,-99.5336) ;Maple Fields Station : (26.4212,-99.4597);South Glen Crossing : (26.5962,-99.5243);Cedar Creek Retreat : (26.56,-99.4519) & Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance

---

### Post #19 by Shashank Tripathi on 2025-03-14T16:06:48.081Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/19

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b_2_690x197.png)

> **Image Description**: The image shows a multiple-choice question for a data science course. The question presents a scenario where the student is a strategic consultant for a motorcycle dealership and needs to analyze factors influencing resale value using Pearson Correlation Coefficient and price retention. The factors to evaluate are mileage, average daily distance, and engine capacity. The question asks for the Pearson Correlation Coefficient between the evaluated factors and price retention. The possible answers provided are correlation values for 'AvgDistance', 'EngineCapacity' and 'Mileage'. The answer selected is 'Mileage: -0.04'.
image1318×377 34.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b.png)

what to do if 3 options have same value -0.04 and all are correct?

---

### Post #20 by Khushi Shah on 2025-03-15T05:54:10.148Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/20

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

My question 7 for GA6 is :

A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance

Whose options provided are :

10418 meters

12287 meters

10965 meters

11149 meters

However, after trying all methods out there my distance comes out to be 6873 meters, I selected 10418 as the answer (closest approximation to 6873 meters)

I assume that the question must have been central command post to summit shores village (whose answer turns out to be 12287 meters)

Kindly look into the question, and let me know about the same (the destination from central command post)

---

### Post #21 by Pradeep Mondal on 2025-03-15T06:40:41.714Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/21

Have you succeeded in running the shape file for Q10? It seems to have some error.

[@lakshaygarg654](/u/lakshaygarg654)

---

### Post #22 by LAKSHAY on 2025-03-15T06:52:44.163Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/22

No,

I use google to get MTFCC code for given road segment and  after that mtfcc pdf to classify that road segment.

---

### Post #23 by Pradeep Mondal on 2025-03-15T07:29:51.684Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/23

I  downloaded the complete shape file zip from the
[census.gov](http://census.gov)
 site.

Here is the link:
[https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl_2024_36_prisecroads.zip](https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl_2024_36_prisecroads.zip)

It works fine in QGIS.

[@lakshaygarg654](/u/lakshaygarg654)

---

### Post #24 by Guddu Kumar Mishra  on 2025-03-15T07:50:50.896Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/24

they have not provide all the files needed to read that shp file in the question .

but your link includes them. thanks…

---

### Post #25 by LAKSHAY on 2025-03-15T09:26:43.798Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/25

I tried to access shapefile from official website 4-5 days ago, but server was under maintenance. I will check again Q10 after quiz 2.

Thanks for sharing.

---

### Post #26 by Kumar Rishabh  on 2025-03-15T15:30:01.842Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/26

My question 9 for GA6 is :

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

[![Screenshot 2025-03-15 205444](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/e/9e4fdb96e0a90caace70968fd4201106dc133169.png)

> **Image Description**: Here's a concise and factual description of the image:

The image shows Python code used to determine an optimal evacuation sequence for several communities based on their distances to a central command post. The code calculates distances using the 'haversine' function, which is imported. It defines coordinates for "OakParkTown," "EastSpringsSettlement," "EastFieldsJunction," "RedPointTown," and the "CentralCommandPostLocation."  It then calculates the distance from each community to the central post and stores these values in a dictionary called "distances". The 'sorted' function is used to order the communities based on their distances from the command post. Finally, the code prints the evacuation sequence, displaying the community name and its distance from the central command post, formatted to two decimal places and labeled with "km".  The output below the code block lists the communities in order of evacuation: 1. EastFieldsJunction - 7.84 km, 2. EastSpringsSettlement - 9.74 km, 3. RedPointTown - 9.81 km, and 4. OakParkTown - 11.76 km.
Screenshot 2025-03-15 205444878×668 38.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/e/9e4fdb96e0a90caace70968fd4201106dc133169.png)

[![Screenshot 2025-03-15 205456](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/0/0004348c8331f2b18dd055c7397be51c8c692902_2_690x189.png)

> **Image Description**: **Image Description**

The image presents a multiple-choice question related to an evacuation strategy. 

*   **Question:** It involves four communities and a Central Command Post with given coordinates. The question asks for the optimal evacuation sequence based on the "nearest community first" strategy, determining the nearest by shortest path distance.

*   **Options:** Four possible evacuation sequences are provided as multiple-choice answers.

*   **Code Snippet:** A Python code snippet is visible, importing the `haversine` library, likely used for distance calculations. Coordinates of each community and the central command post are defined as variables.
Screenshot 2025-03-15 2054561333×366 45.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/0/0004348c8331f2b18dd055c7397be51c8c692902.png)

I solved it in colab but options are getting mismatched there…kindly clarify this issue..

---

### Post #28 by M v Sunil on 2025-03-15T15:45:01.771Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/28

for the above question the options are None of these are matching and answer is around 11.5 kms

3848 meters

6265 meters

4110 meters

5106 meters

---

### Post #29 by Amala Natarajan  on 2025-03-15T18:10:33.693Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/29

For 7th Question in GA6 I got the answer 14265.93 Meters but the option I have in 7th are

6069 meters

7687 meters

6106 meters

7035 meters

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #30 by B R GIRI SUBRAHMANYA on 2025-03-16T03:40:13.358Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/30

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

for question 4, i have tried
=forecast
 and also
=forecast.ets
, both of them are not working. There are two columns for years. One is year of manufacturing, another is year of registration. which one to take.

for question 7, none of the options match. I am selecting the
MOST ACCURATE
 among the given options. Hope, it is correct

---

### Post #31 by Shashannk on 2025-03-16T08:26:37.649Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/31

Can anyone help me out on how to approach and solve the 10th question please!?

---

### Post #32 by LAKSHAY on 2025-03-16T14:22:53.458Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/32

Check the distances of other locations from the central location. One student found
Question 7
 of the
GA6 Option Set
 based on the distances of other points, which do not match the requirements of Question 7.

---

### Post #33 by Vidushi Singh on 2025-03-16T15:42:32.170Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/33

i have the same issue

---

### Post #34 by Vidushi Singh on 2025-03-16T15:43:51.901Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/34

yes i have the same issue

and i got the same answer and am give the same options

[@carlton](/u/carlton)
 sir what to do?

---

### Post #35 by Vidushi Singh on 2025-03-16T16:00:21.856Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/35

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

For 7th Question in GA6 I got the answer 14265.9275 Meters but the option I have in 7th are

6069 meters

7687 meters

6106 meters

7035 meters

---

### Post #36 by Muthupalaniappan on 2025-03-16T18:33:57.063Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/36

Hello Sir,

Can you please check if this is the right answer. As per email received from
[@carlton](/u/carlton)
 sir we should select the absolute maximum value.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/4/b468c32e53fddf462c583b8664f183dd7afe37aa_2_690x277.png)

> **Image Description**: The image shows a multiple-choice question from a data science course. The question asks about key factors influencing motorcycle resale value in Uttar Pradesh, focusing on mileage, average daily distance, and engine capacity's impact on price retention for Royal Enfield. The student incorrectly selected 'AvgDistance: -0.13'. The correct answer, as indicated by "Accepted Answers," is 'EngineCapacity: 0.09'. The student's score is 0.
image978×393 23.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/4/b468c32e53fddf462c583b8664f183dd7afe37aa.png)

Example : If we get answers as -0.3 and 0.2 then -0.3 is the right answer as it’s absolut value is maximum.

For the first question the correlation matrix is as follows,

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/5/c524c9f7645716e0fac9d8850df15c4c20af05dc_2_690x397.png)

> **Image Description**: Here's a concise description of the image for a data science student:

The image shows a correlation heatmap, visualized using a color-coded matrix. The matrix represents the correlations between four variables: "Mileage (km/l)", "Avg Daily Distance (km)", "Engine Capacity (cc)", and "Price Retention (%)". The color intensity indicates the strength and direction of the correlation (blue for negative, red for positive). The numerical values within the matrix represent the correlation coefficients. Notably, the diagonal elements are all 1.00, indicating a perfect correlation of each variable with itself.
image748×431 17.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/5/c524c9f7645716e0fac9d8850df15c4c20af05dc.png)

So shouldn’t it be -0.13?

---

### Post #37 by Carlton D'Silva on 2025-03-17T03:43:16.185Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/37

Thanks for the colour picture.

If you read the aforementioned email…

[![Screenshot 2025-03-17 at 9.09.55 am](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/0/f0a5df3069d591c0175e61d70123d9ffb4ec7e83_2_690x247.png)

> **Image Description**: This image is a screenshot of an email clarifying a question on GA6 in the Tools in Data Science course. The email states that questions 1 and 2 on GA6 were not clear and specifies that the answer is the Absolute Maximum Correlation Coefficient. An example is provided where the student may find options -0.3 and 0.2. The email emphasizes that -0.3 is the correct answer. The email further assures that even if the portal marks the student's answer as incorrect, the right scores will be pushed on the dashboard if the student chose the correct option.
Screenshot 2025-03-17 at 9.09.55 am1760×632 65.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/0/f0a5df3069d591c0175e61d70123d9ffb4ec7e83.png)

Kind regards (in colour
![:wink:](https://emoji.discourse-cdn.com/google/wink.png?v=14)
)

---

### Post #38 by M v Sunil on 2025-03-18T17:07:15.417Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/38

Thank you sir. i have got questions 1 and 2 both marked as 0.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/7/97636ac2d59c3df1caf852a42d90de4642e8ce6f_2_690x329.png)

> **Image Description**: The image shows a question about motorcycle resale value analysis. The question asks for the Pearson Correlation Coefficient between mileage (km/l) and price retention for KTM motorcycles in Maharashtra. The possible answers are:

*   'AvgDistance: 0.01'
*   'Mileage: 0.03'
*   'EngineCapacity: -0.06'
*   'Mileage: 0.95'

The submitted answer was incorrect. The correct answer is 'Mileage: 0.03'.
image962×459 29.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/7/97636ac2d59c3df1caf852a42d90de4642e8ce6f.png)

In my case Please note the above two questions are asked to calculate pearson correlation coefficient for KTM brand and for maharashtra and Karnataka states.

I have used excel to calculate the pearson correlation coefficient. Below the values I got for each question. Please verify.

|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for Karnataka||

-0.026685695

|pearson correlation coefficient between average distance travelled and Price retention for kTM for karnataka||

0.003953219

|pearson correlation coefficient between average Engine capacity and Price retention for kTM for karnataka||

-0.010839295

|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for maharashta||

0.029128825

|pearson correlation coefficient between average distance travelled and Price retention for kTM for Maharashtra||

0.013019585

|pearson correlation coefficient between average Engine capacity and Price retention for kTM for Maharashtra||

-0.056866212

---

### Post #39 by M v Sunil on 2025-03-18T17:14:25.559Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/39

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

Dear sirs,

I have question no 7 got marked as 0. Please check the question below and the haversine distance for the given post comes to around 11.5 kms which is not matccing with any of the options and I have selected the closest answer. please check and let me know.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/f/ff2eccf6d2263eb106345ce8b07d037c0a417845_2_690x390.png)

> **Image Description**: This image presents a multiple-choice question related to calculating the distance between two locations using the Haversine package. The question describes a scenario involving a wildfire and the need to coordinate evacuations from four remote communities. Location coordinates (latitude and longitude) are given for each community, as well as for the central command post. The task is to calculate the distance between the Central Command Post and Pine Pines Junction and select the most accurate distance from the given options. The correct answer is "5106 meters," as indicated in the accepted answers. The image also shows that a previous attempt at answering the question was incorrect, resulting in a score of 0.
image935×529 40.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/f/ff2eccf6d2263eb106345ce8b07d037c0a417845.png)

---

### Post #40 by Khushi Shah on 2025-03-19T17:09:05.009Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/40

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

I did raise the question 2 days before the GA6 Deadline and doing so again after being marked as incorrect

My question 7 was A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance

10418 meters

12287 meters

10965 meters

11149 meters

Whose right answer turned out 6873, however the answer pushed is 12287 meters, which is nowhere near the closest options (it would’ve been correct if the destination was summit shores village which isn’t the case with this question)

Also, my question 4 was :

As an investment analyst monitoring motorcycle resale values, develop a forecasting model to predict future resale prices by brand and segment, considering seasonality and long-term trends. Specifically, forecast the 2027 resale value of the Kawasaki - Ninja 300 in Tamil Nadu, using historical data.

134483

94774

150666

199711

Whose correct option (through different methods and algorithms) was approximately closest to 94774 and again answer pushed is 150666 which again turns out to be incorrect

So is the case with questions 1 and 2 (where answers aren’t pushed according to absolute values, but as conveyed earlier, I believe this shall be resolved)

Kindly look into it

Thanks and Regards

---

### Post #41 by PREMDEEP MAITI on 2025-03-20T14:49:56.474Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/41

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

In Q4 , neither which regression model to use is given nor the what random state to use is given. I tried linear regression, random forest regression but it is giving   answer which vary each time I compute, also, the option values are quite close.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/d/7dbfae953c7d9e015dbc80328ef657b813ba912d_2_690x250.png)

> **Image Description**: The image shows a multiple-choice question related to forecasting motorcycle resale values. The question asks to predict the 2027 resale value of a Hero - HF Deluxe in Punjab, using historical data. The multiple-choice options are numerical values: 194515, 185108, 142646, and 152609. The user selected 142646, but the feedback indicates this answer is incorrect, and the score is 0.
image1227×446 24 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7dbfae953c7d9e015dbc80328ef657b813ba912d.png)

---

### Post #43 by Jivraj Singh Shekhawat on 2025-03-22T12:34:00.092Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/43

@all

we are looking into problems with question 4, 6 and 10.

---

### Post #44 by Swati Kapoor on 2025-04-11T07:29:18.139Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/44

Hi,

Have the corrections been done on GA6 marks?

---

### Post #45 by Jivraj Singh Shekhawat on 2025-04-11T09:33:15.884Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/45

Yes, corrections have been done in Ga6 marks.

---

### Post #46 by Swati Kapoor on 2025-04-11T16:31:37.494Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/graded-assignment-6/169283/46

Just to confirm, were the answers shown on the portal correct because I’m getting the same score as shown in the portal.

---
