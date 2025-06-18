---
title: "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]"
topic_id: 165959
slug: "ga4-data-sourcing-discussion-thread-tds-jan-2025"
original_url: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959
downloaded_at: "2025-06-18T15:56:17.987520"
---

### Post #1 by Anand S on 2025-01-31T16:13:36.640Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/1

Please post any questions related to
[Graded Assignment 4 - Data Sourcing](https://exam.sanand.workers.dev/tds-2025-01-ga4)
.

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline:
Sunday, February 9, 2025 6:29 PM

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

[@carlton](/u/carlton)

---

### Post #2 by Anand S on 2025-01-31T16:14:00.363Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/2

---

### Post #3 by Guddu Kumar Mishra  on 2025-02-01T07:54:31.100Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/3

[![Screenshot 2025-02-01 132301](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/0/0007976ca3410205e4fa403a71b9a1ac79bf5192.png)

> **Image Description**: The image displays a question "What is the JSON data?". Below the question, a partial JSON object is presented, containing the keys "id", "title", "year", and "rating" with corresponding string and numeric values. The JSON object is followed by a comma. An error message "Error: Expected: 2.9 Actual: 2.9" is visible at the bottom of the image.
Screenshot 2025-02-01 132301331×314 12.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/0/0007976ca3410205e4fa403a71b9a1ac79bf5192.png)

what is the error here?? sir
[@Jivraj](/u/jivraj)

---

### Post #5 by Vikram Jeet on 2025-02-01T18:26:06.664Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/5

I have the Same doubt.

---

### Post #6 by Anand S on 2025-02-02T05:30:16.417Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/6

[@22f3001315](/u/22f3001315)

[@21f3002277](/u/21f3002277)

[@24ds2000024](/u/24ds2000024)
 – please try again after reloading the page. The new error message will be clearer, like this:

Error: At [0].rating: Values don't match. Expected: "7.4". Actual: 7.4

FYI, we expect all values as strings, not numbers. That’s because the year can sometimes be a range for a TV series (e.g. 2021 - 2024) and the rating can sometimes be missing.

---

### Post #7 by Sakthivel S on 2025-02-02T05:41:42.494Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/7

In Question 2, it is specifically said to filter the movies however, the evaluator is expecting a TV show there. Should we also include TV shows now?

edit:  This is an everchanging dataset, so will our answers be saved, as, this json might not be in this order tomorrow?

---

### Post #8 by Anand S on 2025-02-02T05:45:48.804Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/8

[@23f2000237](/u/23f2000237)
 A good point. Yes, please include
all
 titles. I’ve reworded the question accordingly. Thanks.

---

### Post #9 by VIKASH PRASAD on 2025-02-02T06:31:48.149Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/9

Q3. How to handle the error ?
[@Jivraj](/u/jivraj)

TypeError: Cannot read properties of null (reading ‘0’)

http://127.0.0.1:8000/api/outline?country=Russia

{"outline":"## Contents\n# Russia\n## Etymology\n## History\n### Early history\n### Kievan Rus'\n### Grand Duchy of Moscow\n### Tsardom of Russia\n### Imperial Russia\n#### Great power and development of society, sciences, and arts\n#### Great liberal reforms and capitalism\n#### Constitutional monarchy and World War\n### Revolution and civil war\n### Soviet Union\n#### Command economy and Soviet society\n#### Stalinism and modernisation\n#### World War II and United Nations\n#### Superpower and Cold War\n#### Khrushchev Thaw reforms and economic development\n#### Period of developed socialism or Era of Stagnation\n#### Perestroika, democratisation and Russian sovereignty\n### Independent Russian Federation\n#### Transition to a market economy and political crises\n#### Modern liberal constitution, international cooperation and economic stabilisation\n#### Movement towards a modernised economy, political centralisation and democratic backsliding\n#### Invasion of Ukraine\n## Geography\n### Climate\n### Biodiversity\n## Government and politics\n### Political divisions\n### Foreign relations\n### Military\n### Human rights\n### Corruption\n### Law and crime\n## Economy\n### Transport and energy\n### Agriculture and fishery\n### Science and technology\n#### Space exploration\n### Tourism\n## Demographics\n### Language\n### Religion\n### Education\n### Health\n## Culture\n### Holidays\n### Art and architecture\n### Music\n### Literature and philosophy\n### Cuisine\n### Mass media and cinema\n### Sports\n## See also\n## Notes\n## References\n## Sources\n## Further reading\n## External links"}

error resolved

---

### Post #11 by Guddu Kumar Mishra  on 2025-02-02T10:06:04.746Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/11

in my output which is correct

there are two \n instead of one .

---

### Post #12 by VIKASH PRASAD on 2025-02-02T10:38:33.945Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/12

it should one(for newline), my code is working now

---

### Post #13 by Vikram Jeet on 2025-02-02T11:54:35.123Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/13

Dear Sir,

I was at 2/10 yesterday. After pasting JSON file of IMDB & reloading as suggested My marks updated to 3/10. Kindly confirm if I have got whole of IMDB question.

---

### Post #14 by VIKASH PRASAD on 2025-02-02T13:00:36.181Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/14

Q4. How to handle the error ?
[@Jivraj](/u/jivraj)

Error: At 2025-02-05: Values don’t match

---

### Post #15 by K Hari Prasath on 2025-02-03T00:37:01.721Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/15

There is no submit button is available in below screen. Is it fine to save the link url only. Please clarify (unless we click submit button the log of Graded Assignment 4 remains red)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/9/699d94f19d189a93a67fb813a5eeed3d1f73abf3_2_690x388.png)

> **Image Description**: The image displays the "Graded Assignment 4" page for the Jan 2025- TDS (Tools in Data Science) course, located under "Module 4: Data Sourcing." The due date for the assignment is 2025-02-09, 23:59 IST. Students are permitted multiple submissions before the deadline, with the final attempt considered for grading.

Instructions for accessing the graded assignment include:
*   Disabling ad blockers.
*   Enabling cookies for authentication; cookie/tracker blocking extensions may prevent access.
*   Ensuring Javascript is enabled.
*   Using Chrome Browser, which is recommended.
*   Disabling any browser extensions that may interfere.
*   Addressing potential issues from overly aggressive anti-virus software or corporate proxies/network policies, suggesting trying mobile internet if necessary.
*   Requiring use of a Student ID (e.g., 22F3xxxxxx@ds.study.iitm.ac.in) for the graded assignment.

The assignment is accessible via the link: `https://exam.sanand.workers.dev/tds-2025-01-ga4`. No code snippets, question statements, commands, graphs, or tables are visible in this view.
image1920×1080 337 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/699d94f19d189a93a67fb813a5eeed3d1f73abf3.png)

---

### Post #16 by Sakthivel S on 2025-02-03T10:06:13.753Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/16

I have a doubt regarding the bonus mark. Suppose someone were to get 10/10 in the assignment, would their mark be recored as 11/10 or just 10?

(Assuming they have interacted in this thread)

---

### Post #17 by Anand S on 2025-02-03T11:16:46.279Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/17

Anyone scoring 10/10 on GA4 and replying with a
relevant
 message on this thread will get 11/10
![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12)

---

### Post #18 by K Hari Prasath on 2025-02-03T11:38:10.970Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/18

For me I just made filter of rating between 2 and 7 in site and typed in console as per  video. with that data got in console worked fine.

copy the coding and save in place use it for data extract when finally submit

---

### Post #19 by Maheshwar Ture on 2025-02-03T16:46:46.395Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/19

For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1b7f2ec2868a09d8b4ed3fc50afa02f8416dad93_2_690x143.png)

> **Image Description**: The image displays a user interface for a search function. On the left, a "Search filters" section is visible, with an "Expand all" option. Under the filters, a "Title name" input field contains the text "Un matrimonio di troppo". A "Title type" filter is partially visible below it. On the right, a "No results found" message is displayed, accompanied by a grey icon of a magnifying glass with a cross. The text further advises, "Please adjust your filters or start a new search."
image1414×295 19 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/b/1b7f2ec2868a09d8b4ed3fc50afa02f8416dad93.png)

---

### Post #20 by Nilay Chugh on 2025-02-04T03:28:57.489Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/20

how to get the BBC weather API key?

---

### Post #21 by Joel Jeffrey on 2025-02-04T05:47:12.930Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/21

Just a quick query on the Bonus mark.

Would this be added to the final grade? Say for example, Someone get a full score in the first 4 assignments. So the total comes up to 39.5/39.5, and would be converted to 0.15 or 15 marks. Would the bonus mark be additional to that 15 or would the score change to 40.5/39.5 and then get normalised to 15?

---

### Post #22 by Anand S on 2025-02-04T06:15:20.501Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/22

[@JoelJeffrey](/u/joeljeffrey)
 It will be added to the GA4 marks, not the final grade. So, it’s roughly worth 0.15% on the total - not a full 1% on the total.

---

### Post #23 by Tushar Jalan  on 2025-02-04T07:43:14.240Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/23

you can go and login using your email id in this below mentioned link

[https://home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys)

---

### Post #24 by Joel Jeffrey on 2025-02-04T08:14:26.582Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/24

Error: At [10].year: Values don’t match. Expected: "2025– ". Actual: “2025–”

Can someone help me with this?

Thanks

Edit: Resolved

---

### Post #25 by K Hari Prasath on 2025-02-04T09:44:51.731Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/25

Q8 I got the Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in. the .yml file contains the following

" name: Daily Commit

on:

schedule:

- cron: ‘0 12 * * *’ # Runs daily at 12:00 PM UTC

workflow_dispatch:  # This allows manual trigger

jobs:

commit:

runs-on: ubuntu-latest

steps:
- name: Checkout repository
  uses: actions/checkout@v2

- name: Make a dummy change with email 23f2003853@ds.study.iitm.ac.in in the commit
  run: |
    echo "This is a daily commit" > daily_commit.txt
    git config --global user.email "23f2003853@ds.study.iitm.ac.in"
    git config --global user.name "23f2003853"
    git add daily_commit.txt
    git commit -m "Daily commit from 23f2003853@ds.study.iitm.ac.in"
    git push"

[@Jivraj](/u/jivraj)
 can help me to fix the issue

---

### Post #26 by Sakthivel S on 2025-02-04T14:53:18.679Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/26

Have a step with your email id as its name. (Instead of checkout repository)

Also make sure you give read and write permission so it commits without any error

---

### Post #27 by Daksh Agarwal on 2025-02-04T16:03:52.872Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/27

name: Daily Commit

on:

schedule:

- cron: ‘0 0 * * *’  # Runs once a day at midnight UTC

workflow_dispatch:  # Allows manual triggering of the workflow

jobs:

commit:

runs-on: ubuntu-latest

steps:
- name: Checkout repository
  uses: actions/checkout@v3

- name: Make daily commit by 23f3000264@ds.study.iitm.ac.in
  run: |
    echo "Daily commit by 23f3000264@ds.study.iitm.ac.in" >> daily_commit.txt
    git add index.html
    git commit -m "Daily commit"
    git push
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

sir this is my code and im getting a error in this

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/7/f740be2ffaea5957ca053368c20e28f7045362d0.png)

> **Image Description**: An image displays a user interface prompt to "Enter your repository URL (format: https://github.com/USER/REPO):". Below this prompt, an input field, highlighted with a red border, contains the URL "https://github.com/dakshagarwal76/daily-update". Beneath the input field, a red error message states: "Error: No executed job step matches 23f3000264@ds.study.iitm.ac.in". The background is dark.
image703×137 9.75 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/7/f740be2ffaea5957ca053368c20e28f7045362d0.png)

---

### Post #28 by Maheshwar Ture on 2025-02-04T16:15:39.892Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/28

dont remove the space after year- for example “year”: "2023- "

---

### Post #29 by Ansh bansal on 2025-02-04T22:17:37.626Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/29

Please anyone help me in doing q1 , my doubt is when i open the website
[Advanced search](http://www.imdb.com/search/title)
 , i have click on movies and then do the coding part if not how to select titles of the movies as there is no movies on the page.

---

### Post #31 by Ansh bansal on 2025-02-04T23:37:55.943Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/31

In q4 i got this error someone pls expalin “Error: At root: Property name mismatch”

---

### Post #33 by Tushar Jalan  on 2025-02-05T06:21:04.530Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/33

Student marks - Group 100

| Maths | Physics | English | Economics | Biology |
| ----- | ------- | ------- | --------- | ------- |
| 48    | 51      | 15      | 47        | 65      |
| 74    | 70      | 23      | 17        | 70      |
| 81    | 50      | 59      | 45        | 51      |
| 80    | 63      | 43      | 99        | 28      |
| 85    | 72      | 82      | 79        | 14      |
| 76    | 50      | 15      | 55        | 13      |
| 21    | 86      | 25      | 14        | 64      |
| 54    | 72      | 98      | 30        | 96      |
| 15    | 24      | 67      | 19        | 35      |
| 68    | 82      | 16      | 70        | 67      |
| 64    | 94      | 42      | 26        | 10      |
| 31    | 79      | 98      | 21        | 24      |
| 90    | 32      | 88      | 39        | 56      |
| 36    | 72      | 79      | 86        | 96      |
| 91    | 61      | 57      | 28        | 23      |
| 81    | 40      | 95      | 74        | 30      |
| 60    | 31      | 66      | 36        | 83      |
| 81    | 16      | 67      | 25        | 90      |
| 40    | 96      | 57      | 84        | 47      |
| 53    | 92      | 10      | 10        | 82      |
| 33    | 40      | 20      | 68        | 95      |
| 95    | 48      | 69      | 24        | 42      |
| 93    | 84      | 79      | 33        | 17      |
| 40    | 81      | 39      | 31        | 60      |
| 31    | 44      | 96      | 78        | 54      |
| 58    | 21      | 98      | 58        | 44      |
| 47    | 22      | 91      | 77        | 46      |
| 61    | 93      | 75      | 25        | 79      |
| 18    | 19      | 47      | 20        | 58      |
| 77    | 51      | 28      | 14        | 97      |

This is the piece of  markdown that is being generated for the last question of ga4.Even after using the prettier of the mentioned version i am getting incorrect answer.

Anyone like to help.

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

[@s.anand](/u/s.anand)

---

### Post #34 by Joel Jeffrey on 2025-02-05T06:25:36.507Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/34

For Q10, I am extracting the text first using PyMuPDF (fitz) and then using markdownify to convert it to markdown and finally prettier. However despite trying changing it from PyMuPDF to other text extraction libraries, I end up getting

Incorrect. Try Again

errors

---

### Post #35 by Sakthivel S on 2025-02-05T06:40:23.675Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/35

I think you have used the wrong document, because, this is the marks list for Q9

---

### Post #36 by Tushar Jalan  on 2025-02-05T07:00:03.570Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/36

which tool you are using ?

---

### Post #37 by Naman Gupta on 2025-02-05T07:10:34.357Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/37

HOW TO GET BBC API KEY

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/2/e2e304a859382b51deb2992386d3dfc8cbae3a77_2_690x317.png)

> **Image Description**: The image displays a data science assignment or task interface. The header indicates "Due Sun, 9 Feb, 2025, 11:59 pm IST" and a "Score: 1/10".

The task is broken down into three steps:
1.  **API Integration and Data Retrieval:** Fetch weather forecast for Tel Aviv using the BBC Weather API, first obtaining a `locationId` from a locator service and including query parameters like API key, locale, filters, and city.
2.  **Weather Data Extraction:** Retrieve forecast data using the obtained `locationId` from a weather broker API endpoint.
3.  **Data Transformation:** Extract `issueDate` and `enhancedWeatherDescription` from the `forecasts` array in the API response. Create a JSON object where `issueDate` is the key and `enhancedWeatherDescription` is the value.

An example of the desired JSON output format is provided, showing date keys mapping to weather descriptions (e.g., `"2025-01-01": "Sunny with scattered clouds"`).

Below the instructions, a question is posed: "What is the JSON weather forecast description for Tel Aviv?". An empty input field is visible, accompanied by a "SyntaxError: Unexpected end of JSON input" message, indicating an issue with a previously attempted or expected JSON input.
image1888×868 75.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/2/e2e304a859382b51deb2992386d3dfc8cbae3a77.png)

---

### Post #38 by Tushar Jalan  on 2025-02-05T07:21:08.047Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/38

in the bbc question what should be starting and the ending date

---

### Post #39 by Guddu Kumar Mishra  on 2025-02-05T08:32:35.339Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/39

you dont need the key you need that file used in 2 lecture videos just look for it.

![:+1:](https://emoji.discourse-cdn.com/google/+1.png?v=12)

---

### Post #40 by K Hari Prasath on 2025-02-05T09:55:21.354Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/40

Please find below the screen shot showing the committed with step name my iitm email id

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/a/7ae7951e4e7d3ea76248632715b376e23d3b0a76_2_690x387.png)

> **Image Description**: The image displays a GitHub Actions workflow run page within a web browser. The URL `github.com/23f2003853/workflows/actions/runs/13154595741/workflow` is visible in the address bar. The left panel indicates a successful workflow run for `23f2003853@ds.study.iitm.ac.in` and highlights the 'Workflow file' section. The main content area shows the YAML configuration for the `daily-commit.yml` workflow. The workflow is named `23f2003853@ds.study.iitm.ac.in` and is configured to run `on` a `schedule` using a `cron` expression (`'0 10 * * *'`) for daily execution at 10:00 AM UTC, and also allows `workflow_dispatch` for manual triggering. It requests `contents: write` permissions. A job named `daily-commit` is defined to run on an `ubuntu-latest` environment. This job includes steps to check out the repository using `actions/checkout@v3` and to `Configure Git`.
image1366×768 79.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/a/7ae7951e4e7d3ea76248632715b376e23d3b0a76.png)

But the answer says

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/9/d9fb33c07548b8cb0f740e38585a1b1b277de791.png)

> **Image Description**: The image displays a form related to GitHub Actions workflows, presenting both instructions and an input field with an error.

The instructions for creating a workflow state it must "Be located in `.github/workflows/` directory".
Subsequent instructions for validating the workflow after creation are:
*   "Trigger the workflow and wait for it to complete"
*   "Ensure it appears as the **most recent action** in your repository"
*   "Verify that it creates a commit during or within 5 minutes of the workflow run"

Below these instructions, there is an input field for "your repository URL", with the specified format `https://github.com/USER/REPO`. The input field currently contains `https://github.com/23f2003853/workflows` and is visually marked in red with an error icon. A red error message beneath the input reads: "Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in". A blue "Check" button is visible at the bottom of the form.
image602×164 21 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/9/d9fb33c07548b8cb0f740e38585a1b1b277de791.png)

Please help to fix the issue

---

### Post #41 by K Hari Prasath on 2025-02-05T10:00:47.264Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/41

Still the issue is there. Have posted screen shot.

---

### Post #42 by K Hari Prasath on 2025-02-05T10:03:31.480Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/42

what Mr. Sakthivel S said is correct. could you tell me what tool did you use to convert .md file. I have done as per links in question and used chatgpt also. but nothing is correct

---

### Post #43 by Tushar Jalan  on 2025-02-05T11:03:45.090Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/43

Please give the solution if you got any…have you been able to solve the bbc weather question?

---

### Post #45 by Ansh bansal on 2025-02-05T14:04:46.408Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/45

[@s.anand](/u/s.anand)

[@carlton](/u/carlton)

In question 8 i got error

“Enter your repository URL (format:
[https://github.com/USER/REPO](https://github.com/USER/REPO)
):

[https://github.com/Ansh205/github-actions](https://github.com/Ansh205/github-actions)

Error: No workflow runs found”

But i have successfully commited

[![Screenshot 2025-02-05 193233](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/e/4e52f03ba17a95acf60684f40c4115cf1a385153_2_690x302.png)

> **Image Description**: The image displays a dark-themed user interface showing a list of four workflow runs. The top left corner is labeled "All workflows" with a subtitle "Showing runs from all workflows." A search bar labeled "Filter workflow runs" with a magnifying glass icon is present in the top right.

Below the main title, "4 workflow runs" indicates the total number of entries. The runs are presented in a list or table format with columns labeled "Event," "Status," "Branch," and "Actor," each having a dropdown arrow.

Each row represents a "Daily Commit Workflow."
- The most recent run, "Daily Commit Workflow #4," initiated "Manually run by Ansh205," shows a green checkmark indicating success, ran on the "main" branch, completed "5 minutes ago" in "19s."
- The three preceding runs, "Daily Commit Workflow #3," "#2," and "#1," also initiated "Manually run by Ansh205," each display a red 'X' indicating failure. All three ran on the "main" branch. Their completion times and durations are "37 minutes ago" (14s), "54 minutes ago" (11s), and "1 hour ago" (14s) respectively.
- Each run entry includes a calendar icon next to the time elapsed and a stopwatch icon next to the duration. A vertical ellipsis icon is present at the end of each row, suggesting further options.
Screenshot 2025-02-05 1932331462×642 38.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/e/4e52f03ba17a95acf60684f40c4115cf1a385153.png)

---

### Post #46 by Chinnam Goutham Nischay on 2025-02-05T17:37:33.037Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/46

Just follow the links and notebooks given in the references.

---

### Post #47 by Shouvik Roy  on 2025-02-06T03:41:58.369Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/47

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

sir i have submitted my GA3 but its showing not submitted why?

[![Untitled design](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b88fa681fcbf676c93202b79b2bcb23d71df28a4_2_353x500.png)

> **Image Description**: The image displays an online assessment interface for "TDS 2025 Jan GA3 - Large Language Models." The assessment, "Graded Assignment 3" for "Module 3: Large Language Models," was due on "Wed, 5 Feb, 2025, 11:39 PM IST" and is currently marked as "Not Submitted" with no score recorded in the assignment table.

Instructions for the assessment are provided:
1.  Students can use any resources, including the internet, ChatGPT, friends, libraries, or frameworks.
2.  Answers can be checked regularly by pressing the 'check' button.
3.  Progress can be saved multiple times using the 'save' button, with the last saved submission being evaluated.
4.  Reloading the page is permissible as answers are saved in the browser.
5.  It is explicitly stated that "hacking the code for this quiz" to obtain answers is "allowed."
6.  A note specifies that multiple exams will run simultaneously within this assessment, and all must be running concurrently while checking or saving answers.

The user is logged in as "23F1001340DB.study.iitm.ac.in." A "Recent saves" section shows a previous save from "Mon, 2/5/2025, 4:04 PM" with a "Score: 5.5." A Discord link is available for questions. The interface also features 'Check all' and 'Save' buttons in the top header.
Untitled design1414×2000 314 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b88fa681fcbf676c93202b79b2bcb23d71df28a4.png)

---

### Post #48 by K Hari Prasath on 2025-02-06T04:24:58.055Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/48

[@s.anand](/u/s.anand)
 Sir no submit button is available. On the top of it say submission is required. Could you clarify us

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/8/d851d2f20816a37ba11ac45568e329bf914ea0b4.png)

> **Image Description**: The image displays the "Graded Assignment 4" page for a "Jan 2025- TDS" (Tools in Data Science) course on an online learning platform. The assignment is due on 2025-02-09, 23:59 IST. Students can submit multiple times, with the last submission before the deadline considered for grading.

Instructions for accessing the assignment include:
- Disabling ad blockers.
- Enabling cookies and Javascript.
- Using Chrome Browser.
- Disabling potentially interfering browser extensions or anti-virus software.
- Addressing corporate proxy or network policy issues by trying alternative internet connections.

A critical instruction states that students must use their Student ID (e.g., 22f3xxxxxx@ds.study.iitm.ac.in) for the graded assignment, otherwise, their score will not be evaluated.

The direct link to the assignment is provided as: `https://exam.sanand.workers.dev/tds-2025-01-ga4`.

The left sidebar indicates the assignment is part of "Module 4: Data Sourcing" and lists other course modules: "Course Introduction," "Module 1: Development Tools," "Module 2: Deployment Tools," "Module 3: Large Language Models," and "Project 1."
image690×388 46.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/8/d851d2f20816a37ba11ac45568e329bf914ea0b4.png)

---

### Post #49 by VIKASH PRASAD on 2025-02-06T04:57:11.068Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/49

what’s your directory structure, is it (.github/workflows/<filename.yaml>) and public

---

### Post #50 by K Hari Prasath on 2025-02-06T05:10:27.978Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/50

As per instruction we need to create a directory in that we should have .yml file. But I tried with there were two issues (1) Github has not allowed to run the file (as there was no menu is available to run manually) (I checked with Copolit AI it says it is not correct to have cron jobs in a directory, I am not sure) (2) when I submit the url to iitm I got the following error

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/f/6fd287b966b7a580fabd12762ac0e6592b0190b5.png)

> **Image Description**: The image displays instructions for a workflow, likely within a GitHub environment. The instructions include:
*   Workflow files must be located in the `.github/workflows/` directory.
*   After creating the workflow, users should trigger it, ensure it is the "most recent action" in their repository, and verify it creates a commit within 5 minutes of the run.

Below the instructions, there is a prompt to "Enter your repository URL" with an example format (`https://github.com/USER/REPO`). An input field contains the URL `https://github.com/23f2003853/workflows`. This input field is highlighted with a red border and an error icon.

Beneath the input field, a blue-highlighted error message states: "YAMLParseError: Implicit keys need to be on a single line at line 1, column 1: <!DOCTYPE html>".
image602×135 24.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/f/6fd287b966b7a580fabd12762ac0e6592b0190b5.png)

I removed the directory and submitted the same url I got the following error

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7ba477a0682a8af40b3fbd474ee66eff108d2ab8.png)

> **Image Description**: The image displays a web interface for entering a GitHub repository URL. The prompt reads "Enter your repository URL (format: https://github.com/USER/REPO):". An input field contains the URL "https://github.com/23f2003853/workflows" and is highlighted with a red border and an exclamation mark icon, indicating an error. Below the input field, a red error message states: "Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in". A blue "Check" button is visible at the bottom.
image1122×184 5.81 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7ba477a0682a8af40b3fbd474ee66eff108d2ab8.png)

I do not know what to do next. Can TA help us

---

### Post #51 by Carlton D'Silva on 2025-02-06T05:14:57.186Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/51

The submission is on the Actual assignment page like for all the previous GAs in TDS. This is the
ONLY
 valid submission button for GA1, GA2, GA3, GA4, GA5.

[![Screenshot 2025-02-06 at 10.43.15 am](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/5/758c516fa4ae8cd2e15a7c42c3059ef4465cf544_2_606x500.png)

> **Image Description**: The image displays a web-based examination or assessment interface. The URL `exam.sanand.workers.dev/tds-2025-01-ga4` indicates the platform. The top bar shows `[Admin]` access, a deadline of `Sun, 9 Feb, 2025, 11:59 pm IST`, a `Score: 0`, a `Check all` button, and a `Save` button (highlighted by a red arrow). The main content area features the title "TDS 2025 Jan GA" (with a red line indicating a strike-through annotation) and a section titled "Instructions". Key instructions include: checking and saving answers regularly using embedded `Check` and `Save` buttons, answers being saved in the browser allowing safe reloading, advice for browser performance, permission to "Use anything" (any resources), and a statement that "It's hackable."
Screenshot 2025-02-06 at 10.43.15 am1390×1146 113 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/5/758c516fa4ae8cd2e15a7c42c3059ef4465cf544.png)

---

### Post #52 by VIKASH PRASAD on 2025-02-06T05:26:10.352Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/52

try with this

name: Set up Git user (23f2003853@ds.study.iitm.ac.in)

run: |

git config --global user.name “GitHub Actions Bot”

git config --global user.email “23f2003853@ds.study.iitm.ac.in”

---

### Post #53 by Ansh bansal on 2025-02-06T05:42:11.105Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/53

Thank you  for your help , my repo was not public before and can you also help me in g4 i got this “Error: At root: Property name mismatch”

---

### Post #54 by VIKASH PRASAD on 2025-02-06T05:50:34.894Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/54

In g4 which Question have that error you are getting

---

### Post #55 by Tushar Jalan  on 2025-02-04T09:14:53.054Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/55

In the last two question of the ga,it is mentioned including both groups.so what is the meaning of this .

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/a/1a9317fe7d6814de3d65512fa7b3121c5a3c8710_2_690x255.png)

> **Image Description**: The image displays a data science task titled "Your Task". It identifies a PDF file, "q-extract-tables-from-pdf.pdf", containing a table of student marks across Maths, Physics, English, Economics, and Biology.

The primary objective is to calculate the total Biology marks for students who achieved 17 or more marks in Physics and belong to groups 43-66 (inclusive).

The task outlines a four-step process:
1.  **Data Extraction**: Retrieve data from the PDF using parsing libraries such as Tabula, Camelot, or PyPDF2, converting it into a workable format (e.g., CSV, Excel, or DataFrame).
2.  **Data Cleaning and Preparation**: Convert extracted marks to numerical data types.
3.  **Data Filtering**: Identify students meeting the criteria of scoring 17 or more in Physics and being in groups 43-66.
4.  **Calculation**: Sum the Biology marks of the filtered students.

The text also highlights the broader benefits of automating student mark analysis for educational institutions, including identifying performance trends, allocating resources, enhancing reporting efficiency, and supporting data-driven strategies. The specific question for which an answer is sought is repeated at the bottom of the image.
image1622×601 85.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/a/1a9317fe7d6814de3d65512fa7b3121c5a3c8710.png)

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

---

### Post #56 by Carlton D'Silva on 2025-02-06T06:09:22.483Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/56

Hi Tushar,

If you looked at the PDF you might have realised that students have been grouped. The question gives you a range for the groups 43-66. Including both groups implies both group 43 and 66 are included in your calculation.

kind regards

---

### Post #57 by Ansh bansal on 2025-02-06T06:15:48.956Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/57

Question 4 "

Sample output

{

“25-02-04”: “Sunny intervals and light winds”,

“25-02-05”: “Light rain and light winds”,

}

Error: At root: Property name mismatch"

---

### Post #58 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-06T06:19:39.985Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/58

Hi, even i’m facing the same issue,

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/1/a17230380d3428649017c6e760ea0ece0b99bf39_2_690x315.png)

> **Image Description**: The image displays a GitHub repository's "Actions" tab, specifically detailing a completed workflow run titled "Daily Commit #10". The repository name is "DigvijaysinhChudasamaIITM / TDS_GA_4".

The summary shows the workflow was manually triggered 16 hours ago by "DigvijaysinhChudasamaIITM" on the "main" branch (commit `c9aef97`). Its status is "Success", with a total duration of "18s" and no artifacts.

On the left sidebar, "Summary" is selected under the workflow details. Under "Jobs," "daily-commit" is listed with a success checkmark. The right pane further details a "daily-commit.yml" workflow, identified as `orc workflow_dispatch`, which completed successfully in "7s".
image1564×715 34.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/1/a17230380d3428649017c6e760ea0ece0b99bf39.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/7/67b187b35695e941e3bdf04461e4c4fa050c6e4d_2_690x317.png)

> **Image Description**: The image displays a GitHub repository interface, specifically the "Code" tab for the `DigvijaysinhChudasamalTM / TDS_GA_4` repository.

On the left, a file navigation panel shows the `main` branch is selected, and the `.github/workflows` directory contains two files: `daily-commit.yml` and `daily-commit.txt`.

The main content area displays the `daily-commit.yml` file, which is a GitHub Actions workflow configuration. Key elements of the workflow include:
*   **Name:** "Daily Commit"
*   **Triggers:** `on:` block specifying a `schedule` (cron job to run at 00:00 UTC daily) and `workflow_dispatch` (allowing manual triggers).
*   **Job:** `daily-commit`
*   **Runner:** `runs-on: ubuntu-latest`
*   **Steps:**
    1.  "Checkout repository" using `actions/checkout@v4`.
    2.  "Set up Git configuration" using `git config --local user.email` and `user.name` (set to GitHub Actions).
    3.  "Create a file with a daily commit message" using `echo "This is an automated daily commit" >> daily-commit.txt`.
    4.  A partially visible step for "Commit changes".

Above the code, commit information indicates the last commit message was "Update daily-commit.yml -- added pull repo code", made 17 hours ago. A banner also suggests "Code 55% faster with GitHub Copilot".
image1916×882 65.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/7/67b187b35695e941e3bdf04461e4c4fa050c6e4d.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/d/5d7f290214dcf1065f3b373c28d04671ef69f7c6_2_690x137.png)

> **Image Description**: The image displays a dark-themed user interface, likely a web form or application, presenting instructions and an error related to a GitHub workflow.

The top section, titled "After creating the workflow:", lists three bullet points for workflow validation:
*   Trigger the workflow and wait for it to complete.
*   Ensure it appears as the "most recent action" in the repository.
*   Verify that it creates a commit during or within 5 minutes of the workflow run.

Below this, a prompt "Enter your repository URL (format: https://github.com/USER/REPO):" precedes an input field. The input field contains the URL `https://github.com/DigvijaysinhChudasamalITM/TDS_GA_4`. This field is highlighted with a red border and an error icon on the right. Beneath the input field, a red error message states: "Error: No executed job step matches 21f2000588@ds.study.iitm.ac.in".
image1605×320 26.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/d/5d7f290214dcf1065f3b373c28d04671ef69f7c6.png)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

[@carlton](/u/carlton)

Can anyone please help to fix this issue and submit this correctly.

---

### Post #59 by K Hari Prasath on 2025-02-06T06:21:39.845Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/59

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f3002277/48/12741_2.png)
 21f3002277:

Set up Git user (23f2003853@ds.study.iitm.ac.in)

Still the same error appears

---

### Post #60 by K Hari Prasath on 2025-02-06T06:23:50.056Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/60

Thanks for providing clarification Sir

---

### Post #61 by Telvin Varghese on 2025-02-06T06:29:16.352Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/61

I am also facing same issue can’t resolve.

---

### Post #62 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-06T06:30:07.514Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/62

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

[@Saransh_Saini](/u/saransh_saini)

In ques 4 Scrap the BBC Weather API,

I scraped the locationId for my city (i.e Mumbai)

and post that also mapped each
issueDate
 to its corresponding
enhancedWeatherDescription
 .

The sample output mentioned was:

The output would look like this:

{
  "2025-01-01": "Sunny with scattered clouds",
  "2025-01-02": "Partly cloudy with a chance of rain",
  "2025-01-03": "Overcast skies",
  // ... additional days
}

And My Output after scraping (And as explained by professor in Video 2 BBC weather was)

{

“2025-02-05”: “A clear sky and light winds”,

“2025-02-06”: “A clear sky and light winds”,

“2025-02-07”: “A clear sky and light winds”,

“2025-02-08”: “A clear sky and light winds”,

“2025-02-09”: “A clear sky and light winds”,

“2025-02-10”: “A clear sky and light winds”,

“2025-02-11”: “A clear sky and light winds”,

“2025-02-12”: “A clear sky and light winds”,

“2025-02-13”: “A clear sky and light winds”,

“2025-02-14”: “A clear sky and light winds”,

“2025-02-15”: “A clear sky and light winds”,

“2025-02-16”: “A clear sky and light winds”,

“2025-02-17”: “A clear sky and light winds”,

“2025-02-18”: “A clear sky and light winds”,

“2025-02-19”: “A clear sky and light winds”

}

But it’s giving Error::

Error: At root: Different number of properties

Can you please help how to fix this issue.

---

### Post #63 by Telvin Varghese on 2025-02-06T06:37:52.150Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/63

Issue resolved for me after following below step

After creating the workflow:

Trigger the workflow and wait for it to complete

Ensure it appears as the
most recent action
 in your repository

Verify that it creates a commit during or within 5 minutes of the workflow run

---

### Post #64 by Ansh bansal on 2025-02-06T06:38:34.157Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/64

In place of “name: Setup up GIT config” change to “name: add commit {your_email}”

---

### Post #65 by VIKASH PRASAD on 2025-02-06T06:45:41.518Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/65

use this
[Google Colab](https://colab.research.google.com/drive/1X5IO8K1Xf8Wh7SOZelSrFAfZgRG-mv4A?usp=sharing)
 with the city name to get the Json Body just change the date format.

[@23f2004752](/u/23f2004752)

---

### Post #66 by Joel Jeffrey on 2025-02-06T07:04:00.243Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/66

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)
 could you please help me with this?

---

### Post #67 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-06T07:19:29.059Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/67

On running this colab with city = Mumbai,

I’m gettingh this error: Error: At root: Property name mismatch

---

### Post #68 by VIKASH PRASAD on 2025-02-06T07:42:32.535Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/68

it’s getting,

{
    "2025-02-06": "Sunny and a gentle breeze",
    "2025-02-07": "Sunny and a gentle breeze",
    "2025-02-08": "Sunny and a gentle breeze",
    "2025-02-09": "Sunny and a gentle breeze",
    "2025-02-10": "Sunny and a gentle breeze",
    "2025-02-11": "Sunny and a gentle breeze",
    "2025-02-12": "Sunny and a moderate breeze",
    "2025-02-13": "Sunny and a gentle breeze",
    "2025-02-14": "Sunny and a gentle breeze",
    "2025-02-15": "Sunny and a gentle breeze",
    "2025-02-16": "Sunny and a gentle breeze",
    "2025-02-17": "Sunny and a gentle breeze",
    "2025-02-18": "Sunny and a gentle breeze",
    "2025-02-19": "Sunny and a gentle breeze"

}

---

### Post #69 by K Hari Prasath on 2025-02-06T08:10:06.762Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/69

can tell me in your .yml which are all place did you use your iitm email id.  Because I got the error No executed job step matches 23f2003853@ds.study.ittm.ac.in. My commit was completed in 11 seconds

---

### Post #70 by Telvin Varghese on 2025-02-06T08:30:20.527Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/70

[@s.anand](/u/s.anand)

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Is there any way to crack this , I tired multiple time no improvement.

Also what does this " It is
very hard
 to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. Reformatting with Prettier helps standardize the output format for comparison." mean.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f9f1180300c81f729381ebb2a3391c53648a28f.png)

> **Image Description**: The image displays a prompt for a task involving PDF to Markdown conversion and formatting, relevant to a "Tools in Data Science" course.

Key elements visible are:
*   A header indicating a sample document: "q-pdf-to-markdown.pdf has the contents of a sample document."
*   A numbered list of three instructions:
    1.  Convert PDF content to Markdown, preserving structure and formatting.
    2.  Format the Markdown using Prettier version 3.4.2.
    3.  Submit the formatted Markdown.
*   A section titled "Impact" detailing benefits of the task, including "Enhances Productivity," "Improves Quality," "Supports Scalability," and "Facilitates Integration."
*   A question: "What is the markdown content of the PDF, formatted with prettier@3.4.2?"
*   A text input/output box showing a user's attempt at the Markdown content, which includes three lines of Latin-like text (e.g., "Ater vulnero solio tabula.") and a horizontal rule (`---`). All text within this box has a red wavy underline, indicating potential errors or misspellings.
*   An error message below the box: "Incorrect. Try again."
*   An explanatory note: "It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. Reformatting with Prettier helps standardize the output format for comparison."
image1327×743 41.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f9f1180300c81f729381ebb2a3391c53648a28f.png)

---

### Post #71 by Guddu Kumar Mishra  on 2025-02-06T09:39:54.578Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/71

Same problem please help me too if you get it right.

---

### Post #72 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-06T10:29:37.045Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/72

Yes followed all these steps, and still the error is being seen,

Error: No executed job step matches 21f2000588@ds.study.iitm.ac.in

---

### Post #73 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-06T10:33:21.057Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/73

Yes true,

Here’s the output:

{

“2025-02-05”: “Sunny and a gentle breeze”,

“2025-02-06”: “Sunny and a gentle breeze”,

“2025-02-07”: “Sunny and a gentle breeze”,

“2025-02-08”: “Sunny and a gentle breeze”,

“2025-02-09”: “Sunny and a gentle breeze”,

“2025-02-10”: “Sunny and a gentle breeze”,

“2025-02-11”: “Sunny and a moderate breeze”,

“2025-02-12”: “Sunny and a gentle breeze”,

“2025-02-13”: “Sunny and a gentle breeze”,

“2025-02-14”: “Sunny and a gentle breeze”,

“2025-02-15”: “Sunny and a gentle breeze”,

“2025-02-16”: “Sunny and a gentle breeze”,

“2025-02-17”: “Sunny and a gentle breeze”,

“2025-02-18”: “Sunny and a gentle breeze”

}

But unfortunately this error persists,

Error: At root: Property name mismatch

---

### Post #74 by K Hari Prasath on 2025-02-06T10:33:30.127Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/74

Now re-check you answer. May it will give link where the issue exists. if it gives url browsers the link and address.

---

### Post #75 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-06T10:33:48.592Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/75

Yes true same happened with me.

---

### Post #76 by K Hari Prasath on 2025-02-06T10:36:03.777Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/76

re-check your answer again it may give an url. check the url

---

### Post #77 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-06T10:36:09.371Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/77

Now on rechecking, the error message has changed to – “TypeError: Failed to fetch”

---

### Post #78 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-06T10:36:50.718Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/78

No its giving such error:

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad4d5271fd3d95f8e832eaa212705300b96245cc_2_690x110.png)

> **Image Description**: The image displays a user interface for entering a GitHub repository URL, likely for a "Tools in Data Science" course assignment or validation.

Visible elements include:
*   An instruction partially visible at the top: "...verify that it creates a commit during or within 5 minutes of the workflow run."
*   A prompt: "Enter your repository URL (format: https://github.com/USER/REPO):"
*   An input field containing the URL: `https://github.com/DigvijaysinhChudasamallTM/TDS_GA_4`.
*   An error indicator (red circle with a symbol) at the end of the input field.
*   An error message displayed below the input field: `TypeError: Failed to fetch`.
*   A blue button labeled "Check" at the bottom of the interface.
image1729×278 15.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/d/ad4d5271fd3d95f8e832eaa212705300b96245cc.png)

---

### Post #79 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-06T10:42:30.147Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/79

Here’s the action’s:

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/5/35164c425fd9bac93a22a798ceb50aff9245edfc_2_690x167.png)

> **Image Description**: The image displays a dark-themed user interface for managing actions and workflows, specifically related to GitHub Actions.

On the left navigation pane, labeled "Actions," there's a "New workflow" button and a list of navigation items including "All workflows" (currently selected), "Daily Commit," and a "Management" section containing "Caches," "Attestations," "Runners," "Usage metrics," and "Performance metrics," each with an associated icon and expand/collapse indicator.

The main content area is titled "All workflows" with a subtitle "Showing runs from all workflows." A search bar labeled "Filter workflow runs" is present at the top right. Below it, a banner invites users to "Help us improve GitHub Actions" with a "Give feedback" button.

A section titled "15 workflow runs" displays a list of completed workflow executions. This section includes filterable column headers for "Event," "Status," "Branch," and "Actor." Two workflow runs are visible:
1.  "Daily Commit #15: Manually run by DigvijaysinhChudasamalTM" on the "main" branch, completed "13 minutes ago" in "16s." A green checkmark indicates a successful status.
2.  "Daily Commit #14: Manually run by DigvijaysinhChudasamalTM" on the "main" branch, completed "13 minutes ago" in "17s." This also shows a green checkmark for success.

Both listed runs include an ellipsis menu icon for further actions.
image1921×467 45.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/5/35164c425fd9bac93a22a798ceb50aff9245edfc.png)

---

### Post #80 by K Hari Prasath on 2025-02-06T10:44:58.593Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/80

Check you Github account and browse Action for your repo. then check All Work flows. Ensure the first item is schedule triggered confirmation

---

### Post #81 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-06T10:47:32.686Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/81

What you meant by " Ensure the first item is schedule triggered confirmation"? You meant the latest one should be this right?

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/8/3812c6855de7c05b79750c6f57eed987122e24f4_2_690x319.png)

> **Image Description**: The image displays a dark-themed GitHub interface for the repository "DigvijaysinhChudasamaTM / TDS_GA_4". The "Actions" tab is currently selected in the top navigation bar, which also includes "Code", "Issues", "Pull requests", "Projects", "Wiki", "Security", "Insights", and "Settings".

On the left sidebar, under "Actions", "All workflows" is highlighted, and a "Daily Commit" workflow is listed. Below this is a "Management" section with options for "Caches", "Attestations", "Runners", "Usage metrics", and "Performance metrics". A "New workflow" button is present.

The main content area shows "All workflows" with a "Filter workflow runs" search bar. A blue banner prompts "Help us improve GitHub Actions" with a "Give feedback" button. Below this, "15 workflow runs" are listed in a table with columns: "Event", "Status", "Branch", and "Actor".

Visible workflow runs include:
*   "Daily Commit #15: Manually run by DigvijaysinhChudasamaTM" (Success, 18 minutes ago, 16 seconds duration on "main" branch).
*   "Daily Commit #14: Manually run by DigvijaysinhChudasamaTM" (Success, 18 minutes ago, 17 seconds duration on "main" branch).
*   "Daily Commit #13: Manually run by DigvijaysinhChudasamaTM" (Failure, 4 hours ago, 10 seconds duration on "main" branch).
*   "Daily Commit #12: Manually run by DigvijaysinhChudasamaTM" (Failure, 4 hours ago, 11 seconds duration on "main" branch).
*   "Daily Commit #11: Scheduled" (Success, 10 hours ago, 14 seconds duration on "main" branch).

Each workflow run entry shows an associated icon indicating success (green checkmark) or failure (orange/red 'x'). The "Actor" column shows the user who ran the workflow or "Scheduled" for automated runs. The top right of the interface contains a search bar and user-related icons.
image1920×889 82 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/8/3812c6855de7c05b79750c6f57eed987122e24f4.png)

---

### Post #82 by K Hari Prasath on 2025-02-06T10:56:41.910Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/82

check this type of screen

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/c/3c228c6f00a24b93336be15b4aa8f8c04c13f168_2_690x197.png)

> **Image Description**: The image displays a GitHub Actions interface, presenting a list of workflow runs. A feedback prompt at the top invites users to improve GitHub Actions. The main section is titled "71 workflow runs" and includes column headers for filtering or sorting by "Event," "Status," "Branch," and "Actor." A single workflow run is visible, indicated by a green checkmark for success. This run was executed by "23f2003853@ds.study.iitm.ac.in" on the "main" branch, explicitly noted as "Manually run." The run was completed "23 minutes ago" and had a duration of "19s."
image1000×286 16.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/c/3c228c6f00a24b93336be15b4aa8f8c04c13f168.png)

---

### Post #84 by Ansh bansal on 2025-02-06T11:26:21.596Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/84

use name:email inside yml page

---

### Post #85 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-06T11:27:18.714Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/85

Yep done, thank you!
![:smiley:](https://emoji.discourse-cdn.com/google/smiley.png?v=12)

---

### Post #87 by Wasim Ansari on 2025-02-06T13:39:36.309Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/87

Depopulo amoveo curo.
Concego creatinue ancilla vesper conicio cinimatico eribro.
Custodia anica arbustum coniceto suma corporis aduno commenoro curiositas augero.
Uredo thesis ancilla alter eun tener vomito praesentium templum.
Magni deprimo celebre.

### Bellum pelor cornu vorax perspiciatis.

Labore elus umerus voluntarius.
Vicissitudo cilíctum cicuta campana.
Desino perspiciatis comodo.

### amarttudo tabesco crinis amissio

tui qui decumbo vobis
audacia charismatubineus contigo
aro eum talio elus
coniuratio cubo ab vere
validus tam patria deficio
agnosco spectaculumcoerceo
spectaculum vulpes valetudo
minima cado suffragium
asperiores thesaurus cometes
vesica amplus cimentarius
volum curiositas cornu

## Paupertrucido confido triduana ante sublime

# Consequatur comminor

Coadunatio delectus atqui placeat atque copia ventosus aer quae.
Tatillo causa damatico validus torrena tivpinca.
Adside nisi atavus aspiente.

[soius tam](https://tds.s-anand.net/#/markdown)

Ceno usilio desino velociter sit aut. Concedo accedo vac congregatio sperno venia sum sordeo animi tametsi. Accusamus suppellex turpis dedecor uliam vaco venusit:

- tu! amicitia ante suppellex studio
- utor debilito suasoria odio
- antea desino despecto magni

[coadunatio voco](https://tds.s-anand.net/#/markdown)

[incidunt aliquam](https://tds.s-anand.net/#/markdown)

Tametsitenuis conscendo.

- tempore vorner aestas commentoro
- absconditus coruscus

## Blanditiis tabula animi succedo

Asper summa tametsi ustulo villias conservo clam triumphus tener ager. Audax conforto adopto vesco arbustum deorsum terror impedit iure. Adsum atrox caries acc

Beatae ducimus aperio amarttudo caries

- cinis solvo unde unde arbustum
- canis civitas viro
- thorax pax demens
- arbustum suficco thorax testimonium ex.
- vinliter sumptus

Explicabo defico adfectus.

Comedo cattus justo tamdiu tumultus confido thesaurus coadunatio volutabrum. Succedo tabula audax copia vinculum.

**cogo audio suffragium**

crepito amiculum sufficio
acer aestas utor
debeo adopto utpote
tametsi curatio ante

## Maxime vulgo depulso decipio atrox

## Career debeo

**conatus cui admoneo**

theatum pauper tego
pecco caeous vulgo
cursim desino arceo
balbus comminor et

In the question no. 10, I have tried numerous time to get it right markdown content but it was incorrect all the time.

I have tried these steps:

import pymupdf4llm
md_text = pymupdf4llm.to_markdown("/content/q-pdf-to-markdown.pdf")

import pathlib
pathlib.Path("output.md").write_bytes(md_text.encode())

Then i run this in bash

prettier --write output.md

And what i got frankly telling was far from this, I did some manual touchups, and this what i have now. This is the best version i could come up with. Saw the preview, it does matches with the pdf.

#Can
 someone please advise me a better approach?

---

### Post #89 by Ansh bansal on 2025-02-05T03:03:39.499Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/89

hey, can you help me in doing this i can’t able to do this.

---

### Post #90 by Carlton D'Silva on 2025-02-06T14:01:32.303Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/90

[@24ds3000090](/u/24ds3000090)

We will be changing this question. Even we found it hard
![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12)

Kind regards

---

### Post #91 by Carlton D'Silva on 2025-02-06T14:02:42.475Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/91

[@JoelJeffrey](/u/joeljeffrey)

We will be changing this question. Even we found it pretty hard
![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12)

Kind regards

---

### Post #92 by Daksh Agarwal on 2025-02-06T15:06:08.271Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/92

sir in the weather question could you provide from where do we get the bbc api because i have searched a lot and havent been able to find it

---

### Post #93 by Carlton D'Silva on 2025-02-06T15:13:07.942Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/93

[https://tds.s-anand.net/#/bbc-weather-api-with-python](https://tds.s-anand.net/#/bbc-weather-api-with-python)

---

### Post #94 by Chinnam Goutham Nischay on 2025-02-06T16:42:32.860Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/94

try manually inspecting the output of the api and compare it with your script output.

Or else try refreshing the browser and check.

---

### Post #95 by Ansh bansal on 2025-02-06T17:52:55.640Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/95

[@carlton](/u/carlton)

Previously i got correct on q2 but now i am getting the error when i refresh the page “TypeError: Cannot read properties of null (reading ‘textContent’)”

---

### Post #96 by Rajalakshmi Rathinasabhapathy on 2025-02-06T19:53:06.705Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/96

Please try city=“Mumbai” as a string literal.

---

### Post #97 by Nelson Jochim DSouza on 2025-02-06T20:56:51.582Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/97

Q4 BBC Weather

I don’t understand why I am getting

Error: At root: Different number of properties

Is it because of different dates? Shall I match the dates?

[@carlton](/u/carlton)
 Please guide. Thank you.

[![BBC weather](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/7/e7c12cee82eccb262d1c2752a98e95c3c3a94457.png)

> **Image Description**: The image displays a data science task broken into three steps: API Integration and Data Retrieval (using BBC Weather API for `locationId`), Weather Data Extraction, and Data Transformation (extracting `issueDate` and `enhancedWeatherDescription`).

An example JSON output format is shown, featuring dates as keys and corresponding weather descriptions as values (e.g., `"2025-01-01": "Sunny with scattered clouds"`), illustrating a dictionary-like structure for three days.

Below the example, a question prompts for the "JSON weather forecast description for Osaka?". A user-provided JSON response is visible, containing five date-keyed weather descriptions (e.g., `"2025-02-06": "A clear sky and light winds"`). Directly beneath this response, a red box highlights an error message: "Error: At root: Different number of properties". A "Check" button is present below the error.
BBC weather565×781 30.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/7/e7c12cee82eccb262d1c2752a98e95c3c3a94457.png)

---

### Post #98 by Mishkat Chougule on 2025-02-02T08:21:23.154Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/98

[](#p-591418-thema-coruscus-1)
thema coruscus

cupiditate celebrer

argentum alius voro soluta

sto decor capto suffoco acs tempus deludo deleo ventus odio

Sordeo tergo beatae coniecto ambitus carus. Vae tamdiu debilito verto confugo

territo acies vos patria. Versus surgo degero vester tersus paulatim chirographum

abeo

super

valetudo adhuc

conatus

comptus

spiculum summisse

alienus

addo

demergo conturbo

uberrime

subseco

altus & ea

apto

cursus

infit & summa

tabula necessitatibus beneficium concido

adhaero tepesco ars

adnuo beatae

cursim ahsens culpa animi aestivus

[](#p-591418-solium-vulgus-commodo-claro-curriculum-valens-2)
Solium vulgus commodo claro curriculum valens

Aut ipsum spiritus tantillus vacuus adsum crebro animus pel paulatim. Tunc vallum

torqueo aequus valens triduana illo. Uredo cursus fuga vir.

Cultellus adipiscor incidunt tondeo benevolentia capto contabesco bene tardus

harum.

Bos subnecto beatae abeo vulnus terra verus balbus

arguo via vallum usus aliquid

tempus balbus videlicet acquiro

attonbitus tardus versus cuppedia

derelinctuo curatio stalla solen

comburo commodo caveo at

deporto aliquid thymum

confero sortitus ago

triduana umquam acies

Beneficium doloremque aspernatur dolor dolorum despecto attonbitus unus alienus

Capto optio dolores.

Commodi sono denuo molestiae terebro

Benigne anser vulgus brevis coaegresco vinum debeo.

Cras aut ullam error terreo absque aro adstringo sublime thymum

[](#p-591418-triumphuslaudantium-curto-certus-3)
Triumphuslaudantium curto certus

Callide stabilis subito claudeo occaecati depono. Turba thymum bis deludo una.

Sumo consuasor necessitatibus vix solitudo dolorum dolorem vinco inflammatio

apparatus spero sulum desino ultra

nauner necessitatibus bos calculus nlaceat

animadverto defessus triumphus

acquiro artificiose minima sortitus terminatio

Aegrus tot tot aetas. Clinís volva tamen sumptus. Solutio deludo suscipio deputo

demens vero audeo annus alo accendo.

I am getting error: Incorrect. Try again.

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
 can you please explain the reason for this error

---

### Post #99 by Carlton D'Silva on 2025-02-07T03:25:45.448Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/99

Hi Mishkat

Please refer to this post.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/91)

[Tools in Data Science](/c/courses/tds-kb/34)

[@JoelJeffrey](/u/joeljeffrey)

We will be changing this question. Even we found it pretty hard
![sweat_smile](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12)

Kind regards

Kind regards

---

### Post #100 by 23f3001356 on 2025-02-07T05:47:13.914Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/100

[@s.anand](/u/s.anand)
 Sir the question 10 of the Graded Assignment 4 is very tough I have tried everything from custom python codes using different libraries to online converted and also formatted using prettier. Please sir guide me how to do the question.

---

### Post #101 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-07T05:48:27.982Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/101

Yep figured that, and after matching the data solved the error and got that question correct.

Though thank you.

---

### Post #102 by 23f3001356 on 2025-02-07T05:49:56.327Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/102

[@s.anand](/u/s.anand)
 Sir I have done the question 2 of the graded assignment but I am very curious to know why the answers language gets periodically change. Is there some kind of backend code which is responsible for that or is something else ?

---

### Post #103 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-07T05:50:27.393Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/103

Yes we’ll were facing this issue.

[@carlton](/u/carlton)
 sir mentioned yesterday that they will change the question.

"We will be changing this question. Even we found it hard
![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12)

Kind regards"

So need to worry about that question for now.

---

### Post #104 by 23f3001356 on 2025-02-07T05:52:26.841Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/104

OK, that is good to hear, you won’t believe that yesterday I was trying this question for 2 hours literally, it can be more also.

---

### Post #105 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-07T05:54:22.421Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/105

I was stuck at that question for 2 days, I tried multiple ways but was not able to format the content with prettier as expected, every time I was getting the error “Incorrect. Try again.”

---

### Post #106 by Anand S on 2025-02-07T06:01:13.973Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/106

On popular demand, I’ve made Q10 of GA4 easier (converting from PDF to Markdown). The question remains the same, but the check is more liberal and the error messages are more helpful. Please give it a shot now.

(FYI, one person
did
 solve it. A colleague, not someone from the IITM DS program.)

---

### Post #107 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-07T06:44:45.158Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/107

Hello Sir, i tried but unfortunately after extracting the contents and formatting the contents and submitting it, it’s showing various errors like Missing links, Missing tables…

But on checking the file i wasn’t able to find any single table in the contents in that case what could be done to fix these errors?

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

[@Saransh_Saini](/u/saransh_saini)

---

### Post #108 by Tushar Jalan  on 2025-02-07T07:33:28.651Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/108

same issue with me as well

---

### Post #109 by K Hari Prasath on 2025-02-07T08:36:08.903Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/109

Sir I checked the pdf file, there is only one place unorder list is given and the same is available in my answer. But the system throws error Missing List (I tried with other symbols * and + also) . Please inform me where I made mistake

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/1/b12c7242be994f334d445739cf3b6ffe1b36c25f.png)

> **Image Description**: The image displays a user interface query and its output. At the top, a question asks: "What is the markdown content of the PDF, formatted with prettier@3.4.2?". Below this, a red-bordered box presents a list of four items, each beginning with a hyphen:
- cuppedia tamquam facilis confugo
- conservo depereo
- consectetur arx
- aeternus celebrer
All words in the list items are underlined with a red wavy line, typically indicating a spelling error. A vertical scrollbar is present on the right side of this box, and a warning icon (exclamation mark in a circle) appears in the top right corner. Below the red-bordered box, an error message states: "Error: Missing lists".
image1108×271 5.87 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/1/b12c7242be994f334d445739cf3b6ffe1b36c25f.png)

---

### Post #110 by K Hari Prasath on 2025-02-07T08:39:47.886Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/110

this is table. Check it

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7d3c3c9414b2bc8323097d34e3ff54b8234f535e.png)

> **Image Description**: The image displays a three-column table. Each column has a bolded header: "capitulus", "deleniti", and "pariatur". Under each header, there are four rows of unbolded text entries.
image313×136 5.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7d3c3c9414b2bc8323097d34e3ff54b8234f535e.png)

---

### Post #111 by Nelson Jochim DSouza on 2025-02-07T08:52:02.503Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/111

Q 10 - PDF to Markdown.

Why it is saying

Incorrect. Try again?

Do I need to add CSS?

Carbo ventosus tametsi patior. Recusandae ciminatio alienus nisi ventosus apud. Theatrum abutor aperio spargo vestrum virga placeat adulescens. Deripio alveus creator omnis tabula patria cupiditate in virga speculum. Acidu`s alienus vehemens vapulus.

earum clamo collum

curtus careo curatio

tendo sunt culpo

Suus sit magni traho tempora.

Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo iusto adfero truculenter.

cresco

solio

ademptio

terreo

bis

tardus

carpo

allatus

depono

benevolentia

tunc

atavus

barba

urbs

considero

adulescensamplitudo

verbum

cultura

id

cenaculum

ipsum

sursum

conturbo

nemo

damno

arbitro

quibusdam

articulus

animadverto

ustulo crudelis depraedor

sophismata tener apostolus suus adopto

coniecto maxime rerum

acceptus virga confero comes

[cresco vomito](#)

[deputo ceno](#)

[](#p-591549-cuppedia-uberrime-socius-atque-paens-1)
Cuppedia uberrime socius atque paens

[](#p-591549-sto-theca-testimonium-aestus-debitis-2)
Sto theca testimonium aestus debitis

[valde vulgus](#)

---

### Post #112 by Nelson Jochim DSouza on 2025-02-07T08:55:44.029Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/112

I checked many times. For me it says “Incorrect. Try again.”

---

### Post #113 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-07T09:31:43.739Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/113

Ya i know, i added tables, list, blockquote, code, tables have all been added still it’s showing errors. Not sure where am I going wrong.

---

### Post #114 by K Hari Prasath on 2025-02-07T09:33:27.992Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/114

Please refer video and document relating to Question 1 of Assignment 3. There it is mentioned how to mark bold, table etc., use those marks

---

### Post #115 by Nelson Jochim DSouza on 2025-02-07T10:04:21.710Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/115

I have added all those and pasted the markdown and it appears as
[above](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/111)
.

`` Carbo ventosus tametsi patior.
Recusandae ciminatio alienus nisi ventosus apud.
Theatrum abutor aperio spargo vestrum virga placeat adulescens.
Deripio alveus creator omnis tabula patria cupiditate in virga speculum.
Acidu`s alienus vehemens vapulus. ``

**earum clamo collum**
curtus careo curatio
tendo sunt culpo
Suus sit magni traho tempora.

Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo iusto adfero truculenter.

| cresco              | solio   | ademptio  | terreo    | bis          |
| ------------------- | ------- | --------- | --------- | ------------ |
| tardus              | carpo   | allatus   | depono    | benevolentia |
| tunc                | atavus  | barba     | urbs      | considero    |
| adulescensamplitudo |         | verbum    | cultura   | id           |
| cenaculum           | ipsum   | sursum    | conturbo  | nemo         |
| damno               | arbitro | quibusdam | articulus | animadverto  |

- ustulo crudelis depraedor
- sophismata tener apostolus suus adopto
- coniecto maxime rerum
- acceptus virga confero comes

[cresco vomito](;;;)

[deputo ceno](;;;)

# Cuppedia uberrime socius atque paens

# Sto theca testimonium aestus debitis

[valde vulgus](;;;)

Below is the screenshot of provided PDF. That font colour strains my eyes. Any particular reason for that PDF?

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/c/5c7b1a8077a70f4a4dc9a91b49a22dd26d960153.png)

> **Image Description**: The image displays a document page featuring light gray Latin text on a white background, resulting in low visual contrast. The content is primarily textual, organized into multiple paragraphs. A distinct section begins with a left bracket, followed by several lines of text. Further down, a block of single words is arranged in a multi-column layout. This is succeeded by a four-item bulleted list, with each item initiated by an asterisk. Towards the bottom, three phrases, 'cresco vomito', 'deputo ceno', and 'valde vulgus', are underlined. The very bottom of the document contains two lines of larger, lighter Latin text.
image541×439 20.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/c/5c7b1a8077a70f4a4dc9a91b49a22dd26d960153.png)

---

### Post #116 by Sujay D on 2025-02-07T10:15:38.429Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/116

I am getting missing link error. I checked in the pdf file also, the blue color text seems a link but its not clickable.

Any suggestion to move nearer to the actual solution.

---

### Post #117 by Nelson Jochim DSouza on 2025-02-07T10:16:40.485Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/117

You may try like this:
[cresco vomito](#)

[cresco vomito](;;;)

---

### Post #118 by Swati Kapoor on 2025-02-07T10:30:52.807Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/118

Even I’m getting a similar error in Q2, it is expecting a foreign title whereas my search result gives only English titles.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f771adcf2eab4ec0113e32a15b3200bd8e1a30dc_2_690x106.png)

> **Image Description**: The image displays a prompt asking "What is the JSON data?". Below the prompt, a text area shows a partially visible JSON-like structure:
```json
"
{
  "id": "tt8712204",
  "title": "25. Batwoman",
  "year": "2019-2022",
  "rating": "3.6"
}
```
This structure is preceded by an extraneous double quote (`"`) and an error icon is visible at the top right of the text area.

Below the text area, a red-highlighted error message states:
"Error: At [12].title: Values don't match. Expected: "13. Pídeme lo que quieras". Actual: "13. Ask Me What You Want""
This error indicates a discrepancy in a title field at an array index `[12]`, where the expected value is "13. Pídeme lo que quieras" and the actual value is "13. Ask Me What You Want". The title visible in the JSON data, "25. Batwoman", does not correspond to either the expected or actual values in the error message.
image1614×250 14.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/7/f771adcf2eab4ec0113e32a15b3200bd8e1a30dc.png)

Please help.

---

### Post #119 by Siddhardh Devulapalli on 2025-02-07T11:06:49.504Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/119

I think the idea behind this font is to make it difficult for people to manually work on the markdown file from scratch. I guess they want us to use the tools (like PyMuPDF4LLM, markitdown) they provided as resources to convert pdf into a markdown and then may be we can do some manual intervention to make it to the result as the scraping tools are not 100% accurate.

Could be another reason too. TAs’ can feel free to pitch in.

---

### Post #120 by Carlton D'Silva on 2025-02-07T15:06:56.278Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/120

A post was merged into an existing topic:
[Tds: assignment is not submitting](/t/tds-assignment-is-not-submitting/166189/21)

---

### Post #121 by Ansh bansal on 2025-02-07T15:08:16.074Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/121

your last saved score (i.e.6 of your’s) will be official score and forgot about seek portal , it is not meant for this type of assignment.

---

### Post #122 by Yashvardhan on 2025-02-07T15:34:36.903Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/122

Thank you for the update! I gave Q10 another shot, and I was able to solve it this time. The more liberal checks and improved error messages made a big difference in understanding where I was going wrong.

Thank again.

---

### Post #123 by Akshit Mittal on 2025-02-07T15:49:48.266Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/123

Can we use hacking to get answers to some questions? Has anyone ever done it?

---

### Post #124 by Peter Paul Pooppally on 2025-02-07T16:00:15.001Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/124

What format is required for the “missing links” here

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/6/d6aa4b0f5bcd99eccd628b708f0821f56116e4f4_2_690x296.png)

> **Image Description**: The image displays a user interface for an exercise on PDF to Markdown conversion and formatting.

Key visible elements include:
*   A main heading: "Impact".
*   An introductory paragraph explaining the exercise's purpose related to EduDocs Inc.'s mission, high-quality resources, and automating PDF to Markdown conversion for consistent formatting.
*   A bulleted list detailing four benefits: "Enhances Productivity", "Improves Quality", "Supports Scalability", and "Facilitates Integration", each with a brief explanatory sentence.
*   A question prompt: "What is the markdown content of the PDF, formatted with prettier@3.4.2?".
*   A text input area containing sample text with Latin-like phrases, where several words are underlined in red, suggesting potential errors or unlinked elements. The text displayed is:
    *   "Audax teneo centum ciliciurn vigor venio."
    *   "Patria credo tonsor."
    *   "Defessus pax volup vomito creator video campana cedo vita votum."
    *   "Laudantium victoria aer via tepidus."
    *   "Adulescens corporis triumphus coruscus sordeo trans dolorum."
    *   This content is followed by an ellipsis (...), indicating truncation.
*   An error message displayed below the text area: "Error: Missing links".
*   A concluding paragraph stating: "It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic things."
image1973×849 93.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/6/d6aa4b0f5bcd99eccd628b708f0821f56116e4f4.png)

Here is my markdown

- statua demulceo amaritudo tametsi

- tam ante

- dens spiritus

- thema succurro sollers audio

Conforto conor tum deputo caecus cervus coepi aegrotatio totam xiphias. Repudiandae ducimus acerbitas ademptio . Delectatio tamquam suus.

Centum usitas tamen cedo auctus turpis video clibanus. Correptius beatus crepusculum decens succedo alias aperte decumbo trado. Talio universe deduco caute sui u

vester undique

- subito umbra

- caritas saepe

- taceo concido bos

Tenetur exercitationem numquam ultio tyrannus aeger vindico. Subvenio ambulo vacuus. Quidem quam tactus tracto aureus cupiditas.

thema astrum

# Spero uter

Harum cometes damnatio theologus virgo aperiam velut cursim.

**venustaspeccatus adsum**

acidus quisquam torrens

clam adeptio virga

Depulso claro consectetur concedo aveho bis pectus traho nobis. Cura adicio colligo corporis eligendi soluta ducimus carus. Allatus sapiente summa atqui deludo cur

Terebro vallum rem velociter currus suppellex.

Viduo damno ustilo valetudo.

Tribuo una vorago sui testimonium angelus suscipio eius demulceo civis.

Delectus coniecto repellendus amoveo amissio incidunt

Audax teneo centum cilicium vigor venio.

Patria credo tonsor.

Defessus pax volup vomito creator video campana cedo vita votum.

Laudantium victoria aer via tepidus.

Adulescens corporis triumphus coruscus sordeo trans dolorum.

- doloremque cum allatus aduro

- inventore thalassinus

- aperiam tergiversatio

- contigo alienus aranea cito cogo

Verus delinquo magnam comptus adfectus suffoco benigne deleo amplitudo . Cura deleniti theologus vestigium aranea denique vester doloribus . Venio cimentarius cr

depereo subvenio

---

---

### Post #125 by Yashvardhan on 2025-02-07T16:24:40.970Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/125

In the pdf you see some blue color font for specific words write that word in format

[word](#)

---

### Post #126 by NK on 2025-02-07T16:25:22.704Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/126

There are only four texts which look like link texts in the pdf.

All four properly coded in link markdown syntax, in the preview, they appear as  link texts same as in pdf.

[Link text](#)

Even after chaning all the 4 texts which appered in blue color in the pdf to link texts,

below error is still observed.

Error: Missing links

Did anyone else face same issue ?

Also, no text in the pdf looks like a code block.

But, Missing Code error was seen and after changing one of the paragraph by using markdown code syntax that error is gone.

Appreciate any suggestions on the link error.

---

### Post #127 by Yashvardhan on 2025-02-07T16:33:35.165Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/127

Replace actual text to expected text until you got correct

---

### Post #128 by Sanchay Naresh Gupta on 2025-02-07T16:44:13.037Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/128

same kind of error is arising with me too.Any suggestion what is wrong with it??

---

### Post #129 by NK on 2025-02-07T16:51:10.877Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/129

the rating should be treated as string.

Format is as “2.9” instead of number 2.9

---

### Post #130 by SHAON BALLAV on 2025-02-07T17:23:44.829Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/130

Yes it can be done. Got the 10th one correct by implementing breakpoint by printing the expected answer which is being used to validate the user answer in the js script.

---

### Post #131 by GURVEER SINGH SEKHON on 2025-02-07T18:20:02.449Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/131

i am facing a similar issue

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/d/7df67bc891ce85e7851b39a7a09749013a2040a0_2_690x302.png)

> **Image Description**: The image displays a programming interface demonstrating JSON data structures.

At the top, an example JSON output is shown, representing a weather forecast. It's a dictionary-like structure with date strings (e.g., "2025-01-01") as keys and weather descriptions (e.g., "Sunny with scattered clouds") as string values. A comment "// ... additional days" indicates continuation.

Below this, a question is posed: "What is the JSON weather forecast description for Shanghai?"

A user's attempt at answering is shown in a text input area. This input is also a JSON-like structure, providing weather descriptions for dates from "2025-02-07" to "2025-02-11". Each entry consists of a date string as a key and a weather description string as a value.

Below the user's input, an error message in red text states: "Error: At root: Different number of properties". A "Check" button is visible at the bottom left.
image1746×766 56.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/d/7df67bc891ce85e7851b39a7a09749013a2040a0.png)

---

### Post #132 by Shahil Khan on 2025-02-07T18:23:37.588Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/132

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/b/3b485ccad1b9c76027319c759cb72bd212d17925_2_690x366.png)

> **Image Description**: The image displays a web page for an online assignment or examination within a "Tools in Data Science" course context. The current task, GA4, is due on Sunday, February 9, 2025, at 11:59 pm IST. The displayed score for this assignment is 10/10. Available actions include "Check all" and "Save" buttons.

The page provides information on bonus marks for engaging in discussions: students can earn 1 bonus mark on this graded assignment by posting a relevant question or reply on the "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]" on Discourse.

Login information shows the user is logged in as `23f200527S@ds.study.iitm.ac.in`, with a "Logout" option.

A "Recent saves" section lists previous attempts or saves with corresponding scores and timestamps:
*   February 7, 2025, 23:51:21: Score 10
*   February 7, 2025, 20:30:21: Score 5
*   February 7, 2025, 18:17:58: Score 3
image1678×892 43.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/b/3b485ccad1b9c76027319c759cb72bd212d17925.png)

succesfully completed GA4 with 10/10 Marks

---

### Post #133 by Daksh Agarwal on 2025-02-07T19:06:13.783Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/133

sir how will we know if we have been awarded with the bonus mark. Will it be reflected in our ga score and the marks would be 11/10 or will it be added later

---

### Post #134 by Dabgar Milav Jayeshkumar on 2025-02-07T19:09:24.706Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/134

In Q2. getting , able to fix most of the errors but

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/6/36bd8aa62d975eb34268da85d1125bcdd130ac93_2_690x388.jpeg)

> **Image Description**: The image displays a Chrome browser window, divided into two main sections. On the left, an IMDb webpage is shown, displaying a list of movies under the URL `imdb.com/search/title/user_rating:4,8`, indicating a search for titles with user ratings between 4.0 and 8.0. The "TITLES" tab is active. Visible movie entries include "Anora" (2024, 7.8 rating), "Blink Twice" (2024, 6.5 rating), "Back in Action" (2025, 5.9 rating), "Flight Risk" (2025, 5.5 rating), and "The Recruit" (2022). Each entry includes a thumbnail, title, year, runtime, user rating, Metascore, and a brief description.

On the right, the Chrome Developer Tools are open, specifically displaying the "Console" tab. The console output presents a series of JSON objects. Each object represents a movie and includes key-value pairs for `id`, `title`, `year`, and `rating`. Visible JSON entries include "Gladiator II," "Babygirl," "High Potential," "Anora," "Blink Twice," "Back in Action," "Flight Risk," "The Recruit," "The Rookie," and "A Complete Unknown," with corresponding `id`, `year`, and `rating` values. The JSON data for "Anora," "Blink Twice," "Back in Action," "Flight Risk," and "The Recruit" aligns with the information displayed on the IMDb webpage.
image1920×1080 159 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/6/36bd8aa62d975eb34268da85d1125bcdd130ac93.jpeg)

Error: At [18].title: Values don’t match. Expected: “19. Graymail”. Actual: “19. The Recruit”

this kind of errors for some titles, even though i only applied Rating filter and nothing else, then why i’m getting different titles then the test cases?

---

### Post #135 by Sarang Tambe on 2025-02-07T19:28:00.399Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/135

Hello Sir, thank you for changing the question.

[@carlton](/u/carlton)
 I’m getting the below error:

Words like https, webbed, impact are missing (or not separated as words).

However, in the source PDF file itself these words are not available.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/5/9592fa553c00b5fa2d2540ef4933814690026709.png)

> **Image Description**: The image displays a user interface element with two rows of Latin words, each word enclosed by vertical pipe characters. Several of these Latin words (e.g., "utrum," "tredecim," "valetudo," "cras," "laudantium," "aetas," "canis") are marked with a red wavy underline, commonly indicating a spelling or validation error. Below this text, a red horizontal line separates the word display from an error message. The error message, also in red, reads: "Error: Words like https, webbed, impact are missing (or not separated as words)". This suggests a data processing or natural language processing tool encountering issues with word tokenization or dictionary lookup for certain terms.
image657×106 7.78 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/5/9592fa553c00b5fa2d2540ef4933814690026709.png)

---

### Post #136 by Mohd Atif on 2025-02-07T20:01:46.758Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/136

Copy the row name that is use to change and paste it in your answers

---

### Post #137 by Debjeet Singha on 2025-02-07T20:38:38.238Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/137

the ranking changes from time to time. you might need to scrape the data again.

---

### Post #138 by GURVEER SINGH SEKHON on 2025-02-07T20:46:04.301Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/138

i am facing issue in Q7.

I am using this command : “
[https://api.github.com/search/users?q=location:Seattle+followers:](https://api.github.com/search/users?q=location:Seattle+followers:)
>120&sort=created&order=desc”

and the output on evaluating is : 2011-05-07T08:30:48Z

But i am getting the error :

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/8/a8b774a9913c5ffd2941af7d0ba271f79309575c_2_690x309.png)

> **Image Description**: The image displays a data science task requiring interaction with the GitHub API. The core objective is to identify the creation date of the "newest" GitHub user profile located in Seattle with over 120 followers.

Key elements visible are:
*   **Task Definition**: Instructions detail using the GitHub API's search endpoints, filtering users by location and follower count, processing the data to isolate relevant profiles, and sorting by `created_at` dates to find the newest user. The required output format for the date is ISO 8601 (e.g., "2024-01-01T00:00:00Z").
*   **Impact Section**: Partially visible bullet points indicate the strategic advantages of automating this data retrieval, including "Targeted Recruitment," "Competitive Intelligence," "Efficiency," and "Data-Driven Decisions."
*   **User Interaction and Feedback**: An input field prompts for the date in ISO 8601 format. A user's input "2011-05-07T08:30:48Z" is marked "Incorrect. Try again."
*   **Correction/Hint**: A detailed hint guides the user: "Search using `location:` and `followers:` filters, sort by `joined` descending, fetch the first `url`, and enter the `created_at` field. Ignore ultra-new users who JUST joined, i.e. after 2/7/2025, 11:00:55 PM." This specifies the exact GitHub search query parameters and the data field to extract.
image1889×848 113 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/8/a8b774a9913c5ffd2941af7d0ba271f79309575c.png)

Can someone please help me on this ?

---

### Post #139 by Debjeet Singha on 2025-02-07T22:02:11.674Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/139

I am also facing the same issue. What is the problem here?

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/6/067aa8362e39ff9020d2cf42d3b7605bcbb0bcf2_2_690x350.png)

> **Image Description**: The image displays an online coding or data science assessment interface with a "Score: 9/10" and a due date of "Sun, 9 Feb, 2025, 11:59 pm IST".

The task outlines three steps for a data science problem:
1.  **API Integration and Data Retrieval:** Use the BBC Weather API to fetch weather forecasts for London by first obtaining a `locationId` from a locator service using a GET request with parameters like API key, locale, filters, and city.
2.  **Weather Data Extraction:** Retrieve forecast data from the weather broker API endpoint using the `locationId`.
3.  **Data Transformation:** Extract `issueDate` and `enhancedWeatherDescription` from the `forecasts` array in the API response. Then, create a JSON object where each key is the `issueDate` and the value is the `enhancedWeatherDescription`.

An example JSON output format is provided, showing date strings as keys and weather descriptions as values (e.g., `{"2025-01-01": "Sunny with scattered clouds"}`).

Below the problem description, a question asks: "What is the JSON weather forecast description for London?". An input field contains a partial JSON object representing a proposed answer, starting from "2025-02-17" to "2025-02-21" with corresponding weather descriptions. Below this input field, an error message "Error: At root: Property name mismatch" is displayed, indicating an issue with the provided JSON structure. A "Check" button is visible at the bottom.
image1788×908 77.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/6/067aa8362e39ff9020d2cf42d3b7605bcbb0bcf2.png)

---

### Post #140 by Anand S on 2025-02-08T03:23:12.990Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/140

[@21F1005510](/u/21f1005510)
 Actually, some IMDb titles have multiple names. For example,
[The Recruit](https://www.imdb.com/title/tt16030542/)
 is
[also known as Graymail in India](https://www.imdb.com/title/tt16030542/releaseinfo/?ref_=tt_dt_aka#akas)
. My server checks from a different region from yours. Hence the need for manual corrections for a few titles.

Why didn’t I pick an exercise that could be fully automated?
 Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.

---

### Post #141 by Anand S on 2025-02-08T03:31:12.813Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/141

To evaluate the bonus mark for replying to this Discourse topic, At around the time of the deadline, we’ll close this thread, load all posts here, and run this in the Console:

[...new Set($$('.names a[href^="/u/"]').map(d => d.textContent))]

… to get the Discourse IDs who posted. Then we’ll match it to the email IDs and pass it to the operations team who will add it to the portal by
2025-02-22T18:30:00Z
.

---

### Post #142 by Karthik V on 2025-02-08T04:54:21.666Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/142

I am getting the error in Q4 as “Error: At root: Property name mismatch”

what could me the cause of this error? Any please help.

[@carlton](/u/carlton)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/8/1865f8e1b730ba9148ccdea4be94bcb314eaa2bc.png)

> **Image Description**: The image displays a prompt asking: "What is the JSON weather forecast description for Sao Paulo?". Below the question, a JSON object is presented, featuring dates as keys (from "2025-02-08" to "2025-02-12") and corresponding weather descriptions as string values. The JSON object is incomplete, missing its closing curly brace. Below the JSON, a red error message states: "Error: At root: Property name mismatch". A blue "Check" button is visible at the bottom.
image716×402 23.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/8/1865f8e1b730ba9148ccdea4be94bcb314eaa2bc.png)

---

### Post #143 by Sarang Tambe on 2025-02-08T05:37:22.199Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/143

This is the only thing which worked for me.

[@carlton](/u/carlton)
 Sir, can I suggest to replace the snapshot of example output which expects the year to be an integer and the ratings as to be floats (instead of actual evaluation which expects them to be strings). Also, it would help to clarify that “Movie 1” should carry the numerical prefix as reported in IMDB.  The current example on the portal is:

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/0/e051d55928f7df633f0a14ed8c7aaa33712cdecf.png)

> **Image Description**: The image displays a snippet of JSON data, formatted as an array of objects. Each object represents a record with key-value pairs for "id" (string), "title" (string), "year" (integer), and "rating" (float). Two complete entries are visible: one for "Movie 1" (ID "tt1234567", year 2021, rating 5.8) and another for "Movie 2" (ID "tt7654321", year 2019, rating 6.2). A comment line `// ... more titles` indicates that the array contains additional, non-visible entries.
image1580×196 4.81 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/0/e051d55928f7df633f0a14ed8c7aaa33712cdecf.png)

---

### Post #144 by Naveen Yadav on 2025-02-08T05:52:49.272Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/144

Your dot of 2.9 may be the dot from alphabet or numeric one

Try to copy the value and then replace it

---

### Post #145 by Naveen Yadav on 2025-02-08T05:55:01.173Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/145

Try to copy the error data

The problem might be off dot

check one dot is on right of m and other right of 0 in keyboard

these two dots may represent different meanings

---

### Post #146 by Raj Rohit Singh on 2025-02-08T06:10:10.342Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/146

is it resolved?

i too am getting the same error,even if it was working fine yesterday.

---

### Post #147 by Karthik V on 2025-02-08T06:13:28.798Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/147

https will be part of the link (provided ‘link’ is one of the checkpoints of evaluation)

---

### Post #148 by LAKSHAY on 2025-02-08T06:40:39.010Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/148

Sir, In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.

I use different classes to extract values for various fields. Could there be any other element on the portal affecting this extraction?

In Q4, one of my classmates is encountering a “root property” error despite using the same extraction method as I do. Upon checking, I found that this issue occurs because the city’s time is displayed as the previous day compared to our time. The portal results seem to be based on the city’s actual time rather than IST.

I would appreciate your guidance on these issues.

---

### Post #149 by Anand S on 2025-02-08T06:45:07.380Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/149

Good idea
[@23f2005138](/u/23f2005138)
 and thanks. I fixed this. The example now reads:

[
  { "id": "tt1234567", "title": "Movie 1", "year": "2021", "rating": "5.8" },
  { "id": "tt7654321", "title": "Movie 2", "year": "2019", "rating": "6.2" },

… with the year and ratings quoted.

---

### Post #150 by Pradeep Mondal on 2025-02-08T07:56:59.322Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/150

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/lakshaygarg654/48/129814_2.png)
 lakshaygarg654:

In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.

I guess for the year part, there are certain series having multiple seasons, for which hyphenated “years” are given.

For the particular instance -
“2024–”
, it appears another season/part is announced, thats why it is written that way.

---

### Post #153 by LAKSHAY on 2025-02-08T08:27:29.717Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/153

Thanks
[@21f2000709](/u/21f2000709)
 for this information. I figure out where i made mistake. During writing console code I added to remove non numeric values in year field which i guess removed that hyphen (“–”). I will rectify that.

---

### Post #154 by GOVARDHANAN N  on 2025-02-08T08:28:27.587Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/154

GA 4 Q2

My JSON matches the titles of the movies as in the website, but in portal it is showing error and expecting something different from what is given in the website. How to handle this ?

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fcac5869001b59aa0b36666aa5096fd3ebfd8a0f.png)

> **Image Description**: The image displays a movie listing from a digital interface. On the left, a movie poster for "WINNIE THE POOH BLOOD AND HONEY" features a character in a Pooh-like mask, with a white plus sign icon in the top-left corner. To the right, the bold title "2. Winnie-the-Pooh: Blood and Honey" is shown, with blue squiggly underlines beneath "the" and "Pooh" within the title text. Below the title, three pieces of information are listed: "2023", "1h 24m", and "Not Rated". Further down, a yellow star icon precedes the rating "2.9 (33K)", followed by an outline star icon and "Rate" text. A red-boxed "16" is displayed next to "Metascore". A large red rectangular outline highlights the movie title, year, duration, rating, and the "16 Metascore" section.
image501×151 37.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fcac5869001b59aa0b36666aa5096fd3ebfd8a0f.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/6/b60003a16d034748f4e97674a5ce778a4c6686d4_2_690x145.png)

> **Image Description**: The image displays a prompt asking "What is the JSON data?". Below the prompt, an incomplete JSON object is shown, containing the keys `"title": "25. Battlefield Earth"`, `"year": "2000"`, and `"rating": "2.5"`. Following the JSON, an error message states "Error: At [1].title: Values don't match." This error message then presents "Expected: "2. Winnie the Pooh: Blood and Honey"" and "Actual: "2. Winnie-the-Pooh: Blood and Honey"", with the 'the-Pooh' part of the actual value underlined.
image1226×258 13.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/6/b60003a16d034748f4e97674a5ce778a4c6686d4.png)

contradiction :

" 2. Winnie-the-Pooh: Blood and Honey" (in web page) & ( delivered by the JSON)

" 2. Winnie the Pooh: Blood and Honey" (expected in portal ) & ( raising error statement )

Regards

GOVADHANAN N

---

### Post #155 by Guddu Kumar Mishra  on 2025-02-08T08:40:07.981Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/155

so just exchange it.

---

### Post #156 by GOVARDHANAN N  on 2025-02-08T08:44:44.640Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/156

Thanks for your response.

Many such titles have contradiction from what is expected and what is there in the website. This case the samples are 25 your approach is accepted to some extent, but on a larger sample space, need to work it right !

---

### Post #157 by Yash Arabhavi on 2025-02-08T09:33:54.075Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/157

thanks for this, was wondering why it wasn’t working!

---

### Post #158 by umra on 2025-02-08T09:48:12.602Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/158

[![question4](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94da9d1e5e22ec3b7a7d0bd8017fae76736aa5c8_2_641x500.jpeg)

> **Image Description**: The image displays a JSON parsing or validation scenario. The top section presents an example of an expected JSON output structure, which is an object containing date strings as keys (e.g., "2025-01-01") and weather descriptions as string values. This example shows three date entries: "2025-01-01", "2025-01-02", and "2025-01-03", followed by a comment indicating "additional days". Below this, a question asks for the "JSON weather forecast description for Kuala Lumpur?". A user's response is provided as `{"2025-02-01": "Thundery showers and light winds"}`. An error message, "Error: At root: Different number of properties", is displayed, indicating that the provided JSON response does not meet a required property count.
question4692×539 36.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/94da9d1e5e22ec3b7a7d0bd8017fae76736aa5c8.jpeg)

sir,  we are getting this error. My  Actual output is after get request on the given api i get only one day forcast data. I have show in above image

---

### Post #159 by Tanya kamboj on 2025-02-08T11:45:56.252Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/159

yes replace manually until you got correct ans . Error will suggest you what to change.

---

### Post #160 by Arya Agrahari  on 2025-02-08T12:13:42.491Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/160

{

“2025-02-08”: “Light snow and light winds”,

“2025-02-09”: “Light snow and light winds”,

“2025-02-10”: “Light cloud and light winds”,

“2025-02-11”: “Sunny intervals and a gentle breeze”,

“2025-02-12”: “Sunny and light winds”,

“2025-02-13”: “Sunny and light winds”,

“2025-02-14”: “Light snow and a gentle breeze”,

“2025-02-15”: “Light snow and a gentle breeze”,

“2025-02-16”: “Sleet and a gentle breeze”,

“2025-02-17”: “Light rain and a gentle breeze”,

“2025-02-18”: “Light rain showers and a gentle breeze”,

“2025-02-19”: “Drizzle and a gentle breeze”,

“2025-02-20”: “Light rain and light winds”,

“2025-02-21”: “Light rain and light winds”

}

i got this after running my python script for question 4 but, got

Error: At root: Property name mismatch" this error message

---

### Post #161 by Saravanan on 2025-02-08T12:25:18.374Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/161

[@s.anand](/u/s.anand)
 sir,

I don’t understand this error. In the website, the movie name doesn’t have a colon “:”, but in the result it is expecting so.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/6/b67037a225011416ec63654326f63aa3ee1542c4_2_690x171.png)

> **Image Description**: The image displays a code snippet resembling a JSON object with four key-value pairs: "id": "tt8790086", "title": "11. Kraven the Hunter", "year": "2024", and "rating": "5.4". Below the object, a red error message states: "Error: At [10].title: Values don't match. Expected: "11. Kraven: The Hunter". Actual: "11. Kraven the Hunter"". This highlights a specific character difference in the "title" string between an expected value (containing a colon) and an actual value (missing the colon).
image1005×250 15.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/6/b67037a225011416ec63654326f63aa3ee1542c4.png)

---

### Post #162 by LAKSHAY on 2025-02-08T12:27:12.734Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/162

For this question, you may use the Google Colab file referenced in the assignment. This file will provide you with the date and description. Additionally, you can generate a weather location ID for the city specified in your assignment. Using this ID, you will obtain the weather URL, which you can then use to verify the date and description.

---

### Post #163 by Tanya kamboj on 2025-02-08T13:13:07.988Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/163

here is the difference of  ‘:’ in the expected ans. so make it manually correct . i did the same and got correct ans .

and in the question also it is mentioned that may be manually you need to correct.  just give a try.

---

### Post #164 by Tanya kamboj on 2025-02-08T13:14:34.661Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/164

run your console script again and match the description.

---

### Post #165 by Tanya kamboj on 2025-02-08T13:15:53.963Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/165

yes, same happened with me . correct it manually.

---

### Post #166 by Chandapara Atul Ramabhai  on 2025-02-08T13:20:13.430Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/166

In q10 links are not accessible through pdf and also creating problems while converting to markdown

---

### Post #167 by Akash Kumar on 2025-02-08T13:26:41.508Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/167

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/e/7ec5aaa6e3eba1d39679fd60881fea0623932254_2_589x500.png)

> **Image Description**: The image displays a web page detailing a data integration task titled "Weather Data Integration for AgroTech Insights."

The main content includes:
1.  **Project Description:** A paragraph explaining AgroTech Insights' work and the need for integrating BBC Weather API data for enhanced weather forecasting capabilities.
2.  **Your Task Section:** Outlines three steps for automating weather data integration:
    *   **API Integration and Data Retrieval:** Use the BBC Weather API to fetch a forecast for Manila, obtaining a `locationId` from a locator service.
    *   **Weather Data Extraction:** Retrieve forecast data using the `locationId` from a weather broker API endpoint.
    *   **Data Transformation:** Extract `issueDate` and `enhancedWeatherDescription` from the `forecasts` array in the API response, then create a JSON object where `issueDate` is the key and `enhancedWeatherDescription` is the value.
3.  **Output Example:** A JSON-like structure demonstrating the desired output format, with "2025-01-01": "Sunny with scattered clouds" as a sample entry.
4.  **Question Prompt:** "What is the JSON weather forecast description for Manila?"
5.  **Pre-filled Answer Box:** Contains a JSON object showing weather descriptions for five days:
    *   `"2025-02-16": "Sunny and a gentle breeze"`
    *   `"2025-02-17": "Sunny and a gentle breeze"`
    *   `"2025-02-18": "Sunny and a gentle breeze"`
    *   `"2025-02-19": "Sunny and a gentle breeze"`
    *   `"2025-02-20": "Sunny and a gentle breeze"`
6.  **Action Button:** A blue button labeled "Check."
image1358×1151 179 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/e/7ec5aaa6e3eba1d39679fd60881fea0623932254.png)

Why question 4 starts failing. It was working correct yesterday. Because of it I am getting 9/10 marks.

---

### Post #168 by GOVARDHANAN N  on 2025-02-08T13:53:07.468Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/168

The result is dynamic with changes made in the API. So try re-executing your code today and it will automatically solve. Your code is right ! Just make a re-run and things will work out
![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12)

---

### Post #169 by Adarsh kumar on 2025-02-08T13:56:29.524Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/169

try running the console again and it will work, make sure the data matches with the one in api as it changes regularly

---

### Post #170 by Saravanan on 2025-02-08T14:00:19.459Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/170

Thanks!.

It is working now. I had to manually correct 5 movie titles to get it correct.

---

### Post #171 by Deepanshu Tomar on 2025-02-08T14:12:53.748Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/171

[![Screenshot 2025-02-08 at 7.41.55 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/6/66bbdf1b8a6c5661e0a95e9e9515f41a1d96816d_2_690x112.png)

> **Image Description**: The image displays a prompt "What is the JSON data?" followed by a partial JSON structure. The visible JSON object includes keys "id" with value "tt10078772", "title" with value "9. Flight Risk", and "year" with value "2025". Below the JSON, an error message is present: "Error: At [10].year: Values don't match. Expected: "2025-". Actual: "2025-"". This error indicates a data validation mismatch for the 'year' field at index 10 within a data structure.
Screenshot 2025-02-08 at 7.41.55 PM2576×420 32.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/6/66bbdf1b8a6c5661e0a95e9e9515f41a1d96816d.png)

What 's the solution?

---

### Post #172 by Neelakandan R on 2025-02-08T14:15:05.761Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/172

Titles (from the output json) should be replaced by the titles which shows in the error message “Expected”. It can only be done manually. There may be multiple titles need to be translated by this method.

Please refer the instruction.

[![1000095240](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/5/159cfd274231dd9585ac818265479de56b3544fd_2_690x116.jpeg)

> **Image Description**: The image displays a text box containing a warning message related to IMDb search results and data scraping. The message states: "IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code." Below this text box, a blue button labeled "Check" is partially visible in the bottom-left corner.
10000952401080×183 43.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/5/159cfd274231dd9585ac818265479de56b3544fd.jpeg)

---

### Post #173 by Preethika Ranganathan on 2025-02-08T14:15:27.390Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/173

you can manually add space after the hyphen

---

### Post #174 by Rajalakshmi Rathinasabhapathy on 2025-02-08T15:27:30.122Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/174

I face the same error, also thinking of issueDate, the value seems to be constant in every loop inside forecasts array (is it because the data is issed on that particular date) that gives same issue date key across the json outcome. Anyways the new json with same issueDate also gives the same Root error

---

### Post #175 by Harshit Chaturvedi on 2025-02-08T16:50:28.081Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/175

Double-check that the rating field in the JSON is indeed a float (
2.9
) and not a string (
"2.9"
) in your code.

---

### Post #176 by Shambhavi  on 2025-02-08T16:55:58.503Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/176

That is perhaps to ensure we don’t manually write the markdown for the pdf. Converting the pdf to markdown and getting the correct output is extremely hard, I tried doing that multiple times yet wasn’t able to get that right by the original method.

But since it is mentioned that the GAA is hackable and we are allowed to do so, for some of the questions, therefore you can try solving that by establishing a breakpoint in the sources and then write the code in the console to get the expected output.

---

### Post #177 by Shambhavi  on 2025-02-08T17:02:30.525Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/177

Write the code referencing the provided collab file and make sure to use the API key

The output actually changes once in a while so you might need to run the code a few times before getting in right

[https://tds.s-anand.net/#/bbc-weather-api-with-python](https://tds.s-anand.net/#/bbc-weather-api-with-python)

---

### Post #178 by JOHANA PRISCY JOHN PONRAJ  on 2025-02-08T18:05:32.112Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/178

your most recently saved score will be evaluated

---

### Post #179 by Avinash Kumar on 2025-02-08T18:26:01.657Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/179

I am getting this error again and again after running the code in collab this city
Nur-Sultan
?

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/a/7a2329cd855e0e0b8018cbfb2c426b91e57fa23d_2_690x252.png)

> **Image Description**: The image displays a Python traceback, indicating an execution error. The top line shows a custom error message: "Error: Could not find location ID for Nur-Sultan". This is followed by a `NameError` traceback. The traceback pinpoints line 35 of the code within an IPython input cell, which is `weather_url = f'https://www.bbc.com/weather/{location_id}'`. Surrounding comments indicate this line is part of code related to a "BBC Weather URL" (line 34) and "Fetch weather data" (line 37). The specific error reported at the bottom is `NameError: name 'location_id' is not defined`.
image936×343 26 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/a/7a2329cd855e0e0b8018cbfb2c426b91e57fa23d.png)

---

### Post #180 by Muhammed Adhil Pt on 2025-02-08T18:38:24.317Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/180

In the second question are we supposed to edit the JSON manually until we reach a correct answer ? I think the expected result has some difference from what shows up in the website

---

### Post #181 by Raghusrini on 2025-02-08T18:44:53.523Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/181

Not able to get the missing links in Q10

Any suggestions welcome please

---

### Post #182 by Anushka Ghosh on 2025-02-08T19:11:13.889Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/182

For question 10 I’ve tried everything. Links and headings work fine, but I’m not able to fix the “missing tables” issue (I’ve also tried using pdfplumber and tabulate). In the pdf as well, I don’t see any tables, any hints or suggestions would be very helpful. Thanks!

---

### Post #184 by Jayesh Bansal on 2025-02-08T19:15:03.641Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/184

there is no location id mentioned as it is mentioned of the different city. please check the city for which you need to find the location id and then proceed

---

### Post #185 by Swati Kapoor on 2025-02-08T19:19:06.435Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/185

I’m getting the same error in Q4:

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/6/b610004bc77d8cb653c10708ce962742396a0d2e_2_690x271.png)

> **Image Description**: The image displays a user interface for a data entry or validation task involving JSON. The top section, labeled "The output would look like this:", presents an example JSON object. This object contains date strings (e.g., "2025-01-01") as keys and weather descriptions (e.g., "Sunny with scattered clouds") as string values, indicating a date-based weather forecast format.

Below the example, a question asks: "What is the JSON weather forecast description for Los Angeles?". An input area is visible, containing a partially entered or erroneous JSON-like structure. The visible content within this area includes several lines, such as `"25-02-17": "Sunny and light winds",` and ends with a closing curly brace `}`. Notably, the first visible entry, `25-02-16: Sunny and light winds,`, appears to be missing enclosing double quotes for the date key.

An error message, "Error: At root: Property name mismatch," is displayed in red below the input area, indicating a formatting or structural issue within the provided JSON. A blue "Check" button is located at the bottom left.
image1631×641 34.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/6/b610004bc77d8cb653c10708ce962742396a0d2e.png)

---

### Post #186 by Harsh Raj on 2025-02-08T19:39:26.546Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/186

How to actually do the HNRSS one…i can’t find much.

---

### Post #187 by Harsh Raj on 2025-02-08T19:40:40.906Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/187

How did u do the links? I’m unable to do links

---

### Post #188 by Tanmay Sahu on 2025-02-08T20:31:47.253Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/188

Just copy paste the expected value in place of actual value in json. Keep doing this eventually it would be the answer would be correct.

This is a format issue when the json is scrapped from the browser.

---

### Post #189 by Koustubh Ramakrishnan on 2025-02-08T21:53:13.622Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/189

Request help on Q4 aboutBBC weather data, the instructions in the question tell us to use BBC broker API and get issueDate & enhancedWeatherdescription value pairs. However, it seems there are only 2 unique values of issueDate (not the expected 14 days)

Please clarify, sharing code and output below for reference.

Code:

import requests

url = "https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/" + getlocid('Bogota')
response = requests.get(url)
json_data=response.json()
print(f"The number of days data is {len(json_data['forecasts'])}")

weather_data = {}

for i in range(len(json_data['forecasts'])): # Use range to create an iterable sequence of indices
  issue_date = json_data['forecasts'][i]['summary']['issueDate']
  weather_description = json_data['forecasts'][i]['summary']['report']['enhancedWeatherDescription']
  weather_data[issue_date]=weather_description
  print("Iteration No. " + str(i))
  print(issue_date)
  print(weather_description)

print("Final Weather Data json below")
print(weather_data)

Output

The number of days data is 14
Iteration No. 0
2025-02-08T04:00:00-05:00
Light rain showers and a gentle breeze
Iteration No. 1
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 2
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 3
2025-02-08T04:00:00-05:00
Thundery showers and light winds
Iteration No. 4
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 5
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 6
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 7
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 8
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 9
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 10
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 11
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 12
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 13
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Final Weather Data json below
{'2025-02-08T04:00:00-05:00': 'Thundery showers and a gentle breeze', '2025-02-08T16:01:58-05:00': 'Thundery showers and a gentle breeze'}

Edit: For now, I have worked around with code posted by
[@21f3002277](/u/21f3002277)
. But the doubt about the question remains

---

### Post #190 by Suhani Thakur on 2025-02-08T23:18:04.439Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/190

same with me. In the project it is written that the form should be submitted but there’s no question in the portal.

---

### Post #191 by Rajalakshmi Rathinasabhapathy on 2025-02-09T00:48:22.810Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/191

I have got the same error as well, verified there are workflows run in my repo/actions/runs

When I checked the reasons, it could be due to API limit exceeded in a hour, but tried even after some time but no workflows found.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f6454e8cc98f502f9844114ea02cb8d6cd523c4_2_690x217.png)

> **Image Description**: The image displays a dark-themed user interface for managing workflows. At the top right, a search bar labeled "Filter workflow runs" is visible. A prominent banner below this invites users to "Help us improve GitHub Actions" with text stating "Tell us how to make GitHub Actions work better for you with three quick questions," accompanied by a "Give feedback" button and a close icon.

The main section is titled "All workflows" with a subtitle "Showing runs from all workflows." Below the banner, a heading indicates "2 workflow runs," followed by column headers for "Event," "Status," "Branch," and "Actor," each with a dropdown arrow.

Two workflow run entries are listed:
1.  **First entry:** Displays a green checkmark indicating successful completion. The workflow is named "Action runs everyday #6: Scheduled." It ran on the "main" branch, completed 2 hours ago, and took 15 seconds. An ellipsis icon is present for more options.
2.  **Second entry:** Also shows a green checkmark for successful completion. This workflow is named "Action runs everyday #5: Manually run by Rajalakshmi12." It ran on the "main" branch, completed 2 hours ago, and took 14 seconds. An ellipsis icon is also present.
image1345×424 23.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/f/3f6454e8cc98f502f9844114ea02cb8d6cd523c4.png)

---

### Post #192 by K Hari Prasath on 2025-02-09T01:05:38.835Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/192

Manual correction will not work. Try to extract - from the console. I did it like that it was not working then I extracted from console then it worked

---

### Post #193 by K Hari Prasath on 2025-02-09T01:12:34.834Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/193

Please ensure that your .yml file should have step name as your email Id. then Manually trigger the task (don’t wait till the scheduled time), ensure it was committed within 5 minutes and that commit should be top most item in all workflows. Then check it, it will work

---

### Post #194 by K Hari Prasath on 2025-02-09T01:30:53.176Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/194

You can find some text blue in color and underline use some dumy url it will work

---

### Post #195 by K Hari Prasath on 2025-02-09T01:35:35.603Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/195

You can find some lines having second, third words are uniformly aligned. Those are tables

---

### Post #196 by Suhani Thakur on 2025-02-09T02:30:28.306Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/196

When I resave the questions, the previously correct questions turn wrong which is extremely frustrating and time taking. I wish there is an option which saves the correct answer and does not require us to have multiple processes running in our pc even after getting the answer right previously.

---

### Post #197 by Udipth on 2025-02-09T02:41:28.911Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/197

In Q 6 I checked all the startups link at
[Hacker News - Newest: "Startup"](https://hnrss.org/newest?q=Startup)
… none is greater than 81 then how to submit that link… is there something i am missing

---

### Post #198 by B R GIRI SUBRAHMANYA on 2025-02-09T03:33:18.398Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/198

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
 ,for question 3, even a random response is shown correct

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/b/2b7de6bb9536ce1199eae286b610bb4cde7c34e5_2_690x184.png)

> **Image Description**: The image displays a prompt related to enabling CORS (Cross-Origin Resource Sharing). It asks "What is the URL of your API endpoint?", with an input field pre-filled with "http://127.0.0.1:8000" and a green checkmark indicating it's "Correct". Below this, a statement reads: "We'll check by sending a request to this URL with ?country=... passing different countries." A "Check" button is visible at the bottom left.
image1765×472 29.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/b/2b7de6bb9536ce1199eae286b610bb4cde7c34e5.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/f/af2fbee5353a1ff49e1bb73c3188f58894cb2dab.png)

> **Image Description**: Here's a concise description of the image for a Tools in Data Science student:

The image shows a web browser displaying the output of a program or script. The URL is `127.0.0.1:8000/?country=india`, suggesting it's running on a local server, and a parameter `country` is set to `india`. The title of the page is "Pretty-print". The visible output "44" is displayed, likely the result of the script.
image766×237 12.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/f/af2fbee5353a1ff49e1bb73c3188f58894cb2dab.png)

---

### Post #199 by Ayush Kumar Shaw  on 2025-02-09T03:42:07.409Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/199

Sir I have solved  Q2, But a problem arises that, At the index 11, in the IMdb website it is listed “The Recruit” but it is showing Expected: “Graymail”.

[![problem](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/2/e2c041886709fd37323cae0daebdb4426d85c7fc.jpeg)

> **Image Description**: The image shows a snippet of JSON data representing a list of movies or TV shows. Each entry contains fields such as "id", "title", "year", and "rating". There is an error message highlighted at the bottom of the image. The error message "Error: At [11].title: Values don't match. Expected: "12. Graymail". Actual: "12. The Recruit"" indicates a data validation failure. Specifically, the expected title for the movie at index 11 is "12. Graymail", but the actual value in the data is "12. The Recruit". The OCR of the last line does not seem correct.
problem621×159 42.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/2/e2c041886709fd37323cae0daebdb4426d85c7fc.jpeg)

How to fix this?

---

### Post #200 by B R GIRI SUBRAHMANYA on 2025-02-09T03:45:34.625Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/200

you have to manually change for a few mismatch.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/s.anand/48/15264_2.png)
 s.anand:

[@21F1005510](/u/21f1005510)
 Actually, some IMDb titles have multiple names. For example,
[The Recruit](https://www.imdb.com/title/tt16030542/)
 is
[also known as Graymail in India](https://www.imdb.com/title/tt16030542/releaseinfo/?ref_=tt_dt_aka#akas)
. My server checks from a different region from yours. Hence the need for manual corrections for a few titles.

Why didn’t I pick an exercise that could be fully automated?
 Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.

---

### Post #201 by Shambhavi  on 2025-02-09T05:52:35.938Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/201

Yes …due to the location difference the search results are different for everyone therefore you need to adjust it accordingly

It might need around 6-7 amendments

---

### Post #203 by Shambhavi  on 2025-02-09T06:13:36.894Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/203

The API is returning 14 days of forecast data, as evidenced by the output However, the issueDate values are not unique for each day. Instead, they represent the time when the forecast was issued or updated.

In your output, there are only two unique issueDate values:

2025-02-08T04:00:00-05:00

2025-02-08T16:01:58-05:00

This means the forecast was updated twice on February 8, 2025, once at 04:00 AM and again at 4:01 PM (both in EST timezone) …To get a unique weather description for each day, you  need to modify your approach by using the actual forecast day for each day instead.

---

### Post #204 by Md Anzar Rabbani on 2025-02-09T06:20:28.925Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/204

While submitting solution, do I need to keep all the local servers running/local URLs like 127.0.0.0 stuff, else I am getting one question as correct & the other one mentions unable to fetch data!? So that means I need to run them in different different ports?

---

### Post #205 by Manmeet Kaur on 2025-02-09T06:34:11.908Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/205

I posted this error message but now the first issue got resolved but I am still keeping it in my post so that if anyone faces same issue, they can try if they can fix it similar to how it worked for me.

Please help with the second issue.

For Q8, the workflow is running on Github and commiting the scraped results to the json file (which is so amazing for me btw!). But I am getting this error for my public repo.

How it got resolved: I set up fixed time for cron schedule instead of every 5 min. Now it works.

Error: No daily scheduled triggers found in workflows.

I had all correct results for Q1 to Q7 till yesterday but it keeps giving errors even when I reload same file for some questions. Do I need to keep addressing those errors or if once correct and saved, I can ignore those?

---

### Post #206 by Abhay Sharma on 2025-02-09T06:45:07.273Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/206

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/b/3bfb8c846507bcd4e7847f27efbfbffac65ca91e.png)

> **Image Description**: The image displays a user interface prompting "What is the JSON data?". Below this question is a partial JSON array containing three distinct movie data objects.

The first object begins with:
`{ "id": "tt0060196", "title": "The Good, the Bad and the Ugly", "year": "1966", "r` (truncated).

The second object is complete and reads:
`{ "id": "tt0137523", "title": "Fight Club", "year": "1999", "rating": "8.8" }`.

The third object starts with:
`{ "id": "tt0120737", "title": "The Lord of the Rings: The Fellowship of the Ring",` (truncated).

Immediately below the JSON data, an error message is displayed: "Error: At [0].id: Values don't match. Expected: "tt20221436". Actual: "tt0437179"". This indicates a mismatch in the `id` field of the first element in the JSON array.
image706×257 17.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/b/3bfb8c846507bcd4e7847f27efbfbffac65ca91e.png)

I have tried several times but still recieving this as error. Please help

---

### Post #207 by Subramanian V on 2025-02-09T07:01:02.715Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/207

[![Screenshot 2025-02-09 at 12.28.48 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/4/d4d7660a2abfcf04327d7b6a5aadd25ae098f4f1_2_690x498.png)

> **Image Description**: The image displays a web application interface and a browser's developer console. The top section outlines an API development task, detailing five steps: 1) creating an API endpoint (e.g., `/api/outline`) using a web framework that accepts a `country` query parameter; 2) fetching Wikipedia HTML content for the country; 3) extracting H1-H6 headings using an HTML parsing library; 4) generating a Markdown-formatted outline; and 5) enabling CORS for GET requests from any origin.

Below the task description, an input field labeled "What is the URL of your API endpoint?" contains `http://localhost:8000/api/outline`. Beneath this, a "TypeError: Load failed" message is visible, along with text indicating that requests will be sent to the URL with `?country=...` parameters. A "Check" button is present.

The lower half of the image shows the browser's developer console with the "Console" tab active. Multiple error messages are displayed. Recurring errors include: "[Blocked] The page at `https://exam.sanand.workers.dev/tds-2025-01-ga4` requested insecure content from `http://localhost:8000/api/outline?country=The+Bahamas`. This content was blocked..." and "Fetch API cannot load `http://localhost:8000/api/outline?country=The+Bahamas` due to access control checks." Additionally, "Not allowed to request resource" errors are listed, often with a `fetch.js:75` call stack reference.
Screenshot 2025-02-09 at 12.28.48 PM1304×943 182 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/4/d4d7660a2abfcf04327d7b6a5aadd25ae098f4f1.png)

I’m able to see the markdown response for different countries for question 3, GA 4 on my browser but I’m unable to submit it probably because of network issues. Can someone help me with a fix. Thank you.

---

### Post #208 by Shashank Tripathi on 2025-02-09T07:07:11.747Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/208

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/2/72c35e3d167b724daf8acafdb49ef67425a1d992_2_690x283.png)

> **Image Description**: The image displays a user interface for submitting JSON data as part of a data science assignment. The task requires submitting JSON data into a text box, which currently contains a JSON object with `id`, `title`, `year`, and `rating` fields. Below the JSON input, an error message "Error: At [10].year. Values don't match. Expected: "2021-". Actual: "2021"" is visible, indicating an issue with the year value in the submitted data. Additional text provides context about the assignment's "Impact" on content acquisition strategy for a streaming service and notes that "IMDb search results may differ by region" and may require manual translation or re-running scraper code.
image1701×699 64.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/2/72c35e3d167b724daf8acafdb49ef67425a1d992.png)

how to tackle this error  as in 10 th movie year is 2025 but it is showing 2021

---

### Post #209 by Avinash Kumar on 2025-02-09T07:21:17.635Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/209

City in my question is
Nur-Sultan
 .When i search
Nur-Sultan
 city name in BBC weather page .its show nothing . when i search in google then show Nur Sultan become Astana . then i am going this city  name "Astana ". and got location id 1526273. after i run in collab then showing error.

[![WhatsApp Image 2025-02-09 at 12.42.40_7957510c](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/9/5936d1d70999c4944a8f11097d2e36da3047c086_2_690x388.jpeg)

> **Image Description**: The image displays a computer screen showing Python code within an interactive development environment (likely Jupyter Notebook) along with a traceback indicating an `IndexError`.

The visible code snippet includes:
-   Generation of a date range using `pd.date_range` and formatting dates.
-   Creation of a dictionary `weather_data` by zipping `datelist` and `daily_summary_list`.
-   Conversion of `weather_data` to a JSON string using `json.dumps`.

Below the code, an `IndexError: list index out of range` is displayed as a traceback. The error occurs in `cell line: 8`, specifically at line 24, which attempts to construct `weather_url` using `result['response']['results'][0]['id']`. Comments indicate that lines 22-24 are related to fetching location data, and line 26 is for fetching weather data. The traceback points to an issue with accessing an element at index 0 within the `results` list, suggesting that the list is empty or does not contain any elements at that index.
WhatsApp Image 2025-02-09 at 12.42.40_7957510c1280×720 109 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/9/5936d1d70999c4944a8f11097d2e36da3047c086.jpeg)

---

### Post #210 by Sathyavathi S  on 2025-02-09T07:49:44.486Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/210

this error comes, whenever you answer the other ones and click save. Please answer this question lastly, and submit immediately. it changes within a second. If it continues means, do manual correction and change according to the “expected”

---

### Post #211 by Guddu Kumar Mishra  on 2025-02-09T07:49:53.990Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/211

while searching dont put any other filter other than asked in Problem statement.

---

### Post #212 by Sathyavathi S  on 2025-02-09T07:54:08.648Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/212

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/8/585776edda81a8af482544acd571fbbdc3c42992_2_690x218.png)

> **Image Description**: The image displays a prompt asking for the markdown content of a PDF, formatted with `prettier@3.4.2`. Below the prompt, a red-bordered box contains the following markdown text:

*   `# Pauci Audientia Sperno Eum` (a level 1 heading)
*   `Tracto adeptio somnus. Neque tantum desidero porro est civitas caute laboriosam valetudo.` (a paragraph of text)
*   `## Key Points` (a level 2 heading)
*   `- Vomito antiquus consequuntur` (a list item)
*   `- Amplus curis subnecto` (another list item)

Several words within the paragraph and list items are underlined with red wavy lines, indicating potential issues. Below the markdown content, a red error message states: "Error: Words like back, legislature, info are missing (or not separated as words)". The image concludes with a text explaining the difficulty of extracting correct Markdown from PDFs: "It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic things."
image1618×513 46.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/8/585776edda81a8af482544acd571fbbdc3c42992.png)

Can anyone help me with the 10th question. Whatever I changed with the code , it is asking something. I checked that these words are not present in the pdf itself

---

### Post #213 by PREMDEEP MAITI on 2025-02-09T08:06:59.795Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/213

I didn’t get any error for Astana.

The error may be due to incorrect loops in your code that’s why it’s going out of range, check for that.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/011280b40bf86e32b458005e1fa0a98d3213106f_2_690x260.png)

> **Image Description**: The image displays a dark-themed online notebook interface, likely a Jupyter environment, with the filename `bbc-weather-scraping.ipynb`.

The top visible cell (`[99]`) shows the output of a data structure, presumably a Pandas DataFrame, presented as a table. This table contains seven rows of weather data, indexed 7 through 13. The columns are: an unnamed index, "Date" (e.g., "25-02-16"), "High" (e.g., "-11"), "Low" (e.g., "-14"), and "Summary" (e.g., "Thick cloud and a gentle breeze"). The dates range from "25-02-16" to "25-02-22".

Below the table, a section labeled "Next steps" presents three interactive buttons: "Generate code with df," "View recommended plots," and "New interactive sheet."

The subsequent cell contains a single line of Python code: `df.to_json(orient='records')`.

Below this code cell, the output is a truncated JSON array. Each element in the array is an object representing a row of data, with keys like "Date," "High," "Low," and "Summary." For example, the first visible record is `{"Date": "25-02-09", "High": "-10\\u00b0", "Low": "-11\\u00b0", "Summary": "Sunny intervals and light winds"}`. The `\\u00b0` sequence indicates a Unicode escape for the degree symbol.
image1860×703 133 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/1/011280b40bf86e32b458005e1fa0a98d3213106f.png)

---

### Post #214 by LAKSHAY on 2025-02-09T08:14:05.998Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/214

It worked for me; only 4–5 values caused errors, which I fixed manually. Additionally, I corrected the console code, which now provides the correct result.

---

### Post #215 by Naga durga prasad E on 2025-02-09T08:21:43.386Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/215

what is this magic trick… please elaborate …

Error: At [10].id: Values don't match. Expected: "tt16027074". Actual: "tt8008948"

i dont see that value in data …

---

### Post #216 by PREMDEEP MAITI on 2025-02-09T08:32:10.545Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/216

You can manually edit that. I also have to manually edit one entry to get the correct answer.

---

### Post #217 by Swati Kapoor on 2025-02-09T08:39:35.814Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/217

Hi,

As mentioned in the question, you have to sort by “joined” so it should be “
[https://api.github.com/search/users?q=location:Seattle+followers:](https://api.github.com/search/users?q=location:Seattle+followers:)
>120&sort=joined&order=desc”

---

### Post #218 by Saravanan on 2025-02-09T08:41:16.475Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/218

There are two “Vienna”. The question4 is referring to which one?

---

### Post #219 by K Hari Prasath on 2025-02-09T09:05:31.841Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/219

Manually make correction in your answer as provided in the error message. If no such words are available insert those and check

---

### Post #220 by Taniya Gupta on 2025-02-09T09:32:07.046Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/220

check if the action is commited

---

### Post #222 by Tarun eshwar on 2025-02-09T09:40:39.232Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/222

try copying the expected result and pasting it inside the quotations

---

### Post #223 by Sudharshini  on 2025-02-09T09:42:45.371Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/223

Check the log of the daily commit .

---

### Post #224 by Shivani Adhiyaman on 2025-02-09T09:47:37.836Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/224

Ahh, I have the same doubt too!

---

### Post #225 by Anushka Ghosh on 2025-02-09T09:55:06.651Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/225

For the links, this format worked for me:

[ < link text > ] (#)

---

### Post #226 by Anushka Ghosh on 2025-02-09T09:58:40.634Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/226

Yes I got it now. Thank you!

---

### Post #227 by HARISH. S on 2025-02-09T09:59:13.731Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/227

it should be “2.9” instead of 2.9

---

### Post #228 by VivekS on 2025-02-09T10:01:39.752Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/228

looks like formatting or the passed conditions have some issue… can you check and verify it once and see?

---

### Post #229 by Aditya Kumar on 2025-02-09T10:24:24.121Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/229

Error: At [3].title: Values don’t match. Expected: “4. 365 Days - Noch Ein Tag”. Actual: “4. The Next 365 Days”

{“id”: “tt21106646”, “title”: “4. The Next 365 Days”, “rating”: “2.9”, “year”: “2022”}

my result , there is no any entry with “4. 365 Days - Noch Ein Tag” on IMDB

---

### Post #230 by Nayonika Arora on 2025-02-09T10:24:39.839Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/230

I am getting missing links as error in the 10th question. How to do it?

---

### Post #231 by Samarth Goel on 2025-02-09T10:30:18.333Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/231

Mine is giving 1/10 on running without even writing anything? This is happening for Q3? Is it just a glitch?

---

### Post #232 by Samarth Goel on 2025-02-09T10:31:15.219Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/232

Yes happened to me too, refresh the page, mine got fixed!

---

### Post #233 by K Hari Prasath on 2025-02-09T10:36:15.286Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/233

Check you pdf you can find a word with blue colour and underline. Give some dummy link and use link mark with the word

---

### Post #234 by Naga durga prasad E on 2025-02-09T10:41:30.178Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/234

Best way to solve Q2 is , look at the network tab in dev tools and get the url used for assessment and get data from it .

---

### Post #235 by Yash kumar on 2025-02-09T10:53:10.517Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/235

u have used a apace (_) after 2.9  which is not visible at front that’s why it is throwing error , it should be just (“2.9”) not ("2.9 ")

---

### Post #236 by Koustubh Ramakrishnan on 2025-02-09T11:09:57.380Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/236

Agreed and I have tweaked my approach to get the correct answer. But I feel the question instructions should be adjusted accordingly - the question says to get every issueDate and enhancedweatherDescription key value pair - but only 2 such pairs exist ; whereas in the final answer it is forecast date & weather description total 14  pairs.

---

### Post #237 by ABHIJITH VS on 2025-02-09T11:11:32.436Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/237

[![Screenshot (7)](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/5/954c6fa15e0841c485fc497035ecb4805336f0cb_2_690x387.png)

> **Image Description**: The image displays a web browser on the left, showing the BBC Weather website with "karachi" entered in a search field, suggesting a location search. On the right, the browser's developer tools are open to the Network tab.

Within the Network tab:
*   A filter "locat" is applied, narrowing down visible requests.
*   Resource type filters are displayed, with "Fetch/XHR" highlighted.
*   A waterfall chart of network activity is visible at the top of the request list.
*   A table of network requests shows one entry:
    *   **Name:** `locations?api_key=AGBFAKx5BHyjQScCXXlY...` (truncated URL)
    *   **Status:** `200`
    *   **Type:** `xhr` (XMLHttpRequest)
    *   **Initiator:** `search.js:2`
    *   **Size:** `486 B`
    *   **Time:** `2.31 s`
*   At the bottom of the Network tab, a summary states: "1 / 234 requests", "486 B / 600 kB transferred", and "255 B / 4.8 MB resources".
*   Below the network requests, tabs for "Console", "AI assistance", and "Issues" are visible.

This setup demonstrates a web application initiating an XHR (AJAX) call, likely to an API (indicated by `api_key` in the URL), to fetch location data dynamically from client-side JavaScript (`search.js`). The 200 status indicates a successful response.
Screenshot (7)1366×768 243 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/5/954c6fa15e0841c485fc497035ecb4805336f0cb.png)

Open the BBC Weather website.

Press
Ctrl + Shift + I
.

Select the ‘Network’ menu.

Select ‘Fetch/XHR’.

Type ‘Karachi’ in the input field on the website.
Do not press Enter
 while entering the location; just type the location. Pressing Enter might cause ‘location?api_key=…’ to disappear.

‘location?api_key=…’ will appear in the inspect menu.

Double-click it to open a web page (
[https://locator-service.api.bbci.co.uk/locations?api_key={api_key}](https://locator-service.api.bbci.co.uk/locations?api_key=%7Bapi_key%7D)
). This will give the API.

Alternatively, single-clicking ‘location?api_key=…’ will open headers where you can see the Request URL and the API key.

---

### Post #238 by HARISH. S on 2025-02-09T11:22:34.616Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/238

type 2025 instead of only using 25 for the year

---

### Post #239 by Thereasa Joe J on 2025-02-09T11:28:01.981Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/239

HOW TO DO SCRAPING USING GITHUB ACTIONS

I’m getting no workflow runs error Sir

---

### Post #240 by Deveshu Pathak on 2025-02-09T11:37:59.808Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/240

How to resolve “Error: Incorrect latitude. Check OSM ID ending with 2077”

---

### Post #241 by Sarthak Singh Gaur on 2025-02-09T11:42:26.613Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/241

[@22f3000657](/u/22f3000657)

you can try this-

[https://nominatim.openstreetmap.org/search?format=jsonv2&city=Chennai&country=India](https://nominatim.openstreetmap.org/search?format=jsonv2&city=Chennai&country=India)

change the city and country in the url

there will be a bounding_box field: [min_lat, max_lat, min_long, max_long]

---

### Post #242 by Ishaan on 2025-02-09T11:43:05.537Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/242

#question
 10

Hi, Can anyone help me with Question 10?

No matter how i try to post the markdown, it is always showing that either the words are missing or are different from the original. I have tried every possible way i could think of but it is not working.

---

### Post #243 by Shambhavi  on 2025-02-09T12:11:40.484Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/243

Getting this question right is a tough nut to crack…so I would rather suggest you to do using the developer tools by inspecting the source code and  putting the breakpoint followed by writing the code in the console to retrieve the expected answer

---

### Post #244 by Aryan Tikam on 2025-02-09T12:15:53.311Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/244

[![Screenshot from 2025-02-09 17-40-58](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5ae54f911b5d605c241abb9be7073563156a5a8_2_690x66.png)

> **Image Description**: The image displays a dark-themed user interface for entering a GitHub repository URL. A prompt states, "Enter your repository URL (format: https://github.com/USER/REPO):". Below this, an input field shows the entered URL "https://github.com/AryanTikam/AryanTikam". An error icon is visible at the right end of the input field, accompanied by a red error message: "Error: Latest run does https://github.com/AryanTikam/actions/runs/13225496 not include 23f2001216@ds.study.iitm.ac.in in the name".
Screenshot from 2025-02-09 17-40-581599×155 26.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f5ae54f911b5d605c241abb9be7073563156a5a8.png)

Can’t seem to get this working, have tried many variations by now like including my email in each of the name sections in every possible permutation. Probably just some silly mistake I haven’t noticed yet but any help would be appreciated. On Linux Mint if that’s relevant.

main.yml:

name: Daily Commit Workflow

on:
  schedule:
    - cron: '10 17 * * *'
  workflow_dispatch:

jobs:
  commit:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Add commit using 23f2001216@ds.study.iitm.ac.in
        env:
          PAT: ${{ secrets.PAT }}  # PAT stored as a secret
        run: |
          git config --global user.name "Aryan"
          git config --global user.email "23f2001216@ds.study.iitm.ac.in"

          echo "Daily commit on $(date)" >> daily-log.txt

          git add daily-log.txt
          git commit -m "Automated daily commit on $(date)"

          ls -la
          git status

          git push origin main
          git push "https://${{ secrets.PAT }}@github.com/${{ github.repository }}.git" main

---

### Post #245 by Arulvadivelan V on 2025-02-09T12:29:57.475Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/245

Hi Team,

I have made the JSON from the IMDB website using JS, But do i miss any filter conditions,

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/7/67d552f9ef5b8b06cae0421fe8d91bcdf4352af7_2_690x127.png)

> **Image Description**: The image displays a user interface prompt asking "What is the JSON data?". Partially visible JSON-like data includes key-value pairs such as `"year": "2024"`, `"rating": "6.0"`, and `"id": "tt30292390"`. An error message is present, stating: "Error: At [10].title: Values don't match. Expected: '11. Sebastian Fitzeks Der Heimweg'. Actual: '11. The Calendar Killer'". Below the error, an informational message explains: "IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code."
image1640×302 20.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/7/67d552f9ef5b8b06cae0421fe8d91bcdf4352af7.png)

I took first 25 films which 5 to 6 rating, but json seems to be different.

Could anyone please tell me what i did wrong here?

---

### Post #246 by Arulvadivelan V on 2025-02-09T12:36:29.100Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/246

Solved the above issue, please ignore it.

---

### Post #247 by NamanBeri on 2025-02-09T12:52:04.835Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/247

Believe it or not, I solved it

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/1/414417f047a85a16fdcf3ef8d9f1e0ac38298e91.png)

> **Image Description**: The image displays a user interface screenshot related to Markdown content and formatting.

1.  **Question Statement:** At the top, a question asks: "What is the markdown content of the PDF, formatted with prettier@3.4.2?"
2.  **Markdown Content Box:** Below the question, a dark-themed text input box contains the following Markdown content:
    *   `|adficio|chirographum|`
    *   `|---|---|`
    *   `|vitae|ipsam|`
    *   `|spectaculum|claudeo|`
    *   `|comes|celebrer|`
    *   (A blank line)
    *   `Decumbo decumbo suadeo totidem apto.`
    A green checkmark icon is present in the top-right corner of this box, indicating correctness.
3.  **Feedback:** Directly below the content box, the word "Correct" is displayed in green.
4.  **Instructional Text:** Further below, additional text provides context: "It is *very hard* to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic things."
image657×516 26.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/1/414417f047a85a16fdcf3ef8d9f1e0ac38298e91.png)

---

### Post #248 by Arnav M on 2025-02-09T12:54:22.008Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/248

In the 10th question, how do we add headings and links to the markdown output?(getting error: Headings missing)

---

### Post #249 by NamanBeri on 2025-02-09T13:00:26.515Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/249

first convert it roughly to md file then use ai and tell it to add (all the errors one by one). and slowly it will solve all the errors

yes i know it is not the correct way to convert pdf to md file but its just a way to trick the checking system.

but i have an issue it gave me error that it does not contains the word “bash, javascript, whole  redesign, net, suasoria” which is not in the actual pdf, but i added it and it worked. it was just pure trial and error.

---

### Post #250 by Vedant Bhanushali on 2025-02-09T13:01:11.101Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/250

this is a changing dataset so make changes to your answer accordingly and you will get it correct

---

### Post #251 by Vedant Bhanushali on 2025-02-09T13:02:38.460Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/251

Do the necessary changes as it is said below as it is an everchanging dataset.

You will get the answer correct once you make the changes asked after checking.

---

### Post #252 by Vedant Bhanushali on 2025-02-09T13:04:14.674Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/252

check you code and do the changes like max_latitude

replace [0] to [1]

---

### Post #253 by Arnav Raj  on 2025-02-09T13:04:24.869Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/253

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/4/f450d51580b01f5c78c74fda3d31e33c39d5e4cd.png)

> **Image Description**: The image displays a programming interface or an interactive coding environment. It features two JSON-like code blocks and a question.

The top code block presents a weather forecast with dates and descriptions, starting from "2025-01-01" to "2025-01-03".

Below this, a question is posed: "What is the JSON weather forecast description for Nur-Sultan?".

Following the question, there is an input area containing another JSON-like structure, partially obscured at the top, showing weather descriptions for dates "2025-02-14" through "2025-02-21". This input area is highlighted with a red border and an error icon.

Beneath the input area, a "TypeError: Cannot read properties of undefined (reading 'id')" message is displayed. A "Check" button is visible at the bottom of the interface.
image835×606 34.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/4/f450d51580b01f5c78c74fda3d31e33c39d5e4cd.png)

sir in Q4 i am getting this error:

TypeError: Cannot read properties of undefined (reading 'id')

please help me out with it.

Additionally even if i write anything in the code block the err remains same!

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

[@s.anand](/u/s.anand)
 sir please help me out as only this question left.

anyone facing this issue? let me know

{
     "25-02-09": "Partly cloudy and a moderate breeze",
     "25-02-10": "Sunny intervals and a moderate breeze",
     "25-02-11": "Sunny and a gentle breeze",
     "25-02-12": "Light snow and a fresh breeze",
     "25-02-13": "Light snow and a fresh breeze",
     "25-02-14": "Light snow and a gentle breeze",
     "25-02-15": "Light snow and a gentle breeze",
     "25-02-16": "Light snow and a gentle breeze",
     "25-02-17": "Light snow and a gentle breeze",
     "25-02-18": "Sunny intervals and a gentle breeze",
     "25-02-19": "Light cloud and a gentle breeze",
     "25-02-20": "Light cloud and a gentle breeze",
     "25-02-21": "Sunny and a moderate breeze"
}

---

### Post #254 by Yogaswetha on 2025-02-09T13:13:32.686Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/254

in my dashboard there is no submit button for ga2,3,and 4 as well and if i check for scores in grades tab for ga2 and ga3 it was given as not submitted , does everyone facing the same ?? if the submit button is visible for anyone plss guide me to rectify that.

regards and thanks.

---

### Post #255 by Yogaswetha on 2025-02-09T13:18:09.159Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/255

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/f/ef219ad49e61451fe1acd27ae7ca8e29282183ec.png)

> **Image Description**: The image displays a user interface or problem statement related to web API development.

The top section, against a dark background, shows a Markdown-formatted outline structure. It includes examples of various heading levels, such as `# Vanuatu`, `## Etymology`, `## History`, and `### Prehistory`, followed by an ellipsis, indicating a longer outline.

The bottom section, on a white background, presents a numbered list of five steps for developing a web application:
1.  **API Development:** Creating an API endpoint (e.g., `/api/outline`) using a web framework (e.g., FastAPI) that accepts a `country` query parameter.
2.  **Fetching Wikipedia Content:** Retrieving the HTML from a Wikipedia page for a given country.
3.  **Extracting Headings:** Parsing the fetched HTML using a library (e.g., BeautifulSoup, lxml) to extract all H1 through H6 headings, maintaining their order.
4.  **Generating Markdown Outline:** Converting the extracted headings into a Markdown-formatted outline, with headings beginning with `#`.
5.  **Enabling CORS:** Configuring the web application to include appropriate CORS headers to allow GET requests from any origin.

Below these instructions, a question asks: "What is the URL of your API endpoint?" An input field is pre-filled with the URL `http://127.0.0.1:8000/api/outline?country=france`. Beneath this input field, a red error message states: `TypeError: Failed to fetch`.
image1224×540 18.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/f/ef219ad49e61451fe1acd27ae7ca8e29282183ec.png)

it is showing correct but if i reload the page or press ctrl+c in my terminal its showing this error what should i do now ??

---

### Post #256 by D HARICHARAN  on 2025-02-09T13:34:26.111Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/256

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/1/71457b8edf035cb36daa79ab63829130b5308c5e.png)

> **Image Description**: The image displays a problem statement titled "Media Intelligence for TechInsight Analytics," detailing a task for a Tools in Data Science course. The text describes TechInsight Analytics' need to monitor Hacker News posts using the HNRSS API for topic monitoring, engagement filtering, and data extraction.

The "Your Task" section provides specific instructions:
1.  **Automate Data Retrieval:** Use the Hacker News RSS API to fetch the latest posts, searching for topics and filtering by a minimum number of points.
2.  **Extract and Present Data:** Extract the most recent `<item>` element and its enclosed `<link>` tag.
3.  **Share the result:** Type the URL into the answer field.

The specific question posed is: "What is the link to the latest Hacker News post mentioning WebRTC having at least 30 points?" Below the question, an input field shows a user's attempted URL answer: "https://news.ycombinator.com/item?id=41699323," with an accompanying "Error: Incorrect link" message, and a "Check" button.
image1150×776 54.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/1/71457b8edf035cb36daa79ab63829130b5308c5e.png)

Respected Sir,

How can I Solve this, I’m not able to solve this one

---

### Post #257 by Arulvadivelan V on 2025-02-09T13:39:15.522Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/257

Hi,

For the 4th question, We can get the necessary information issueDate and its description from Summary itself right? or am I seeing the stuff in the wrong place?

---

### Post #258 by maroof abdullah on 2025-02-09T13:40:26.226Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/258

Change it manually.

add the expected answer

---

### Post #259 by Arnav Raj  on 2025-02-09T13:51:57.206Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/259

when you press ctrl+c it turns off the server and same goes for refresh.

also you dont need to manually write ?country… just write till outline and turn on the server n you are good to go.

---

### Post #260 by Yogaswetha on 2025-02-09T13:54:54.255Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/260

ok this is fine for now and its showing correct also but at the time of evaluation will my server runs??

---

### Post #261 by PREMDEEP MAITI on 2025-02-09T14:06:29.442Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/261

It is written in the ques to get the link in the link tag. Not the post link.  Like this

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/f/1feee64a40176f409c30dd00704be9b67c9b32e7_2_690x263.png)

> **Image Description**: The image displays an XML document, likely an RSS feed, with a dark background and colored text. The document starts with a top message indicating a lack of style information and shows the document tree below.

The XML structure includes a root `<rss>` element with namespace declarations. Nested within, a `<channel>` element contains general feed information such as:
- `<title>`: "Hacker News - Newest: "LLM""
- `<link>`: "https://news.ycombinator.com/newest/"
- `<description>`: "Hacker News RSS"
- `<generator>`: "hnrss v2.1.1"
- `<lastBuildDate>`: "Sun, 09 Feb 2025 08:44:00 +0000"

The `<channel>` also contains an `<item>` element, representing a single feed entry. This item includes:
- `<title>`: "<!--[CDATA[ DoppelBot: Replace Your CEO with an LLM ]]-->"
- `<description>`: A `CDATA` section containing HTML with an article URL (https://modal.com/docs/examples/slack-finetune), comments URL, points (232), and number of comments (116).
- `<pubDate>`: "Tue, 04 Feb 2025 15:08:21 +0000"
- A `<link>` tag containing the URL "https://modal.com/docs/examples/slack-finetune", which is highlighted by a red rectangle.
- `<dc:creator>`: "gk1"
- `<comments>`: "https://news.ycombinator.com/item?id=42933256"
- `<guid isPermalink="false">`: "https://news.ycombinator.com/item?id=42933256"
image1464×560 115 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/f/1feee64a40176f409c30dd00704be9b67c9b32e7.png)

---

### Post #262 by D HARICHARAN  on 2025-02-09T14:08:38.790Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/262

Thank you bro, I will try this

---

### Post #263 by Arnav Raj  on 2025-02-09T14:11:14.190Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/263

not at all. your last saved marks will be considered

---

### Post #264 by DHANUSH.R on 2025-02-09T14:18:30.851Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/264

just replace value instead of it. same problem I also that time I check code and modify serval time I faced same error. so just ignore it and replace expected value instead of actual value in our Json.

---

### Post #265 by Thereasa Joe J on 2025-02-09T14:21:38.216Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/265

extract the pdf to markdown format using chatgpt then add links,tables and one blockquote

---

### Post #266 by Rajalakshmi Rathinasabhapathy on 2025-02-09T14:22:18.004Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/266

Try to use the key ‘enhancedWeatherDescription’ parsing through the summary object (or) use the BeautifulSoup to find ‘div’ with attributes of

class: wr-day-summary

---

### Post #267 by Rajalakshmi Rathinasabhapathy on 2025-02-09T14:35:34.384Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/267

Hi, please  ensure that your repository is public, if private the response would be 404. If workflow runs is not found, it might be that the number of API calls to your profile/repo might have exceeded, it usually gets reset at the end of the day. Please try again after sometime)

---

### Post #268 by GIRISH VISHVESHVAR BHAT on 2025-02-09T14:47:12.663Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/268

In question 1 i am getting this error

 {
    "id": "tt21227864",
    "title": "2. You're Cordially Invited",
    "year": "2025",
    "rating": "5.5"
  }

my answer is in above format i tried changing to “2024-”, "2024- " to number tried after reloading the page but still i am getting

Error: At [11].year: Values don’t match. Expected: “2024”. Actual: "2024– "

---

### Post #269 by Sagandeep Kaur on 2025-02-09T15:05:50.845Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/269

You have to manually change these thing

from actual change to expected.

For me, error was almost 10 times.

---

### Post #270 by Sagandeep Kaur on 2025-02-09T15:06:58.477Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/270

on your 11th or 12th instance change it

write the actual value

---

### Post #271 by Ritwik Trivedi on 2025-02-09T15:11:37.467Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/271

If you have submitted on the assignment site and saved it in time, then that score is the actual score and will be updated directly on the student dashboard.

---

### Post #272 by Md anas alam on 2025-02-09T15:21:41.857Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/272

Your answer is correct. Just add a space after the hyphen—it will resolve the problem. Or you can copy and paste from here: '2025– '.

---

### Post #273 by D HARICHARAN  on 2025-02-09T15:22:57.529Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/273

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/e/3e2860ae2ae9e6113188a70581f1c1ce7e7913b4_2_690x355.png)

> **Image Description**: The image displays an online assessment interface with a dark theme. A top banner shows a timer (03:08:26 left), score (7/10), and 'Check all' and 'Save' buttons. The main content outlines an exercise to convert a PDF document (`q.pdf-to-markdown.pdf`) into Markdown format, accurately preserving its structure, and then formatting the converted Markdown using Prettier version 3.4.2. The task requires submitting the final formatted Markdown file. The screen includes an 'Impact' section detailing benefits like 'Enhances Productivity' and 'Facilitates Integration'. A question prompt asks, 'What is the markdown content of the PDF, formatted with prettier@3.4.2?'. Below this, a text input area, outlined in red, contains pre-filled content. This content includes Markdown-formatted hyperlinks `[tricesimus admitto](https://example.com/tricesimus-admitto)` and `[adeptio colligo](https://example.com/adeptio-colligo)`, which are visually indicated with red underlines, along with Latin text segments 'Suggero comes denique argentum.' and 'Desipio crudelis antea quis.'. An error message 'Error: Missing code' is displayed directly beneath the input area. A final note clarifies that accurate PDF to Markdown conversion is challenging and the question only checks basic aspects.
image1895×975 73.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/e/3e2860ae2ae9e6113188a70581f1c1ce7e7913b4.png)

i wrote everything that was there in the pdf file after converting to markdown, there is no code inside the pdf file then how does it expect to have code in markdown, can anyone help

---

### Post #274 by Rishit on 2025-02-09T15:36:39.718Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/274

Yeah! His issue is genuine. Arnav’s JSON seems to be correct, yet these are some issues faced by him.

---

### Post #275 by Rishit on 2025-02-09T15:41:57.385Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/275

Yeah! even I am facing this issue. Despite lot of efforts, last question markdown seems to always incorrect. It is always throwing any sort of error for no reason.

---

### Post #276 by Sandeep S on 2025-02-09T15:43:25.700Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/276

The IMDB and weather questions was a pain along with the 10th question, wasted so much time
[@s.anand](/u/s.anand)
 , the questions were nowhere tough, it was the problems with the evaluation part i had spend hours just to  sit and correct the JSON file and no comments on the 10th question’s part.

I am fine with the academia being challenging to study not the evalation making me manually edit solutions

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

---

### Post #278 by Tanya kamboj on 2025-02-09T15:46:29.876Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/278

yes change manually, there are slight changes which we have to do

---

### Post #279 by Shahsank J Shetty on 2025-02-09T15:46:42.193Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/279

For the 8th question, i am getting an error that tells me i have not run the action, though i manually triggered it and confirmed the commit was made. Cant figure out whats wrong.

---

### Post #280 by Jayaram on 2025-02-09T15:50:47.039Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/280

for second query i am getting this result as row 4 and 5 (Screenshot)… but when testing the results it shows

{"id":"tt22804850","title":"3. The Sand Castle","year":"2024","rating":"4.7"},
{"id":"tt10128846","title":"4. Megalopolis","year":"2024","rating":"4.8"},
{"id":"tt2322441","title":"5. Fifty Shades of Grey","year":"2015","rating":"4.2"},
{"id":"tt4978420","title":"6. Borderlands","year":"2024","rating":"4.6"},

Error: At [4].title: Values don’t match. Expected: “5. Cinquanta sfumature di grigio”. Actual: “5. Fifty Shades of Grey”

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/03e20670dbfaddeb6f2f989235b64cdb9ef7f5c4_2_690x433.png)

> **Image Description**: The image displays a partial list of two movies, numbered 4 and 5, presented with a consistent data structure.

For movie 4, "Megalopolis":
- Release Year: 2024
- Runtime: 2 hours 18 minutes
- Age Rating: 15
- User Rating: 4.8 out of 5 stars, based on 33,000 (33K) reviews.
- Metascore: 55
- A truncated plot description begins with: "The city of New Rome faces the duel between Cesar Catilina, a brilliant artist in th mayor Franklyn Cicero. Between them is Julia Cicero, with her loyalty divided bet".
- A movie poster featuring multiple characters is displayed to the left.

For movie 5, "Fifty Shades of Grey":
- Release Year: 2015
- Runtime: 2 hours 5 minutes
- Age Rating: 18
- User Rating: 4.2 out of 5 stars, based on 344,000 (344K) reviews.
- Metascore: 46
- A truncated plot description begins with: "Literature student Anastasia Steele's life changes forever when she meets hands".
- A movie poster, predominantly grayscale and depicting a man, is displayed to the left.

Both movie posters feature a clickable "+" icon in the top-left corner. The data for each movie is presented in a structured format, including textual descriptions and numerical metrics.
image784×492 91.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03e20670dbfaddeb6f2f989235b64cdb9ef7f5c4.png)

---

### Post #281 by Tanya kamboj on 2025-02-09T15:58:59.656Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/281

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f57651c1c8662de593d35d1771ddf8eb5f3f2cc2.png)

> **Image Description**: The image displays a question: "What is the JSON weather forecast description for Vienna?" Below the question, a JSON object is presented. This object contains five key-value pairs, where keys are dates ranging from "2025-02-10" to "2025-02-14", and values are string descriptions of the weather (e.g., "Sunny and a gentle breeze"). The JSON object is syntactically incorrect due to a trailing comma after the last property. Beneath the JSON structure, an error message states: "Error: At root: Different number of properties".
image606×293 20.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f57651c1c8662de593d35d1771ddf8eb5f3f2cc2.png)

sir earlier it was correct and now i submit it again after running my code it shows error.  sir i have done it correct two times earlier. but now again as i click on save button it changed. these tasks are taking too much time and creating more difficulties. please look into this
[@s.anand](/u/s.anand)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

---

### Post #282 by AnandMurti on 2025-02-09T15:59:12.855Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/282

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/03c2659de1532aefc02ea8eaa831c0955bf85b5d_2_690x131.png)

> **Image Description**: The image displays a screen capture from a data validation or coding interface. A question at the top asks, "What is the JSON data?". Below the question, a partial JSON structure is visible, beginning with an object containing:
- `"title": "1. The Night Agent"`
- `"year": "2023-"` (the year value appears incomplete)
- `"rating": "7.5"`
This object is followed by `}, {` indicating it's part of a JSON array and the start of a new object, whose `title` field begins with `"MESO...` but is mostly truncated.

An error message is prominently displayed at the bottom: "Error: At [8].title: Values don't match. Expected: "9. Incorrect answer [partially visible, likely 'également invités']". Actual: "9. You're Cordially Invited"". This error indicates a mismatch in the `title` value for the element at index 8 within a JSON array, showing both the expected and actual values.
image2100×400 38.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03c2659de1532aefc02ea8eaa831c0955bf85b5d.png)

Hi Team ,

Are we expecting the result to match exactly as per the benchmark of qa4.

---

### Post #283 by Arnav Raj  on 2025-02-09T16:04:51.693Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/283

just edit some of the spellings in answers manually as per errors you get n you are good to go.

---

### Post #284 by Madhu on 2025-02-09T16:05:40.244Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/284

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002723/48/110636_2.png)
 22f3002723:

Cinquanta sfumature di grigio

It is just a translation of the same movie… it’s not different

Copy paste the Expected: “title” and click on check

It’ll work

---

### Post #285 by B Varun karthik on 2025-02-09T16:09:30.499Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/285

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/2/221c84f86d6febf296e0a4a6903bb70c607afd41_2_690x287.png)

> **Image Description**: The image displays a quiz interface with a remaining time of "02:23:44" and a current "Score: 0", along with "Check all" and "Save" buttons. A statement explicitly indicates the quiz is "hackable" and that "hacking the code for this quiz" to obtain answers is permitted. A section labeled "Have questions?" directs users to "Join the discussion on Discourse" via a clickable link. Below this, a "Bonus marks for posting on Discourse" section describes a policy where IITM BS students can earn 1 bonus mark on the graded assignment by contributing a "relevant question or reply" to the "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]". The user's login ID is displayed as "23f2001305@ds.study.iitm.ac.in", accompanied by a "Logout" button. A loading spinner is present at the bottom.
image1802×751 40 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/2/221c84f86d6febf296e0a4a6903bb70c607afd41.png)

Saved responses are not being displayed and also page keeps refreshing…

---

### Post #286 by Naman S.  on 2025-02-09T16:09:48.477Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/286

@all
, in q4 Actually the answer data is sync with current weather description therefore the answer changes. Make sure to update your json file before submitting.

---

### Post #287 by Chinnam Goutham Nischay on 2025-02-09T16:10:43.735Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/287

try refreshing the page and re-run the script. as the data gets updated the answer also changes.

---

### Post #288 by VIKASH PRASAD on 2025-02-09T16:13:55.561Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/288

refer to the link post,

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f3002277/48/12741_2.png)

[GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/65)

[Tools in Data Science](/c/courses/tds-kb/34)

    use this
[Google Colab](https://colab.research.google.com/drive/1X5IO8K1Xf8Wh7SOZelSrFAfZgRG-mv4A?usp=sharing)
 with the city name to get the Json Body just change the date format.

[@23f2004752](/u/23f2004752)

---

### Post #290 by Rohit Garg on 2025-02-09T16:15:41.126Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/290

i 'm here for the bonus marks,

But since i am here. Just want to appreciate the course and your efforts towards this.

We need more “teachers” like you, who really puts an extra effort in the course.

And i have never seen any course cool as this,

like appreciating tweaking things, using dev console to tweak things, keep the code checks on client side (
and as S Anand’s Student i have leveraged that freedom
![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12)
, gave client side answer checks’s code to
o1
 and it reverse engineered the minifed code, and lots of question were solved by that only, but really curious on how others are doing this
)

keeping the cutting edge tech in course, like function calling from OpenAI.

(
i have seen some students solutions, they were using regex to solve that problem
![:smiling_face_with_tear:](https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=12)
)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/5/45b8773aa8f61abb7b67eaa7e81ae42fcfc0e576_2_690x319.png)

> **Image Description**: The image displays a web page interface for a student in a Tools in Data Science course. It features a section for questions, encouraging students to "Join the discussion on Discourse" via a clickable link. A "Bonus marks for posting on Discourse" section states that IITM BS students can earn 1 bonus mark on a graded assignment by posting relevant questions or replies on the "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]" link.

The page shows the user logged in as "22f2001394@ds.study.iitm.ac.in" with a "Logout" button. Below this, a "Recent saves" section lists previous assignment scores and timestamps, indicating the most recent save is the official score. The entries include:
*   2/9/2025, 9:26:17 PM, Score: 10
*   2/9/2025, 7:48:07 PM, Score: 8
*   2/9/2025, 7:44:44 PM, Score: 8
Each entry has a "Reload" button associated with it.
image1483×687 48.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/5/45b8773aa8f61abb7b67eaa7e81ae42fcfc0e576.png)

---

### Post #291 by Abhay Mehra on 2025-02-09T16:17:12.810Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/291

why everytime question 2 answer is showing error in json?

---

### Post #292 by Rohit Garg on 2025-02-09T16:20:29.219Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/292

What error are you getting
[@Abhay222](/u/abhay222)
 ?

Can you post a screenshot or error details ?

---

### Post #293 by Matlin Jeleshiya  on 2025-02-09T16:20:47.342Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/293

Is it safe to skip Q4 for those who got the city named Nur-Sultan, since it has been renamed to Astana, and the answer for Astana is incorrect in the portal?

---

### Post #294 by Parth Patel on 2025-02-09T16:23:37.267Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/294

[@s.anand](/u/s.anand)

There is possibly wrong evaluation in q6 as it is taking in 2nd latest link as the correct answer. I might be wrong, but the latest one is giving me incorrect evaluation while the 2nd latest is giving me the correct score.

---

### Post #295 by Rahul  on 2025-02-09T16:23:43.629Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/295

getting the same issue Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

---

### Post #296 by Abhay Mehra on 2025-02-09T16:25:24.448Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/296

yes this kind errors.

---

### Post #297 by Rohit Garg on 2025-02-09T16:29:06.442Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/297

[@Abhay222](/u/abhay222)

[@22f3002184](/u/22f3002184)

if you look closely the expected value is
2024-
 and actual that you are supplying is
2024
.

Difference ? your value does have a
-
 and a space at the end.

reason ? you might be scraping it ?
trim()
 or maybe using
innerText
 to get tag’s text ?

---

### Post #298 by Anudeep on 2025-02-09T16:30:02.184Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/298

it seems we are intended to provide country specific versions for Individual students simulating being an analyst for MNC in various locations. Clearly you got Spain and I seem to have gotten France, although it doesn’t seem to be mentioned in the question itself.

---

### Post #299 by Saransh Saini on 2025-02-09T16:30:25.035Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/299

Thank you Tanya for pointing out this issue.

Just tell me this, has your city changed? If yes then what was it earlier and what is it now.

---

### Post #301 by Yogaswetha on 2025-02-09T16:33:41.438Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/301

any reply regarding this please

---

### Post #302 by Debarpita Dash on 2025-02-09T16:34:55.919Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/302

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f2000113/48/67775_2.png)
 22f2000113:

For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name

the movie may have  different title on IMDb (perhaps in another language) according to region which is why there isnt an exact match u can manually format it to get marks

---

### Post #303 by Saransh Saini on 2025-02-09T16:35:18.237Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/303

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/saransh_saini/48/123495_2.png)

[GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/171)

[Tools in Data Science](/c/courses/tds-kb/34)

    We have removed that button, cause it was causing confusion among the students.
If you have saved your answers on the TDS portal then you need not worry, you will be marked. The button was just there to ensure you saw the assignment on the TDS portal.
Regards,
TDS TA

Read this

---

### Post #304 by Nayonika Arora on 2025-02-09T16:40:31.628Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/304

Try changing it manually. Some values keep changing due to change in server.

---

### Post #305 by Aarsh Sohane on 2025-02-09T16:42:06.985Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/305

Alright so in Q4 of W4, We have to extract weather forecast data from bbc servers for a given city. The city I have been given Nur-Sultan is not present in the bbc data base, it appears the city is now known as Astana and is listed in the bbc database as Astana.

Since Nur-Sultan doesn’t exist in the bbc database, all of my attempts to extract data for it were meet with failure. So I extracted the data for Astana and pasted it in the portal but that doesn’t work as well and throws the following error “TypeError: Cannot read properties of undefined (reading ‘id’)”

What am I suppose to do?
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

[![Screenshot 2025-02-09 175948](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/b/cb0483e0b093e1e994ba44b8136f6b4f5865cdc7_2_690x321.png)

> **Image Description**: The image displays a data science exercise interface.

The top section includes:
*   A timer: "06:00:20 left"
*   A score: "Score: 3 / 10"
*   Buttons: "Check all", "Save"

Below, three numbered instructions detail a data processing task:
1.  **API Integration and Data Retrieval:** Use the BBC Weather API to fetch weather forecast for Nur-Sultan. This involves a GET request to a locator service to obtain a `locationId`, including query parameters like API key, locale, filters, and search term (city).
2.  **Weather Data Extraction:** Send a GET request to a weather broker API endpoint using the `locationId` to retrieve weather forecast data.
3.  **Data Transformation:** Extract `issueDate` and `enhancedWeatherDescription` from each day's forecast within the `forecasts` array of the API response. Create a JSON object where each key is the `issueDate` and the value is the `enhancedWeatherDescription`.

An example output format is provided:
```json
{
  "2025-01-01": "Sunny with scattered clouds",
  "2025-01-02": "Partly cloudy with a chance of rain",
  "2025-01-03": "Overcast skies"
  // ... additional days
}
```

The main question is posed: "What is the JSON weather forecast description for Nur-Sultan?"

Below the question, an input field shows a user's attempted JSON response:
```json
{
  "2025-02-09": "Partly cloudy and a moderate breeze",
  "2025-02-10": "Sunny intervals and a moderate breeze",
  "2025-02-11": "Sunny and a gentle breeze",
  "2025-02-12": "Light snow and a fresh breeze",
  "2025-02-13": "Light snow and a fresh breeze"
}
```
An error message `TypeError: Cannot read properties of undefined (reading 'id')` is displayed below the input. A "Check" button is visible at the bottom.
Screenshot 2025-02-09 1759481823×850 82.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/b/cb0483e0b093e1e994ba44b8136f6b4f5865cdc7.png)

Below is the data for Astana that I was able to extract, Since Nur-Sultan doesn’t exist in the bbc database:

{

“2025-02-09”: “Partly cloudy and a moderate breeze”,

“2025-02-10”: “Sunny intervals and a moderate breeze”,

“2025-02-11”: “Sunny and a gentle breeze”,

“2025-02-12”: “Light snow and a fresh breeze”,

“2025-02-13”: “Light snow and a fresh breeze”,

“2025-02-14”: “Light snow and a gentle breeze”,

“2025-02-15”: “Light snow and a gentle breeze”,

“2025-02-16”: “Light snow and a gentle breeze”,

“2025-02-17”: “Light cloud and a gentle breeze”,

“2025-02-18”: “Sunny intervals and a gentle breeze”,

“2025-02-19”: “Light cloud and a gentle breeze”,

“2025-02-20”: “Light cloud and a gentle breeze”,

“2025-02-21”: “Sunny and a moderate breeze”,

“2025-02-22”: “Light snow and a moderate breeze”

}

---

### Post #306 by Anvitha on 2025-02-09T16:42:55.994Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/306

same problem, could anyone help what is wrong.

---

### Post #307 by Rohit Garg on 2025-02-09T16:48:37.375Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/307

[@AnvithaV](/u/anvithav)
  check this out

---

### Post #308 by Tanya kamboj on 2025-02-09T16:50:23.681Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/308

No the city is same as before. But i think it fetches the latest data. As i saved it yesterday it was correct. But today when i  clicked on save button again it got wrong.

---

### Post #309 by Tanya kamboj on 2025-02-09T16:52:32.951Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/309

What error are you getting ?

---

### Post #310 by Vidya Bharti on 2025-02-09T16:52:52.617Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/310

how to approach question 8 of ga4

---

### Post #311 by Syed Zakiyuddin on 2025-02-09T16:53:06.031Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/311

For question
#8
. Can I use the .github/workflows that I created for the previous assignments or i need to create a new workflow?

---

### Post #312 by Rahul  on 2025-02-09T16:55:01.459Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/312

still the same   {“id”:“tt24871974”,“title”:“12. Subservience”,“year”:“2024”,“rating”:“5.4”},

Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

---

### Post #313 by Baddila Mohan Sai on 2025-02-09T16:55:45.350Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/313

Change the value manually

---

### Post #314 by Steven Robert on 2025-02-09T16:55:51.950Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/314

I am still not sure why the github action question is not working for me. I have manually triggered the workflow multiple times but i keep getting the same ‘name’ error even though it has been specified in the code. Can somebody kindly help?

---

### Post #315 by Tanya kamboj on 2025-02-09T16:56:34.118Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/315

Have you given your email id in name ?

---

### Post #316 by Jash Mevada on 2025-02-09T16:57:04.532Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/316

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/1/21dbd684835d5255b1520553a57a871933d026c3_2_690x291.png)

> **Image Description**: The image displays a user interface for an online assessment or assignment in a dark mode theme. The top green bar indicates "01:37:59 left" and "Score: 10 / 10," along with "Check all" and "Save" buttons. A user is logged in as "23f2003807@ds.study.iitm.ac.in" with a "Logout" option. A section titled "Recent saves" shows three previous scores with corresponding timestamps and "Reload" buttons: two saves on "2/9/2025" at "10:20:36 PM" and "10:20:18 PM" with "Score: 10," and one save at "9:42:55 PM" with "Score: 7." The interface also presents the beginning of a "Questions" section, with the first question stated as "1. Import HTML to Google Sheets (1 mark)."
image1865×789 48 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/1/21dbd684835d5255b1520553a57a871933d026c3.png)

Completed GA4 with 10/10.

I have also use tweak that the some answer and question are check and generate on client side.

---

### Post #317 by Tanya kamboj on 2025-02-09T16:57:11.845Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/317

See there is difference of hyphen . Correct it manually.

---

### Post #318 by Saransh Saini on 2025-02-09T16:57:35.122Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/318

Just try re-running your code once and paste in the current response. Check if its working or not.

---

### Post #319 by Baddila Mohan Sai on 2025-02-09T16:58:00.163Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/319

Change the slight differences manually accordingly with the expected values

---

### Post #320 by Ashish on 2025-02-09T17:01:51.864Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/320

I haven’t done MLP and BDM so should I drop TDS now

---

### Post #321 by Arulvadivelan V on 2025-02-09T17:06:00.951Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/321

Hi,

I couldn’t able to create markdown from pdf, it showing missing links, but i couldn’t able to find the link in pdf either. I think i’m missing something.

anyone suggest some way how to do pdf to markdown correctly?

---

### Post #322 by B R GIRI SUBRAHMANYA on 2025-02-09T17:08:16.185Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/322

if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary

---

### Post #323 by Steven Robert on 2025-02-09T17:08:23.051Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/323

yes

But still doesnt work

---

### Post #324 by Tanya kamboj on 2025-02-09T17:10:40.176Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/324

In q10 i am geeting …missing links- error

Any idea how to correct this

---

### Post #326 by Parmeet Singh on 2025-02-09T17:12:23.430Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/326

Beyond the specific tools mentioned (like
IMPORTHTML
 in Google Sheets or
httpx
 and
lxml
 in Python), what are the broader
ethical considerations
 when scraping data from websites, and how can developers ensure they are acting responsibly and respecting website owners’ rights and resources?

---

### Post #327 by Yogaswetha on 2025-02-09T17:12:57.853Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/327

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/b/eb807d6c56fc02a8517f9390f49d9b582b1f8150.png)

> **Image Description**: The image displays a multi-step data retrieval and extraction task. The core task is to search the Hacker News RSS API for the latest post mentioning "WebAssembly" with a minimum of 86 points and extract its corresponding URL. Instructions detail utilizing the HNRSS API for topic search and point filtering, followed by extracting the `<link>` tag from the most recent `<item>` element in the retrieved RSS feed. A provided input field shows an incorrect submission (`https://news.ycombinator.com/item?id=38790552`), accompanied by an "Error: Incorrect link" message.
image1104×369 21.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/b/eb807d6c56fc02a8517f9390f49d9b582b1f8150.png)

is everything fine with the answer format?? i am trying this for so long anything i want to change ??

---

### Post #328 by Tanya kamboj on 2025-02-09T17:18:23.735Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/328

What is the error are you facing ?

---

### Post #329 by Hemant Singh on 2025-02-09T17:20:50.330Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/329

can someone  help through this error!!

[![Capture](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/5/e5e41010e6ca37b8390b22c4c9ea80d49ea2394d_2_690x125.jpeg)

> **Image Description**: The image displays a text-based interface featuring a question, a block of JSON data, and an error message.

The question posed is "What is the JSON data?".

Below the question, a partial JSON array is visible, containing six objects. Each object represents an item (likely a movie or show) and includes four key-value pairs:
*   `"id"`: A string identifier (e.g., `"tt8999762"`).
*   `"title"`: A string title (e.g., `"5. The Brutalist"`).
*   `"year"`: A string representing the year or a year range (e.g., `"2024"`, `"2021-2025"`).
*   `"rating"`: A string representing a numerical rating (e.g., `"8.0"`).

The visible data includes entries such as:
*   `{"id":"tt8999762", "title":"5. The Brutalist", "year":"2024", "rating":"8.0"}`
*   `{"id":"tt27657135", "title":"6. Saturday Night", "year":"2024", "rating":"7.0"}`
*   `{"id":"tt17526714", "title":"7. The Substance", "year":"2024", "rating":"7.3"}`
*   `{"id":"tt10919420", "title":"8. Squid Game", "year":"2021-2025", "rating":"8.0"}`
*   `{"id":"tt21227864", "title":"9. Un matrimonio di troppo", "year":"2025", "rating":"5.5"}`
*   A partially visible sixth entry `{"id":"tt26584495", "title":"10. Companion", "year":"2025", "rating":"7.4"}`.

Below the JSON data, an error message is displayed: "Error: At [10]year: Values don't match. Expected: "2021-". Actual: "2021-"".
Capture1119×204 37.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/5/e5e41010e6ca37b8390b22c4c9ea80d49ea2394d.jpeg)

---

### Post #330 by B R GIRI SUBRAHMANYA on 2025-02-09T17:22:36.650Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/330

Check if you have made the query proprly. also, check if you taken the correct link from the item

---

### Post #331 by Tanya kamboj on 2025-02-09T17:22:37.064Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/331

in q10 i am getting error- missing links.

can i get any explanation about this error so that i can figure out this ?

[@Saransh_Saini](/u/saransh_saini)
  as i left with this question only

---

### Post #332 by Jash Mevada on 2025-02-09T17:23:01.174Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/332

Pdf content one link, I think your converting method was unable to convert link into markdown format , add it manual from pdf.

---

### Post #333 by Tanya kamboj on 2025-02-09T17:23:44.720Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/333

I have done that also but still getting same error

---

### Post #334 by Tanya kamboj on 2025-02-09T17:24:22.138Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/334

The one with blue line must be link here in the pdf.

---

### Post #335 by Arulvadivelan V on 2025-02-09T17:25:39.334Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/335

After that it asking to add tables, i added the same but the issue ‘Missing Tables’ exists

---

### Post #336 by B R GIRI SUBRAHMANYA on 2025-02-09T17:25:58.086Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/336

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png)
 23f2000573:

if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary

refer to this
[@21f3000745](/u/21f3000745)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000804/48/87428_2.png)
 22f3000804:

can someone help through this error!!

if it is saying something has a mismatch, just spot the mismatch one by one and manually change it
[@22f3000804](/u/22f3000804)

---

### Post #338 by Sayan Das on 2025-02-09T17:34:04.509Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/338

Here for the bonus marks, it was great solving the GA4.

---

### Post #339 by Megha Gupta on 2025-02-09T17:36:09.369Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/339

After you click the link, a page containing all the questions will appear. Attempt them and save it on that particular page using your IITM email ID. Through your ID, submissions will be taken.

---

### Post #340 by Tanya kamboj on 2025-02-09T17:39:48.455Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/340

Thankyou , but now i am getting missing code error. What it means?
[@23f2000573](/u/23f2000573)

---

### Post #341 by Ian Jem on 2025-02-09T17:41:44.880Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/341

You just have to add a space after a hyphen

---

### Post #342 by Saransh Saini on 2025-02-09T17:46:11.087Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/342

Check if you are using table formating where there is a table, also there is perhaps a code block in the pdf where a small section of text is in different font than the rest.

---

### Post #343 by Tanya kamboj on 2025-02-09T17:49:43.501Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/343

No there is no code block in the pdf. Now i m getting missing code error. Why this error can arise
[@Saransh_Saini](/u/saransh_saini)

---

### Post #344 by Sohini Sarkar  on 2025-02-09T17:52:19.318Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/344

I am also facing the same error in this question

---

### Post #345 by Vidushi Singh on 2025-02-09T18:00:21.016Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/345

the answer format is correct the link is probably not the latest one, I had the same issue because my code was working only for the first 100 entries… you should try paginating your code so it can cover more entries

---

### Post #346 by Aditya goyal on 2025-02-09T18:00:29.669Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/346

just change the values as itis coming in the error

---

### Post #347 by Vidushi Singh on 2025-02-09T18:06:17.921Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/347

change the name manually as the name is diiferent on imdb according to the region, I had the same issue…

---

### Post #348 by Arnav Raj  on 2025-02-09T18:06:48.092Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/348

are you able do it now? Reload and check

---

### Post #349 by Rahul  on 2025-02-09T18:08:17.696Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/349

yes facing the same thing

---

### Post #350 by B R GIRI SUBRAHMANYA on 2025-02-09T18:10:54.794Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/350

you are missing code block

Normal : print(123)

Code Block :
print(123)

you can refer to week 2 q1  for the syntax of code block

---

### Post #351 by Nishant kaushik on 2025-02-09T18:11:10.464Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/351

[![Screenshot 2025-02-09 234028](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/b/2b416c389edbb461f8f61e84d1ab68d273774860_2_690x113.png)

> **Image Description**: The image displays a user interface element with the question "What is the JSON data?". Below this, a text box contains a partial JSON array. The visible data includes multiple objects, each likely representing a movie with fields such as `id`, `title`, `year`, and `rating`. Examples of movie titles include "Crow", "A Serbian Film", and "Madame Web". An error icon is present within the text box. Below the text box, a `TypeError` message is visible, stating "Cannot read properties of null (reading 'textContent')".
Screenshot 2025-02-09 2340281910×314 56.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/b/2b416c389edbb461f8f61e84d1ab68d273774860.png)

anyone have idea about this error?

---

### Post #352 by Rahul  on 2025-02-09T18:13:12.352Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/352

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/d/dd7e129ca76ee1af2b83f85ed831e58c5010f861_2_690x144.png)

> **Image Description**: The image displays a user interface element from a data science tool, featuring a section titled "Impact." This section describes the benefits of automating bounding box data extraction and processing for "UrbanRide," listing improvements in "Optimize Routing," "Improve Fleet Allocation," "Enhance Market Analysis," and "Scale Operations." Below this, a question is posed: "What is the maximum latitude of the bounding box of the city Riyadh in the country Saudi Arabia on the Nominatim API? Value of the maximum latitude". An input field shows the value "27.7020999" with a red border, indicating an error. Underneath the input field, an error message states: "Error: Incorrect latitude. Check OSM ID ending with 8390".
image1757×367 48.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/d/dd7e129ca76ee1af2b83f85ed831e58c5010f861.png)

getting this error

---

### Post #353 by Tanya kamboj on 2025-02-09T18:13:35.541Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/353

Yes thankyou i noticed that code block.

But now getting missig heading
[@Saransh_Saini](/u/saransh_saini)

---

### Post #354 by Arnav Raj  on 2025-02-09T18:13:40.353Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/354

[@carlton](/u/carlton)
 sir what about this question.

---

### Post #355 by Ian Jem on 2025-02-09T18:13:51.114Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/355

You have to go to the Settings tab, select Actions from the left panel and choose General from the drop-down list. Then scroll down completely and choose “Read and Write Permission” under the Workflow Permission section

---

### Post #356 by Jayaram on 2025-02-09T18:17:00.243Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/356

Getting at root differnt number of properties for below

"2025-02-10": "Sunny intervals and a gentle breeze",
"2025-02-11": "Light rain showers and a gentle breeze",
"2025-02-12": "Thundery showers and a gentle breeze",
"2025-02-13": "Thundery showers and a moderate breeze",
"2025-02-14": "Sunny intervals and a gentle breeze",
"2025-02-15": "Drizzle and a gentle breeze",
"2025-02-16": "Sunny and a gentle breeze",
"2025-02-17": "Sunny intervals and a gentle breeze",
"2025-02-18": "Sunny intervals and a gentle breeze"}

---

### Post #357 by Katherine Barreto on 2025-02-09T18:18:19.669Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/357

I’m assuming it’s occurring because the text formatting for the JSON is incorrect. Try and put it in the correct format

---

### Post #358 by Aarsh Sohane on 2025-02-09T18:20:37.267Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/358

I’ve reloaded a dozen time and even extracted the data again and again to account for any changes but it still doesn’t work.

---

### Post #359 by Jayaram on 2025-02-09T18:20:50.841Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/359

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002723/48/110636_2.png)
 22f3002723:

{"2025-02-10": "Sunny intervals and a gentle breeze",
"2025-02-11": "Light rain showers and a gentle breeze",
"2025-02-12": "Thundery showers and a gentle breeze",
"2025-02-13": "Thundery showers and a moderate breeze",
"2025-02-14": "Sunny intervals and a gentle breeze",
"2025-02-15": "Drizzle and a gentle breeze",
"2025-02-16": "Sunny and a gentle breeze",
"2025-02-17": "Sunny intervals and a gentle breeze",
"2025-02-18": "Sunny intervals and a gentle breeze"}

{“2025-02-09”: “Partly cloudy and light winds”,

“2025-02-10”: “Sunny intervals and a gentle breeze”,

“2025-02-11”: “Light rain showers and a gentle breeze”,

“2025-02-12”: “Thundery showers and a gentle breeze”,

“2025-02-13”: “Thundery showers and a moderate breeze”,

“2025-02-14”: “Sunny intervals and a gentle breeze”,

“2025-02-15”: “Drizzle and a gentle breeze”,

“2025-02-16”: “Sunny and a gentle breeze”,

“2025-02-17”: “Sunny intervals and a gentle breeze”,

“2025-02-18”: “Sunny intervals and a gentle breeze”}

---

### Post #361 by Katherine Barreto on 2025-02-09T18:23:16.226Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/361

There needs to be two weeks worth of data so if it’s starting from the 9th it should be till the 22nd

---

### Post #362 by Shivansh Gupta on 2025-02-09T18:24:45.474Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/362

make the edits clearly in the repository and then open it, the url that is then showed. Just copy and paste it into the box, it will work

---

### Post #363 by Mohit Singhal on 2025-02-09T18:25:05.322Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/363

what problem is their in ques 2 and 3

---

### Post #364 by Arnav Raj  on 2025-02-09T18:25:08.080Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/364

yeah same for me. seems we were unlucky
![:frowning:](https://emoji.discourse-cdn.com/google/frowning.png?v=12)

---

### Post #365 by Raunak Dey on 2025-02-09T18:27:55.976Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/365

What can I refer to for proper steps to solve Question 10?

Thanks!

---

### Post #367 by Rohit Bhatia on 2025-02-09T18:30:30.946Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/367

Q10 is giving errors even after doing everything

---

### Post #368 by Jayaram on 2025-02-09T18:30:52.842Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/368

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23ds3000241/48/119137_2.png)
 23ds3000241:

o if it’s

getting values dont match for below now

{“2025-02-09”: “Partly cloudy and light winds”,

“2025-02-10”: “Sunny intervals and a gentle breeze”,

“2025-02-11”: “Light rain showers and a gentle breeze”,

“2025-02-12”: “Thundery showers and a gentle breeze”,

“2025-02-13”: “Thundery showers and a moderate breeze”,

“2025-02-14”: “Sunny intervals and a gentle breeze”,

“2025-02-15”: “Drizzle and a gentle breeze”,

“2025-02-16”: “Sunny and a gentle breeze”,

“2025-02-17”: “Sunny intervals and a gentle breeze”,

“2025-02-18”: “Sunny intervals and a gentle breeze”,

“2025-02-19”: “Light cloud and a gentle breeze”,

“2025-02-20”: “Sunny intervals and a moderate breeze”,

“2025-02-21”: “Light rain showers and a moderate breeze”,

“2025-02-22”: “Light cloud and a moderate breeze”}

---

### Post #369 by Jayaram on 2025-02-09T18:32:09.036Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/369

thanks for the help…

---

### Post #371 by Carlton D'Silva on 2025-02-10T05:09:13.069Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/371

[@23f3002537](/u/23f3002537)
,
[@21f3000745](/u/21f3000745)
,
[@Jeleshiya](/u/jeleshiya)

Anyone who received the Nur-Sultan parameter for this question and at least attempted it will get a mark.

Kind regards

---

### Post #372 by Arnav Raj  on 2025-02-10T12:19:48.767Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/372

sir what about bonus marks cuz my score was 9/10 due to q4(Nur-sultan).

---

### Post #373 by Carlton D'Silva on 2025-02-11T03:21:36.200Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/373

The bonus mark will be processed afterwards. That is checked before the scores are pushed to portal.

---

### Post #374 by vaishnavi on 2025-02-11T08:51:36.710Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/374

Nominatim API gives me the bounding box of the location. How exactly the bounding box helps me to find the details of the location?

---

### Post #375 by Rehbar khan on 2025-02-11T08:51:42.895Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/375

I am facing issues in Q9 , can you help me out?

---

### Post #376 by Lokessh Rana on 2025-02-11T08:51:45.993Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/376

const movies =
;

document.querySelectorAll(‘.sc-d5ea4b9d-0.ejavrk’).forEach((item, index) => {

if (index >= 25) return; // Stop after collecting 25 movies

const titleElement = item.querySelector('.ipc-title__text');
const yearElement = item.querySelector('.sc-d5ea4b9d-7.URyjV.dli-title-metadata-item');
const ratingElement = item.querySelector('.ipc-rating-star--rating');

if (titleElement && yearElement) {
    const idMatch = item.querySelector('a[href*="/title/tt"]')?.href.match(/tt(\d+)/);
    const id = idMatch ? `tt${idMatch[1]}` : null;
    const title = titleElement.innerText.trim();
    //const yearText = yearElement.innerText.replace(/\D/g, "").trim(); // Remove non-numeric characters
    const yearText = yearElement.innerText.trim();
    const year = yearText ? yearText : null; // Keep year as a string
    const rating = ratingElement ? ratingElement.innerText.trim() : null; // Keep rating as a string

    if (id && title && year && rating && parseFloat(rating) >= 3 && parseFloat(rating) <= 5) {
        movies.push({ id, title, year, rating });
    }
}

});

// Output JSON data with no spaces after colon

console.log(JSON.stringify(movies, (key, value) => typeof value === ‘string’ ? value.trim() : value, 0));

---

### Post #377 by HARISH. S on 2025-02-11T16:03:33.614Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/377

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/3/43e1fb12da806e25ca6f883d5d24726944c0fb38_2_690x292.png)

> **Image Description**: The image displays an online assignment or quiz interface with a dark theme. A red header indicates the activity "Ended at Sun, 9 Feb, 2025, 11:59 pm IST," showing a current "Score: 0" and "Check all" and "Save" buttons.

A green section offers "Bonus marks for posting on Discourse," stating that IITM BS students can earn 1 bonus mark on the graded assignment by replying with a relevant question or reply to the "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]" link.

Below this, the user's login is displayed as "23f3000975@ds.study.iitm.ac.in" with a "Logout" button.

The "Recent saves" section lists previous attempts and scores, with the most recent being the official score:
*   Saved on 9/2/2025, 8:04:05 pm, Score: 8
*   Saved on 9/2/2025, 8:03:25 pm, Score: 8
*   Saved on 9/2/2025, 4:03:58 pm, Score: 4
Each save entry includes a "Reload" button.
image1903×808 62.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/3/43e1fb12da806e25ca6f883d5d24726944c0fb38.png)

sir i have completed and saved the test but it shows score 0. and also

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/c/6c41591b6b3db0e9e48a14f4e11e3a21719ee2ce_2_690x307.png)

> **Image Description**: The image displays a learning management system interface. On the left, a navigation sidebar lists course content, including "Development Tools", "Module 2: Deployment Tools", "Module 3: Large Language Models", "Project 1", "Module 4: Data Sourcing", and "Module 5: Data Preparation". "Graded Assignment 4" is visible and highlighted with an alert icon, indicating it is an "Assignment".

The main content area shows details for "Graded Assignment 3". A red text warning indicates that "The due date for submitting this assignment has passed. Due on 2025-02-05, 23:59 IST." General submission instructions state, "You may submit any number of times before the due date. The final submission will be considered for grading." A list of common causes for difficulty accessing the assignment includes disabling ad blockers, enabling cookies and Javascript, using Chrome Browser, disabling browser extensions, and checking anti-virus software. A critical instruction notes, "You MUST use your Student Id (eg. 22f3xxxxxx@ds.study.iitm.ac.in) to do the Graded Assignment, otherwise your score will not be considered for evaluation." A link to "Graded Assignment 3" is provided: `https://exam.sanand.workers.dev/tds-2025-01-ga3`.
image1735×772 124 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/c/6c41591b6b3db0e9e48a14f4e11e3a21719ee2ce.png)

the graded assignment is showing like i didn’t submit it. please check on this.

---

### Post #378 by SADIYA MAHEEN SIDDIQUI on 2025-02-11T18:41:15.166Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/378

Your most recent score will be considered, as long as you saved it before the deadline

---

### Post #379 by Anand S on 2025-02-13T19:20:06.743Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/379

Here are the Discourse IDs that replied to this post.
[@carlton](/u/carlton)
 could you please add 1 mark to them in the GA (not the overall score)?

Please include only those are enrolled this term, obviously.

If they didn’t attempt GA4, please include them anyway and give them 1/10.

If they got 10/10 already, please add 1 mark anyway and give them 11/10.

21F1005510
21f2000296
21f2000588
21f2000709
21f2001369
21f3000745
21f3001379
21f3001797
21f3001993
21f3002277
22ds2000011
22ds3000157
22f1000120
22f1000535
22f2000008
22f2000113
22f2001590
22f2001640
22f3000079
22f3000519
22f3000586
22f3000639
22f3000657
22f3000804
22f3000910
22f3001011
22f3001315
22f3001754
22f3001840
22f3002034
22f3002175
22f3002184
22f3002723
22f3002771
23ds3000040
23ds3000149
23ds3000241
23f1000299
23f1000422
23f1000625
23f1001126
23f1001174
23f1001231
23f1001301
23f1001839
23f1002534
23f1002571
23f1003139
23f2000098
23f2000237
23f2000573
23f2000926
23f2001177
23f2001286
23f2001305
23f2001413
23f2001738
23f2002291
23f2003268
23f2003717
23f2003751
23f2003853
23f2004042
23f2004636
23f2004644
23f2004752
23f2004907
23f2004941
23f2005138
23f2005275
23f2005419
23f3001208
23f3001601
23f3001752
23f3002537
23F300327
23f3003594
23f3003871
23f3004024
23f3004114
23f3004162
24ds1000082_Vivek
24ds2000024
24ds2000108
24ds3000032
24ds3000090
24f2000695
24f2003130
Abhay222
ABHIJITH_VS
adeepu.here
Adityism
akashkunwar
anu2023
AnvithaV
AryanTikam
Atif01
carlton
daksh76
Deepanshutomar
GIRISH_VISHVESHVAR_B
gouthamnischay
H1Dd3n_xx
Haricharan
HARISH.S
iamsarthak
jashmevada
Jayeshbansal
Jeleshiya
JoelJeffrey
koustubhr
lakshaygarg654
Lokkiii
Megha
mohiit
Namannn28
namanshyamsukha
nayonika
Neelakandan
Nelson
nilaychugh
parthpatel
rabbaniIITB
Rehbar
Rohitb
rohitgarg
roy2003
Rrishit
Sagan
sandeepstele
Saransh_Saini
sarvan108
sha_512_av
ShahbaazSingh
sharma_abhay
ShivaniAdhiyaman
shivanshgupta0007
Siddhu3050
Suhani
swatikap
tanmaysahu295
tarundude02
Udipth
vaishnavi.k
Vedant22
vidushi
vidya19
yasharabhavi

---

### Post #381 by Nayonika Arora on 2025-02-18T13:13:08.478Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/381

Hello sir, my name is mentioned here however I did not get the bonus mark.

Warm regards,

Nayonika Arora

24ds1000090

---

### Post #382 by Rohit Garg on 2025-02-18T13:26:28.016Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/382

ig, they have not updated.

not reflected on my portal too

---

### Post #383 by Avinash Kumar on 2025-02-18T13:49:29.368Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/383

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/4/d4d9c422431c2ca2a06ac2ac397ddf40ca620253_2_690x320.png)

> **Image Description**: The image displays a discussion thread from a "GA4 - Data Sourcing" course, labeled "[TDS Jan 2025]". A user's post highlights a recurring error encountered while running code in Colab for "Nur-Sultan". The visible output is a Python `NameError` traceback. The initial error message states: "Error: Could not find location ID for Nur-Sultan". The traceback points to line 35, showing the code `weather_url = f'https://www.bbc.com/weather/{location_id}'`. The final error message is `NameError: name 'location_id' is not defined`. A left sidebar shows navigation options including "Topics," "My Posts," "Docs," and categories such as "Courses," "Operational Issues," and "Professionals Corner," along with tags like "clarification."
image1880×873 141 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/4/d4d9c422431c2ca2a06ac2ac397ddf40ca620253.png)

As you can see in this screen shot i already tried this question and getting error so i posted it on discourse. But still i did not get any marks for attempting this question.

i got only 9/10.

---

### Post #384 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-18T14:12:47.049Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/384

Hello
[@s.anand](/u/s.anand)

[@carlton](/u/carlton)
 Sir,

As can be seen, my roll number is present in this list (21f2000588) and in GA4 I have got 10/10 but unfortunately, that bonus mark hasn’t been added (as can be seen from the score displayed on the dashboard). So I request you to add that bonus mark to the total kindly.

Hoping for a positive response.

Thanks & Regards

Digvijaysinh Chudasama

21f2000588

---

### Post #385 by Jivraj Singh Shekhawat on 2025-02-18T15:43:57.703Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/385

[@22f2000008](/u/22f2000008)
 Your roll number is in the list shared by professor Anand.

---

### Post #386 by Jivraj Singh Shekhawat on 2025-02-18T15:44:03.726Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/386

---

### Post #387 by Avinash Kumar on 2025-02-18T16:50:40.193Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/387

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/e/5ebde997ebbaa1a9814e6e79b23821f118c198c2_2_690x312.png)

> **Image Description**: The image displays a dark-themed discussion forum titled "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]," which is categorized under "Tools in Data Science" and includes tags such as "announcement," "graded-assignment," and "week-4." A left sidebar lists categories like "Courses" and "Operational Issues" and a "clarification" tag. The main content area shows two posts in a discussion thread. The first post, from "rohitgarg," states, "ig. they have not updated. not reflected on my portal too." The second post, from "carlton" (identified as Course TA), addresses specific user IDs (@23f3002537, @21f3000745, @Jeleshiya) and communicates, "Anyone who received the Nur-Sultan parameter for this question and at least attempted it will get a mark." A vertical scrollbar on the right indicates "360 / 364" posts, with a timeline spanning from January 31 to February 18.
image1900×860 118 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/e/5ebde997ebbaa1a9814e6e79b23821f118c198c2.png)

I am not saying anything regarding bonus marks. I am asking GA4 q4  about

Nur-Sultan in this question everyone getting error after post in discourse ,sir say who attempt this question get a marks .But i am not recieved this question marks

---

### Post #388 by Sarthak Singh Gaur on 2025-02-18T23:42:37.819Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/388

if a student has 10/10 and his name is in the bonus list, how would that look like in the dashboard?

I don’t think it is added in my case.

---

### Post #389 by Carlton D'Silva on 2025-02-19T06:57:41.395Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/389

It will show up as 110  marks. Bonus marks are for all discourse posts on this thread that Anand has identified as valid. I have provided operations team with the update corrected scores. You will start seeing them in the dashboard soon.

Also these are the list of students that have been affected by Nur-Sultan in their questions. These will get an automatic mark for that question if they attempted it. Note that this is not a bonus mark. This is a free mark.

23f3002537@ds.study.iitm.ac.in

23f3003875@ds.study.iitm.ac.in

21f3002112@ds.study.iitm.ac.in

23f2003437@ds.study.iitm.ac.in

22f3002236@ds.study.iitm.ac.in

22f3001705@ds.study.iitm.ac.in

22f2000008@ds.study.iitm.ac.in

21f1001892@ds.study.iitm.ac.in

23f1002075@ds.study.iitm.ac.in

23f1001126@ds.study.iitm.ac.in

22f3002661@ds.study.iitm.ac.in

22f2000506@ds.study.iitm.ac.in

24f1002149@ds.study.iitm.ac.in

23f2002473@ds.study.iitm.ac.in

Kind regards

---

### Post #390 by Carlton D'Silva on 2025-02-19T06:58:58.390Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/390

Please refer to this reply.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/389)

[Tools in Data Science](/c/courses/tds-kb/34)

    It will show up as 110  marks. Bonus marks are for all discourse posts on this thread that Anand has identified as valid. I have provided operations team with the update corrected scores. You will start seeing them in the dashboard soon.
Also these are the list of students that have been affected by Nur-Sultan in their questions. These will get an automatic mark for that question if they attempted it. Note that this is not a bonus mark. This is a free mark.
23f3002537@ds.study.iitm.ac.in
23f3…

Kind regards

---

### Post #391 by Andrew David on 2025-02-19T08:10:42.117Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/391

For those who didn’t submit but still need to practice the questions like to check if the answer is right, or cross-check the solutions for GA 4 and GA 5, is there a special link where the portal just checks the answer and says right or wrong. I wasn’t able to do GA4 or even try to attempt GA 5 before deadline, but i would like to go through the process of submitting etc. is there any link or solutions for GA 4 and GA5.

---

### Post #392 by Andrew David on 2025-02-24T05:46:12.726Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/392

is there anyway to practice the assignments and check answers even though the deadline for the assignment passes? or is the answer given somewhere just for learning sake. I  understand that each set of students get different questions.
[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

[@s.anand](/u/s.anand)

---
