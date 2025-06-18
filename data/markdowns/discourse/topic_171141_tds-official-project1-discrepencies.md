---
title: "Tds-official-Project1-discrepencies"
topic_id: 171141
slug: "tds-official-project1-discrepencies"
original_url: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141
downloaded_at: "2025-06-18T17:01:34.600343"
---

### Post #1 by Jivraj Singh Shekhawat on 2025-03-28T18:34:41.099Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/1

Please post any discrepancies related to project1.

[@carlton](/u/carlton)

[](#p-612319-who-were-evaluated-how-did-we-decide-what-to-evaluate-1)
Who were evaluated? How did we decide what to evaluate?

All the image ids we evaluated were what
you
 submitted to us. This is the list of docker repos that was given to us by
[@s.anand](/u/s.anand)
 as the official list that met all the pre-requisites of Project 1. Therefore we will only evaluate those on this list who are eligible for evaluation with the repos
you
 gave us.

For clarity. Your docker repo gets a unique id every time it is changed. We will ONLY evaluate the image id which was present at the time of the docker repo being pulled. This acts as a time stamped frozen version of your repo. No other image id will be evaluated.

[](#p-612319-how-to-fix-bugs-in-our-scripts-2)
How to fix bugs in our scripts

Create Pull requests to
[Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1)
 .

[](#p-612319-docker-image-architecture-issue-report-3)
Docker Image Architecture Issue Report

If your Docker image was run on the wrong architecture, please fill out this form:

[Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)

[](#p-612319-bug-fixes-4)
Bug fixes

If you find bugs in our evaluation scripts, you might benefit from more marks because of the bug fix. So it is in your interest to look through our scripts and logs and identify bugs or anomalies. You might just go from 0 to heros.

Kind regards,

TDS Team

---

### Post #2 by Jivraj Singh Shekhawat on 2025-03-28T18:35:12.862Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/2

---

### Post #3 by ABHIJEET KUMAR  on 2025-03-28T19:03:42.095Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/3

What is the highest mark anyone has scored? Is it 22/20

[@Carlton](/u/carlton)
?

---

### Post #4 by Aarush saxena  on 2025-03-28T19:11:04.307Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/4

How come me and my group used same code but some got 10 some 11 some 12?

---

### Post #5 by Yogesh on 2025-03-28T19:11:39.267Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/5

[@carlton](/u/carlton)
 Please make clear what the average marks are, what highest marks are, and how the project will be evaulated.

We are very close to the end semester exam, and we are still not clear on assignment and project marks. It is a bit frustrating to plan in such circumstances.

---

### Post #6 by Carlton D'Silva on 2025-03-28T19:12:51.933Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/6

You have to see the logs for that. We have shared the logs. Everyone was graded by the exact same code, so there is no partiality. Your code did not produce consistent results.

---

### Post #7 by Dhruv on 2025-03-28T19:14:57.376Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/7

I have noticed that my image was run on a
x86_64
 architecture ( I can see my email in the logs shared ) whereas I built this docker image on my mac which is
ARM
. This is why I can see that my docker image never ran properly and threw the
exec format error
.

This was never mentioned on which architecture machine, our images will be evaluated. I request that my evaluation be done again on the right machine.

---

### Post #8 by Ritwika Dutta  on 2025-03-28T19:15:19.619Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/8

My evaluation log file is missing, although I followed all the steps to generate the docker image correctly, it’s showing the server didn’t start for 5 minutes but when I uploaded it, it was working fine. Please help me out sir, I worked hard on the project. I’ll get a zero, but I made the submissions correctly. Some other student also got the “server didn’t start in 5 minutes” but he has an evaluation log file. Please kindly help me out. My roll no. is 22f2001389

---

### Post #9 by Carlton D'Silva on 2025-03-28T19:16:38.027Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/9

We will check and rerun on arm if we ran it on the wrong emulation.

---

### Post #11 by Ritwika Dutta  on 2025-03-28T19:19:15.240Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/11

Any suggestions for my case sir ? I’m really tensed.

---

### Post #12 by Pradeep Mondal on 2025-03-28T19:20:38.723Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/12

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002933/48/118648_2.png)
 22f3002933:

I have noticed that my image was run on a
x86_64
 architecture ( I can see my email in the logs shared ) whereas I built this docker image on my mac which is
ARM
. This is why I can see that my docker image never ran properly and threw the
exec format error
.

This was never mentioned on which architecture machine, our images will be evaluated. I request that my evaluation be done again on the right machine.

[@carlton](/u/carlton)
  same issue, My image was also run on a
x86_64
 architecture. I too built on my mac which is
ARM
 (M1 Processor). I too can see that my docker image never ran properly and threw the
exec format error
  and
Evaluation log file
 is MISSING.

Actually my image was run on x86_64 architecture as it was present in that log file and because of the wrong architecture it never started.

I also request that my evaluation be done again on the right machine.

[![Screenshot 2025-03-29 at 12.51.59 AM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d_2_690x77.png)

> **Image Description**: The image shows information related to a Docker image.

The image is tagged as "latest". It was last pushed about a month ago by "pradeepmondal". The Docker pull command is: `docker pull pradeepmondal/final-tds-project-pradeep-mondal:latest`.

The Digest is `a4d9cad3b5f5`. The OS/ARCH is linux/arm64/v8. The last pull was 1 day ago. The compressed size is 179.2 MB.
Screenshot 2025-03-29 at 12.51.59 AM1613×182 19.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/b/0b6f4a9053f0f57c567c507af19f734eb316ca4d.png)

Even just now I tried running the exact image:

[![Screenshot 2025-03-29 at 12.53.35 AM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2_2_690x95.png)

> **Image Description**: The image shows the output of a `podman run` command. 

The command runs a container with the image `047fa151bf43`. The environment variable `AIPROXY_TOKEN` is set using the value of `$AIPROXY_TOKEN` and port 8000 is mapped from the host to the container.

The output shows that a server process started, the application completed startup, and Uvicorn is running on `http://0.0.0.0:8000`. It also indicates that CTRL+C can be used to quit.
Screenshot 2025-03-29 at 12.53.35 AM1220×169 25.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/a/4ab114b0db84001838ccde428fb3ece583a87cd2.png)

It is running fine on my macbook air m1 (ARM)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

---

### Post #13 by Anisha Seth on 2025-03-28T19:26:23.746Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/13

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f2001389/48/12849_2.png)
 22f2001389:

uploaded

Facing the same issue sir, kindly look into it. I had made sure all the files including the docker file were working perfectly fine. Please help me out.

Roll no. 23f1002056

---

### Post #14 by Pranav Kshirsagar on 2025-03-28T19:27:25.982Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/14

My evaluation log file is missing in report provided. It says tasksA was not found. but I have submitted tasksA in my project file. Also it says server didnt start for 5 mins but for me image was working fine. please kindly help me out. I have made submissions correctly. I request for re evaluation of my project. my roll no is 22f1000703

---

### Post #15 by SP on 2025-03-28T19:30:09.940Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/15

Respected,

I haven’t received any mail yet regarding the TDS Project 1 marks.

Please look into it.

Regards,

Soham

---

### Post #16 by AYUSH SINGH on 2025-03-28T19:37:05.650Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/16

My evaluation log file is missing.

The 2 other log files i’m given doesnt have my email inside it listed.

the Image id which is given in the MAIL is not present in my docker desktop, my project’s docker image is listed in docker desktop, which doesnot matches the image id given in the MAIL,

What was evaluated? How it was evaluated?

This is the id of the docker image that was evaluated: 0ade87d1bf07

My terminal shows 2 images as last, with respective image ids. I am not sure which one is the real, so please check with both the ids.

tds-project-1              latest    c854274f078d   5 weeks ago    1.38GB

ayush6871/fastapi-agent    latest    27e8375b0ab1   6 weeks ago    1.66GB

I am requesting to look into this case. I think there has been some mistake somewhere.

21f3001194

---

### Post #17 by Adithya S on 2025-03-28T19:42:12.154Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/17

I have also built the image on Mac and facing the same issue

exec format error

It is running fine on my Macbook Pro M1

[@carlton](/u/carlton)

[@Saransh_Saini](/u/saransh_saini)

[@Jivraj](/u/jivraj)

---

### Post #18 by Ritwika Dutta  on 2025-03-28T19:44:32.573Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/18

Sir I have noticed a technical glitch for the docker issue, wherein I mistakenly uploaded the wrong docker image link so kindly please kindly re evaluate it.

---

### Post #19 by Abhay Mehra on 2025-03-28T19:53:44.965Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/19

Sir I haven’t received any mail regarding this Project1 marks.
[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

---

### Post #20 by JAHAR KUMAR PAUL on 2025-03-28T19:54:41.344Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/20

[@carlton](/u/carlton)
 Sir , my Docker image is built on Macbook M1 which as you know uses ARM64 architecture . But evaluated with x86_64 which caused the exec format error due to cross platform compatibility issues . I am kindly requesting you to re-evaluate the project once again .

---

### Post #21 by Harsh Jaiswal on 2025-03-28T20:04:57.116Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/21

This is the id of the docker image that was evaluated: d0f14a872042  , but i had never provided this docker image then how it get evaluated, also none of the docker image created by me has this id.

Please, look over it.

Regards,

Harsh Jaiswal

23f1001995

---

### Post #22 by Arjun Dwarakesh Janarthanan on 2025-03-28T20:15:01.465Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/22

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

I wanted to kindly request if you could review the bonus additional tasks, as they were not reflected in the evaluation, despite being mentioned in the instructions. Apart from that I understand and accept my score overall, especially since I had hardcoded the folder paths in my prompt for some questions, which I believe led to those failures.

Bonus: Additional tasks
. We
may
 pass additional tasks beyond the list above. If your code handles them correctly, you get 1 bonus mark per task.

Regards,

---

### Post #24 by ABHIJEET KUMAR  on 2025-03-28T20:34:52.748Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/24

Would you mind reviewing the evaluation.log screenshot I have attached? I believe I may deserve marks for Task B6.
[@carlton](/u/carlton)
, could you kindly take a look?

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_690x276.png)

> **Image Description**: The image shows the output of a data scraping process in a "Tools in Data Science" context, likely a code execution result. The process attempts to save scraped data to a JSON file located at "./data/b6.json". The output indicates a failed test ("B6 FAILED"). The output includes an HTTP request, the expected content of the "/data/b6.json" file (a list of authors), and the actual result, which is a JSON object with a single key, ".author", associated with a list of authors. The expected list and the result list are similar but contain some differences in the order and content of the authors.
image1460×585 24.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345.png)

---

### Post #25 by Joseph Manoj Louis on 2025-03-28T20:53:25.507Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/25

I am also facing the same Please help my roll no is 21f3001750

---

### Post #26 by Debjeet Singha on 2025-03-28T20:59:57.711Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/26

can you please take a look at this screenshot?

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/b/fb3792e2a76ea8dd4cead0146f0366ceabc3dbb3_2_690x304.png)

> **Image Description**: The image shows a log output of a task involving image processing and data extraction. 

- The task involved passing an image `/data/card.jpg` containing a credit card to a Large Language Model (LLM) to extract the credit card number and save it as `/data/cc-number.txt` without spaces.
- A POST request was made to `http://localhost:8001/run` with a task description.
- A successful HTTP 200 response indicates the task completed.
- A subsequent GET request to `http://localhost:8001/read?path=/data/cc-number.txt` retrieves the extracted card number.
- The expected card number is `6011598665215965`.
- The actual result is `6011598656215965`.
- The output indicates a mismatch between the expected and actual card number, suggesting an error in the extraction or processing step.
- The overall task status is indicated as "A7 PASSED" despite the result mismatch.
image1451×640 64.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/b/fb3792e2a76ea8dd4cead0146f0366ceabc3dbb3.png)

The task was done but the LLM made a mistake. I think this type of mistake was outside our control.
[@carlton](/u/carlton)

---

### Post #27 by Arjun Dwarakesh Janarthanan on 2025-03-28T21:11:37.250Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/27

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Please correct me if I’m wrong, but I noticed that for tasks
B7
,
B8
, and
B10
, the evaluation log does not include any
POST
 or
GET
 request traces
, unlike the other tasks which have clearly recorded request flows, generated code, and outputs. In these three cases, the log shows only the failure message without any indication that the script was executed or that the output file was read.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_690x256.png)

> **Image Description**: Here's a description of the image for a Data Science student:

The image shows the output of a data science task, likely from a web scraping or data processing exercise. It includes HTTP requests and responses, code snippets, and error messages.

*   **HTTP Requests:** The image displays two HTTP requests:
    *   A POST request to a local server to scrape quotes from a website (`quotes.toscrape.com`). The request includes task parameters related to extracting author names.
    *   A GET request to read a JSON file (`/data/b6.json`) containing author names.
*   **HTTP Responses:** The image includes HTTP 200 OK responses indicating success. The responses include status messages, task descriptions, generated Python code (likely for web scraping using `requests`, `BeautifulSoup`, and `json`), and output (empty in this case).
*   **Task Status:** Task B6 (related to the scraped author data) is marked as "PASSED".
*   **Task B7:** This task involves downloading an image and resizing it. It is marked as "Failed".
*   **Error Messages:** The image contains error messages that states that Task B8 is `not all arguments converted during string formatting`.

In essence, the image captures a data workflow involving web scraping, data extraction, and image processing with error messages indicating failure in latter stages of the process.
image2003×745 95 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846.png)

---

### Post #28 by Md Ayan Arshad on 2025-03-28T21:30:36.014Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/28

Same issue with my. I have built my docker image in mac air m1 but i found that my image was run on a x86_64 architecture (I can see this in the logs shared for x86_server_start.log)

---

### Post #29 by Md anas alam on 2025-03-28T21:42:49.249Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/29

[@carlton](/u/carlton)
 sir i have same issue.

I have built my docker image in mac air m1 but i found that my image was run on a x86_64 architecture.

---

### Post #30 by S Smriti on 2025-03-28T21:53:34.701Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/30

Sir even my evaluation log file is missing and I really don’t know what to do because during submission 8/10 of my A tasks were working. Please look into it sir. This is really going to affect my grade and I remember how hard I tried just to get my A tasks running. Please sir

Role nom 23f2000599

[![1000472083](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/c/bc7199b82a901c91f7d040bb2328b9b116b55eac_2_225x500.jpeg)

> **Image Description**: Here's a concise description of the image for a Tools in Data Science student:

The image shows a message indicating issues with a Docker image evaluation. Key points:

*   Evaluation either didn't run or image was misconfigured.
*   Missing files lead to a score of 0.
*   Image must be responsive within 5 minutes.
*   Evaluation was on an 8-core Xeon Google Cloud unit with 1 Gigabit network.
*   Lists seven missing files:
    1.  Evaluation Log File (MISSING)
    2.  Docker Log File (drive.google.com link provided)
    3.  Server Start Log File (attachment)
    4.  Evaluation Script File (attachment)
    5.  Data Generation File (attachment)
    6.  Docker Orchestration File (attachment)
    7.  Solution Script (attachment ZIP)
*   Docker image ID evaluated: e1f186d9ce91
10004720831080×2400 255 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/c/bc7199b82a901c91f7d040bb2328b9b116b55eac.jpeg)

---

### Post #31 by Harsha on 2025-03-28T22:58:27.139Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/31

Hi
[@jivraj](/u/jivraj)
,

The contents of Expected and Result matches, but still test case’s failed.

Is there formatting check for answer , Isn’t prettier to be done ?

I see that your expected answer isn’t formatted using prettier , am i wrong ?

eg:

![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=14)
 EXPECTED:

[{‘first_name’: ‘Kevin’, ‘last_name’: ‘Allen’, ‘email’: ‘tonya41@example.com’}, {‘first_name’: ‘Kimberly’, ‘last_name’: ‘Allison’, ‘email’: ‘vmendoza@example.com’}, {‘first_name’: ‘Kathleen’, ‘last_name’: ‘Baldwin’, ‘email’: ‘amclean@example.com’}, {‘first_name’: ‘Jason’, ‘last_name’: ‘Banks’, ‘email’: ‘sharptara@example.org’}, {‘first_name’: ‘Tami’, ‘last_name’: ‘Bass’, ‘email’: ‘kristy61@example.com’}, {‘first_name’: ‘Brenda’, …

![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=14)
 RESULT:

[

{

“first_name”: “Kevin”,

“last_name”: “Allen”,

“email”: “
[tonya41@example.com](mailto:tonya41@example.com)
”

},

{

“first_name”: “Kimberly”,

“last_name”: “Allison”,

“email”: “
[vmendoza@example.com](mailto:vmendoza@example.com)
”

},

{

“first_name”: “Kathleen”,

“last_name”: “Baldwin”,

“email”: “
[amclean@example.com](mailto:amclean@example.com)
”

},

{

“first_name”: “Jason”,

“last_name”: “Banks”,

“email”: “
[sharptara@example.org](mailto:sharptara@example.org)
”

},

{

“first_name”: “Tami”,

“last_name”: “Bass”,

“email”: “
[kristy61@example.com](mailto:kristy61@example.com)
”

},

{

“first_name”: “Brenda”,

“last_name”: “Bradford”,

“email”: “
[amandakeith@example.com](mailto:amandakeith@example.com)
”

},…

---

### Post #32 by Jivraj Singh Shekhawat on 2025-03-29T01:10:47.753Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/32

---

### Post #33 by Jivraj Singh Shekhawat on 2025-03-29T01:13:24.998Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/33

Hi
@all

We will identify why arm images created a problem and were run using x86 platform.

We will also rerun evaluations for all the x86 and arm images one more time, before pushing to the dashboard.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f3003302/48/67422_2.png)
 23f3003302:

Hi
[@jivraj](/u/jivraj)
,

[@23f3003302](/u/23f3003302)
 output from your server’s response is correct, we will update our evaluation script.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2004912/48/108710_2.png)
 23f2004912:

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345_2_690x276.png)image1460×585 24.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/f/4f1dd8069b7f12f5d9d2005215621bc73be9a345.png)

[@23f2004912](/u/23f2004912)
 We will discuss internally if we can do something about it, but I can’t assure if you will get marks for it, since output from your server is a bit different.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001611/48/67277_2.png)
 23f1001611:

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846_2_690x256.png)image2003×745 95 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c16494f34e29ae68a356211e09a264d5ba3f5846.png)

image2003×745 95 KB

[@23f1001611](/u/23f1001611)
 we will look into it

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/harshjaiswal/48/69560_2.png)
 HarshJaiswal:

This is the id of the docker image that was evaluated: d0f14a872042 , but i had never provided this docker image then how it get evaluated, also none of the docker image created by me has this id.

[@HarshJaiswal](/u/harshjaiswal)
 I looked for your response for project1 docker image, and found out that we used correct image id. Here is repo information
harshjaiswal1/tds_project_final      latest    d0f14a872042   5 weeks ago    214MB

[@AYUSH_SINGH](/u/ayush_singh)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/ayush_singh/48/14039_2.png)
 AYUSH_SINGH:

ayush6871/fastapi-agent latest 27e8375b0ab1 6 weeks ago 1.66GB

This was submitted to us through google form, for project1.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/ayush_singh/48/14039_2.png)
 AYUSH_SINGH:

The 2 other log files i’m given doesnt have my email inside it listed.

We are aware about it results for 12 students are not generated, we will look into it, and see what caused those 12 images not to run.

[@22f1000703](/u/22f1000703)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f1000703/48/125463_2.png)
 22f1000703:

My evaluation log file is missing in report provided. It says tasksA was not found. but I have submitted tasksA in my project file. Also it says server didnt start for 5 mins but for me image was working fine. please kindly help me out. I have made submissions correctly.

It would have run at your end but it was supposed to run at anywhere, after dockerising it didn’t run, reason is taskA module was not found.

---

### Post #34 by Sahana S on 2025-03-29T02:30:50.629Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/34

Same issue for me sir. When I evaluated my file using evaluate.py my 9 cases out of the 10 in Task A was passed but the email I received shows that my evaluation log file is missing. I don’t understand why does it show like that. Please do check and help me out sir.

Reg no. 24f1002633

---

### Post #35 by Yogesh on 2025-03-29T02:37:27.452Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/35

I suspect there is something wrong with how the evaluation has been done. Although A1 task succeeded, all of my A tasks failed.

---

### Post #36 by Lovepreet Singh on 2025-03-29T02:45:35.166Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/36

I have checked my log file in all of the cases where a file is required it says file not found or directory not found error in the code, how can I check /data folder was provided to the program?

[@carlton](/u/carlton)

---

### Post #37 by Pritul Santosh Raut  on 2025-03-29T03:17:56.348Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/37

[@Jivraj](/u/jivraj)
 ,
[@carlton](/u/carlton)

It was a good project, and I have obtained the log files. Upon reviewing the log files, I realized that they are unable to read the files. I checked my project on GitHub and discovered that I forgot to uncomment the line that defines the path using the
os
 library. As a result, all file evaluations returned errors such as “can’t read the file.”

I understand that this oversight was my mistake. However, is there any way to reevaluate the code by simply uncommenting that line? I believe the rest of the code is properly written, but due to this single comment, all the files remained unchecked or resulted in errors.

[![Screenshot (177)](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad651e6c7b4c4df44a6b4c7ed935673b7576a076_2_690x388.png)

> **Image Description**: Here's a concise description of the image for a Tools in Data Science student:

The image shows a log file ("24f1002555@ds.study.iitm.ac.in_evaluation.log") likely generated during the execution of a data science task. The log contains HTTP requests and error messages, indicating issues with file access and processing. Some key observations:

*   **File Not Found Errors:**  Several errors of type "HTTP 500" with "detail": "500: [Errno 2] No such file or directory" are present. Specific missing files include `/app./data/mail.txt` and `/data/card.jpg`.
*   **404 Errors:** HTTP 404 "Not Found" errors are also present for requests to `/data/mail-sender.txt` and `/data/cc-number.txt`.
*   **Failed Tasks:** Multiple tasks (A7, A8) are marked as "FAILED" with associated "Cannot read" errors.
*   **Task Descriptions:** The log shows descriptions of data processing tasks, such as extracting credit card numbers from an image and finding similar comments using embeddings.
*   **API Requests:** There's an HTTP POST request to an OpenAI embeddings API endpoint (via "aiproxy.sanand.workers.dev") that returned a "200 OK", indicating a successful call.

In essence, the log highlights issues related to file input/output and API calls within a data science workflow. The log indicates issues reading files and problems with running the described tasks.
Screenshot (177)1920×1080 206 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/d/ad651e6c7b4c4df44a6b4c7ed935673b7576a076.png)

[![Screenshot (179)](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/7/078748473287587894e2c880e392cb511618d1f2_2_690x388.png)

> **Image Description**: Here's a concise description of the image for a Data Science Tools student:

**Content:** The image shows a Python code file ("app.py") in a GitHub repository named "LLM-based-Automation-Agent". The code uses the FastAPI framework to create an API with two endpoints: "/read" and "/run". The "/read" endpoint reads a file from the file system (after validation), and the "/run" endpoint executes a task (implementation not visible in this crop). 
The right sidebar shows a list of the functions and variables defined in the code, such as `ai_proxy_url`, `start`, `read_file`, `run_task`, `function_caller`.
Screenshot (179)1920×1080 199 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/7/078748473287587894e2c880e392cb511618d1f2.png)

---

### Post #38 by Naman S.  on 2025-03-29T03:18:32.508Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/38

Same here. I also dis not recieve any mail sir.

---

### Post #40 by Maulik Dang on 2025-03-29T04:34:28.653Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/40

I noticed that my Docker image was run on an x86_64 architecture (as indicated by my email in the shared logs), whereas I originally built it on my Mac (ARM architecture). Due to this mismatch, the image failed to run properly and resulted in an exec format error.

Since there was no prior mention of the architecture on which our images would be evaluated, I request that my evaluation be conducted again on the appropriate machine. Please help as after doing it correctly getting 0 marks because of such an error feels wrong

---

### Post #41 by Carlton D'Silva on 2025-03-29T04:39:03.187Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/41

[@23f2001975](/u/23f2001975)
 we had to rely on docker telling us whether an image was arm or x86. So thats why we just did what docker software told us. If it classified an image as arm then we ran it on arm. If it did not then we ran it on x86. Thats why we need students to look through the logs and identify issues so that we can make sure you get the correct evaluation.

If students notify us their image is actually arm based, then we will run it on arm. So dont worry, just inform us of any discrepancy as well as bugs. Our evaluation might not be perfect, there may be bugs. If students can precisely create bug reports then we can take that into consideration when evaluating students as well. The benefit being you might get extra marks because of the bug fix.

We have a script that looks at this discourse post each day and tells us who requires a fresh evaluation. So we will check your image on arm.

Kind regards

---

### Post #42 by Bhavin Biju on 2025-03-29T04:49:26.499Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/42

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/ea516be0e1c56eed1350af31ea0a2546b58528a6.png)

> **Image Description**: The image shows a Python traceback error. The error occurs in the file `/app/app.py` on line 30, in the module scope. The line attempts to assign the value of the environment variable `AIRPROXY_TOKEN` to a variable named `AIPROXY_TOKEN`. The traceback indicates a `KeyError`, specifically that the key `'AIRPROXY_TOKEN'` is not found in the environment variables (`os.environ`). This means the program is trying to access an environment variable that is not set.
image633×197 4.25 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/ea516be0e1c56eed1350af31ea0a2546b58528a6.png)

This is a screenshot of my docker log file. This works if you pass the actual value of the airproxy token at the command line while pulling the docker image. Please do look into this as I’ve put a lot of effort into this.

Thank you

Regards,

23f3002677

---

### Post #43 by Rohit Garg on 2025-03-29T04:49:39.987Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/43

@cartlon
 Same issue.

My image was also run on a
x86_64
 architecture. I too built on my mac which is
ARM
 (M1 Processor). I too can see that my docker image never ran properly and threw the
exec format error
 and
Evaluation log file
 is MISSING.

Can you please rerun the image on ARM based

---

### Post #44 by Carlton D'Silva on 2025-03-29T05:00:23.762Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/44

You have a misspelling in your environment variable, thats why it failed. We do pass the token to your docker exactly as specified in Project 1 page.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/9/59feb291f76643832a4b1b0f68037c2dee61deb1.png)

> **Image Description**: The image shows a Python traceback, indicating an error during program execution. Specifically, the error is a `KeyError: 'AIRPROXY_TOKEN'`. This error occurs in the file `/app/app.py` at line 30, where the program attempts to access the environment variable `AIRPROXY_TOKEN` using `os.environ['AIRPROXY_TOKEN']`. The `KeyError` signifies that the environment variable `AIRPROXY_TOKEN` is not set or does not exist in the system's environment. The error also occurs in the `<frozen os>` file, line 716, in the `__getitem__` method, which is used to access elements of a dictionary or other collection.
image633×197 5.21 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/9/59feb291f76643832a4b1b0f68037c2dee61deb1.png)

Kind regards

---

### Post #45 by Carlton D'Silva on 2025-03-29T05:03:26.390Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/45

You have to identify the exact bug for your claim to be considered. Thats why we have provided you with the scripts and the logs. You might get lots of marks. Its in your interest to identify the bug.

Kind regards

---

### Post #46 by S Smriti on 2025-03-29T05:06:09.078Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/46

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)
 what do I do sir am seriously clueless and heartbroken rn pls help atleast for A tasks we should get it

---

### Post #47 by Carlton D'Silva on 2025-03-29T05:08:12.916Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/47

We demoed in the live session the complete process of how to dockerise your project so that it can be run anywhere. Running on your local machine is not a sufficient criteria for passing the evaluation. It is absolutely vital for students to understand deployment. This is a critical skill for anyone who is serious about working in this field.

Also just check if yours is an arm based image or x86. Sometimes that makes a difference. For us there is no way to know other than docker software telling us. As it turns out several students had an arm based image but docker did not tell us that. So we will re run those.

If yours has been run on the wrong emulation then we will re run.

Kind regards

---

### Post #48 by Avnish Jajodia on 2025-03-29T05:08:33.580Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/48

[@carlton](/u/carlton)

I encountered an HTTP 500 error with the following detail:

{
"detail": "'choices'"
}

This issue appears across all tasks, even though they were running fine before submission. I suspect there might be a problem with APIPROXY_TOKEN. Could you please look into this?

Additionally, my solution is very similar to the one shared by the System Commands team in their email.

[![Screenshot 2025-03-29 103327](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/6/168fb0afeb8b965e92d70295ca00374c5179d6d9.png)

> **Image Description**: Here's a concise description of the image for a data science student:

The image shows a series of error messages related to a task involving installing 'uv' (likely a package manager) and running a script from a GitHub Gist, alongside formatting a file.

Specific issues:

*   Internal Server Errors (HTTP 500) are encountered during POST requests to `localhost:8180/run`, possibly during installation and formatting tasks.
*   GET requests to `localhost:8180/read?path=/data/format.md` result in "HTTP/1.1 404 Not Found" errors, indicating that the specified file is not found.
*   Errors A1 and A2 indicate that the system failed to read the `/data/format.md` file.
*   The formatting task utilizes `prettier@3.4.2` on the `/data/format.md` file.
Screenshot 2025-03-29 1033271511×749 29 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/6/168fb0afeb8b965e92d70295ca00374c5179d6d9.png)

---

### Post #49 by Carlton D'Silva on 2025-03-29T05:12:07.235Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/49

We have given you the evaluation scripts. Identify where exactly you believe the bug is.

Just guesses is not going to get you extra marks. You have to give us something specific.

Kind regards

---

### Post #50 by Ritwika Dutta  on 2025-03-29T05:18:39.537Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/50

[@Jivraj](/u/jivraj)
 sir please kindly look into it. Please re-evaluate my image, everything was working fine it is an issue with the docker image. Please re-evaluate it sir and please guide me as what to do

---

### Post #51 by Sakthivel S on 2025-03-29T05:24:12.600Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/51

I encountered the same issue with
evaluate.py
. However, since you previously advised against coding strictly with
evaluate.py
, I didn’t pursue it further. Now, I’m concerned—how is this a mistake?

[![Screenshot (56)](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/448bed1174becff2ecb28c56f9d75eb37e2d3689.png)

> **Image Description**: Here is a description of the image for a student in a Data Science course:

The image shows a text-based output from a log file ("/data/logs-latest.txt"). It presents an "EXPECTED" outcome and a "RESULT" section, likely comparing the two. The text content seems to be a series of sentences or phrases, rather than code or data tables. The "RESULT" section appears to duplicate the "EXPECTED" content. At the bottom, the image indicates that "A5 FAILED," suggesting a test or process didn't meet the expected outcome. There are no graphs or numerical data presented.
Screenshot (56)1492×362 22.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/448bed1174becff2ecb28c56f9d75eb37e2d3689.png)

---

### Post #52 by Yogesh on 2025-03-29T05:30:05.991Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/52

Please provide more time for this. Right now, we are also busy with the second project. There are other courses as well.

---

### Post #53 by Mayank Singh on 2025-03-29T05:46:07.918Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/53

yaa same issue i am also facing ,

and this LLM thing is very new for us , and we tried our best to complete. , but because of local machine issue , or anything , people end up getting 0 marks , or 4-5 marks , ..

As a lot of students are getting 0 , so please give some bonus , or some marking for there efforts ,

TDS dont have quiz , ,and getting 0 in project will decrease our CGPA too .

please think for it sir
[@carlton](/u/carlton)

---

### Post #54 by ROHIT B LAKSHMANAN on 2025-03-29T05:47:03.197Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/54

This is the id of the docker image that was evaluated: 468630ef32b8

I believe this is not my docker ID that was submitted, my docker ID is “bd2d0e570ec6”:

proof:

REPOSITORY                           TAG          DIGEST                                                                    IMAGE ID       CREATED        SIZE

rohit23f1001156/project1_tds         v3           sha256:bd2d0e570ec6b9a4a2b1565602a7c6abd118c4df06ca39e9dd78b0c06cab7542   bd2d0e570ec6   5 weeks ago    816MB

Please, look over it.

Also, in my docker log file, it is showing the error as:

[![Screenshot 2025-03-29 at 11.10.03 AM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94b76c5b49a749a2750e840d06fef2715c0b0b69_2_690x462.png)

> **Image Description**: The image shows a Python traceback from a server application. The error indicates a `FileNotFoundError`: the system cannot find the file `system_input.txt`. This error occurs within the `extract_specific_text_using_llm` function in the `app/function_tasks.py` file, specifically at line 290, where the code attempts to open the file. The traceback also shows calls to the `execute_function_call` and `run_task` functions in `app/main.py`. The server returns a 500 Internal Server Error.  The error occurs as part of a function call related to extracting specific text using a language model, where the input file is not found. There's also a "costError" indicating "crypto.createHash is not a function", suggesting a potential cryptographic issue earlier in the process.
Screenshot 2025-03-29 at 11.10.03 AM2360×1582 503 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/94b76c5b49a749a2750e840d06fef2715c0b0b69.png)

what is the reason for this?

It was running properly before, please help.

Regards,

Rohit

23f1001156

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

---

### Post #55 by Carlton D'Silva on 2025-03-29T05:51:25.513Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/55

[@ROHIT_B_LAKSHMANAN](/u/rohit_b_lakshmanan)

This is
exactly
 what
you
 submitted. We will ONLY consider this as valid.

2/16/2025 9:30:05	23f1001156@ds.study.iitm.ac.in
[GitHub - Rohit23f1001156/project1_tds](https://github.com/Rohit23f1001156/project1_tds)
	rohit23f1001156/project1_tds

---

### Post #56 by ROHIT B LAKSHMANAN on 2025-03-29T06:08:44.794Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/56

Yes, I agree.

So, did my docker ID change when I submitted?

I am sorry sir, but I did not make any changes after submitting the project, so I guess my Docker ID should remain the same as before, if I am not mistaken. I kindly request you to check just once more please, as I really don’t know where I have went wrong.

Jivraj Sir had checked liked this for another student, so I just wanted to confirm the same for me.

" I looked for your response for project1 docker image, and found out that we used correct image id. Here is repo information
harshjaiswal1/tds_project_final      latest    d0f14a872042   5 weeks ago    214MB
"

Also sir, could you please tell me why the error as shown in my previous message is being shown? and if there is no chance of it getting correct.

thanks

---

### Post #57 by Shashannk on 2025-03-29T06:23:39.304Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/57

Hi
[@carlton](/u/carlton)
 !

I am reaching out with deep frustration and concern regarding the evaluation of my project. I have worked tirelessly on this for almost two weeks, dedicating day and night to ensure that the tasks were executed correctly. During my own testing, I was able to get at least 7 out of 10 A tasks working as expected. However, after the evaluation, I was informed that none of the tasks were executed properly, which was quite shocking!

Given the effort and time I have put in, I kindly request you to review my project once more. I am more than willing to demonstrate the functionality in real time to clarify any issues or misunderstandings. Please let me know if there is a possibility to discuss this further, as I genuinely believe my work deserves another review.

---

### Post #58 by ABHIJEET KUMAR  on 2025-03-29T06:26:10.621Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/58

[@carlton](/u/carlton)
,

Jivraj said,
“We will discuss internally if we can do something about it.”
 I understand this well. The output from my server is slightly different, but it still achieves over 95% accuracy. Please do consider it.

---

### Post #59 by Jivraj Singh Shekhawat on 2025-03-29T06:27:03.386Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/59

Hi
[@Pritul_raut](/u/pritul_raut)

No, we won’t reevaluating it.

---

### Post #60 by Jivraj Singh Shekhawat on 2025-03-29T06:39:00.764Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/60

Hi
[@22f2001389](/u/22f2001389)

  File "/app/app.py", line 4, in <module>
    from tasksA import *
ModuleNotFoundError: No module named 'tasksA'

The error occurs because Python cannot find the
tasksA
 module. This is due to the file not existing, not being in the correct directory.

Kind regards

---

### Post #61 by Jivraj Singh Shekhawat on 2025-03-29T06:48:30.446Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/61

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/rohit_b_lakshmanan/48/67205_2.png)
 ROHIT_B_LAKSHMANAN:

This is the id of the docker image that was evaluated: 468630ef32b8

We evaluated you on correct file

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/7/d73b7915b1fb24bc215068e0695616f82f122f96.png)

> **Image Description**: Here's a description of the image:

The image shows terminal commands and their outputs related to Docker. 
- A `docker pull` command is executed to download an image named `rohit23f1001156/project1_tds` with tag `v3` for an ARM64 architecture.
- The output indicates the image was successfully pulled.
- A `docker images` command is piped to `grep` to filter for images with the name `rohit23f1001156/project1_tds`.
- The output shows the image `rohit23f1001156/project1_tds` with the tag `v3`, image ID `468630ef32b8`, was created 5 weeks ago, and has a size of 581MB.
image1757×250 24.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/7/d73b7915b1fb24bc215068e0695616f82f122f96.png)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/rohit_b_lakshmanan/48/67205_2.png)
 ROHIT_B_LAKSHMANAN:

what is the reason for this?

It was running properly before, please help.

Try running docker container after pulling, check if evaluate.py is able to do it’s job.

If you feel there is some issues from our side, we have provided with scirpts we used. You can create a pull request to
[Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1)

---

### Post #62 by Aditya Shankar Naidu on 2025-03-29T06:53:21.048Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/62

I’m facing “exec /usr/local/bin/uvicorn: exec format error” ,  My roll number is 21f3003062@ds.study.iitm.ac.in , My roll is in x86 list/log , not in ARM list/log. I have written and tested my code on ARM computer. I request to please check my code manually.
[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
 .

---

### Post #63 by Srijan Dutt on 2025-03-29T07:00:00.640Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/63

I cannot understand why the project marks are marked zero for me ? i have used the same code as usual but the results are not same ?

---

### Post #64 by Ritwika Dutta  on 2025-03-29T07:01:00.632Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/64

No no sir, I can send you an SS of my code, it’s very much there sir, the tasksA file, i really don’t know why this happened.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/2/227c1d29047c3e45a7c98d98421e983e014f666f_2_281x500.jpeg)

> **Image Description**: The image shows a Visual Studio Code (VS Code) window, likely displaying a Python project structure. On the left side, a file explorer panel shows a list of files and folders, including Python scripts (e.g., app.py, datagen.py, evaluate.py, tasksA.py), configuration files (.gitignore, .env, pyvenv.cfg, .dockerignore), executables (pip.exe, pip3.13.exe, pip3.exe, python.exe, pythonw.exe), and Docker-related files (docker-compose.deb..., docker-compose.yml, Dockerfile). The file "app.py" is currently selected. On the right side, there's a "PROBLEMS" section and a command prompt indicating a user directory (C:\Users\Ri). The status bar at the bottom displays "Python extension loading...".
image2160×3840 1.92 MB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/2/227c1d29047c3e45a7c98d98421e983e014f666f.jpeg)

---

### Post #65 by Rahul  on 2025-03-29T07:12:44.037Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/65

Same issue with me also

---

### Post #66 by Jivraj Singh Shekhawat on 2025-03-29T07:15:09.835Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/66

Yeah, it’s there on your local machine, but you didn’t copy it to docker container.

Below is content of your docker file which doesn’t copy tasksA.py file it only copies app.py. You could have figured this out by just running docker container on your local machine earlier, it would have shown you that error.

FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app

# Copy application files
COPY app.py /app

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]

---

### Post #67 by Mohd Atif on 2025-03-29T07:18:38.983Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/67

[@carlton](/u/carlton)
 good afternoon sir,

I completed my project 1 and submitted it as instructed. But the result show that evaluate file missing. I did everything right but don’t know how this as the result come. I also had evaluation file in my project too. Please go through things again as this is very unfair for those who took 2 weeks to do this project. My roll no. is 22f3001664. I hope I will get marks, of not full then should be 10/20.

Thank you sir

---

### Post #68 by Ritwika Dutta  on 2025-03-29T07:20:45.877Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/68

What to do now sir ? Is there no way to fix this now ? I can change the docker file and overwrite the docker image if you allow me to do so.

---

### Post #69 by Jivraj Singh Shekhawat on 2025-03-29T07:34:25.276Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/69

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/0/10a8acf6ce192b7da1304573e931a156dd91e89f.jpeg)

> **Image Description**: The image is a meme that features a stadium under construction with visible scaffolding. The text overlay reads: "WHEN YOU CANNOT REFACTOR THE CODE BECAUSE OF A TIGHT DEADLINE." The meme humorously relates messy construction to poorly written, unrefactored code due to time constraints. The image doesn't contain any actual code, graphs, or tables.
image474×474 41.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/0/10a8acf6ce192b7da1304573e931a156dd91e89f.jpeg)

---

### Post #70 by Jivraj Singh Shekhawat on 2025-03-29T07:42:52.795Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/70

Figure out the problem in our script and do a pull request to it, we will fix it if it’s a valid bug.

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png)
 Jivraj:

Create Pull requests to
[Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1)
 .

---

### Post #71 by Jivraj Singh Shekhawat on 2025-03-29T07:51:29.081Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/71

We looked at your script and there are errors in it. It doesn’t follow what we mentioned in live sessions.

Line number 81 of your app.py

subprocess.run(["uv", "run", script_name, "--root", "./data"] + args, check=True)

which creates a data directory inside app directory but evaluate.py expects data directory to be in root directory.

---

### Post #72 by Khushi Shah on 2025-03-29T07:56:48.878Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/72

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

I’m writing here to express my concerns regarding the evaluation of my TDS Project-1. Also, kindly pardon me for the long message.

I have received a MISSING statement in my evaluation log file in the project 1 score mail that was released yesterday.

These are the detailed point wise concerns :

I at the earlier stages, found the Tools in Data Science course relatively challenging as it’s just my second term in Diploma and I have only completed BDM and MLF Course till now. Hence, I decided to drop the course in February, however when I could still view the course on the portal, and raised concerns, the assistance provided to me was very grim and low, and after numerous follow-ups, I was finally informed 2½ weeks after dropping my course, that my drop application was received in draft and they would not proceed with it, and I had to continue my course.

By this time, I had already missed 2 graded assignment deadlines and the project 1 submission was due in the coming 2 days. Not losing my spirit and with whatever I could learn and implement I completed the TDS project 1. However, I accidentally attached the wrong docker image link, and I also raised the issue, but didn’t receive a reply.

I understand that it was a fault on my part, but evaluating a student as 0, even though all their functions are right, and they give the required answers, is also wrong since we are expected to provide correct answers, and learn to build the docker image, however, there can be occurrences where a student might make a small mistake like uploading the wrong link, and they must be given a small chance to reprimand them.

I also didn’t receive the mail from the TDS Team which they issued for students whose docker image or GitHub link was erroneous, and hence I realised after the deadline that I had uploaded the wrong docker image link.

I have rechecked all my function, and they are all correct, giving a 0 to a student, who worked hard within the limited available time(given the student had dropped the course but the course team didn’t process it) is very unfair.

Kindly provide me a way to either re-upload my project-1 Docker image link, or ask them to provide me marks on the basis of the functions and codes written, whichever is feasible, atleast to encourage the efforts and time put into the project with little knowledge.

I hope you would look into my plight, and take necessary measures.

Thanks and Regards

---

### Post #73 by ParamanandaSamantara on 2025-03-29T07:57:00.535Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/73

I haven’t received any mails regarding the tds project 1 please look into my concern

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@s.anand](/u/s.anand)

---

### Post #74 by Ritwika Dutta  on 2025-03-29T08:13:58.219Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/74

Sir please consider a re-evaluation for me, please :’)

---

### Post #75 by Hisham Kadambot on 2025-03-29T08:18:20.144Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/75

Please consider my situation a peer whos results were exactly same as mine has received 9, then how could I get 1 . 23f1002630 this is my role number please reconsider

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #76 by Jayesh Bansal on 2025-03-29T08:20:13.355Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/76

Few Students including me have not received any mails regarding TDS Project 1. We don’t even know what went wrong or why we didn’t received. Initially I thought that it can be due to some sending error and i will receive little late but even after 14hrs we have not received anything from the team. How are we supposed to check log and see our mistakes when we didn’t even received marks and logs. I request to check into it and provide us our marks and logs.

Thank You.

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@s.anand](/u/s.anand)

---

### Post #77 by Achuthan M on 2025-03-29T08:41:38.347Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/77

I had built the project well on my Mac OS machine. I am very disappointed with the scores. How do i make amends for revaluation as I feel the code ran well for all tasks on my machine. Please give written steps for revaluation.

---

### Post #78 by Raunak Narwal on 2025-03-29T08:42:03.850Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/78

Its saying that my evaluation log file is missing, i submitted everything properly. It also says no module named TasksA is found while i got 9/10 marks in the tasksA evaluation script. Kindly look into this, i worked really harrd for this project,
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #79 by Jivraj Singh Shekhawat on 2025-03-29T08:43:25.935Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/79

[@22f3000935](/u/22f3000935)

[Page Not Found | Docker Hub](https://hub.docker.com/r/pscoeds24/dataworks-agent)

you submitted this docker url through form response for project1, this repo doesn’t exists on docker.

---

### Post #80 by S Smriti on 2025-03-29T08:44:55.816Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/80

[@Jivraj](/u/jivraj)
 sir please tell me whats the issue am very confused and worried

---

### Post #81 by Jivraj Singh Shekhawat on 2025-03-29T08:45:12.085Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/81

We are aware about such mistakes and we are looking into it. We will reevaluate those images.

---

### Post #82 by Jivraj Singh Shekhawat on 2025-03-29T08:46:19.633Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/82

If evaluation file is missing for anyone, we will reevaluate it once more and send same through email.

Can you fill form for architecture detection.

---

### Post #84 by Aditya Shankar Naidu on 2025-03-29T08:47:47.413Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/84

Also please , kindly share evaluation log file after execution

---

### Post #85 by Raunak Narwal on 2025-03-29T08:48:29.711Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/85

I did upload all the necessary files but it stil says tasksA is missing, and i am getting zero marks. Kindly help out
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[![Screenshot 2025-03-29 141448](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/eff7ce6ffba0a1ad0a375cd1f2ea39eb613d333d_2_690x335.png)

> **Image Description**: The image is a screenshot of a file directory in a repository named "TDS_Project_1". It appears to be a software project. The directory contains files such as ".env", "Dockerfile", "app.py", "readme.md", "tasksA.py", and "tasksB.py". The last commit messages for most files is "Add files via upload". The last commit date is "last month" for all files. The user who last committed is "RaunakNarwal735", with the message "Update Dockerfile". There is an "Add file" button on the top right.
Screenshot 2025-03-29 1414481387×674 42.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/f/eff7ce6ffba0a1ad0a375cd1f2ea39eb613d333d.png)

---

### Post #86 by S Smriti on 2025-03-29T08:49:55.974Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/86

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/9/294b6ca3b2e386ec06fa6a9e356f2e2004eba2fc.png)

> **Image Description**: The image shows a snippet from a software repository, possibly Docker Hub or a similar platform. The key elements are:

*   **Tag:** The image is tagged as "latest," indicated by a green dot next to the tag name.
*   **Last Pushed:** The image was last updated about 1 month ago by user "23f2000599".
*   **Digest:** A cryptographic hash "5217284cc507" is shown, representing a unique identifier for the image content.
*   **OS/ARCH:** The image is built for the "linux/amd64" architecture, indicating that it is designed to run on Linux-based systems with the amd64 (x86-64) processor architecture.
image469×233 8.48 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/9/294b6ca3b2e386ec06fa6a9e356f2e2004eba2fc.png)

linux/amd64

which form should i fill sir?

---

### Post #87 by Jivraj Singh Shekhawat on 2025-03-29T08:51:52.117Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/87

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/aditya_naidu/48/12438_2.png)
 Aditya_Naidu:

21f3003062@ds.study.iitm.ac.in , My roll is in x86 list/log , not in ARM list/log. I have written and tested my code on ARM computer. I request to please check my code manually.
[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
 .

please fill the form for collecting architecture, so that we can rerun evals earlier we relied on docker api to tell us which architecture is being used, but it didn’t classify them correctly.

---

### Post #88 by Jivraj Singh Shekhawat on 2025-03-29T08:55:29.026Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/88

Hi
[@23f2000599](/u/23f2000599)
 check this out

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png)
 Jivraj:

Docker Image Architecture Issue Report

If your Docker image was run on the wrong architecture, please fill out this form:

[Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)

---

### Post #89 by S Smriti on 2025-03-29T08:57:30.720Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/89

mine is linux/amd64 sir it doesnt come under arm or x86 i think

---

### Post #90 by Jivraj Singh Shekhawat on 2025-03-29T09:00:06.623Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/90

Hi
[@23f2002400](/u/23f2002400)

Check your Dockerfile if it copies tasksA.py file to docker container.

If it does where does it copy, these are possible mistakes. You were expected to test docker images.

---

### Post #91 by Jivraj Singh Shekhawat on 2025-03-29T09:00:49.471Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/91

Hi
[@23f2000599](/u/23f2000599)

amd64 is x86

---

### Post #92 by S Smriti on 2025-03-29T09:01:55.378Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/92

Ok sir, will fill the form, thank you

---

### Post #93 by Achuthan M on 2025-03-29T09:02:52.068Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/93

One issue file is my app is listening on port 8000. But evaluations being done on 8219 port. so how it will succeed. Please guide what to do.

---

### Post #94 by Jivraj Singh Shekhawat on 2025-03-29T09:09:48.134Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/94

That’s external port mapping, we mapped your docker’s port 8000 to external 8219 port, so it won’t create issues.

Just look at docker_orchestration.py file for logic behind it, basically it was for evaluating multiple images parallely.

---

### Post #96 by ParamanandaSamantara on 2025-03-29T09:25:29.908Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/96

There is a mistake in the url I guess check this out I have a fully functional image which was pushed 1 month ago

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/256b97d98b6ef5ae6fab6edb3882f92c73f210da_2_690x382.png)

> **Image Description**: The image shows the "Image Management" interface for a Docker repository named "pscodes24/dataworks-agent". It displays a list of Docker images with details such as their digest, tags (including "latest"), media type (Image), OS/ARCH (linux/amd64), size, when they were last pushed, and when they were last pulled.  The repository's size is reported as 490.1 MB, and the images were last pushed about a month ago. Docker commands for pushing a new tag to this repository are also visible. There are two images listed, one tagged as "latest".
image1103×611 55.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/5/256b97d98b6ef5ae6fab6edb3882f92c73f210da.png)

Please check this out

url::
[https://hub.docker.com/repository/docker/pscodes24/dataworks-agent/general](https://hub.docker.com/repository/docker/pscodes24/dataworks-agent/general)

---

### Post #97 by Vivek Rekha Ashoka on 2025-03-29T09:35:51.071Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/97

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/0/7070e3c250af7985b5ca777719e26fb065ee2bb9.png)

> **Image Description**: The image shows a comparison of expected and actual results from processing a markdown file named `format.md`. The expected markdown output includes a header "# Header", a table with columns "Start", "Mid", and "End" containing values 1, 2, and 3, respectively, and a paragraph "Paragraph has extra spaces and trailing whitespace." along with a Python code block that prints an email address. The actual result displays a string representation of the processed markdown which includes the header, table elements, the trailing whitespace paragraph and a python code block. The final line indicates that test A2 failed.
image1340×431 9.45 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/0/7070e3c250af7985b5ca777719e26fb065ee2bb9.png)

This is the correct answer, eval script is not considering newlines properly.
[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

---

### Post #98 by Dipshikha Patel on 2025-03-29T09:52:52.362Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/98

same with me
![:smiling_face_with_tear:](https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=14)
 i dont understand how i got 0.

---

### Post #100 by Atharva Antapurkar on 2025-03-29T09:54:45.174Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/100

This is the id of the docker image that was evaluated: 2a8ffa96b140 , but i had never provided this docker image instead my image id is 735a5a477fb2 then how it get evaluated, also none of the docker image created by me has this id. My docker image was created on linux/amd64.

Please, look over it
[@carlton](/u/carlton)
 ,
[@Jivraj](/u/jivraj)
 .

Regards,

Atharva Antapurkar

23f1002558

---

### Post #101 by Aravind Ram on 2025-03-29T10:00:09.138Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/101

Sir, my evaluation log file is missing, even though I followed all the steps to generate the Docker image correctly. The system indicates that the server didn’t start within 5 minutes, but when I uploaded it, everything was working fine. I put in a lot of effort into this project, and I’m worried I might receive a zero despite making the submission correctly. Kindly help me resolve this issue. My roll number is 22F3004068.

Additionally, my Docker image ID was
d2f27c03b878
, but the ID mentioned in the email was
dfac8596cd4c
. Please provide clarity on this discrepancy.

I have also attached my Docker
[log file](https://drive.google.com/file/d/1exrdQOCjbrCFux2hC4OQH_BfgiijCzD1/view?usp=drivesdk)
 for reference

Docker
[image](https://hub.docker.com/repository/docker/docaravind21/tds-project-1/tags)

---

### Post #102 by Pritul Santosh Raut  on 2025-03-29T10:11:22.282Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/102

I realized that I made a mistake in my project by forgetting to uncomment a single line of code: os.path.join(os.getcwd(), “path_given”). I feel really bad about this oversight, especially after working so hard on the project and formatting everything carefully. It was an honest mistake, and I take full responsibility for it.

I sincerely request you to consider re-evaluating my work, as I believe it reflects the effort and dedication I put into it. I truly regret this error and will be more careful in the Project 2

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #103 by Sudharshini  on 2025-03-29T10:20:28.584Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/103

[![Screenshot (423)](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/b/8b35872a380e8ff279af497184852fd80401b602.png)

> **Image Description**: The image shows a Python traceback, indicating an error occurred while running a Uvicorn application. The traceback details the sequence of function calls leading to the error. Specifically, the error is a "KeyError: 'USER_EMAIL'", which arises because the application, specifically in the file `/app/main.py` at line 22, tries to access the environment variable "USER_EMAIL" using `os.environ`, but this environment variable is not set. The traceback also indicates that the application uses libraries like `click`, `asyncio`, and `importlib`.
Screenshot (423)1486×895 43.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/b/8b35872a380e8ff279af497184852fd80401b602.png)

Sir so the  user_email isn’t passed while pulling the docker image?

Thank you.

---

### Post #104 by VIVEK RATNAKAR (22f3002551) on 2025-03-29T10:20:29.023Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/104

Hi Team,

I have resolved the issues and pushed a new Docker image.

New Docker Image ID:

913320f92eb3

Tag:

latest

OS/ARCH:

linux/amd64

Please evaluate my updated submission.

Thanks!

---

### Post #105 by Lovepreet Singh on 2025-03-29T10:22:41.482Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/105

Hello,

My log file shows a “file not found” or “directory not found” error. Could you confirm whether
datagen.py
 was executed inside the Docker container or on the host OS? If it ran on the host, I don’t see any mounting process for the
/data
 folder into the container. Could you please clarify this?

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #106 by ROHIT B LAKSHMANAN on 2025-03-29T10:36:01.452Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/106

is it like this: FileNotFoundError: [Errno 2] No such file or directory: ‘system_input.txt’ ?

I am getting this error.

---

### Post #107 by Ritwika Dutta  on 2025-03-29T10:43:12.740Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/107

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
 sir, I have fixed my docker image issue that was causing the error. Please re-pull my docker image so that I can get score. Please consider me for re-evaluation. All the codes were correct, only issue was a glitch in the docker image.

---

### Post #108 by Santosh Sharma on 2025-03-29T11:15:28.607Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/108

Hello Sir, I am facing the same issue. Please look into it. Before submission, I ran my Docker file with the evaluation script to ensure it was working, and it worked fine. Kindly help me out. My roll number is 23F3004321.

---

### Post #109 by Lovepreet Singh on 2025-03-29T11:22:18.174Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/109

Yes, something like that, My log file shows when script tries to access file it says file not found or directory not found.

---

### Post #110 by Yashvardhan on 2025-03-29T11:48:22.794Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/110

Sir, I checked my evaluation log, and the error occurred because the
AI proxy token limit was exceeded
. I ran the evaluation script to verify, and I scored
12/20
.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/3/73d3123eb9274a1374ee2ee10f20e9a269c283f8.png)

> **Image Description**: The image shows a Python Flask application running in a development environment, indicated by the warning message. The application is accessible via `http://127.0.0.1:8000` and `http://172.17.0.8:8000`.

Several HTTP requests are made to the server, including POST requests to `/run` with different tasks encoded in the URL parameters, and GET requests to `/read?path=/data/format.md`. Some requests result in a 500 error (Internal Server Error) and others in a 404 error (Not Found).

The traceback shows an `AttributeError: 'NoneType' object has no attribute 'lower'`, which suggests that the `classification.get("action", "")` call is returning `None` when an action is not available, causing an error when `.lower()` is called.
image1456×765 41.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/3/73d3123eb9274a1374ee2ee10f20e9a269c283f8.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/941a71108a292d453f81c1bd42681cdc91acb222.png)

> **Image Description**: The image shows logs from a program, indicating errors and HTTP requests. The first error message is: `"error": "unable to open database file"`.  A subsequent HTTP GET request to `http://localhost:8000/read?path=/data/b10.csv` resulted in a "404 NOT FOUND" error. The log also indicates that reading `/data/b10.csv` failed, resulting in the label "B10 FAILED" and a score of 12/20.  A subsequent HTTP POST request to `https://aiproxy.sanand.workers.dev/openai/v1/embeddings` was successful, returning "200 OK".
image1094×256 9.59 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/941a71108a292d453f81c1bd42681cdc91acb222.png)

---

### Post #111 by Jiya Vemra on 2025-03-29T12:50:26.967Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/111

Sir, my project scored 1/20, with only B1 passed. However, when I ran the evaluation script, I got 6/10 in A tasks. Is there any way this can be checked, as the project works on deployed.

Kind Regards and thanks

---

### Post #112 by S Sharmile on 2025-03-29T12:57:02.183Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/112

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Sir,

This is the id of the docker image that was evaluated: 82aeb74ca739  ,

but i had never provided this docker image instead my image id is de8235663462

then how it get evaluated, also none of the docker image created by me has this id. My docker image was created on linux/amd64.

Please, look over it
[@carlton](/u/carlton)
 ,
[@Jivraj](/u/jivraj)
 .

Regards,

S Sharmile

23f3001688

---

### Post #113 by Sahana S on 2025-03-29T13:23:08.100Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/113

Sir the evaluated docker file ID was mentioned as  5b28fd5b25a7 in the mail sent by you but my docker file ID is 4d8c0cc34e35. I think my docker file is not evaluated properly. Kindly do check this and help me out. My reg no 24f1002633.

---

### Post #114 by Shivaditya Bhattacharya on 2025-03-29T13:24:44.800Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/114

[@carlton](/u/carlton)

My docker logs shows that
OSError: Cannot find resource
 error occurred when the data generation script tried to access font files in generation for a8.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/f/dfc4c289dcc2ddda315bd9f97a9ff21c166792af.png)

> **Image Description**: The image shows a Python traceback, indicating an error related to opening a font resource in the PIL (Pillow) library. The error "OSError: cannot open resource" occurs when the program attempts to load font files "arial.ttf" and "DejaVuSans.ttf". The traceback highlights the relevant lines in the "ImageFont.py" file within the PIL library and the user's code file "datagenmrt9km.py", where the font loading is attempted. The script is likely trying to generate images that require specific fonts. The image also shows an attempt to install and run a script from a GitHub Gist.
image1485×807 37.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/f/dfc4c289dcc2ddda315bd9f97a9ff21c166792af.png)

The datagen.py script looked for Arial font in the try block and when it encountered error it went to the except block to use DejaVuSans, the Pillow default, except it encountered the same error there, which was not handled. Thus, datagen.py stopped abruptly without creating files for A9 and A10 as well. So effectively, my A9 and A10 did not get evaluated properly as it did not have the required files due to error during data generation for A8. Can you please re-evaluate by enclosing each of the data generation function calls in their own try-except blocks?

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/681a3a02c951eaf7014d116d45b9ac35b8fdd2de.png)

> **Image Description**: The image shows a list of Python function names. The function names all start with "a" followed by a number (2 through 10) and an underscore. The rest of the function names suggest their functionality, such as "format_markdown," "dates," "contacts," "logs," "docs," "email," "credit_card_image," "comments," and "ticket_sales."
image302×252 3.45 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/8/681a3a02c951eaf7014d116d45b9ac35b8fdd2de.png)

I think it would be better to enclose each of these function calls in their own try-except blocks. This screenshot is taken from the datagen.py file sent in yesterday’s results mail.

So, will it be possible to re-evaluate my task A1, A8, A9 and A10? At least A9 and A10 did not even get the files to work on as they weren’t even created due to insufficient error handling in datagen.py .

Also, can you help me to identify the cause of even the Pillow default font not being available? I don’t understand how a font not being available could be caused by my code.

Thank you

---

### Post #115 by Vihaan Verma on 2025-03-29T13:35:11.651Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/115

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03b1e9282075d90736c4e6d9c652495660500acd.png)

> **Image Description**: The image shows a log output. 

*   It starts with a task to install `uv` (if required) and run a script from a GitHub gist. The script `datagen.py` is being executed with `23f3003196@ds.study.iitm.ac.in` as the only argument.
*   Following this is an HTTP Request made via POST to `http://localhost:8503/run` with a long query string that appears to encode the task information.
*   Finally, there are HTTP 500 Internal Server Error messages. The first is a general message. The second specifies an "Agent error" with a "429 Client Error: Too Many Requests" for the URL `https://aiproxy.sanand.workers.dev/openai/v1/chat/completions`. This indicates rate limiting issues when accessing an OpenAI completions API.
image1505×276 16.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03b1e9282075d90736c4e6d9c652495660500acd.png)

this is a 429 from sanand which is an error from your side. The evaluation already so delayed now has such issues because of which I am getting 1/20.
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #116 by Jayesh Bansal on 2025-03-29T13:52:10.940Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/116

does that mean our script is not evaluated?

---

### Post #117 by Jivraj Singh Shekhawat on 2025-03-29T14:27:26.029Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/117

Hi
[@Vihaanv07](/u/vihaanv07)

This was a good spot, we will rerun all the images where string
Agent Errro: 429 Client Error....
 is present.

Thanks and kind regards

---

### Post #118 by Jivraj Singh Shekhawat on 2025-03-29T14:28:42.845Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/118

Hi
[@Jayeshbansal](/u/jayeshbansal)

There were 12 emails for which we didn’t rerun, we will be fair with grading you and will take care of it.

---

### Post #119 by Mishkat Chougule on 2025-03-29T14:28:53.477Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/119

[![Screenshot 2025-03-29 at 7.53.20 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/99027ea63de1e32da4a8e843b59386029099553d.png)

> **Image Description**: The image shows the output of the `docker images` command in a terminal. It displays a table of Docker images on a system, listing their repository name, tag, image ID, creation date, and size. The table shows several images, including `tds-project1`, `mishkat02/automation-agent`, `franky1/tesseract`, `mish/myrepo`, `docker/welcome-to-docker`, `vimagick/tesseract`, `otiai10/tesseract`, and `ngrok/ngrok`. The sizes of the images vary from 12.2MB to 1.75GB, and the creation dates range from 5 weeks ago to 55 years ago.
Screenshot 2025-03-29 at 7.53.20 PM1440×900 13.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/99027ea63de1e32da4a8e843b59386029099553d.png)

My docker image id is different than the one I submitted

“This is the id of the docker image that was evaluated: 10f11a0e0cd6”

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@s.anand](/u/s.anand)
 plz check this

---

### Post #120 by Carlton D'Silva on 2025-03-29T15:08:04.421Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/120

Hi
[@23F300327](/u/23f300327)

This is what you submitted to us in the gform.

23f3003027@ds.study.iitm.ac.in	mishkat02/automation-agent:latest

We will only evaluate this image.

Kind regards

---

### Post #121 by Mishkat Chougule on 2025-03-29T15:11:48.786Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/121

[@carlton](/u/carlton)
 then why is the image id different?

in the docker hub as well as my local terminal the image id is 07b16dc68225

---

### Post #122 by Carlton D'Silva on 2025-03-29T15:20:02.379Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/122

When we build it after pulling it, it will get a unique identifier that makes sure we will only ever evaluate exactly that version. We pull it from your submission in the form.

In other words, if any changes occur to the docker repo, our id will no longer match a newer version of the file. This way we can make sure we are evaluating the right version every time. Your id does not have to match ours.

But we can detect changes made to the docker repo through our image id. I hope that is clear.

We will do some extra sanity checks before the 1/4/2025 just incase there are any issues. But thanks for asking the question.

Kind regards

---

### Post #123 by NK on 2025-03-29T16:06:00.271Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/123

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

My logs show,  ‘exec format error’ and it is due to architecture issue,  image was built on mac.

I have updated the google form regarding the architecture. Please rerun my image. Thanks

---

### Post #125 by Jivraj Singh Shekhawat on 2025-03-29T16:16:01.956Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/125

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png)
 Jivraj:

Docker Image Architecture Issue Report

If your Docker image was run on the wrong architecture, please fill out this form:

[Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)

Just fill the google form, we are rerunning such images.

---

### Post #126 by Santosh Sharma on 2025-03-30T05:06:28.932Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/126

Greetings, Sir,

I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between
pandas
 and
numpy
 caused the container to fail. To my surprise, the same versions (
pandas==2.0.3
 and
numpy==1.24.3
) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.

To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.

I’ve pushed the updated image to Docker Hub (
santoshsharma003/tds-project-one-1:latest
). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.

Thank you for your assistance!

---

### Post #127 by bharath on 2025-03-30T05:07:21.018Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/127

Hi
[@carlton](/u/carlton)
, I checked my Docker log file now and realised I missed to push a couple of files to the image. Is there anything I could do now? I have all the required files in my Git repo though. Please help.

---

### Post #128 by Daksh Agarwal on 2025-03-30T06:40:47.576Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/128

Sir in my logs it is showing that there’s cv2 module missing i mightve missed adding that in the requirements. Is there anything you could do to help me please?

---

### Post #129 by Roopika on 2025-03-30T10:15:36.886Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/129

I am also facing the same issue. I tried evaluating the scripts with the evaluation file also. Please rerun and let me know. My Roll No is 21F1002866.

---

### Post #130 by RAJ K BOOPATHI on 2025-03-30T10:31:12.160Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/130

Hi,

For Tasks A8, A9 & A10, I am not seeing any errors in my Docker execution logs. I am assuming the evaluation script failed to fetch the output file to verify the output for some reason. Can you please try rerunning these three tasks again? These tasks are working fine for me.

For Task B1. “Data outside /data is never accessed or exfiltrated, even if the task description asks for it.” - So when the evaluation asked to write something to /tmp/hello.txt it has correctly thrown an error saying access denied. I think this should be marked as correct. As the task description itself says so, the return is passed as 200 OK

ERROR:main:Error executing write_file: Access denied: /tmp/hello.txt
INFO:     172.17.0.1:60918 - "POST /run?task=Write+%27Hello+World%27+to+%60%2Ftmp%2Fhello.txt%60 HTTP/1.1" 200 OK

Similarly for task B2.

INFO:main:Checking file path: /data/format.md
ERROR:main:Error executing file_folder_deletion: Deletion not allowed: /data/format.md
INFO:     172.17.0.1:59446 - "POST /run?task=Delete+%2Fdata%2Fformat.md HTTP/1.1" 200 OK

For Task B4, if branch is not given we are assuming it as ‘main’ branch. Is it not correct? We would have at least expected the branch passed in the request.

For Task B8, I could not see the task description sent in the request in evaluation log file. Can you please check if the task request was passed properly?

Because I see only “=4 B8 failed: not all arguments converted during string formatting” for Task B8

---

### Post #131 by Jayaram on 2025-03-30T17:22:14.882Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/131

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

Thanks for your encouragement.. tried debugging the issue of image not starting up in the orchestrator script.. I found that the issue was happening because of the http and https proxies being set in docker build

ARG http_proxy=http://www-proxy-adcq7.us.<xxx>.com:80
 ARG https_proxy=http://www-proxy-adcq7.us.<xxx>.com:80

ENV http_proxy=${http_proxy}
 ENV https_proxy=${https_proxy}

This was required  as my office environment was behind the proxy and it was required for uv to download the dependencies on startup..

So this had caused the image to run in my office environment and not in orchestrator environment.. now removed the same and tested in a different vm altogether and noticed that the container  started up without issues..

Checkin url:
[Update Dockerfile removed hard coded proxies · rsjay1976/TDS-Project1-Jan25@a71e3a8 · GitHub](https://github.com/rsjay1976/TDS-Project1-Jan25/commit/a71e3a84b284d7621f2a769308340454ebd58583)

Have pushed the latet image (rsjay1976/tds-project1-jan25:latests) to docker hub as well..  didnt make any source changes or any other changes in the image.. Would be great if this is considered and image be considered for reevaluation… Appreciate your help

---

### Post #132 by Tasneem Shahnawaz on 2025-03-30T23:45:37.348Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/132

I am also with the same situation sir. Please help with this issue. I have submitted everything correctly and it was working fine. Thanks

---

### Post #133 by Naman S.  on 2025-03-31T06:38:27.518Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/133

Hello Sir,

Greetings,

I have not recieved amy mail regarding my Project 1 Marks, can you please look into it.

Thank you/

---

### Post #134 by Daksh Agarwal on 2025-03-31T06:41:26.100Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/134

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
 please sir could you help me with this issue previously when i ran on my system it was working perfectly fine

---

### Post #135 by K Senthur Kumaran  on 2025-03-31T09:29:51.137Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/135

Hello sir

I noticed that the log mentioned:

“python: can’t open file ‘/app/app/main.py’: [Errno 2] No such file or directory.”

However, my main file was named run.py, which might have caused the issue. Since the code was present, I was given a 0. Would it be possible to run it again or consider partial marks for the submission?

Thank you for your time and consideration. I appreciate your help!

---

### Post #136 by Varad Rajadhyax  on 2025-03-31T10:29:34.265Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/136

Even my file saying the same. I got the ‘No module named tasksA’ error whereas at the time of submission it was working perfectly fine. Please kindly look into this issues sir.

Thank you.

---

### Post #137 by Sahil Sharma on 2025-03-31T11:06:22.363Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/137

no taskA.py even though i ran the evalution getting 12 score still no evalution.log

help the students please give them second chance

---

### Post #138 by Jayaram on 2025-03-31T11:31:30.396Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/138

on a side note, to validate and test our docker/podman images on a platform outside of our dev environment we can use
[https://labs.play-with-docker.com/](https://labs.play-with-docker.com/)
.. this is a free platform to download run and test docker images …

---

### Post #139 by Shiva Ramakrishna on 2025-03-31T12:59:59.522Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/139

Hi
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

I might have found a bug in my code, I have hardcoded my file directory into my code but I didn’t change it later. I have created a safe_open function that will throw a HTTP_403_FORBIDDEN error when tried to access files outside that directory. Because of this all the tasks failed. There also might be environment and configuration issues in my Dockerfile. When I tested locally, it worked fine but because of this small mistake I am now only getting 1/20. Is it possible to change/modify my code?

Thanks for considering, any help would be appreciated. Worked very hard for this

---

### Post #140 by Garima on 2025-03-31T17:03:28.971Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/140

The docker id of the image that was evaluated (as specified the mail 1ae3f64427f0) is not correct, the correct id is 51168f246618.

Name of Docker image -

garriimaa/llm_automation:latest

Please evaluate with the above image name.

GitHub repository for reference -
[GitHub - Garima1603/llm_automation](https://github.com/Garima1603/llm_automation)

---

### Post #141 by Ritwika Dutta  on 2025-03-31T20:07:47.011Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/141

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
 sir I fixed my issue with docker during the given window for discrepancy and requested a re-pulling of the image but still got a mail of score 0. Please sir, I request you to do a re-evaluation, the docker issue is fixed long back by me. It’s an earnest request sir.

---

### Post #142 by Afsal on 2025-03-31T20:16:46.949Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/142

Dear sir,
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

I got result as fail for the project 1 and the reasons listed are as in the screenshot. But as you can see in the second screenshot, i still have that repository which is public, have license file and docker file in it, created 2 months back. I actually don’t know how this issues come in, please resolve this.

[![1](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/c/2c922cdf1470207949392f3402b7cea1989e2397_2_690x294.jpeg)

> **Image Description**: The image shows the prerequisite checks and evaluation results for a project in the Tools in Data Science course. The prerequisites include having a publicly accessible GitHub repository with a LICENSE file (MIT license) and a valid Dockerfile. The Docker image must be publicly accessible and run via podman, using the same Dockerfile as in the GitHub repository.

The evaluation results show that the Docker image is present in dockerhub and public (PASS), but the GitHub repository is either not present or not public (FAIL). The Dockerfile and MIT license are not present in the root of the GitHub repository (FAIL). As a result, the overall prerequisites are marked as FAIL, and the project score is 0.
1885×378 56.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/c/2c922cdf1470207949392f3402b7cea1989e2397.jpeg)

[![2](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/8/c8edbd63c9ebf7c97ccc221d7c91fa9ee4c8554c_2_690x439.jpeg)

> **Image Description**: The image shows a GitHub repository named "tds_proj1" with a public visibility. The repository has one branch called "main", and it contains several files including Python scripts (app.py, datagen.py, evaluate.py, tasksA.py), a Dockerfile, a LICENSE file, a requirements.txt file, and directories named '_pycache_', 'data', and 'env'. Recent updates to most files happened 2 months ago. The repository has 10 commits.
2908×579 59.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/8/c8edbd63c9ebf7c97ccc221d7c91fa9ee4c8554c.jpeg)

---

### Post #143 by Sirimilla Karthik Balaji on 2025-03-31T20:29:32.826Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/143

[@carlton](/u/carlton)

I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:

“Is Dockerfile present in root of GitHub repo?”

Despite this, my dockerfile is present in the root directory of my repository.

Github repo link:
[GitHub - karthiksirimilla/tds_project1_final](https://github.com/karthiksirimilla/tds_project1_final)

My evaluation.log , contains the score 6/20

Roll no : 23f1002398

Mailid: 23f1002398@ds.study.iitm.ac.in

My evaluation.log

[![IMG_6418](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/b/db1247df1beef8d4878a7ab13e5ad4eb7e626868_2_246x500.jpeg)

> **Image Description**: The image shows a log output containing error messages related to a data processing task. 

*   **Errors:** There are multiple "failed" messages for reading data from `/data/b9.html` and `/data/b10.csv`. There is also an HTTP 400 error ("Bad Request") and a connection refusal error.
*   **Task Description:** A datasette server is run on port 8001 in the background. It aims to count the rows where the "type" column is "Bronze" in the `ticket-sales.csv` dataset.
*   **Database Query:** The SQL query used is `SELECT COUNT(*) FROM tickets WHERE type='Bronze'`.
*   **HTTP Requests:** The log shows HTTP GET and POST requests to local URLs (e.g., `http://localhost:8309/read?path=/data/b9.html`) and an external URL (`https://aiproxy.sanand.workers.dev/openai/v1/embeddings`). One request to the external URL shows a successful HTTP 200 OK response.
*   **Score:** The score is 6/20.
IMG_64181290×2619 566 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/b/db1247df1beef8d4878a7ab13e5ad4eb7e626868.jpeg)

---

### Post #144 by Sirimilla Karthik Balaji on 2025-03-31T20:32:07.504Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/144

[![IMG_6417](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_230x500.png)

> **Image Description**: Here's a concise description of the image for a student in the Tools in Data Science course:

The image is a screenshot of an email regarding Project 1 prerequisite evaluations. The email outlines the following requirements:

1.  GitHub repository exists and is publicly accessible.
2.  GitHub repository has a LICENSE file with the MIT license.
3.  GitHub repository has a valid Dockerfile.
4.  Docker image is publicly accessible and runs via `podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME`.
5.  Docker image uses the same Dockerfile as in the GitHub repository.

The email then shows the evaluation results:

*   Docker image in Docker Hub and public: PASS
*   GitHub repo present and public: PASS
*   Dockerfile present in root of GitHub repo: FAIL
*   MIT license present at root of GitHub repo: PASS

The final result is that the Prerequisites are FAIL, and the Project 1 Score is 0.
IMG_64171290×2796 305 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56.png)

---

### Post #145 by Abhinav on 2025-03-31T20:33:36.179Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/145

[@carlton](/u/carlton)
  Sir, the image id written in my notification email is wrong. The correct image is this:
[https://hub.docker.com/repository/docker/24f1002064/project1/general](https://hub.docker.com/repository/docker/24f1002064/project1/general)

can you please double check this? You can also verify that I have made no changes to it since the due date.

---

### Post #146 by Sirimilla Karthik Balaji on 2025-03-31T20:20:12.508Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/146

[@carlton](/u/carlton)

I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:

“Is Dockerfile present in root of GitHub repo?”

Despite this, my dockerfile is present in the root directory of my repository.

Github repo link:
[GitHub - karthiksirimilla/tds_project1_final](https://github.com/karthiksirimilla/tds_project1_final)

My evaluation.log , contains the score 6/20

Roll no : 23f1002398

Mailid: 23f1002398@ds.study.iitm.ac.in

[![IMG_6417](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56_2_230x500.png)IMG_64171290×2796 305 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0a7b429e7053632f4184b89d4948de42cd6c7f56.png)

---

### Post #147 by Carlton D'Silva on 2025-03-31T20:39:43.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/147

Your dockerfile is misspelt.

---

### Post #148 by Sirimilla Karthik Balaji on 2025-03-31T21:01:01.155Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/148

Thanks for your quick response sir. I just wanted to clarify that my dockerfile was recognized by Docker, and my image was successfully built, so it seems that Docker itself didn’t have an issue with the filename.

However, I understand that the evaluation script might be case-sensitive and specifically looking for “Dockerfile” with an uppercase “D”. If that’s the issue, should I rename and push the file again to the repo sir.

Please let me know if that’s the right fix or if I need to do anything else sir.

---

### Post #149 by Carlton D'Silva on 2025-03-31T21:01:54.794Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/149

The image id varies depending on the system it was built on. When we build it on our Xeon cloud compute it will get a different image id from yours (unless you have a Xeon system). What is common is the dcoker hub image name and tag we used. We used the one you submitted on your form.

But the image id serves the same purpose. If you alter the dockerhub image, our image will no longer match the one from dockerhub. the image id sha will change. So do not worry about whether your sha matches our sha. It just acts as a way for us to make sure that we are consistently looking at the same image.

Kind regards

---

### Post #150 by SP on 2025-03-31T21:05:40.325Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/150

I recently received an email stating that my Docker image is not publicly available, resulting in a failed prerequisite check for the TDS Project 1. However, I have ensured that my Docker image is publicly accessible. Please help.

[@carlton](/u/carlton)

My Docker image ID is "
99d08f2002fa
 ", and it is set to public. I kindly request you to review this issue, as I have worked very hard on this project and would appreciate the opportunity for a fair evaluation.

---

### Post #151 by Abhinav on 2025-03-31T21:15:37.954Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/151

can you share the sha?

---

### Post #152 by LAKSHAY on 2025-03-31T21:34:08.281Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/152

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

There might be some glitches in the system. Could you kindly verify the process again?

[![1000430602](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/0/80c8cd52c9f19a6d4047702b56fa98cbcf59b266_2_223x500.jpeg)

> **Image Description**: Here's a description of the image:

The image is a screenshot of an email about prerequisites for Project 1 in a course (likely Tools in Data Science or similar based on the mention of data science tools).

The email outlines the following requirements:

1.  GitHub repository exists and is publicly accessible.
2.  GitHub repository has a LICENSE file with the MIT license.
3.  GitHub repository has a valid Dockerfile.
4.  Docker image is publicly accessible and runs via `podman`.
5.  The Docker image uses the same Dockerfile as in the GitHub repository.

The email then provides an evaluation of these prerequisites for the recipient:

*   Docker image present and public: PASS
*   GitHub repository present and public: FAIL
*   Dockerfile present in root of GitHub repo: FAIL
*   MIT license present at root of GitHub repo: FAIL

The email concludes that the prerequisites have FAILED, resulting in a Project 1 score of 0.
10004306021080×2412 160 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/0/80c8cd52c9f19a6d4047702b56fa98cbcf59b266.jpeg)

I’ve already received my score in the evaluation log. Additionally, the Docker Hub run logs show no errors, and both the GitHub repo and Docker image are publicly accessible. All the content has been verified and meets the prerequisites.

Let me know if any further action is needed from my end.

---

### Post #153 by Ritwika Dutta  on 2025-04-01T03:18:01.579Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/153

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
 please kindly re-pull my docker image and re-evaluate my project sir. I fixed the issue long back. Please reply kindly. My roll no is : 22f2001389. I have been trying to get to you for long now. Please kindly help me out. Please reply.

---

### Post #155 by Vansh Mittal on 2025-04-01T03:43:51.523Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/155

[@carlton](/u/carlton)

I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:

“Is Dockerfile present in root of GitHub repo?”

Despite this, my dockerfile is present in the root directory of my repository.

Github repo link:
[GitHub - Vansh-22f300/project_tds](https://github.com/Vansh-22f300/project_tds.git)

My evaluation.log , contains the score .

Roll no : 22f3001851

Mail id:22f3001851@ds.study.iitm.ac.in

[![Screenshot_2025-04-01-09-11-54-385_com.android.chrome](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/4/d4df01a394ced7de96bc204dd764e71d18c62389_2_225x500.jpeg)

> **Image Description**: The image shows a GitHub repository with the following information:

*   **License:** MIT License
*   **Stats:** 0 stars, 0 forks, 1 watching, 1 branch, 0 tags
*   **Repository Status:** Public
*   **Branch:** main
*   **Owner:** Vansh-22f300, last updated 2 months ago.
*   **Files/Directories:**
    *   `__pycache__` (directory)
    *   `.env`
    *   `.gitignore`
    *   `LICENSE`
    *   `README.md`
    *   `app.py`
    *   `datagen.py`
    *   `dockerfile`
    *   `evaluate.py`
    *   `requirements.txt`
    *   `tasksA.py`
    *   `tasksB.py`
Screenshot_2025-04-01-09-11-54-385_com.android.chrome1080×2400 171 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/4/d4df01a394ced7de96bc204dd764e71d18c62389.jpeg)

---

### Post #156 by Vaddi Yaswanth on 2025-04-01T04:00:56.662Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/156

dockerfile is spelling mistake it should be Dockerfile same thing happened to me .

---

### Post #157 by Aarush saxena  on 2025-04-01T04:18:39.805Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/157

[@carlton](/u/carlton)

Pls look into this evaluation.py contains two result

Can u confirm that u guys will use 10/20 one ?

[![Screenshot_2025-04-01-08-51-03-781_com.google.android.apps.docs](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/0/c0842e4115f2f72cc643b6b066c8c503b592c608_2_230x500.jpeg)

> **Image Description**: Here's a concise description of the image for a Tools in Data Science student:

The image shows a terminal output related to a data science task. It includes instructions for:

1.  **Counting rows with SQL** using 'curl' to request data from a local Datasette server. The curl command constructs a SQL query.
2.  **Stopping the Datasette server** using 'kill' command.

The terminal output indicates an error, "B10 failed: Cannot read /data/b10.csv", suggesting that the command to read the CSV file was unsuccessful.

The image also mentions the need to ensure that 'uvx' and 'datasette' are installed and configured, and that the '/data' directory is writable.

Finally, it shows some HTTP requests, one returning "404 Not Found", and another with a "200 OK" status code. The student's score on the task is 10/20.
Screenshot_2025-04-01-08-51-03-781_com.google.android.apps.docs1080×2340 253 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/0/c0842e4115f2f72cc643b6b066c8c503b592c608.jpeg)

[![Screenshot_2025-04-01-08-51-01-349_com.google.android.apps.docs](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/7/f7ff60d992c45e083570f274407f2914b3f3f4c3_2_230x500.jpeg)

> **Image Description**: Here's a concise description of the image for a student in the Tools in Data Science course:

The image shows a series of error messages and HTTP requests related to a data science task.  Specifically:

*   An attempt to run a datasette server via an HTTP POST request to localhost on port 8462. This appears to involve a query counting "Bronze" tickets and saving the result to /data/b10.csv.  This request results in an "HTTP/1.1 500 Internal Server Error" with detail "choices."
*   An HTTP GET request to read the file /data/b10.csv from the localhost server, resulting in an "HTTP/1.1 404 Not Found" error, indicated by the message "B10 failed: Cannot read /data/b10.csv".
*   An HTTP POST request to an OpenAI API for embeddings, resulting in an "HTTP/1.1 429 Too Many Requests" error.
*   A task to install 'uv' and run the script datagen.py from a GitHub Gist, presumably using a student email as an argument.
*   The current score is 1/20.
Screenshot_2025-04-01-08-51-01-349_com.google.android.apps.docs1080×2340 219 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/7/f7ff60d992c45e083570f274407f2914b3f3f4c3.jpeg)

---

### Post #158 by Yashvardhan on 2025-04-01T04:23:55.817Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/158

HELLO SIR , DOCKET IMAGE PRESENT IN DOCKER HUB  AND IT IS PUBLIC THEN WHY IT IS FAIL

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/749d670a5762fa641b21182e8967d86071f7b99e.png)

> **Image Description**: The image displays the prerequisite evaluation results for Project 1. It shows that the Github repo, Dockerfile, and MIT license all passed the check. However, the Docker image is not present in Dockerhub and is public, which resulted in a "FAIL". As a consequence, the overall Prerequisites status is "FAIL," and the Project 1 Score is 0.
image619×241 5.07 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/749d670a5762fa641b21182e8967d86071f7b99e.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/e/de8f280fe809b7770d0e86b62b74b614ed50e17a_2_690x451.png)

> **Image Description**: Here's a concise and factual description of the image:

**Content:** This image depicts a repository overview, likely from a Docker image registry or a similar platform.

**Key Details:**

*   **Repository Name:** 23f2004644/data\_automation\_agent
*   **Last Push:**  About 1 month ago
*   **Repository Size:** 757 MB
*   **Tabs:** General, Tags, Image Management (BETA), Collaborators, Webhooks, Settings. The "Tags" tab is currently selected.
*   **Tags Section:**
    *   The repository contains 1 tag.
    *   It lists the "latest" tag.
    *   **OS:** Linux.
    *   **Type:** Image
    *   **Pulled:** 5 days ago
    *   **Pushed:** About 1 month ago
image919×602 28.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/e/de8f280fe809b7770d0e86b62b74b614ed50e17a.png)

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/efd0ca8b5a79aca303f8ae07d632c1a62c07bb1f_2_690x37.png)

> **Image Description**: The image displays information about an image file named "23f2004644/data_automation_agent". The file was created "about 1 month ago" and is marked as "IMAGE" type with "Public" visibility and "Inactive" status.

[@carlton](/u/carlton)

---

### Post #159 by Mayank Singh on 2025-04-01T05:36:06.406Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/159

same issue i am also facing ,

[@carlton](/u/carlton)

---

### Post #161 by Santosh Sharma on 2025-04-01T05:49:15.993Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/161

Respected Sir,

I have received a
FAIL
 status for the prerequisite check:

“Is Docker image present in Docker Hub AND is public.”

However, as shown in my Docker Hub repository, my Docker images are publicly accessible.

I have attached a screenshot for the reference.

Thank you for your time and support.

[![Screenshot From 2025-04-01 11-17-44](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c33d5a5cb98598131cd2f106e811773a37d4e830_2_690x110.png)

> **Image Description**: Here is a summary of the image for a student in the Tools in Data Science course:

The image shows a user interface, specifically the "Repositories" section within a Docker Personal account under the username "santoshsharma003". It lists repositories within that namespace, showing a search bar for repository names and a dropdown menu for filtering "All content".

The UI presents a table displaying repository details:
*   **Name**: `santoshsharma003/ds-project-one-1`
*   **Last Pushed**: "2 days ago"
*   **Contains**: "IMAGE"
*   **Visibility**: "Public"
*   **Scout**: "Inactive"

There's also a "Create a repository" button.
Screenshot From 2025-04-01 11-17-441866×300 32.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/3/c33d5a5cb98598131cd2f106e811773a37d4e830.png)

---

### Post #162 by Atishay on 2025-04-01T07:41:26.018Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/162

Dear team,

The evaluation shows that the Github repo was not found, however the repository has published and public.

[![2025-04-01_13:10:20](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/a/5a304d3e8e047dc18282918c2571491ac331bd11.png)

> **Image Description**: The image shows the evaluation results of the prerequisites for Project 1. The Docker image is present in Docker Hub and public. The GitHub repo is not present and public. The Dockerfile and MIT license are not present in the root of the GitHub repo. The prerequisites are marked as FAIL, and the Project 1 score is 0.
2025-04-01_13:10:20564×317 12.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/a/5a304d3e8e047dc18282918c2571491ac331bd11.png)

Github URL
[GitHub - 22f3003029/llm_agent](https://github.com/22f3003029/llm_agent)

Roll Number: 22f3003029

Request your assistance on the issue.

Thank you

---

### Post #163 by Anushka Kumar on 2025-04-01T07:56:15.782Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/163

Respected Team,

I received an email stating I failed to fulfil prerequisite and scored 0 because of it.

[![Screenshot 2025-04-01 132313](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/c/2c79db055fab11beede425b974311028f0d93e1b.png)

> **Image Description**: The image shows the results of a project prerequisite evaluation. The results indicate that the GitHub repo, Dockerfile, and MIT license are present and public. The Docker image fails to meet the requirement of being present and public in Dockerhub, resulting in a "FAIL" for the prerequisites and a project score of 0.
Screenshot 2025-04-01 132313651×276 6.99 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/c/2c79db055fab11beede425b974311028f0d93e1b.png)

I checked my Docker Hub and there it is showing “Public”

[![Screenshot 2025-04-01 131944](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/b/7bb1e9a2434b55bd730c069340ad3c290255089c_2_690x57.png)

> **Image Description**: The image shows a table with columns for "Name", "Last Pushed", "Contains", "Visibility", and "Scout". The table has one row. The "Name" is "coolsisters7/llm". The "Last Pushed" value is "about 1 month ago" with an upward pointing arrow. The "Contains" value is "IMAGE". The "Visibility" is "Public". The "Scout" is "Inactive".
Screenshot 2025-04-01 1319441479×124 7.78 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7bb1e9a2434b55bd730c069340ad3c290255089c.png)

Can Anyone explain what I did wrong ?

---

### Post #164 by Jayesh Bansal on 2025-04-01T08:32:10.438Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/164

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/5/25537a49251705580ea50e7a1891ee99cda55e65_2_396x500.png)

> **Image Description**: The image is a Project 1 evaluation for a Tools in Data Science student. The evaluation checks for several pre-requisite criteria related to Docker and GitHub repositories. The first point is that Docker image is not present in Docker Hub and public. The GitHub repository is present and public. The Dockerfile is in the root of the GitHub repo and there is an MIT License present at the root of the GitHub repository. The overall assessment states that the student did not meet the requirements because there Docker Hub check failed and the project score is zero.
image593×747 61 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/5/25537a49251705580ea50e7a1891ee99cda55e65.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/1/317e57a3184948d62a96fd0206a53043bb0d2bac_2_690x335.png)

> **Image Description**: The image shows the Docker Hub page for the repository `jayeshbansal/tds_project1`.

Key elements visible are:
*   Repository information: "Last pushed about 1 month ago", "Repository size: 77 MB"
*   Tabs for "General", "Tags", "Image Management", "Collaborators", "Webhooks", and "Settings". The "Tags" tab is currently selected.
*   A table listing available tags, specifically the "latest" tag. The digest for the "latest" tag is "2bdbd090a678" and it is built for the "linux/amd64" architecture. It was last pulled "about 1 month" ago, and its compressed size is "77.02 MB".
*   A Docker command to pull the "latest" tag: `docker pull jayeshbansal/tds_project1:latest`.
*   A Docker command to push a new tag: `docker push jayeshbansal/tds_project1:tagname`.
image1525×741 52.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/1/317e57a3184948d62a96fd0206a53043bb0d2bac.png)

Sir, I have the image in the docker and it is upload last month and it is public. So why have I received a message saying that the image is not available in the hub. Can you confirm and reevaluate the error.

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

[@s.anand](/u/s.anand)

---

### Post #165 by Jivraj Singh Shekhawat on 2025-04-01T08:39:32.875Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/165

Hi
[@Jayeshbansal](/u/jayeshbansal)
 ,

The docker repo name that you submitted through submission form was different than what your screenshot shows.
/jayeshbansal/add9a05689d3
 docker repo doesn’t exists or might not be public, that’s why it failed for you.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e740a0a63b41602934accaa8c9ebceea5202b19_2_690x83.png)

> **Image Description**: Here is a concise description of the image:

The image presents a table with data related to a GitHub repository and a DockerHub image. The table includes the following columns: Timestamp, Email Address, GitHub repository link for Project 1 code, and the name of the image published on DockerHub. The data shows a timestamp of 2/16/2025 23:55:44, an email address of "24f1001895@ds.study.iitm.ac.in," a GitHub repository link of "https://github.com/jayesh-bansal/TDS-Project1/," and a DockerHub image name of "jayeshbansal/add9a05689d3."
image1826×222 23 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/e/6e740a0a63b41602934accaa8c9ebceea5202b19.png)

---

### Post #166 by Joel Jeffrey on 2025-04-01T08:57:06.531Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/166

The log file provided to me too contains File not found error for task A. However, running the code on the evaluate.py files gave me results. Could you please look into the datagen part?

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Thanks

---

### Post #168 by Vansh Mittal on 2025-04-01T09:08:59.871Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/168

It is the request to the team,to consider this since it is a problem of just a case letter otherwise the whole hardwork of doing the project will be wasted.

Thank you

---

### Post #169 by PalakAnand on 2025-04-01T09:16:36.251Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/169

Dear instructors, I received the mail today regarding project 1 TDS scores and I have been marked fail because the MIT license is not present. But as can be seen in the screenshot below the MIT license file is present in my GitHub repository. Pls look into this matter.

[![Screenshot 2025-04-01 at 2.45.57 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf6f3e0168b08a862b7613b75dc9dbf83e914086_2_690x406.png)

> **Image Description**: Here's a concise and factual description of the image for a student in a Tools in Data Science course:

The image is a screenshot of a GitHub repository named "Project1-TDS" with public visibility. The main branch is currently selected. It contains the following files and directories:

*   `_pycache_` (directory)
*   `app` (directory)
*   `.DS_Store` (file)
*   `Dockerfile` (file)
*   `MIT LICENSE` (file)
*   `datagen.py` (Python script)
*   `evaluate.py` (Python script)
*   `requirements.txt` (file)

The most recent commit was made by "PalakAnand30" with the message "Rename LICENSE to MIT LICENSE", and has 5 commits. The date when the last commit was 2 months ago. Each file and directory lists the reason it was committed and the date it was committed. The initial commit was made 2 months ago.
Screenshot 2025-04-01 at 2.45.57 PM1776×1046 91.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/f/cf6f3e0168b08a862b7613b75dc9dbf83e914086.png)

---

### Post #170 by Jivraj Singh Shekhawat on 2025-04-01T09:23:59.524Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/170

It depends where you tested it running, if it’s running inside a docker container and you feel there is problem with our script then you can debug our code and create a pull request on repo.

---

### Post #171 by Jivraj Singh Shekhawat on 2025-04-01T09:25:28.846Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/171

Hi
[@24ds2000125](/u/24ds2000125)

You didn’t meet the standard naming convention for mit license naming.  Name should be LICENSE(all caps) or LICENSE.md.

check this out.

[Adding a license to a repository - GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)

---

### Post #172 by Jivraj Singh Shekhawat on 2025-04-01T09:27:50.740Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/172

Hi
[@22f3001851](/u/22f3001851)

Standard naming convention for Dockerfile name was not followed we won’t be able to evaluate it.

---

### Post #173 by Shreyan Chaubey on 2025-04-01T09:37:21.052Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/173

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/9/19ee62dc5d7a4dc1f92c30889a34483fe266978d.png)

> **Image Description**: The image displays a checklist with results related to a project, specifically concerning Docker and GitHub repositories. The items checked are:
- The presence and public accessibility of a Docker image in Docker Hub: FAIL.
- The presence and public accessibility of a GitHub repository: PASS.
- The presence of a Dockerfile in the root of the GitHub repository: PASS.
- The presence of an MIT license in the root of the GitHub repository: PASS.
- The prerequisites for the project: FAIL.
- The score for Project 1 is 0.
image412×167 4.49 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/9/19ee62dc5d7a4dc1f92c30889a34483fe266978d.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png)

> **Image Description**: The image presents a table with three columns: "Last Pushed", "Contains", and "Visibility". The first row shows "about 2 hours ago" under "Last Pushed", "IMAGE" under "Contains", and "Public" under "Visibility". The second row displays "2 months ago" under "Last Pushed", "IMAGE" under "Contains", and "Public" under "Visibility". A red circle surrounds the "Public" entry in the first row.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png)

My email is 22f3001642@ds.study.iitm.ac.in

[@Jivraj](/u/jivraj)
  Could you please check what’s wrong?

---

### Post #174 by Pradeep Mondal on 2025-04-01T09:39:25.986Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/174

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

[@Saransh_Saini](/u/saransh_saini)
 any updates for the people like me whose image was run on the wrong architecture - mine was ARM ( was evaluated or ×86 ). I filled the form that was later sent for selecting the architecture.

I haven’t received any mail since then. But found many mails are sent to others in while.

---

### Post #175 by Mayank Singh on 2025-04-01T09:55:48.188Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/175

[![Screenshot 2025-04-01 at 3.17.14 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1baedfbbb7140eb2f3bc80273f8dcfa799bb85e3_2_690x486.png)

> **Image Description**: The image shows a GitHub repository named "tds-trail-1" owned by "Mayank8IITM," marked as public. The repository's structure includes:

*   A list of files such as `__pycache__`, `data`, `.dockerignore`, `Dockerfile`, `LICENSE`, `README.md`, `datagen.py`, `evaluate.py`, `main.py`, and `requirements.txt`.
*   Commit messages like "Project is done 7/10", "updated dockerfile", "Rename dockerfile to Dockerfile", "Create LICENSE", "Create README.md", "A2 and A9 left", and "added dockerfile".
*   Information about the main branch, which has 1 branch and 0 tags, with 10 commits made over 2 months.
Screenshot 2025-04-01 at 3.17.14 PM2054×1448 294 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/b/1baedfbbb7140eb2f3bc80273f8dcfa799bb85e3.png)

[![Screenshot 2025-04-01 at 3.19.32 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/4/e4a17e2340281059ba12ec777f0a33a1c662f3ea_2_690x172.png)

> **Image Description**: Here's a concise description of the image for a Tools in Data Science student:

The image shows a prerequisite evaluation report for "Project 1".  The evaluation includes the following checks, with the results:

*   Docker image present in dockerhub AND is public: PASS
*   Github repo present AND public: FAIL
*   Dockerfile present in root of github repo: FAIL
*   MIT license present at root of github repo: FAIL

The overall "Prerequisites" status is FAIL, and the Project 1 Score is 0.
Screenshot 2025-04-01 at 3.19.32 PM1894×474 49.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/4/e4a17e2340281059ba12ec777f0a33a1c662f3ea.png)

Sir , I received the mail today regarding project 1 TDS scores and I have been marked fail because my repo is not public , and no docker file , no licence . but they all are present in my repo , and it is public too , , i am attaching the screenshot , you can see that too ,

My email is 23f1000598@ds.study.iitm.ac.in

Could you please check what’s wrong?

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

[@carlton](/u/carlton)

---

### Post #176 by Carlton D'Silva on 2025-04-01T10:06:03.718Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/176

The task B6 was

[https://quotes.toscrape.com/](https://quotes.toscrape.com/)
 has quotes from famous people.

The .author class has the quote author’s name.

Extract and save all authors from the first page, in order, to /data/b6.json as an array of strings.

E.g.
["Douglas Adams", "J.K. Rowling", ...]

The output in your file is not an array of double quoted strings.

Instead it is an array of an json object with the keyword author and values as an array of authors.

These are two different things. Almost there but not quite.

Kind regards

---

### Post #177 by RAJ K BOOPATHI on 2025-04-01T10:15:47.725Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/177

Hi Course Team,

I have also received an email today saying that my Project1 failed. But few days back I received an email with evaluation log saying I got 8/20. Which one is true?

[![1000112508](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/5/459244734bb379e3b318b5cc687ad47358f764bc_2_314x500.jpeg)

> **Image Description**: Here's a description of the image for a Tools in Data Science student:

The image is an email concerning Project 1 scores.  It outlines prerequisite checks for the project.

Key details include:

*   **Prerequisites:**
    *   Docker image present in Docker Hub and public: PASS
    *   GitHub repo present and public: PASS
    *   Dockerfile present in the root of the GitHub repo: FAIL
    *   MIT license present at the root of the GitHub repo: PASS

*   **Overall Status:**
    *   Prerequisites: FAIL
    *   Project 1 Score: 0

The email also specifies the requirements that have to be met for the project submission to be evaluated. The GitHub repository must exist and be publicly accessible, contain a LICENSE file with the MIT license, and contain a valid Dockerfile. The Docker image must be publicly accessible, run via `podman`, and use the same Dockerfile as in the GitHub repository.
10001125081080×1716 242 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/5/459244734bb379e3b318b5cc687ad47358f764bc.jpeg)

---

### Post #178 by RAJ K BOOPATHI on 2025-04-01T10:18:11.331Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/178

Can someone from TA team reply to this?

---

### Post #179 by Suhani Dubey on 2025-04-01T12:38:17.909Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/179

can somebody tell me how the dockerfile not running in 5 mins is my fault? i had the same requirements.txt as many other people and their file ran in given time while mine did not. what was the need for this, sorry for my harsh words but i’m frustrated, stupid rule?

---

### Post #180 by Jivraj Singh Shekhawat on 2025-04-01T12:58:31.631Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/180

For your case there was problem with our script that, we have correct, and your submission have dockerfile, license and repo exisits as well, it will be evaluated.

---

### Post #181 by ashish al rashid on 2025-04-01T13:11:55.193Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/181

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/f/1fedb48b369376de753a03a5286bc7e16a317dbd.png)

> **Image Description**: The image shows a report for "Project 1 Prerequisite evaluations". It lists four checks: 
1. Docker image present in dockerhub AND is public: PASS
2. Github repo present AND public: PASS
3. Is Dockerfile present in root of github repo: FAIL
4. Is MIT license present at root of github repo: PASS
The Dockerfile check failed. The rest passed.
image522×190 5.51 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/f/1fedb48b369376de753a03a5286bc7e16a317dbd.png)

my dockerfile is available in github, Please look into the issue

Thank you

---

### Post #182 by LAKSHAY on 2025-04-01T13:14:42.027Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/182

[@Jivraj](/u/jivraj)

I also have same issue, can you check this…

[Repo link](https://github.com/21f3001076/TDS_Project_1)

[![1000431136](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/2/0284e9e1646abcf1a2b8e0720b33dcd4d483e301_2_258x500.jpeg)

> **Image Description**: The image shows a GitHub repository. The repository contains files such as "Dockerfile", "LICENSE", "README.md", "app.py", "requirements.txt", and "task_handler.py". The README file is displayed below the file list, showing the title "TDS Project 1 - LLM-based Automation Agent" and a link to "Create an API". The code was last updated by user "lakshay654" 2 months ago.
10004311361079×2087 175 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/2/0284e9e1646abcf1a2b8e0720b33dcd4d483e301.jpeg)

---

### Post #183 by Shreyan Chaubey on 2025-04-01T13:40:53.458Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/183

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)
 My P1 submission successfully passed all the basic sanity checks on February 15th and obtained a satisfactory score in the P1 evaluation, which was disclosed on March 29th. However, I received a communication today, April 1, stating that my Docker image is not present or public on DockerHub. I kindly request the TDS course team to investigate this matter at the earliest and provide a resolution for students encountering similar issues.

This situation is particularly disheartening—
seeing days of effort and dedication to Project 1 reduced to nothing, especially given the already demanding pace of the course.

I will appreciate your prompt attention to this matter.

Kind regards

---

### Post #184 by Jayesh Bansal on 2025-04-01T14:40:02.251Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/184

I understand the problem. It may be possible that the image id i gave may be different as i had multiple dockerfile and there is a possibility that i gave the wrong image id due to some confusion. Is it possible for reevaluation. I have worked very hard and I don’t want to lose my marks because of some wrong id misconfusion. I request to check my dockerfile once again and provide the marks accordingly

---

### Post #185 by Afsal on 2025-04-01T14:49:37.068Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/185

dear
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

Dear Sirs,

I have seen that many others have posted similar issues to mine, and you have responded to some of them. To seek your attention, I am replying to this thread.

Please consider my request as well, as I do not want to lose marks on a project I have worked hard on, while also helping others. I am expecting a timely and positive response from your end.

Thank you.

---

### Post #186 by Rahul Pathak on 2025-04-01T15:14:23.701Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/186

Dear Sir,

I hope you’re doing well. I haven’t received any email regarding the results of Project 1. Could you please check if my result was sent or if there’s any update on this?

I would really appreciate your confirmation.

Mail id - 23f2000798@ds.study.iitm.ac.in

---

### Post #187 by Sujith Sai K on 2025-04-01T15:23:46.604Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/187

[@carlton](/u/carlton)

Respected Sir,

I have submitted my project following all the guidelines and fulfilling all the prerequisites. My docker file is available publicly and it is present in the root directory of github repo, still the mail says that the file is missing and my score is zero. Can you please look into this issue

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/3/332ce73b428520a8174e81c0d1a6922c2f1e334a.png)

> **Image Description**: The image shows a file directory listing, presumably from a code repository. The listed files include: `datagen.py`, `dockerfile`, `evaluate.py`, `requirements.txt`, `tasksA.py`, and `tasksB.py`. The modifications for `datagen.py`, `evaluate.py`, `tasksA.py`, and `tasksB.py` are tagged as `v1`. The `dockerfile` has been modified with `docker updatae`. The `requirements.txt` is tagged as `v1.1`. All files were modified 2 months ago.
image1145×334 7.28 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/3/332ce73b428520a8174e81c0d1a6922c2f1e334a.png)

---

### Post #188 by Jivraj Singh Shekhawat on 2025-04-01T16:47:18.686Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/188

Name of your dockerfile doesn’t match the standard’s.

It should be
Dockerfile
(with D caps).

---

### Post #189 by Jivraj Singh Shekhawat on 2025-04-01T16:48:19.889Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/189

No we are doing another run of evaluations. Results will be sent soon.

---

### Post #190 by Vaddi Yaswanth on 2025-04-01T16:48:22.878Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/190

dockerfile name should be Dockerfile as this is the standard they are considering .so it was not evaluated you better change that, if they revaluate it will be passed

---

### Post #191 by Jivraj Singh Shekhawat on 2025-04-01T16:51:25.206Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/191

Your submission have Dockerfile, LICENSE and repo exists as well, we found some problems because of redirects not handled in our script.

Your submission will be evaluated.

---

### Post #192 by Jivraj Singh Shekhawat on 2025-04-01T16:53:06.940Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/192

We won’t be considering changes after deadline, our script looks for commits before deadline and fetches latest commits before deadline.

---

### Post #193 by Jivraj Singh Shekhawat on 2025-04-01T16:54:41.830Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/193

That’s not possible, anything after deadline is not appreciated.

---

### Post #194 by Vaddi Yaswanth on 2025-04-01T16:54:55.948Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/194

We have updated just files names will it be considered??

---

### Post #195 by Veer Shah on 2025-04-01T16:55:11.504Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/195

same issue with me , my repo has both the dockerfile , license and is public. Please look into this .
[@carlton](/u/carlton)
 sir .
[@Jivraj](/u/jivraj)

[GitHub - veershah1231/tds_proj_1: Tds project](https://github.com/veershah1231/tds_proj_1)
 and i have made them 2 months ago and is not a new commit.

[![1000105386](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_299x500.jpeg)

> **Image Description**: Here's a concise and factual description of the image:

The image shows an email regarding Project 1 prerequisites for a Tools in Data Science course. The email lists five requirements related to GitHub repositories, Dockerfiles, and Docker images. An evaluation section indicates whether each requirement was met. 

*   Docker image present in dockerhub AND public: PASS
*   Github repo present AND public: FAIL
*   Dockerfile present in root of github repo: FAIL
*   MIT license present at root of github repo: FAIL

The student failed the prerequisites, resulting in a Project 1 score of 0.
10001053861072×1787 256 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3.jpeg)

---

### Post #197 by Shashikumar Kohir on 2025-04-01T17:13:03.760Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/197

![:cross_mark:](https://emoji.discourse-cdn.com/google/cross_mark.png?v=14)
 Did Not Receive Project 1 Score – Need Clarification

Post Content:

Hello, sir

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

I received the evaluation email for my
Project 1 Docker Image
 submission, but unlike my friend (who got an email with his score), my email did
not
 include my score.

My Docker image ID:
6f446c9b84da

The email I received only contains logs and attachments, but no information about my actual score. in the mail recieved by my friend the score is clearly mentioned,

I would really appreciate it if you could
clarify my project score
 and let me know if it was properly evaluated. If there is any issue, I request a reconsideration of my project evaluation.

Thank you for your help!

Attachments:

but in the email which i recieved i got the below thing , there is no information about the project score

[![my email without score](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/8/f86eddb6cefbdcfd3e1b7d54b8310cedaad53edf.png)

> **Image Description**: The image shows an email regarding a docker image project submission. The email provides feedback on the submission, lists files that are missing or attached (such as evaluation logs, docker logs, server start logs, evaluation script, data generation file, docker orchestration file, and solution script), and discusses the evaluation process and scoring. The email also contains a link to the docker log file on Google Drive. There is mention of the evaluation server's specifications (8 core Xeon Google Cloud compute unit with 1 Gigabit network bandwidth). The email concludes by informing the recipient that scores are not final and offering an opportunity to report discrepancies.
my email without score1403×811 35.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/8/f86eddb6cefbdcfd3e1b7d54b8310cedaad53edf.png)

sir could you please clarify about my project score ???

waiting for the response

---

### Post #198 by SAKSHI PATHAK on 2025-04-01T17:14:28.160Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/198

I am also facing the same issue sir please provide proper answer for our query. Please consider to recheck the project once again.

Docker image - 5ff55c499b54

[![1000161685](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/e/2e0e98a294f898f58e4d9dc68708cf723207c1ad_2_225x500.jpeg)

> **Image Description**: The image shows an email from "22t1 se2002" to the recipient, providing feedback on their project 1 docker image submission. The evaluation found the following issues:

*   The Evaluation log file is missing, which contains the performance report.
*   The Docker log file is available via a Google Drive link.
*   The Server start log file, Evaluation script file, Data generation file, and Docker orchestration file are attached to the email.
*   The email mentions that a missing file will result in a score of 0.
*   The evaluation was performed on an 8-core Xeon Google Cloud compute unit.
*   The docker image should become responsive in 5 minutes after launch.
10001616851080×2400 224 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/e/2e0e98a294f898f58e4d9dc68708cf723207c1ad.jpeg)

[@carlton](/u/carlton)
 ,
[@Jivraj](/u/jivraj)
 ,
[@Saransh_Saini](/u/saransh_saini)

---

### Post #199 by Jayaram on 2025-04-01T17:32:53.177Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/199

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Got a email stating that prereq failed stating below..

Is Docker image present in dockerhub AND is public: FAIL

but i can see that image is public as shown below image.. am i missing something..

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/ea109fa33e1cd4ca86ced5d663681c124e261b09_2_690x135.png)

> **Image Description**: The image shows a table with data about a repository named "rsjay1976/tds-project1-jan25". The table has four columns: "Name", "Last Pushed", "Contains", and "Visibility". The "Last Pushed" value is "2 days ago". The "Contains" value is "IMAGE", and the "Visibility" is "Public".
image902×177 12.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/ea109fa33e1cd4ca86ced5d663681c124e261b09.png)

---

### Post #200 by Jivraj Singh Shekhawat on 2025-04-01T17:35:45.124Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/200

Given that you noticed an error on our side, you could have informed us about the same. However, you made your changes 22 hours ago, which is not acceptable.

tags = httpx.get(
                f"https://hub.docker.com/v2/repositories/{username}/{repo}/tags?ordering=last_updated",timeout = 60
            ).json()
            tag, size = next(
                (
                    (tag["name"], tag["full_size"])
                    for tag in tags.get("results", [])
                    if pd.Timestamp(tag["last_updated"]) <= DEADLINE
                ),
                (None, 0),
            )

This is part of our script that does the validation check for docker repo.

---

### Post #201 by Reva Lakshmy Paul on 2025-04-01T17:47:02.771Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/201

Sir,

The License file is present in the github repository however i received a mail that said that it was absent.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/6/a63b3e5cf7847aad19780199e18d9767880f3de8_2_690x405.png)

> **Image Description**: The image shows a GitHub repository named "tds_project-1" which is public. The repository is on the "main" branch and has one branch and no tags. The most recent commit has the ID "22f3000585" and the message "Create LICENSE". The repository contains several files and directories including "_pycache_", "venv", "Dockerfile", "LICENSE", "MIT LICENSE", "app.py", "requirements.txt", and "test.txt". The "LICENSE" file was created "now", while the other files were last modified "2 months ago". The most recent commit has the short code "c61a6ef" and involved 6 commits.
image1145×673 33.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a63b3e5cf7847aad19780199e18d9767880f3de8.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/4/3401452ad3977fe3c1b1abed1f71a21c212e2b67.png)

> **Image Description**: The image shows the results of a Project 1 prerequisite evaluation. The evaluation includes checks for:

*   A Docker image present in Docker Hub and publicly accessible.
*   A GitHub repository that is present and public.
*   A Dockerfile in the root directory of the GitHub repository.
*   An MIT license in the root directory of the GitHub repository.

The evaluation shows that the first three checks passed, while the MIT license check failed. As a result, the overall "Prerequisites" status is "FAIL" and the Project 1 score is 0.
image633×336 7.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/4/3401452ad3977fe3c1b1abed1f71a21c212e2b67.png)

Sir I thought that the ‘LICENSE’ file had to be renamed to ‘MIT LICENSE’.

Can you please look into it. Thankyou!

---

### Post #202 by LAKSHAY on 2025-04-01T17:48:50.614Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/202

[@Jivraj](/u/jivraj)

Can you also clarify my issue?

My submission meets all the prerequisites according to my Git repository and Docker image. Additionally, I can see the results in the evaluation log.

You can check the details in the images below. Screenshot of mail and repository

Roll no. : 21f3001076

[GitHub Repo link](https://github.com/21f3001076/TDS_Project_1)

[![1000431410](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/e/ee709e09763f171bdd0bbadccb2887556edbfa68_2_690x352.jpeg)

> **Image Description**: The image shows a Project 1 prerequisite evaluation. The Docker image is present in Docker Hub and public, indicated by "PASS." However, the Github repo is not present or public ("FAIL"). A Dockerfile and an MIT license are also missing from the root of the Github repo ("FAIL"). The overall prerequisites evaluation is "FAIL," and the project score is 0.
10004314101080×551 159 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/e/ee709e09763f171bdd0bbadccb2887556edbfa68.jpeg)

[![1000431413](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/4/94566b0ed49bb7659aa9c8a0941fa3b41bfb563e_2_690x472.jpeg)

> **Image Description**: The image shows text providing links to log files related to a performance evaluation. It lists links to: 1) an Evaluation log file on Google Drive, described as containing performance reports on individual tasks; 2) a Docker log file on Google Drive, described as providing the technical performance of a container; and 3) a Server start log file (as an attachment), noting separate logs for arm vs x86 architectures.
10004314131080×740 187 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/4/94566b0ed49bb7659aa9c8a0941fa3b41bfb563e.jpeg)

[![1000431415](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/f/6f945a759e9a4e932192211dd679839ae21921fe_2_330x500.jpeg)

> **Image Description**: Here's a description of the image for a Tools in Data Science student:

The image shows a GitHub repository interface. The repository contains files: `Dockerfile`, `LICENSE`, `README.md`, `app.py`, `requirements.txt`, and `task_handler.py`. The current branch is `main`. The repository owner is "lakshay654", and the files were last updated 2 months ago. The repository's README is displayed, with the title "TDS Project 1 - LLM-based". The repository uses the MIT license.
10004314151079×1630 134 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/f/6f945a759e9a4e932192211dd679839ae21921fe.jpeg)

---

### Post #203 by Jivraj Singh Shekhawat on 2025-04-01T17:49:39.668Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/203

Standard name of dockerfile is Dockerfile that’s why it didn’t pass Dockerfile check

---

### Post #204 by Sirimilla Karthik Balaji on 2025-04-01T18:24:32.092Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/204

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

I understand sir Dockerfile name was misspelt sir. Since my Docker image was built and recognized, I didn’t realize this would prevent evaluation.

I worked hard on this project sir, and my Docker image was built successfully. Please consider my submission sir.

---

### Post #205 by Ansh on 2025-04-01T18:24:46.558Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/205

I  have been trying to resolve all the errors but just noticed that my docker image id associated with the project is “c9dc7fbcf405” , meanwhile the mail I received mentions that some other image id was evaluated.

Can you please look into this matter and evaluate the correct Image ID.

Roll number: 23F1001012

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #206 by Shreyan Chaubey on 2025-04-01T19:02:11.386Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/206

[@Jivraj](/u/jivraj)

[@Carlton](/u/carlton)
 I completely understand that changes to the Docker image after the deadline cannot be accepted.

However, there are specific cases like mine where the Project 1 submission successfully passed the sanity checks on Feb 15 and received a decent score when the evaluation results were released on Mar 29.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/a/9acc2fc47ea84b9e26c1ed21442ba873d0dca20e.png)

> **Image Description**: Here's a concise and factual description of the image for a student in a Tools in Data Science course:

The image presents a list of files and resources related to a docker image evaluation.  It includes:

*   Links to Google Drive files: "Evaluation log file" and "Docker log file".
*   Mentions of attachments: "Server start log file", "Evaluation script file", "Data generation file", "Docker orchestration file", and "Solution script".
*   Brief descriptions of the purpose of each file (e.g., performance report, technical performance, tests used, etc.).
*   The ID of the evaluated docker image: "11aa22fc1545"
image1272×395 25.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/a/9acc2fc47ea84b9e26c1ed21442ba873d0dca20e.png)

But here’s the catch:** Since the problem statement for Project 1 and Project 2 is nearly the same, I took the opportunity to improve upon my Project 1 and use it as the foundation for my Project 2 submission, which I did by:*

Implementing a ReAct-based workflow planning & orchestration agent, inspired by the paper
[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
.

Implementing various tools for web-serping, web-scraping, read-eval-print-loops interpreters for quick calculations, etc.

Enhancing Shell-use & Python-use by improving upon the existing code interpreter I had implemented for P1. This allowed the agent to dynamically generate and execute code without hardcoding anything.

Adding useful API endpoints, including an
/api/
 multipart/form endpoint, alongside the existing
/read
 and
/run
 endpoints from Project 1, plus a
/clear
 endpoint to reset the agent’s conversation memory if the context window gets saturated.

Deploying the entire project on a paid GCP VM Instance with a static IP
, utilizing my own OpenAI API key while keeping OpenAI’s API as a fallback in case AIPROXY ever gave up.

All this hard work evolved my project into something far beyond a simple Tool-Calling Agent—it essentially became a ReAct Principles based Computer-Using Agent capable of executing complex, non-linear workflows entirely within a container. And I’m not exaggerating: You could ask it to perform something like
hyperparameter tuning for a Random Forest Classifier, offloading the results locally on a JSON file and displaying its contents
, and it would do that for you—without
ever
 declining the request. I like to think of it as a
terminal version of

[OpenAI’s Computer-Using Agent](https://openai.com/index/computer-using-agent/)
.

Given all the effort, time, and money that went into this, it’s incredibly discouraging to see my project
naturally fail a sanity check (Docker image digest mismatch) (because of the aforesaid updates)
 and not get evaluated as a result. This is not the kind of experience that encourages students to learn, experiment, and innovate.

[](#p-614374-to-clarify-all-the-updates-mentioned-above-took-place-after-march-29-after-project-1-had-already-been-evaluated-and-results-had-been-handed-out-furthermore-we-were-never-informed-that-a-reevaluation-would-take-place-on-april-1-had-i-known-i-would-have-ensured-that-my-original-submission-remained-unchanged-and-considered-creating-a-duplicate-of-my-docker-image-and-implementing-all-the-aforementioned-enhancements-on-it-1)
To clarify,
all the updates mentioned above took place after March 29
,
after Project 1 had already been evaluated, and results had been handed out.
 Furthermore, we were
never informed
 that a reevaluation would take place on April 1. Had I known, I would have ensured that my original submission remained unchanged and considered creating a duplicate of my Docker image and implementing all the aforementioned enhancements on it.

My only request is that if my
updated P1 submission cannot be evaluated
 due to the changes made after March 29 (before the P1 reevaluation on April 1), I would really appreciate it if my
original P1 eval score could be reinstated
 instead of receiving a
0
—since it was already evaluated and graded.

Would highly appreciate your prompt support in this regard
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #207 by Pooja M on 2025-04-01T16:15:15.814Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/207

[![pro 1](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0daeec08afc5b8bf1176ea341a88da5d99a592e8_2_225x500.jpeg)

> **Image Description**: Here's a description of the image:

The image displays results from a project submission evaluation. Key findings:

*   **Docker Image:** Present in Dockerhub and public (PASS).
*   **Github Repo:** Present and public (PASS).
*   **Dockerfile:** NOT present in the root of the Github repo (FAIL).
*   **MIT License:** Present in the root of the Github repo (PASS).
*   **Overall:** Prerequisites FAIL, Project 1 Score is 0.
pro 1720×1600 81.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/d/0daeec08afc5b8bf1176ea341a88da5d99a592e8.jpeg)

Actually I got the email as my docker file is not in root git hub repository. But everything thing looks fine and my docker file also runs well.. I want to check my repo again ..sir kindly do my my evaluation again and we have put lot of efforts doing this project 1 . Hope the team evaluated and gives the deserved marks

[@carlton](/u/carlton)

@ TDS TEAM

---

### Post #208 by Jivraj Singh Shekhawat on 2025-04-02T00:45:03.921Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/208

There is no Dockerfile in the root directory of your GitHub repository. The standard naming convention for a Dockerfile is Dockerfile.

---

### Post #209 by Jayaram on 2025-04-02T03:08:21.150Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/209

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)
 please let know if any issues in my end on the docker image not present issue.. As explained in earlier thread , the only reason docker image had to be pushed  was the removal my office proxies in the docker image which was making the container not to startup from orchestration environment.. any help is appreciated..

---

### Post #210 by NK on 2025-04-02T06:51:17.887Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/210

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
  I updated google form 4 days ago on the architecture, Could you let me know when it will be re-evaluated ? Thanks

---

### Post #211 by Jivraj Singh Shekhawat on 2025-04-02T07:35:26.123Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/211

Hi
[@thinkmachine](/u/thinkmachine)

[@22f3002723](/u/22f3002723)

Since you updated docker repo few days ago and docker api doens’t support timestamp based pulling we will pull your GitHub repo before 18 th feb and will build through it and run evaluations.

We also have your docker repo evaluation score, will discuss which one to keep.

This is for anyone who updated their docker repo and there are around 10-20 such cases

---

### Post #212 by Jayaram on 2025-04-02T08:20:36.942Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/212

Thanks for the understanding
[@Jivraj](/u/jivraj)

---

### Post #213 by Saransh Saini on 2025-04-02T09:08:13.004Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/213

Hi
[@thinkmachine](/u/thinkmachine)

As we said before that changes in Docker image after deadline won’t be accepted. Even an extension of the deadline won’t help in this case, simply because Docker API doesn’t support timestamp based pulling. However we would be pulling your GitHub repositories before 18th Feb build a Docker container and run evaluations on that.

---

### Post #214 by Atishay on 2025-04-02T09:12:10.439Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/214

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

[@Saransh_Saini](/u/saransh_saini)
 request your help in clarification for the same, the Github repo has been always present but it is marking it as fail. Thank you

---

### Post #215 by Shreyan Chaubey on 2025-04-02T09:31:53.254Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/215

A sigh of relief! Thank you so much for the heads up
[@Jivraj](/u/jivraj)
.

[@Saransh_Saini](/u/saransh_saini)
 Yup! The Docker issue is perfectly understandable. Even I checked my Hub repo, and I couldn’t seem to find an image having the pre-18th Feb digest. Had I been aware of this issue, and the fact that a re-eval would be carried out, I would’ve tagged the updated image differently. Hopefully, cases like mine will aid in resolving any issues in the future.

Once again, thank you both!

---

### Post #216 by LAKSHAY on 2025-04-02T12:59:33.351Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/216

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

[@Saransh_Saini](/u/saransh_saini)

I am still uncertain as to why I received a second email regarding my project 1 score, indicating a failure due to unmet pre-requisites. I have inquired multiple times, yet I have not received a response. Meanwhile, several other posts, both before and after mine, have been addressed. Kindly clarify about that mail.

Thankyou

---

### Post #217 by Yashvardhan on 2025-04-02T13:09:36.259Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/217

[@carlton](/u/carlton)
   Sir pls see my issue

---

### Post #218 by Swati Kapoor on 2025-04-02T13:38:07.523Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/218

I have the same issue. I also received a second mail stating I had failed due to some missing prerequisites though in the first mail my project evaluation had been carried out.

---

### Post #219 by Carlton D'Silva on 2025-04-02T14:18:50.862Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/219

Hi
[@lakshaygarg654](/u/lakshaygarg654)

Dont worry you passed pre-requsites. The script that was used earlier for basic checks used a stricter criteria, the newer one we wrote allowed for a looser check. You have scored very well in your latest run. 12 correct tasks.

We have not responded quickly because we are in the midst of finalising all the scores and doing normalisation etc, i.e operational work for Project 1 and 2.

We hope to have Project 2 scores out by this weekend.

Kind regards

---

### Post #220 by Vansh Mittal on 2025-04-02T14:26:27.322Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/220

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Sir can you also see the case of Dockerfile name. Many students have named it dockerfile , lower case ‘d’ character instead of upper case.

Please sir see through it

---

### Post #221 by LAKSHAY on 2025-04-02T14:30:33.339Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/221

Thanks
[@carlton](/u/carlton)
 , for your response.

I was never worried about the result, whether it comes late or early. I know you will release it once everything is processed correctly. My concern was only about getting a response. Anyway, thanks for replying.

Also, today’s session has been canceled. I wanted to ask about the issue with editing responses in the Project 2 form. Is there any update on this?

---

### Post #222 by Chinnam Goutham Nischay on 2025-04-02T18:21:51.820Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/222

Hi just wanted to know, there was no mail prior stating to keep the Dockerfile in the root folder of the repo (correct me if im wrong). Therefore i have put everything inside a folder - wont this be considered? Please clarify if possible.

[![Screenshot 2025-04-02 at 11.41.14 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f31f9a238afa57c9c57655de5c717546fa4f9268_2_690x274.png)

> **Image Description**: The image is a screenshot of a GitHub repository named "tds_project1". It is a public repository. The current branch is "main". The repository has 1 branch and 0 tags. The files and directories in the repository include:
- A directory named "tds-project-1"
- A file named "LICENSE"
- A file named "README.md"
- A file named "README" with the MIT License
The most recent commit was made 2 months ago and is titled "done". The repository has 14 commits.
Screenshot 2025-04-02 at 11.41.14 PM1884×750 69.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/3/f31f9a238afa57c9c57655de5c717546fa4f9268.png)

[![Screenshot 2025-04-02 at 11.43.17 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/5/85aed36152ce7c20f03accf0e9d01a5fc596109c_2_690x224.png)

> **Image Description**: The image shows a GitHub repository named "tds_project1" with the sub-path "tds-project-1". The last commit was "21f1002409" with the message "done". The repository contains the following files and directories: "app", ".gitignore", "Dockerfile", and "README.md". The last commit message for all files is "done" and the last commit date is "2 months ago". There is an option to "Add file" and a "History" button indicating commit history.
Screenshot 2025-04-02 at 11.43.17 PM2290×744 55.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/5/85aed36152ce7c20f03accf0e9d01a5fc596109c.png)

---

### Post #223 by Aryan Tikam on 2025-04-02T18:26:01.598Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/223

[![1000004176](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/a/da4e9a282399e03a47410d7ddb796d4a01802f5d_2_690x259.png)

> **Image Description**: The image shows an HTTP 500 error message in JSON format. The "details" field indicates a "Task handling error" where the LLM response failed after three attempts, resulting in a 401 error. The nested "error" field specifies that the authentication token is not from a valid issuer, with the error code being "invalid_issuer". The overall error is "Internal server error".
10000041761187×446 55 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/a/da4e9a282399e03a47410d7ddb796d4a01802f5d.png)

Can anyone explain what errors of this sort mean?

---

### Post #224 by Carlton D'Silva on 2025-04-03T00:30:31.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/224

You have to show which task triggered this error. Is it all of them or only one of them. Only then we can diagnose what the problem is.

---

### Post #225 by Aryan Tikam on 2025-04-03T03:32:09.872Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/225

[![1000004190](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a204d9c51d90a584e4e56d593b24821129e056e_2_519x500.png)

> **Image Description**: The image shows a console output with error messages related to a task failing. 

- A formatting task on the file `/data/format.md` using `prettier@3.4.2` failed in-place.
- An HTTP POST request to `http://localhost:8365/run` resulted in a `500 INTERNAL SERVER ERROR`. The task parameter in the request includes the file path and prettier version.
- The details indicate a task handling error, specifically failing to get an LLM response after three attempts. The error code is 401, indicating an invalid authentication token issuer.
- An HTTP GET request to `http://localhost:8365/read` for the file `/data/format.md` resulted in a `400 BAD REQUEST`.
- Finally, it reports that A2 failed because it cannot read the `/data/format.md` file.
10000041901193×1149 136 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/a/6a204d9c51d90a584e4e56d593b24821129e056e.png)

Here it is with the task, however the error doesn’t seem to be related to the task itself based on the returned message in the JSON. It seems to be something wrong with the OpenAI API key. From the reading I did, it seems that the key was perhaps not set properly during evaluation? Not completely sure but please look into it.

---

### Post #226 by Carlton D'Silva on 2025-04-03T04:12:16.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/226

Did all tasks produce the same error?

---

### Post #227 by Aryan Tikam on 2025-04-03T04:21:12.815Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/227

Yes except B1 somehow.

---

### Post #228 by Jivraj Singh Shekhawat on 2025-04-03T04:53:30.583Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/228

Hi
[@AryanTikam](/u/aryantikam)

I looked at your github repo, You have used python’s
openai
 module for doing project1, but AIPROXY_TOKEN is supposed to be used through anand sir’s proxy.

---

### Post #229 by Aarush saxena  on 2025-04-03T04:55:29.269Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/229

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

Can you pls tell me my project 1 marks

My evaluation.py had 2 score

First one 1/20 where every task showed error second one had 10/20…

---

### Post #230 by Jivraj Singh Shekhawat on 2025-04-03T05:00:40.458Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/230

Dockerfile has to be insider root directory of github repo.

---

### Post #231 by Jivraj Singh Shekhawat on 2025-04-03T05:29:41.769Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/231

This was mistake from our end we rectified it and reevaluated your submission.

Your submission has a good score.

---

### Post #232 by Jivraj Singh Shekhawat on 2025-04-03T05:31:50.788Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/232

[swati-iitm/project1_final](https://github.com/swati-iitm/project1_final)

This is your github repo which doesn’t have a Dockerfile. That’s why It didn’t pass Prechecks

---

### Post #233 by Jivraj Singh Shekhawat on 2025-04-03T05:35:55.465Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/233

We have reevaluated it, we have scores avaliable for your submission.

---

### Post #234 by S Smriti on 2025-04-03T05:43:00.016Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/234

Sir I understand you will be busy evaluating all the files and reevaluating them as well. I just wanted to know if its a confirm 0 for those who got evaluation log file MISSING and didnt get the other mail that many got in the past 2 days… Just to confirm… cause i think am getting 0 from that
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #235 by Aryan Tikam on 2025-04-03T06:13:03.047Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/235

So can anything be done about it now as it seems to pass more tasks without the proxy requirement? It is fine if not.

---

### Post #236 by Chinnam Goutham Nischay on 2025-04-03T06:29:32.803Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/236

Please, can you put a screenshot of where it has been communicated, prior to the deadline.

---

### Post #237 by Carlton D'Silva on 2025-04-03T06:51:18.604Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/237

We have communicated it in the live sessions. It was also communicated via an email when students failed first prerequisite check pass back in February 16th. At that time we gave students a time window to fix it.

We discussed it internally with
[@s.anand](/u/s.anand)
 and he stated that it is standard industry practise to put Dockerfile in the root folder of a github and he expects students to do it
regardless of whether we explicitly mentioned it or not
 on the project 1 page. The reason being, any Docker image being built from a github repo is never going to look for the file sitting inside a directory. All build requirements have to be at root (this is not just for Docker, but also any other type of application build). Since root is where the core files to build an application always reside, again this is standard industry practise.

In our meeting we advocated for a lenient approach to search for Dockerfile inside the github and it was vetoed by
[@s.anand](/u/s.anand)

So unless you can give a convincing argument why we should change our evaluation script and re run it for everyone again, (because that is effectively what we would have to do to make it fair to everyone), we will not be able to evaluate your docker image.

Kind regards,

TDS team

---

### Post #238 by Saini Nirmal on 2025-03-31T21:18:59.717Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/238

[@carlton](/u/carlton)
 Sir, I would like to respectfully ask if this is some sort of April Fool’s joke, as it appears that the TDS team is still only verifying the presence of files in the git repository and checking the accessibility of the repository. I fully understand the importance of marks and the effort we put into Project 1. That’s why I carefully ensured that all the necessary files and links were correctly uploaded yet I received a 0 Score.

I am not the only one facing this issue; several others have encountered the same problem. I kindly request you to review my submission again.

Additionally, I have faced multiple technical issues in recent times. Initially, I was failed in the L1 viva due to a typing mistake, which was later acknowledged. Similarly, in both OPPE 1 and OPPE 2, many students experienced Google Meet issues. On March 29, during my SC OPPE, I faced camera issues in Google Meet, along with VM lagging. Many students have raised similar concerns with Proctor.

Given this track record of technical problems, I strongly believe this could be another error in evaluation. I sincerely request you to re-evaluate my submission.

[![Screenshot 2025-04-01 020618](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c15a5d064b9f2bc82a892ef7da1228f031feb29b_2_690x344.png)

> **Image Description**: Here is a description of the image:

The image is a screenshot of an email titled "TDS Jan 25 Project 1 Scores". The email outlines the prerequisites for Project 1, which includes:
*   A publicly accessible GitHub repository.
*   A LICENSE file with the MIT license in the GitHub repository.
*   A valid Dockerfile in the GitHub repository.
*   A publicly accessible Docker image that runs via podman.
*   The Docker image using the same Dockerfile as in the GitHub repository.

The email includes a "Project 1 Prerequisite evaluations" section, with the following results:

*   Is Docker image present in dockerhub AND is public: PASS
*   Is Github repo present AND public: FAIL
*   Is Dockerfile present in root of github repo: FAIL
*   Is MIT license present at root of github repo: FAIL

Overall, the prerequisites are marked as "FAIL".
Screenshot 2025-04-01 0206181335×667 57.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c15a5d064b9f2bc82a892ef7da1228f031feb29b.png)

---

### Post #239 by Vedant Bhanushali on 2025-04-01T05:52:49.180Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/239

[![IMG_7078](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_394x500.jpeg)

> **Image Description**: The image shows results of a prerequisite evaluation for a project. The evaluations include:
-Docker image present in dockerhub AND is public: FAIL
-Github repo present AND public: PASS
-Dockerfile present in root of github repo: PASS
-MIT license present at root of github repo: PASS

The overall "Prerequisites" evaluation is FAIL and the "Project 1 Score" is 0.
The image also refers to using a Dockerfile, a Docker image, and a GitHub repository. The Docker image should be accessible, run with a specific command using podman, and use the same Dockerfile as in the GitHub repository.
IMG_7078828×1049 164 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899.jpeg)

Same for me sir, i had everything correct still its showing:- Is Docker image present in dockerhub

AND is public: FAIL

I have submitted everything correctly . Please carefully look into this and recheck the project submitted.

---

### Post #240 by Vedant Bhanushali on 2025-04-01T05:55:19.131Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/240

Sir,it appears that the TDS team is still only verifying the presence of files in the git repository and checking the accessibility of the repository. I fully understand the importance of marks and the effort we put into Project 1. That’s why I carefully ensured that all the necessary files and links were correctly uploaded yet I received a 0

[@carlton](/u/carlton)
 Sir please look into this.

[![IMG_7078](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899_2_394x500.jpeg)IMG_7078828×1049 164 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/4089a9e8f0f406a1c06ffd2c33cff5f18a832899.jpeg)

[@carlton](/u/carlton)
 Sir, given  this track record of technical problems, I strongly believe this could be another error in evaluation. I sincerely request you to re-evaluate my submission.

---

### Post #241 by Deepak kumar on 2025-04-01T07:24:27.184Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/241

[![Screenshot 2025-04-01 at 12.50.38 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c240e636b74a12f59d3c0d50fc904bb7361a481a_2_690x439.png)

> **Image Description**: Here's a description of the image for a student in the Tools in Data Science course:

The image is a screenshot of an email titled "TDS Jan 25 Project 1 Scores." The email outlines the prerequisite checks for Project 1:

*   GitHub repository exists and is publicly accessible.
*   GitHub repository has a LICENSE file with the MIT license.
*   GitHub repository has a valid Dockerfile.
*   Docker image is publicly accessible and runs via `podman run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME`.
*   Docker image uses the same Dockerfile as in the GitHub repository.

The email indicates that the following evaluations failed:

*   Docker image present in dockerhub AND is public: FAIL
*   GitHub repo present AND public: FAIL
*   Dockerfile present in the root of the GitHub repo: FAIL
*   MIT license present at the root of the GitHub repo: FAIL

The final assessment shows "Prerequisites: FAIL" and "Project 1 Score: 0".
Screenshot 2025-04-01 at 12.50.38 PM2062×1314 262 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/2/c240e636b74a12f59d3c0d50fc904bb7361a481a.png)

[@carlton](/u/carlton)
 sir, i would like to ask why marks showing 0 infact i am submitting all my requirements things in that form so plz look into this matter.

---

### Post #242 by Prashant Aswani  on 2025-04-02T17:45:24.192Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/242

[@carlton](/u/carlton)
 sir, similar thing happened to me as well, I had got the mail that git repo, dockerfile and lisence is not present or accessible while all the prerequisites are completed from my end. Can you please reevaluate my submission.

[![1000051556](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eab711c7e3854b0163bab1970630905785492718_2_290x500.jpeg)

> **Image Description**: The image is an evaluation report for a TDS (Tools in Data Science) Project 1. The evaluation checks the following:

1.  GitHub repository exists and is publicly accessible.
2.  GitHub repository has a LICENSE file with the MIT license.
3.  GitHub repository has a valid Dockerfile.
4.  Docker image is publicly accessible and runs via podman.
5.  Docker image uses the same Dockerfile as in the GitHub repository.

The student's Project 1 evaluations are:

*   Docker image present in dockerhub AND is public: PASS
*   Github repo present AND public: FAIL
*   Dockerfile present in root of github repo: FAIL
*   MIT license present at root of github repo: FAIL

Overall, the prerequisites are marked as FAIL, resulting in a Project 1 score of 0.
10000515561238×2131 182 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/eab711c7e3854b0163bab1970630905785492718.jpeg)

---

### Post #243 by Carlton D'Silva on 2025-04-03T03:03:12.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/243

Hi Prashant,

Your prerequisites have passed and your evaluation is 6 tasks have been completed successfully. The email was auto sent because we were doing some checks with an older, stricter script. The newer script passes your evaluation.

Kind regards

---

### Post #244 by Chinnam Goutham Nischay on 2025-04-03T07:07:07.893Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/244

Thanks for the quick reply, i don’t have a convincing argument to counter. Just a suggestion it would have been better if you have explicitly put in the sanity check requirements. Something so obvious to you might not be so for others.

if you are referring to this email even here, it was not explicit. Might have missed it in the gmeet. A mail would have been good.

[![Screenshot 2025-04-03 at 12.28.22 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/d/ad091bfbf1e7642fa941a72ce2d527fac1e26dd8_2_690x281.png)

> **Image Description**: Here's a description of the image:

**Type:** Email

**Sender:** donot_reply@study.iitm.ac.in

**Subject:** [TDS Jan 2025] Important: Please check your submissions for basic sanity

**Content:**

*   The email informs students to check their submissions for basic sanity.
*   Basic sanity checks include:
    *   GitHub repo being public
    *   MIT license availability
    *   Existence of a DockerFile
    *   Docker image accessibility
*   Out of 530+ submissions, only 284 cleared the basic sanity check. Students are asked to check their email (Inbox and SPAM) for errors from the course admin (se2002) with the subject "[IMPORTANT]".
*   Project 1 submissions are at risk of scoring 0 marks if the errors are not fixed.
*   The email emphasizes that the last submission in the form was taken for validation.
*   Students are urged to correct the reported errors.
Screenshot 2025-04-03 at 12.28.22 PM2236×912 208 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/d/ad091bfbf1e7642fa941a72ce2d527fac1e26dd8.png)

---

### Post #245 by Carlton D'Silva on 2025-04-03T07:20:58.966Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/245

I agree with you. It should have been explicitly mentioned in the project page (even if we have mentioned it in live sessions)

---

### Post #246 by Aarush saxena  on 2025-04-03T07:33:53.126Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/246

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Put some light on this poor soul’s message also ;')

---

### Post #247 by Veer Shah on 2025-04-03T08:50:54.826Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/247

my repo has both the dockerfile with correct name (Dockerfile and in the root folder), license and is public. Please look into this .
[@carlton](/u/carlton)
 sir .
[@Jivraj](/u/jivraj)

[GitHub - veershah1231/tds_proj_1: Tds project](https://github.com/veershah1231/tds_proj_1)
 and i have made them 2 months ago and is not a new commit.

[![1000105386](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3_2_299x500.jpeg)10001053861072×1787 256 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/f/7f60eaa650a67981fa545775751b5533966b09e3.jpeg)

why is it saying i got 0? please look into it.

---

### Post #248 by NIKHIL TEJA C on 2025-04-03T08:56:00.727Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/248

[@carlton](/u/carlton)

[@jivraj](/u/jivraj)
 Sir I received a mail like everyone that my git-hub repository is not public and not MIT licensed. I even filled the g-form correctly while submitting.

But I had fulfilled the above required criteria. Please look into this matter ASAP.

Here is my git repo link : [
[GitHub - 23f1001415/llm_aa_tds_project](https://github.com/23f1001415/llm_aa_tds_project)
]. (
[https://github.com/23f1001415/llm_](https://github.com/23f1001415/llm_)

[![Screenshot (390)](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/2/a2b81c003a14d06f5359d4e97e908dd4d87665f7_2_690x388.png)

> **Image Description**: Here's a concise and factual description of the image:

The image is a screenshot of a Gmail inbox. An email is open, titled "Project 1 Prerequisite evaluations". The email contains information about requirements for Project 1, including:

*   **Prerequisites:** The project requires passing certain checks detailed on the "TDS Project 1: Evaluation page". These checks include having a publicly accessible GitHub repository, a LICENSE file, a valid Dockerfile, a publicly accessible Docker image that runs via a specific podman command, and ensuring the Docker image uses the same Dockerfile as in the GitHub repository.
*   **Evaluation Results:** The email lists evaluation results for specific prerequisites:
    *   Docker image present in dockerhub AND is public: PASS
    *   Github repo present AND public: FAIL
    *   Dockerfile present in root of github repo: FAIL
    *   MIT license present at root of github repo: FAIL
*   **Overall Result:** Prerequisites: FAIL, Project 1 Score: 0.
Screenshot (390)1920×1080 266 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/2/a2b81c003a14d06f5359d4e97e908dd4d87665f7.png)

[![Screenshot (391)](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/1/915ae521873c3a286c2e898ddc8d33881ff5969e_2_690x388.png)

> **Image Description**: Here's a concise description of the image for a Tools in Data Science student:

The image is a screenshot of a GitHub repository named "llm_aa_tds_project".  It displays the file structure of the project, including files like `app.py`, `datagen.py`, `evaluate.py`, `tasksA.py`, `tasksB.py`, `Dockerfile`, `.env`, `README.md`, `LICENSE`, `dockerignore`, and a `data` directory.  The commit history shows "Initial commit with Dockerfile and application code" repeated for several files. The project's "About" section is empty. The repository's language breakdown is shown as Python 98.4% and Dockerfile 1.6%.
Screenshot (391)1920×1080 208 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/1/915ae521873c3a286c2e898ddc8d33881ff5969e.png)

aa_tds_project).

I have attached screenshots for your reference.

Thank you

---

### Post #249 by Pradeep Mondal on 2025-04-03T09:27:48.605Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/249

[@Jivraj](/u/jivraj)
 I too had the same issue (image was run on wrong architecture) and filled the gform that was circulated. When should we expect to get our scores?

Thanks

Pradeep Mondal

---

### Post #250 by Jivraj Singh Shekhawat on 2025-04-03T09:32:07.849Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/250

Hi
[@21f2000709](/u/21f2000709)

We have used another approach because of architecture problem, by pulling through latest commit from github before 18th feb. Just checked we have results for you.

---

### Post #251 by Jivraj Singh Shekhawat on 2025-04-03T09:33:34.669Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/251

Hi
[@23f1001415](/u/23f1001415)

This was a problem from our side and we rechecked and now we score against your submission.

---

### Post #252 by Jivraj Singh Shekhawat on 2025-04-03T09:36:01.806Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/252

Hi
[@23f1001524](/u/23f1001524)

This was a problem from our end, we have recitified it your submission was valid.

---

### Post #253 by Jivraj Singh Shekhawat on 2025-04-03T09:37:05.156Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/253

Your latest score through pulling from github and building image thorugh dockerfile have higher score than these 2.

---

### Post #254 by Jivraj Singh Shekhawat on 2025-04-03T09:43:47.672Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/254

Hi
[@23f2004563](/u/23f2004563)

I checked we have scores against your submission.

---

### Post #255 by Jivraj Singh Shekhawat on 2025-04-03T09:45:32.643Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/255

There was some problem with our script, later we correct and your submission was valid, I have just checked and confirm you.

---

### Post #256 by Aarush saxena  on 2025-04-03T09:48:41.922Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/256

Can u pls share marks :') dying with curiosity

---

### Post #257 by Jivraj Singh Shekhawat on 2025-04-03T09:49:46.945Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/257

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d5e2932465ab30873ba0e0d597c29da8049ac05_2_690x92.png)

> **Image Description**: Here's a description of the image:

The image shows a table containing data related to a student's project, likely for a data science course. The table includes the following columns:

*   **Timestamp:** The date and time of the entry (2/16/2025 20:39:53).
*   **Email Address:** The student's email address (23f1000057@ds.study.iitm.ac.in).
*   **GitHub Repository Link:** A link to the student's GitHub repository containing the code for Project 1 (https://github.com/Vedant22042004/project).
*   **DockerHub Image Name:** The name of the image published on DockerHub (vedant22042004/project).

The image also shows a search bar, which has been used to find the student in question, who is under the student id 23f1000057@ds.study.iitm.ac.in.
image1841×248 24.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/d/6d5e2932465ab30873ba0e0d597c29da8049ac05.png)

This was your submission and we could not locate a docker repo against it.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/2/12102c6f548ec1535363f91201441acbc019a484_2_690x336.png)

> **Image Description**: The image shows a "404" error page on Docker Hub, with the URL indicating a project called "vedant2204". The error message "Oops! The page you have requested was not found" is displayed. The interface includes a search bar labeled "Search Docker Hub" and navigation options for "Explore" and "My Hub". Other features visible are Ctrl+K, Updates, and a user avatar.
image1885×918 92 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/2/12102c6f548ec1535363f91201441acbc019a484.png)

---

### Post #258 by Jivraj Singh Shekhawat on 2025-04-03T09:54:19.130Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/258

Your submission was valid there was some issues with our script for checking. But after building your image after pulling github repo, it didn’t one
taskA
 module was missing.

---

### Post #259 by Jivraj Singh Shekhawat on 2025-04-03T09:57:36.781Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/259

If you used openai’s python module then you were needed to pass your own api key, hardcode it in code.

API key that we were sending was only valid through proxy server created by professor anand.

---

### Post #260 by Jivraj Singh Shekhawat on 2025-04-03T09:58:24.485Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/260

mail will be sent by either today or tomorrow.

---

### Post #261 by S Smriti on 2025-04-03T09:59:02.115Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/261

any idea on this sir?..

---

### Post #262 by Jivraj Singh Shekhawat on 2025-04-03T10:06:24.597Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/262

No we pulled through github and build image on gcloud vm. Anyone with valid submission didn’t receive mail, your submission was valid.

---

### Post #263 by S Smriti on 2025-04-03T10:08:07.339Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/263

but my evaluation log file was missing… so that would make it a 0 right..I have accepted my fate that it would be a 0 but just a lil hope
![:melting_face:](https://emoji.discourse-cdn.com/google/melting_face.png?v=14)

---

### Post #264 by Jivraj Singh Shekhawat on 2025-04-03T10:11:36.623Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/264

We reevaluated and found your submission was valid but it was running on a different port, 5000 but it was expected to run on 8000 port.

---

### Post #265 by S Smriti on 2025-04-03T10:12:22.800Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/265

oh so… is it going to be considered? like will i get some score other than a 0… am sorry for asking so much

---

### Post #266 by Jivraj Singh Shekhawat on 2025-04-03T10:13:15.214Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/266

No it won’t be considered. It was supposed to be running on 8000 port.

---

### Post #267 by S Smriti on 2025-04-03T10:13:56.338Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/267

Ok got it. Thank you so much
![:cry:](https://emoji.discourse-cdn.com/google/cry.png?v=14)

---

### Post #268 by Syed Zakiyuddin on 2025-04-01T16:57:54.024Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/268

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a9cdf3350a4eeebd0363ccf02a341ca2dce1716f_2_690x290.png)

> **Image Description**: The image shows a Docker Hub repository page for "zakiy7/my-fastapi-app". The "Tags" tab is selected, displaying the "latest" tag with details like:

*   **Last Pushed:** About 1 month ago.
*   **Digest:** 740fcf3f65bb.
*   **OS/ARCH:** linux/amd64.
*   **Last Pull:** 5 days.
*   **Compressed Size:** 261.49 MB.
*   **Pull Command:** docker pull zakiy7/my-fastapi-app:latest.
image1867×787 43.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/9/a9cdf3350a4eeebd0363ccf02a341ca2dce1716f.png)

Hi sir, my Architecture says amd64, in the google docs I have selected x86, i hope it is correct. Also,  I have used podman to test the pull and its working well. Please let me know if i need to do anything else.

[@carlton](/u/carlton)

---

### Post #269 by Carlton D'Silva on 2025-04-02T16:07:20.865Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/269

We are rebuilding all docker submissions from github commit before 18th of Feb, using your Dockerfile manifest present in the repo.

That way there is no architecture issues.

Its part of our secondary check. And more students have gotten scores in this  check. So dont worry.

---

### Post #270 by S Smriti on 2025-04-03T10:27:21.369Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/270

I just checked from my side also, wow a very dumb mistake now costing me a 0…should have read the project document more clearly
![:cry:](https://emoji.discourse-cdn.com/google/cry.png?v=14)
 So sorry for asking.

Am assuming no lenient correction can be done for that? like during the evaluation …

podman run --rm -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:5000 $IMAGE_NAME

---

### Post #272 by Saini Nirmal on 2025-04-03T10:40:03.358Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/272

[![Screenshot 2025-04-03 160336](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/c/4c563983c5ccd623597938159d4356f9857f2dd8_2_690x466.png)

> **Image Description**: Here's a concise and factual description of the image:

The image is a screenshot of a GitHub repository named "llm-automation-agent" owned by user "23f1002643." The repository is on the "main" branch, has 1 branch and 0 tags. The latest commit, by "23f1002643," was "Add files via upload" 2 months ago and has 4 commits.  The repository contains the following files:
- _pycache_
- Dockerfile
- LICENSE
- README.md
- app.py
- datagen.py
- evaluate.py
- requirements.txt
- tasksA.py
- tasksB.py
Screenshot 2025-04-03 1603361373×928 80.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/c/4c563983c5ccd623597938159d4356f9857f2dd8.png)

I checked it multiple times before submitting, I got 9/10 in task A.

---

### Post #273 by Jivraj Singh Shekhawat on 2025-04-03T10:49:04.701Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/273

No. Because someone else might have another minor issue they want to fix. We have to apply the rule uniformly.

---

### Post #274 by S Smriti on 2025-04-03T10:55:10.291Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/274

Ok… I do have a doubt tho, i actually have app.py and main.py in my github, my main.py is running on 8000 and app.py on 5000 …

---

### Post #275 by Jivraj Singh Shekhawat on 2025-04-03T11:00:44.378Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/275

but in Dockerfile in your github repo you didn’t run main.py,

---

### Post #276 by Jivraj Singh Shekhawat on 2025-04-03T11:02:19.716Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/276

In your Dockerfile you didn’t copy taskA.py to the container.

---

### Post #277 by S Smriti on 2025-04-03T11:04:16.031Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/277

Ouch, ok sir… hopefully project 2 doesnt disappoint
![:sob:](https://emoji.discourse-cdn.com/google/sob.png?v=14)

---

### Post #278 by Swati Kapoor on 2025-04-03T12:01:40.520Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/278

It is there in the master branch of the repository. Now, will the previous evaluation mail that we got be considered or this one?

---

### Post #279 by Khushi Dhankhar on 2025-04-03T16:52:22.629Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/279

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

I recently received an email with an evaluation file for Project 1, which included a score. However, in the recent email, I noticed that my score was recorded as zero, despite fulfilling all the prerequisites.

I kindly request a re-evaluation of my project, as I believe this may be an error.

---

### Post #280 by AYUSH SINGH on 2025-04-03T17:50:50.831Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/280

[@Jivraj](/u/jivraj)

My discrepancy is still not fixed. Please take a look at it

---

### Post #281 by SP on 2025-04-03T18:35:09.380Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/281

[@Jivraj](/u/jivraj)

Hlo, could you please check and let me know how much am I scoring in Project 1 after the latest evaluation?

---

### Post #282 by Gaurav Ghodge on 2025-04-04T05:21:02.368Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/282

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

Sir,

In the mail that i got about project 1 report. In the log file it was written as TasksA.py file not found in docker, which was the case i observed with many students.

[![Screenshot 2025-04-04 at 10.31.02 AM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/968890ec5cffbca81bafeef7181db1173e1a6528_2_690x460.png)

> **Image Description**: The image shows the output of a Python script execution, indicating a `ModuleNotFoundError`. The error message "No module named 'tasksA'" indicates that the Python script, located at `/app/app.py` line 22, attempts to import a module named `tasksA`, which is not found in the current environment. Prior to the error message, the output displays the installation of several Python packages (antiorm, db, db-sqlite3, scipy, pandas, numpy, pydantic-core, and duckdb) and their successful download and build, culminating in the installation of 33 packages in 56ms.
Screenshot 2025-04-04 at 10.31.02 AM1358×906 47.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/6/968890ec5cffbca81bafeef7181db1173e1a6528.png)

This is my Github repo:

[![Screenshot 2025-04-04 at 10.44.24 AM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/c/0ce93452fedd6a15660a312186ed7f3b3a10a39e_2_690x372.png)

> **Image Description**: The image is a screenshot of a GitHub repository named "tds-project1" owned by "GaURaVinDeX". It displays the code tab of the repository, showing the main branch with the following files: '__pycache__', '.gitignore', 'Dockerfile', 'LICENSE', 'app.py', 'requirements.txt', 'tasksA.py', and 'tasksB.py'. Each file has an "Initial commit" message and was last updated "2 months ago". The repository's "About" section indicates no description, website, or topics have been provided. The repository has an MIT license, 0 stars, 1 watcher, and 0 forks. A section promotes adding a README file. The languages used are Python (98.0%) and Dockerfile (2.0%).
Screenshot 2025-04-04 at 10.44.24 AM3324×1794 497 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/c/0ce93452fedd6a15660a312186ed7f3b3a10a39e.png)

I built the image using docker build command in vs code terminal. And pushed it same way to dockerhub using docker push command. How is it possible that the docker container missed the TasksA.py file while building or pushing it?

After getting this mail, I ran the project locally again mutliple times just to check if there was any issues in the code. It was getting 9/10 test cases passed.

---

### Post #283 by Carlton D'Silva on 2025-04-04T05:46:33.814Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/283

This is a common mistake many, many students made. They created a working application but not a working container.

[![Screenshot 2025-04-04 at 11.13.32 am](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e_2_690x493.png)

> **Image Description**: This image shows a `Dockerfile` for a Python application. The Dockerfile starts with the `python:3.12-slim-bookworm` image. It then installs dependencies using `apt-get`, downloads and installs `uv` (likely a tool or library), installs FastAPI and Uvicorn using pip, and sets the PATH environment variable.  The working directory is set to `/app` and the `app.py` file is copied into the `/app` directory in the Docker image. Finally, it specifies the command to run the application using `uv`.
Screenshot 2025-04-04 at 11.13.32 am2116×1512 323 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/040ebf28145e23dec6db3e1a742f886299a5170e.png)

You only copied
app.py
 into your docker image.

How do you expect your application to run without the other files that your repo clearly shows is needed?

Thats why many people are failing this. Hope the image makes this clear.

Kind regards

---

### Post #284 by Aryan Kumar on 2025-04-04T05:53:01.165Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/284

[![1000050348](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f56ad9b52eb9d732629f1a36b7353194cf6acd9e_2_230x500.jpeg)

> **Image Description**: Here's a concise description of the image for a Tools in Data Science student, focusing on the visible content:

The image shows an email related to "Project 1" prerequisites.  It lists the following requirements for a GitHub repository:

1.  Public accessibility.
2.  Presence of a LICENSE file with the MIT license.
3.  A valid Dockerfile.
4.  Publicly accessible Docker image that runs via podman.
5.  Docker image using the same Dockerfile as in the GitHub repository.

The email then shows the results of a prerequisite evaluation. It indicates "PASS" for:
*   Docker image present in dockerhub AND public.
*   Github repo present AND public.
*   Dockerfile present in root of github repo

It indicates "FAIL" for:
*   MIT license present at root of github repo.

Consequently, the overall "Prerequisites" status is "FAIL," and the "Project 1 Score" is 0.
10000503481080×2340 154 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f56ad9b52eb9d732629f1a36b7353194cf6acd9e.jpeg)

[![1000050349](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/031fb8ca7808375905f4725bba8fa6e38751802d_2_230x500.jpeg)

> **Image Description**: The image shows a GitHub repository named "00-Aryan". It is a public repository with 0 stars, 0 forks, and 1 watcher. It has 1 branch and 0 tags. The repository contains several files and directories:
- __pycache__
- data
- .env
- Dockerfile
- LICENCE
- app.py
- datagen.py
- evaluate.py
- requirements.txt
- tasksA.py
- tasksB.py
- README with an MIT license.
All the files and directories were last updated 2 months ago.
10000503491080×2340 190 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/031fb8ca7808375905f4725bba8fa6e38751802d.jpeg)

I am getting license not present at root of github repo but i have the license added could someone please explain why ?

---

### Post #285 by Carlton D'Silva on 2025-04-04T06:06:04.491Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/285

[@thinkmachine](/u/thinkmachine)

Firstly, you have passed evaluation and got a decent score (on a more lenient script that we used for everyone.) The email was sent by a script that used a more stricter evaluation (which understandably caused some stress). So you can breathe a sigh of relief.
![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=14)

However
 with regards to your long post…

Let me tell you a true story. I personally know a
very
 experienced senior engineer at a top defense contractor for the US, here is some pearls of wisdom from him.

What you have done is what is called in industry as
gold plating
. Its a cardinal sin in software engineering. NEVER gold plate. ALWAYS build to spec.

In fact its a good reason to fire an engineer. Why?

Because it does not deliver what was required,

Wastes valuable time and resources

Increases technical debt (this is actually a huge cost over the expected lifetime of the project!)

Complicates testing

Leads to scope creep

His advice to me was simple: NEVER gold plate.

I hope you take this pearl of wisdom in your career. It will help you advance and make you stand out.

For personal hobbies this does not apply. But for a client (including us) if you fail to deliver the minimum spec then we cannot grant you an evaluation (by the way this post is not targetted specifically for you, it just felt like an appropriate place to explain this).

Kindest regards

---

### Post #286 by Abhay Mehra on 2025-04-04T08:04:19.957Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/286

Hi Sir,

I just realized that I mistakenly submitted the image tag “abhay227/version1” instead of the correct image ID. The correct image ID is
4db729a03f74
 , which is part of version1 that is already present and publicly available.

I have worked very hard on this project, and I am concerned that due to this error, my whole effort may be wasted. Unfortunately, I did not receive any notification regarding an invalid submission after I submitted the Project1 form, and I only recently became aware of this mistake. I kindly request you please consider this correct image ID.

Thank you for your understanding and assistance. I look forward to your positive response.

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[![Screenshot 2025-04-02 132214](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_690x93.png)

> **Image Description**: Here's a description of the image for a Tools in Data Science student:

**Content:**

The image is a screenshot of a Docker image repository entry.  It displays metadata about a specific image tagged as "version1".

**Key Information Displayed:**

*   **Tag:** "version1"
*   **Last Pushed:** About 1 month ago by "abhay227"
*   **Digest:** "4db729a03174" (a unique identifier for the image)
*   **OS/ARCH:** "linux/amd64" (the operating system and architecture the image is built for)
*   **Last Pull:**  Approximately 1 month ago
*   **Docker Pull Command:** "docker pull abhay227/tds\_project:version1" (The command to download the image).
*   **Compressed Size:**  261.98 MB
Screenshot 2025-04-02 1322141843×250 18.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1.png)

---

### Post #287 by Carlton D'Silva on 2025-04-04T09:06:11.401Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/287

Hi Abhay,

This was a basic error. Unfortunately for basic errors we are not able to relax the requirements. All students were given a clear directive on what the minimum requirements were in order to be evaluated. Failure to follow those clear instructions prevents us from making any exceptions, because then we just have to dump all those requirements for all students and that would not be fair to those that took the care to be careful about their submissions.

Kind regards

---

### Post #288 by SP on 2025-04-04T21:47:18.782Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/288

Hi sir, hope you are doing well.

Could you please check and let me know if I have passed the project 1 and if yes then how much am I scoring in Project 1 after the latest evaluation?

[@carlton](/u/carlton)

---

### Post #289 by Shreyan Chaubey on 2025-04-04T22:16:43.757Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/289

Thanks for the clarification regarding the evaluation,
[@carlton](/u/carlton)
. It’s a relief to know that my original submission was successfully evaluated. Had I known that the stricter evaluation script would pull the image matching the digest from the time of submission (which had been overwritten by April 1), I would’ve used a separate tag to avoid the issue altogether.

Regarding your point on gold plating — I completely understand and have come to appreciate the importance of building to spec from personal experience, especially in production or client-facing settings where fixed targets, maintainability, and minimal scope creep are key. That said, with TDS projects, my goal was purely exploratory — to explore the boundaries of what’s possible
within the scope of the problem statement
.

What began as just another (pun intended)
tedious
 assignment slowly evolved into a hobbyist research project on LLM agents.
![:grinning_face_with_smiling_eyes:](https://emoji.discourse-cdn.com/google/grinning_face_with_smiling_eyes.png?v=14)

(…caution: long post ahead
![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=14)
)

I noticed that
test cases in Project 1 and 2 were highly specific and often overlapping on Python & Shell use
. While it would’ve been easy to hardcode 50+ Python functions to pass these cases (which, frankly, many of us were doing), it is non-scalable at best. I quickly realized that stochastic parrots + hardcoded functions were a recipe for disaster, especially considering the
inherent randomness in LLM-generated payloads
. No two payloads are exactly alike — even minor differences, like an absolute vs relative file path, or some hidden edge case could cause a hardcoded solution to fail unpredictably. There’s also really no way to predict an edge case caused by an LLM.

Some might suggest using
temperature=0
 to get more deterministic LLM behavior — and while true to an extent, it does little to encourage exploration, especially in tasks that require self-correction based on environmental feedback. Prompt engineering too wouldn’t be helpful here as 4o-mini isn’t all that great at 0-shot instruction following, especially when the system prompt is already saturated with 50+ fine-grained instructions. There’s only so much stuff it can pay attention to.

Hardcoded tool agents also aren’t really “agents” in my view— they’re more like passive AI powered regex matchers
: merely mapping inputs to functions by inferring from context window. That puts all the burden of answering on the hardcoded functions, leaving the agent itself uninvolved in the solutioning process. If they break, the agent will never try to ‘fix’ them and keep calling them like a broken record.

At the core of it, it’s all about
how much flexibility vs rigidity
 we give to the agent. Fully rigid solutions (e.g. hardcoding) overfit and break easily; fully flexible ones (e.g. pure LLM based) hallucinate or drift off-target. The sweet spot lies somewhere in between — The right solution would naturally balance the lesser of two evils in an ideal ratio.

Since most LLMs already excel at code generation and structured solutioning, the most effective strategy that I figured out for the agent was to,

Reason about the task, understand intent,

Reflect, whether this problem is solvable using available tools without human intervention and design structured workflows, in whatever order appropriate (i.e.
design
 a DAG, where each node can be a python step or a shell step or something else)

Execute those workflows (
walk
 the DAG) observing the feedback at each step and reiterating if needed.

Observe the final result, and repeat if needed.

Interestingly, a similar framework was suggested in
[this ICLR 2022 paper](https://arxiv.org/abs/2210.03629)
. That was all the validation I needed to know I was stepping in the right direction.

To make environment interaction possible, the agent didn’t need dozens of narrow tools — just a small, well-defined set of
general-purpose tools
:

A REPL executor (for quick calcs)

A Python script runner

A Shell executor

With just these, it could handle most tasks flexibly and naturally — avoiding overengineering while still enabling powerful behaviors. Potentially allowing for full fledged Computer-Use via shell and so much more.

As for the fact that it ended up being capable of things beyond the scope of Project 1 (like training & tuning ML models autonomously, reporting results etc.) — that was
emergent behavior
, not deliberate gold plating. It was a pleasant surprise even to me. I’ve yet to discover more of such interesting hidden use cases. While some might naturally call it scope creeping (and yes that is true, given that we had a deadline, and a play-pretend client-business relationship with the course team), I saw it as an opportunity for exploration and research.
Frankly, I AM personally very keen about researching stuff!

I am actually very thankful to the TDS course team &
[@s.anand](/u/s.anand)
 for devising such a thoughtful project that sparked some interesting ideas that I can tinker with.
Food for thought! Really!

As for my next project, I now have a fair idea of what I’ll be experimenting with— modalities.

PS: I’m not claiming it’s perfect or production-ready, or it should score a perfect 22/20, but it aligned well with what I believe was the spirit of these projects:
thoughtful use of LLMs in agent design
. At this point, I’m less concerned about the marks, I’m actually enjoying the thought joyride.
![:grinning_face_with_smiling_eyes:](https://emoji.discourse-cdn.com/google/grinning_face_with_smiling_eyes.png?v=14)

TL;DR

My approach doesn’t rely on regex or hardcoded mappings. Instead, it passes user input directly to an LLM, which then plans and executes workflows using general tools inside a containerized environment. It also learns from feedback and iterates — much like a human. The fact that it can do more than just the minimum spec is a byproduct of that framework. I’ve only just wired the pieces together.

Kind regards

---

### Post #291 by Vansh Mittal on 2025-04-05T07:12:52.908Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/291

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)
  Sir please Consider this request!

---

### Post #292 by Srishty on 2025-04-05T13:32:19.021Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/292

Hello Sir,

[![Screenshot_2025-04-05-18-51-43-721_com.google.android.gm](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/5/05553623c126727b31b481bf5da4faedb58f8405_2_225x500.jpeg)

> **Image Description**: Here's a concise and factual description of the image:

The image is a screenshot of an email regarding project prerequisites for a Tools in Data Science course. It lists requirements like having a public GitHub repository with a LICENSE file and a valid Dockerfile. It states that the Docker image must be publicly accessible and use the same Dockerfile as the GitHub repository.

The email also shows the results of prerequisite evaluations:
- Docker image is present and public: PASS
- GitHub repo present and public: FAIL
- Dockerfile present in the root of the repo: FAIL
- MIT license present in the root of the repo: FAIL

The email indicates that the prerequisites are not met, resulting in a score of 0 for Project 1.
Screenshot_2025-04-05-18-51-43-721_com.google.android.gm1080×2400 144 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/5/05553623c126727b31b481bf5da4faedb58f8405.jpeg)

I got this mail regarding my project 1 scores. My github repo is present and public as well as MIT License and Dockerfile  is also present at the root of the repo

[github.com](https://github.com/SrishtySnehi/Project_1_tds)

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/9/f93c7a8f75b0e5f3c99be032499e49464d57c7a2_2_690x344.png)

> **Image Description**: The image shows a GitHub repository named "SrishtySnehi/Project_1_tds". It has 1 contributor, 0 issues, 0 stars, and 0 forks. The repository icon depicts a red cross-like symbol.

[GitHub - SrishtySnehi/Project_1_tds](https://github.com/SrishtySnehi/Project_1_tds)

Contribute to SrishtySnehi/Project_1_tds development by creating an account on GitHub.

---

### Post #293 by Jivraj Singh Shekhawat on 2025-04-05T13:43:36.526Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/293

Hi
[@Srishty_Snehi](/u/srishty_snehi)

Your submission is valid, we but it failed while running server, with this error.

taskA module missing

For regenerating this error:

Pull github repo(latest commit before 18th Feb)

Build image using Dockerfile of fetched repo

Run that image.

---

### Post #294 by Jivraj Singh Shekhawat on 2025-04-05T13:45:08.530Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/294

We are not considering Dockerfile’s with wrong name(anything other than Dockerfile), and wrong location(anything other than root) in github repo.

---

### Post #295 by Srishty on 2025-04-05T13:52:15.950Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/295

Will I still get a zero?

---

### Post #296 by S Smriti on 2025-04-05T15:04:50.084Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/296

Can we expect the results for project 1 and 2 by tomorrow?
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #297 by Aarush saxena  on 2025-04-05T16:02:30.289Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/297

when can we expect our project 1 result?

[@Jivraj](/u/jivraj)

---

### Post #299 by S Smriti on 2025-04-06T10:10:34.222Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/299

I got my result!! 2/20 so happy its not a 0 thank you for the bonus
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

![:sob:](https://emoji.discourse-cdn.com/google/sob.png?v=14)

Also really great how yall have given the error logs for everyone individually
![:saluting_face:](https://emoji.discourse-cdn.com/google/saluting_face.png?v=14)

---

### Post #300 by Shubham Atkal on 2025-04-06T10:19:54.144Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/300

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)
 in earlier evaluation of P1 in that my B1 is passed but in this final scores email it is showing as 0 for B1 pls help

![finalB1](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/04980bbcf7941e08ba08f59e10a384708518a9eb.png)

> **Image Description**: Here's a concise description of the image:

The image shows a snippet of a table or spreadsheet. The cell labeled "B1" contains the value "0".

[![b1passed](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/3/53a192933345964a58001aea8268e62a2e03e5f0_2_690x87.png)

> **Image Description**: The image shows a log output indicating the progress of a data manipulation task. First, "B1 PASSED" indicates a successful initial step. Then, a task is running to delete the file "/data/format.md". Finally, an HTTP POST request is shown targeting the URL http://localhost:8325/run?task=Delete+%2Fdata%2Fformat.md, with the server responding "HTTP/1.1 200 OK", signifying a successful operation.
b1passed1109×141 12.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/3/53a192933345964a58001aea8268e62a2e03e5f0.png)

---

### Post #301 by HariOm Pandey on 2025-04-06T10:21:36.138Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/301

Request for Clarification on Zero Marks Given – Repository Was Public with All Required Files

Dear
[@Carlton](/u/carlton)
 sir

I wanted to kindly request a clarification regarding the evaluation of my project submission. I noticed that I have been awarded zero marks, and I’m a bit confused because I had made sure that everything was in place.

My GitHub repository was
public
 at the time of submission.

I had included the
Dockerfile
 as required.

I also added the
MIT License
 to the project.

For your reference, I am also attaching a
snapshot
 of the repository as it was during the submission time.

Given all these were in place, I would really appreciate it if you could provide a
concrete reason
 for giving
zero marks
. I’m eager to understand what went wrong so I can avoid it in the future and improve myself. But u saying in email that my repo was not public , not having dockerfile and not having mit licsence .

[![emailsnapshotfor_discourse](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/e/8e3c9683970a3d0b4da1305c4b85a634f235f437_2_690x369.png)

> **Image Description**: Here's a concise and factual description of the image for a student in a Tools in Data Science course:

The image is a screenshot of a Gmail inbox. The email contains information about project grading. Key elements are:

*   **Task Scoring:** A point system for tasks A1-A10, B1-B10, and bonus tasks C1-C5.
*   **Total Score:** The total possible score is 20.
*   **Normalization:** Task scores are normalized based on a maximum score of 16 from Project 1.
*   **Bonus:** Awarded for the number of commits and repo size, scaled with a power transform (weight of 2.5).
*   **Final Score:** The final score is calculated as the minimum of 20 and (task score + bonus).
*   **Repository Links:** Github and Docker repository links are provided.
*   **Prerequisites Check:** Pass/fail criteria based on repository properties (existence, public access, timestamps, LICENSE file, Dockerfile).
*   **Table:** A table displays scores, with labels A1-A10 and B1-B10 all set to zero.
emailsnapshotfor_discourse1785×957 130 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/e/8e3c9683970a3d0b4da1305c4b85a634f235f437.png)

[![repo_snapshotforDiscourse](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/a/6a6a5cdd6a3ef7b88e3a82742621e730b10c68dd_2_690x362.png)

> **Image Description**: The image shows a GitHub repository named "tds_llm_automation-agent" owned by "harrypandey829". It's a public repository with an MIT license. The repository contains various Python files (app.py, datagen.py, evaluate.py, tasksA.py, tasksB.py), a Dockerfile, a .env file, a LICENSE file, a README file, and a _pycache_ directory. The project has 0 stars, 0 forks, and 1 person watching. The "About" section states: "This is my final effort towards tds project." The repository has 3 commits. The project's language is 100% Python.
repo_snapshotforDiscourse1842×968 84.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/a/6a6a5cdd6a3ef7b88e3a82742621e730b10c68dd.png)

please just check my repo  manually  and clarify whether it was public or not . What is going on this degree .

---

### Post #302 by HariOm Pandey on 2025-04-06T10:25:14.903Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/302

And also i ran the evaluate.py and got the 10/10 during submission , atleast you can give 4-5 by which i can pass this course .

---

### Post #303 by Arun Vembu S on 2025-04-06T10:27:58.037Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/303

Hi sir

I noticed a discrepancy in my Project 1 results. In the initial results shared on March 29th, I had received 8/20 based on the evaluation logs. However, the final result I received today states that none of the tasks in Task A and B were working, and I was awarded only 1 bonus mark.

During my own testing, I was consistently getting 7/10 correct in Task A, so I’m a bit confused about the change.

Kindly request you to look into this discrepancy sir

Thank you

---

### Post #304 by Gautam Ashish Goyal on 2025-04-06T10:28:00.542Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/304

Dear
[@carlton](/u/carlton)
 Sir,

I was getting 8 marks in your evaluation but today I checked the mail, I was awarded 0 marks. I am not sure what happened. Everything was in place. I would really appreciate if you can provide a reason for zero marks. I rechecked everything and looks good. Awaiting your reply. Thanks.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/999d8f9a8df3be1555d6c16db66daa5d56bbed93.png)

> **Image Description**: The image displays computer code with the following information:
- BIO FAILED
- Score: 8 / 20
- HTTP Request: POST https://aipro
image452×132 6.53 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/9/999d8f9a8df3be1555d6c16db66daa5d56bbed93.png)

---

### Post #305 by Bharat Choudhary on 2025-04-06T10:39:13.548Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/305

same i also got 8 marks but today in mail i got 0 marks

---

### Post #306 by Abhishek on 2025-04-06T10:46:30.789Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/306

Same issue for me, I was getting 10/20 earlier and now, in mail it shows 1.

---

### Post #307 by Adarsh kumar on 2025-04-06T10:56:01.110Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/307

Same issue for me, i had got 4/20 before but in the mail, my marks is given as 0. Please help

---

### Post #308 by Anisha Seth on 2025-04-06T11:08:05.832Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/308

Respected sir,

I have passed all pre-requisites however my file wasn’t evaluated due to port error (127.0.0.1). Please allow me rectify it as it everything else has passed and is in accordance to the guidelines and I had worked really hard for it not to be evaluated only.

---

### Post #309 by Bingi Sai Mohith on 2025-04-06T11:09:50.310Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/309

Dear
[@carlton](/u/carlton)
 Sir,

I’ve noticed discrepancies in my Project 1 results. During the tests I ran before submitting, I consistently got about 7/10 in Task A. In the results shared earlier, I was informed that my evaluation log file was missing. Later, a Gform regarding the architecture was sent, which I filled and submitted. Now, the final result I received today, shows that the taskA module is missing and I’ve been given a bonus of 1 mark.

I kindly request you to look into the matter and provide an explanation and solution in this regard.

Thank you.

---

### Post #310 by Santosh Sharma on 2025-04-06T11:56:39.048Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/310

Respected Sir,

I hope you’re all doing well. I’m writing regarding my Project 1 evaluation, as I’ve encountered a discrepancy that I’d like some help with.

According to the evaluation email I received, my score was 0 for all the tasks with an additional bonus of 1 (totaling a P1 score of 1). However, when I ran the provided evaluation script before my submission, I got 7 in Phase A. Additionally, after reviewing the Docker logs, evaluation logs, and the p1_evaluation_error_logs (from the linked Google Sheets), I couldn’t find any reference to my roll number.

Could someone please help me investigate this issue? I’d really appreciate any guidance from the evaluation team.

Thank you for your time and assistance!

---

### Post #311 by Kartikay Taunk on 2025-04-06T11:57:17.109Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/311

[@carlton](/u/carlton)
 i am sure i had cleared 8/10 test cases in part A of the project despite rigrous checking and no error was found my be but still i have been alloted 0 in all the cases , this is no small issue as project holds a significant amount of weightage in the end term

I had spent hours finishing my project and this i am sure my marks are not on par with the desired work i did

Look into this matter as it signifies if i will be able yo pass tds in this term or not.

---

### Post #312 by Kartikay Taunk on 2025-04-06T11:58:19.746Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/312

I am facing the exact same issue

---

### Post #314 by Carlton D'Silva on 2025-04-06T12:03:01.767Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/314

Hi Hari,

I just
manually
 checked your repo.

[![Screenshot 2025-04-06 at 5.32.06 pm](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559_2_690x436.jpeg)

> **Image Description**: The image shows a GitHub 404 error page. The URL in the browser address bar is "https://github.com/harrypandey829/tds_llm_automation-agent". The page displays a "404" error message along with the text "This is not the web page you are looking for." There is also an illustration of a cartoon character.
Screenshot 2025-04-06 at 5.32.06 pm1504×952 62.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559.jpeg)

This is what
you
 submitted:

2/15/2025 21:08:32

21f3002112@ds.study.iitm.ac.in

[https://github.com/harrypandey829/tds_llm_automation-agent](https://github.com/harrypandey829/tds_llm_automation-agent)

hariompandey6388/ll-automation-agent2

Kind regards

---

### Post #315 by Avinash Kumar on 2025-04-06T12:16:09.978Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/315

[@carlton](/u/carlton)
  sir  When I submitted project 1, I was passing part A with 8/10 marks but today it is showing 0 marks on my email, but when I run it just now it is showing 4/10 on my vs code.

Whereas when I download the file from GitHub and run it, it is showing 1/10 now.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/d/9d7495b7d3d112adfac7d592ee6e9024351dc618_2_690x351.png)

> **Image Description**: The image displays a code editor (likely VS Code) with multiple Python files open: `app.py`, `datagen.py`, `evaluate.py`, `tasksA.py`, and `tasksB.py`. The `app.py` file shows a script with dependencies listed. The terminal output indicates a failed test "A10," where an expected value of 177250.79 was not equal to the actual result of 200401.84. The test pertains to querying a SQLite database file `/data/ticket-sales.db` for the total sales of "Gold" type tickets. The HTTP request shown is GET `http://localhost:8000/read?path=/data/ticket-sales-gold.txt`.
image1897×965 112 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/d/9d7495b7d3d112adfac7d592ee6e9024351dc618.png)

[![WhatsApp Image 2025-04-06 at 17.28.47_927a687b](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3fe91b246d5e0f0bf26245d8b4d0ab0d074827f5_2_666x500.jpeg)

> **Image Description**: Here's a concise description of the image for a student in a Tools in Data Science course:

The image shows a laptop screen displaying code in VS Code. Multiple Python files are open, including `app.py`, `evaluate.py`, `tasksApy.3`, `tasksB.py`, `dockerfile`, and `datagen.py`. The `app.py` file imports modules like `FastAPI`, `HTTPException`, `Query`, `PlainTextResponse`, `JSONResponse`, and `CORSMiddleware`.

The terminal output section shows a failed test case, labeled "A10 FAILED," related to a task involving an SQLite database file `/data/ticket-sales.db`. The task asks for the total sales of "Gold" tickets. The expected result (177250.79) differs from the actual result (200401.84). The current score is 4/10. The prompt also makes mention of the /data/ticket-sales-gold.txt directory.
WhatsApp Image 2025-04-06 at 17.28.47_927a687b1600×1200 181 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/f/3fe91b246d5e0f0bf26245d8b4d0ab0d074827f5.jpeg)

---

### Post #316 by Carlton D'Silva on 2025-04-06T12:22:00.340Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316

To replicate the test environment:

Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv.

# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo
import argparse
import os
import zipfile

parser = argparse.ArgumentParser (description="Fetch the latest commit before a given deadline.")
parser.add_argument (
    "--owner",
    type=str,
    required=True,
    help="GitHub username."
)
parser.add_argument (
    "--repo",
    type=str,
    required=True,
    help="GitHub repository name."
)
parser.add_argument (
    "--save",
    type=str,
    default="../github/",
    help="Path to save the zip file. Default='../github/'"
)
parser.add_argument (
    "--extract",
    type=str,
    default="../github/",
    help="Path to extract the zip file. Default='../github/'"
)

args = parser.parse_args ()
owner = args.owner
repo = args.repo
save_path = args.save
extract_path = args.extract

deadline = dt.datetime (2025, 2, 18, tzinfo=zoneinfo.ZoneInfo("Asia/Kolkata"))
deadline_str = deadline.isoformat ()

github_headers = {
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "fetch_git_before",
}

url = f"https://api.github.com/repos/{owner}/{repo}/commits?until={deadline_str}&per_page=1&page=1"

try:
    response = requests.get (url, headers=github_headers, timeout=60)
    response.raise_for_status ()  # Raise an error for bad responses

    # Get the sha
    commits = response.json ()
    if commits:
        latest_sha = commits[0]["sha"]
        print (f"Latest commit before {deadline_str}: {latest_sha}")

        # Get the zip of the commit
        zip_url = f"https://api.github.com/repos/{owner}/{repo}/zipball/{latest_sha}"
        zip_response = requests.get (zip_url, headers=github_headers, timeout=60)
        zip_response.raise_for_status ()
        zip_filename = f"{latest_sha}.zip"

        # Create the directory if it doesn't exist
        os.makedirs (save_path, exist_ok=True)

        with open (save_path + zip_filename, "wb") as f:
            f.write (zip_response.content)
        print (f"Downloaded zip file: {zip_filename}")

        # Create the directory if it doesn't exist
        os.makedirs (extract_path, exist_ok=True)

        # Extract the zip file
        with zipfile.ZipFile (extract_path + zip_filename, "r") as zip_ref:
            zip_ref.extractall (extract_path)
        print (f"Extracted zip file to: {extract_path}")

    else:
        print (f"No commits found before {deadline_str}")

except:
    print(f"Error fetching commits: {response.status_code} - {response.text}")

Pass the required arguments to the above application and it will find the latest commit before the 18th, fetch it and unzip it to the folder you specified. Please use the appropriate arguments as specified in the application.

docker build -t <your image name>   .

Run new docker image using

docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 <your image name>

Keep datagen.py and evaluate.py in same folder

uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000

This then re-produces the exact environment how your application was  tested.

You have to provide a token from your environment for testing.

These instructions are same for everyone. So check first before posting here.

---

### Post #317 by Kasif khan on 2025-04-06T12:22:16.600Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/317

I am also facing same issue cleared 8/10 test cases in part A of the project despite rigrous checking and no error was found  but still i have been alloted 0 in all the cases

---

### Post #318 by Carlton D'Silva on 2025-04-06T12:28:18.259Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/318

[@Arunvembu](/u/arunvembu)

[@22f2000008](/u/22f2000008)

[@23f1000879](/u/23f1000879)

[@22f3003201](/u/22f3003201)

[@23f2000926](/u/23f2000926)

[@22f3001702](/u/22f3001702)

[@Santoshsharma](/u/santoshsharma)

[@kartikay1](/u/kartikay1)

[@Kasif](/u/kasif)

Check first by following the instructions show here:

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

[Tools in Data Science](/c/courses/tds-kb/34)

    To replicate the test environment:
git clone <your repo url>
cd <your repo directory>
docker build -t <your image name>
Run new docker image using
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 <your image name>
Keep datagen.py and evaluate.py in same folder
uv run evaluate.py --email=<any email> --token_counter 1 --external_port 8000
This then re-produces the exact environment how your application was  tested.
You have to provide a token from your environment for testing.
The…

Then post with your queries after testing as mentioned above.

Also check the evaluation logs first to see why it failed. Address that question.

Posting “it ran before submission” is insufficient evidence.

The whole point of deployability is that it runs anywhere at anytime.

That is what is being tested, not that it ran on your machine (unless you replicate the test environment exactly).

Kind regards

---

### Post #319 by HariOm Pandey on 2025-04-06T12:44:34.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/319

But in email u said n , your repo was not public, even not had dockerfile nor mit licence that’s what I mentioned.

---

### Post #320 by Carlton D'Silva on 2025-04-06T12:47:16.601Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/320

Your repo is not public! Thats why we cannot see any other files either. If its not public we cannot see if other files exist. We cannot evaluate an invisible repo.

---

### Post #321 by HariOm Pandey on 2025-04-06T12:47:43.321Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/321

I got email , your repo was not public even had not a dockerfile nor mit licence, that’ what I mentioned.

---

### Post #322 by HariOm Pandey on 2025-04-06T12:50:04.091Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/322

My repo is public even before it was. How can I set to public..thisis same n while creating new repo u just select the public and not private that’s it n.

---

### Post #323 by HariOm Pandey on 2025-04-06T12:50:21.105Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/323

What else I can do . For public.

---

### Post #324 by Carlton D'Silva on 2025-04-06T12:53:18.888Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/324

You misspelt your repo. Did you even check the post i sent with your details?

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/314)

[Tools in Data Science](/c/courses/tds-kb/34)

    Hi Hari,
I just manually checked your repo.

[[Screenshot 2025-04-06 at 5.32.06 pm]](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559.jpeg)

This is what you submitted:

2/15/2025 21:08:32
21f3002112@ds.study.iitm.ac.in

[https://github.com/harrypandey829/tds_llm_automation-agent](https://github.com/harrypandey829/tds_llm_automation-agent)

hariompandey6388/ll-automation-agent2
Kind regards

---

### Post #325 by Yashvardhan on 2025-04-06T12:58:18.421Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/325

Dear
[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
 Sir,

I run evalution  script that you provide us via mail recently, my code is actively running and able to pass 11 task but I was awarded 1 Marks pls check where is the issue,[My full code was done in linux Environment]  (github codespace)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/2/42c024fb5f0088b9a033625cd6e7338bba0c22f2_2_690x170.png)

> **Image Description**: The image shows a screenshot of a terminal or code editor. 

- There are two HTTP requests displayed:
  - A GET request to `http://localhost:8000/read?path=/data/c5.txt` which resulted in a "404 NOT FOUND" error.
  - A POST request to `https://aiproxy.sanand.workers.dev/openai/v1/embeddings` which resulted in a "200 OK" status.
- "C5 failed: Cannot read /data/c5.txt" indicating a file read error.
- The score is "11/25".
- It suggests a path: "/workspaces/Large-Language-Model".
- A dialog box is open that asks the user if they want to install the recommended "Python" extension from Microsoft.
image1380×341 63.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/2/42c024fb5f0088b9a033625cd6e7338bba0c22f2.png)

---

### Post #326 by Carlton D'Silva on 2025-04-06T13:00:28.513Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/326

You have to replicate this test environment for testing.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

[Tools in Data Science](/c/courses/tds-kb/34)

    To replicate the test environment:
git clone <your repo url>
cd <your repo directory>
docker build -t <your image name>
Run new docker image using
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 <your image name>
Keep datagen.py and evaluate.py in same folder
uv run evaluate.py --email=<any email> --token_counter 1 --external_port 8000
This then re-produces the exact environment how your application was  tested.
You have to provide a token from your environment for testing.
The…

Please replicate this first. We also run it on a linux server.

Kind regards

---

### Post #327 by HariOm Pandey on 2025-04-06T13:01:22.911Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/327

I am not talking about this , just see the snapshot that I applied above on that email u said your repo is not public

---

### Post #328 by Carlton D'Silva on 2025-04-06T13:03:31.773Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/328

We are ONLY going to evaluate what you submitted. Its the same rule for everyone. If the repo you provided is not accessible,  you will not be evaluated.

---

### Post #329 by HariOm Pandey on 2025-04-06T13:06:40.691Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/329

Okay tell me one thing if I got fail in this course then in the next term, I will have not to give roe because it’s rule for every other courses.And see provide the content of tds in Indian guy youtuber because we belong to rural areas and not able to understand the accent of foreigners youtuber . It’s kind your sympathy.

---

### Post #330 by Tushar Jalan  on 2025-04-06T13:29:44.621Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/330

Things i have done for my project to work locally:

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
 carlton:

git clone <your repo url>

cloned my repo which looked like this after cloning(ignore those green dots)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/517fe247c71c06f80741f22983662ba012749382.png)

> **Image Description**: The image shows a file explorer from a code editor, likely VS Code. The project "TDS_PROJECT_1" is open, containing a folder "tds-project-1" (currently collapsed) and a file named "LICENSE" denoted by a key icon. There are icons for "New File", "New Folder", "Refresh" and "Collapse Folders in Explorer" present above the project.
image274×118 2.87 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/517fe247c71c06f80741f22983662ba012749382.png)

All the files are  in this folder (I wasn’t aware that we cannot have the subfolder in the root directory,I shouldn’t get penalized for this) and added the datagen and evaluate.py file.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
 carlton:

Keep datagen.py and evaluate.py in same folder

when i do this(
![:down_arrow:](https://emoji.discourse-cdn.com/google/down_arrow.png?v=14)
) i get this error

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
 carlton:

docker build -t <your image name>

PS D:\TDS_Project_1\tds-project-1> docker build -t "tushar2k5/tds-project-1"
ERROR: "docker buildx build" requires exactly 1 argument.
See 'docker buildx build --help'.

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Start a build

Instead,in order to run the docker image successfully  we have to do either of the two things(taken help from chatgpt
![:upside_down_face:](https://emoji.discourse-cdn.com/google/upside_down_face.png?v=14)
):

1)

Use full path (recommended if you're outside the project folder):

docker build -t tushar2k5/tds-project-1 D:\TDS_Project_1\tds-project-1

OR

2)

Add a dot (.) at the end to specify the current directory as the build context:

docker build -t tushar2k5/tds-project-1 .

Both the things work for me
(
![:up_arrow:](https://emoji.discourse-cdn.com/google/up_arrow.png?v=14)
)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
 carlton:

docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 <your image name>

docker run -e AIPROXY_TOKEN=i.am.still.noob.inTDS -p 8000:8000 tushar2k5/tds-project-1

Done this(can’t leak my token,already many students stolen it from my project-2🤦‍♂️)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
 carlton:

uv run evaluate.py --email=<any email> --token_counter 1 --external_port 8000

uv run evaluate.py --email=23f2003751@ds.study.iitm.ac.in --token_counter 1 --external_port 8000

Done this to evaluate my project

Any finally the main part (DRUM ROLLS
![:drum:](https://emoji.discourse-cdn.com/google/drum.png?v=14)
,not this one
![:oil_drum:](https://emoji.discourse-cdn.com/google/oil_drum.png?v=14)
 (IUKUK))

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fc6fad6517b25106749f3c9c504cf38cc72bed3c.png)

> **Image Description**: The image shows the terminal output of a code execution environment, likely a coding assignment or competition.

- **Task**: The program is tasked with determining whether the statement "I hate you" has a positive or negative connotation and saving the result ("POSITIVE" or "NEGATIVE") to a file.
- **Error**: The program encountered a failure during execution, specifically "C5 failed: Server disconnected without sending a response." This suggests an issue with network connectivity or server availability during the execution.
- **Score**: The execution resulted in a score of 6 out of 25, indicating the code's failure to properly complete the task.
- **HTTP Request**: An HTTP POST request was made to a URL related to OpenAI embeddings. This suggests that the program potentially relies on external embeddings service.
image1462×305 14.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fc6fad6517b25106749f3c9c504cf38cc72bed3c.png)

THATS 6/25

Currently I’m getting a big 0 beacause the github doen’t contain the dockerfile(which it does clearly)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/5/55f769f57bb4a5678a20b414877b8f2dee2d7e5d.png)

> **Image Description**: The image shows a pre-requisites check list with four items, each marked with either "1" for pass or "0" for fail. The items are:
- Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
- Github repo exists and is public (should have a timestamp before 18th of Feb): 1
- Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
- Gihub repo check - Dockerfile exists: 0
image686×141 5.46 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/5/55f769f57bb4a5678a20b414877b8f2dee2d7e5d.png)

Hopping to get a response from you guys,

Thanks a lot(wrote this much for first time for any course)

(PS:This course has some special place in my heart
![:heart:](https://emoji.discourse-cdn.com/google/heart.png?v=14)
)

[@Jivraj](/u/jivraj)

[@s.anand](/u/s.anand)

---

### Post #331 by Jivraj Singh Shekhawat on 2025-04-06T13:31:50.869Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/331

We fetched your latest github commit before 18th Feb and build image through that and evaluated.

Your latest github repo before 18 has:

username :
singh-yash129

Repo :
Large-Language-Model

commit_sha:
88f7439471151283f1218b46d209030dd7f4e5ae

Use
https://github.com/<username>/<repo>/archive/<commit_sha>.zip
 for downloading repo.

If You feel there is any problem with our evaluation script suggest edits to the scirpt.

---

### Post #332 by Jivraj Singh Shekhawat on 2025-04-06T13:37:57.159Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/332

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2003751/48/68010_2.png)
 23f2003751:

Currently I’m getting a big 0 beacause the github doen’t contain the dockerfile(which it does clearly

Dockerfile has to be inside root of any github repo, this is standard and we had discussion with Professor Anand about such cases where it’s not part of root directory, he suggested we will consider only Dockerfile being present in root folder of the repo.

---

### Post #333 by Tushar Jalan  on 2025-04-06T13:49:39.300Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/333

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png)
 Jivraj:

Dockerfile has to be inside root of any github repo, this is standard and we had discussion with Professor Anand about such cases where it’s not part of root directory, he suggested we will consider only Dockerfile being present in root folder of the repo.

Sorry but its not possible to attend every single session and you guys haven’t informed us via email so how its our fault.For cases like this you guys should allow us to move our files to the root directory so it can work…(we just have to move files  in the repo please consider it)
[@carlton](/u/carlton)

[@Saransh_Saini](/u/saransh_saini)

[@s.anand](/u/s.anand)

(i have already made a rookie mistake in my dockerfile otherwise i would have got 9/25 but keeping that aside please let me get 6/25)

---

### Post #335 by Pranaav on 2025-04-06T14:10:37.709Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/335

Good evening sir.

My original project evaluation conducted by IITM gave me 7/20, however the new evaluation gave me 0/20.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/c/cc8129304f5afb06949f9302d76a9676ce4dea17_2_361x500.png)

> **Image Description**: Here's a concise description of the image for a Tools in Data Science student:

The image shows a log file titled "23f1002223@ds.study.iitm.ac.in_evaluation.log". It displays a series of HTTP requests and responses related to data processing tasks. Some tasks are marked with a green check indicating success (e.g., "B9 Task"). Others are marked with red indicating errors, such as "B9 failed: Cannot read /data/b9.html" and "B10 failed: Cannot read /data/b10.csv". There's also an HTTP 400 Bad Request error related to a database query. The final score is indicated as 7/20.
image650×898 106 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/c/cc8129304f5afb06949f9302d76a9676ce4dea17.png)

This was from the official evaluation sir, could you kindly look into it.

---

### Post #336 by Bharat Choudhary on 2025-04-06T14:13:19.854Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/336

did everything as mentioned i got 7/25 but in mail i got 2 which is bonus?

i know i didn’t add flask in docker it was my mistake
![:frowning:](https://emoji.discourse-cdn.com/google/frowning.png?v=14)
 but can we just for once neglect that. pleaseeeeeeeee

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/9/09a6d31fb7df32c7cd6ef945bb25dfce03707a15.png)

> **Image Description**: The image shows a terminal output with the following information:

*   An HTTP GET request to `http://localhost:8000/read?path=/data/c5.txt` resulted in a "404 Not Found" error.
*   The output indicates that the program "C5" failed because it could not read the file `/data/c5.txt`.
*   "C5 FAILED" is explicitly displayed.
*   The score is 7 out of 25.
*   An HTTP POST request to `https://aiproxy.sanand.workers.dev/openai/v1/embeddings` returned an "HTTP/1.1 200 OK" status.
*   The terminal prompt indicates the current directory is `C:\Users\choud\OneDrive\Desktop\tds1\TDS_Project_1`.
image787×249 8.87 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/9/09a6d31fb7df32c7cd6ef945bb25dfce03707a15.png)

---

### Post #337 by Sanjita Prabhu on 2025-04-06T14:16:52.383Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/337

Please do consider allowing us to change the position of the dockerfile to the root. We are doing nothing but changing its location in the repo. This was not mentioned anywhere in the prerequisites before the submission and it is unfair to not consider all our work for a criteria that was nowhere mentioned in the course page before the submissions. It may be standard practice but a lot of us were unaware. Please do consider this request.

---

### Post #338 by Abhay Mehra on 2025-04-06T14:21:15.929Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/338

Sir, could you please fetch my latest GitHub commit before 18th Feb and build the image through that one?

I received a mail saying that the Docker image is not accessible, but it is already there. Kindly request you to evaluate my submission.

---

### Post #339 by Jivraj Singh Shekhawat on 2025-04-06T14:25:38.244Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/339

Hi
[@Abhay222](/u/abhay222)

Docker image submitted by you doesn’t exists.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/6/f633d628d646e068273aef8682b5405527cabb65_2_690x342.png)

> **Image Description**: The image shows a Docker Hub page displaying a "404 Oops!" error message. This indicates that the requested page, specifically related to the "abhay227/version1/tags" repository, was not found. The page also features the Docker Hub logo and search bar.
image1902×943 93.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/6/f633d628d646e068273aef8682b5405527cabb65.png)

---

### Post #340 by Jivraj Singh Shekhawat on 2025-04-06T14:27:42.362Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/340

Hi
[@23f1000879](/u/23f1000879)

This basically tells you didn’t validate docker Dockerfile and docker image by building and running them, otherwise you would have corrected the mistake.

---

### Post #341 by Abhay Mehra on 2025-04-06T14:28:03.210Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/341

[![Screenshot 2025-04-02 132214](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1_2_690x93.png)Screenshot 2025-04-02 1322141843×250 18.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/d/6d91cbdb81d6b92d0da76715ba6725eb015b11d1.png)

but it is available under version1.

---

### Post #342 by Jivraj Singh Shekhawat on 2025-04-06T14:32:55.129Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/342

repo that you submitted through google form was different then this one.

Your Gform response

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8aee4e76f9cd47c8bc2e24137881ea41f00a37f_2_690x100.png)

> **Image Description**: The image shows a table with data related to a GitHub repository and a DockerHub image. The columns are: Timestamp, Email Address, GitHub repository link, and DockerHub image name.  Row 919 contains the data: Timestamp "2/16/2025 23:10:43", Email Address "23f1001120@ds.study.iitm.ac.in", GitHub link "https://github.com/23f1001120/Tds_Project1", and DockerHub image name "abhay227/version1". The image also shows a search bar with the query "23f1001120@ds.study.iitm.ac.in". The file has 1069 lines and a size of 127 KB.
image1660×242 21.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b8aee4e76f9cd47c8bc2e24137881ea41f00a37f.png)

---

### Post #343 by RAJ K BOOPATHI on 2025-04-06T14:35:49.703Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/343

Hi, I work in the IT industry. There is no standard like “docker file has to be only in the root folder.”

If at all you are setting a requirement why was this not mentioned in the project page?

We were asked to build an app which solves the given tasks. You were OK for whatever code/tools/method to use as long as it works, there the “industry standard” didn’t show up ironically!!!

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.

In the same industry that I work - we build the dockers and give it for prod push.

---

### Post #344 by Afsal on 2025-04-06T14:44:59.635Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/344

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Dear Sir,

I got log with error as /bin/sh: 1: [/root/.local/bin/uv,: not found.

I debugged that I had a small issue in the dockerfile that was submitted and it is

CMD [“/root/.local/bin/uv”, “run”, “app.py”]  has an
invisible Unicode non-breaking space
 (
U+00A0
) between
"run", "app.py"
 instead of a regular space. This causes the shell to misread the command.

I know it’s very late for the submission to reconsider, but this small mistake spoiled my hard earned project which got local score 8/25 which could finally get converted to 12 marks. I made this change and pushed it to docker and github repository. Considering this, I request you to please evaluate my submission if possible, because I don’t want to lose the marks which i tried my level best to score. I already have good score in GA’s and ROE.  Expecting a positive response from your end.

---

### Post #345 by Bharat Choudhary on 2025-04-06T14:49:28.608Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/345

sir, but before submission i run evluate.py and it gave me 8/10 in task A. after submission i also got result mail stating that i got 8/20.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/6/6689843088265aa67624484279c35e788ed5d74c_2_690x341.png)

> **Image Description**: Here's a concise, factual description of the image for a Data Science Tools student:

The image shows a log file from a data processing task. Several errors are indicated ("FAILED") within the log, specifically referencing issues with file access ("Cannot read /data/b9.html", "Cannot read /data/b10.csv") and string formatting. It includes HTTP requests and responses with status codes (e.g., "HTTP/1.1 404 Not Found", "HTTP/1.1 400 Bad Request"). One section details a task involving running a datasette instance on a dataset ("ticket-sales.db"), querying it with SQL ("SELECT COUNT(*) FROM tickets WHERE type = 'Bronze'"), and encountering connection errors. The final score is "Score: 8 / 20".
image1895×938 90 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/6/6689843088265aa67624484279c35e788ed5d74c.png)

also this mail result Earlier i got From your side.
![:frowning:](https://emoji.discourse-cdn.com/google/frowning.png?v=14)

---

### Post #346 by Abhay Mehra on 2025-04-06T14:50:49.740Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/346

Sir, I realized that I mistakenly submitted the image tag
"abhay227/version1"
 instead of the correct image ID. The correct image ID is
4db729a03f74
, which is part of version1 and is already present and publicly available.

Unfortunately, I didn’t receive any notification about this issue after submission. Receiving this mail at this stage feels disheartening after all the effort I’ve put into the project.  I kindly request you please consider this correct image ID.

---

### Post #347 by Maithreyi on 2025-04-06T15:05:57.719Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/347

[![Screenshot 2025-04-06 202736](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/b/fbbc7606d11dda4948aceedc2d598b7f3f4b96b5.png)

> **Image Description**: The image displays a checklist of pre-requisites for a project, with each item marked as either passing (1) or failing (0). The checklist items are:

1.  Docker repo exists and is public (timestamp before 18th of Feb): 1
2.  Github repo exists and is public (timestamp before 18th of Feb): 1
3.  Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
4.  Github repo check - Dockerfile exists: 1
Screenshot 2025-04-06 202736662×141 5.41 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/b/fbbc7606d11dda4948aceedc2d598b7f3f4b96b5.png)

Hi, all my pre-requisites have been fulfilled, and the evaluation logs say I have a score of 10/25. But I have gotten a score of 0, saying ‘Task A module missing’. This is a kind request to confirm the scores.

---

### Post #348 by Veer Shah on 2025-04-06T15:10:17.226Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/348

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/9/695ad6dd9f35a4590a41863def948b9903941388_2_690x282.png)

> **Image Description**: The image shows a Google Sheets document titled "p1_evaluation_error_logs." The sheet contains columns labeled "email" (column A) and another unlabeled column (column B), with data populated from rows 55 to 74. Column A contains email addresses and column B contains the error messages. The error messages include "taskA module missing", "app module missing", "application running on 5000 port", "SyntaxError: unmatched '", "flask module missing", "Container was bound to 127.0.0.1 instead of 0.0.0.0 which is why docker container port 8000 is not accessible outside(host os)", "npx not found", ".env file missing", "openai module missing", and "PhaseA module missing". There is a highlighted search bar at the top right corner that contains the text "2311001524 0 of 0". The document is in "View only" mode.
image1915×783 79.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/695ad6dd9f35a4590a41863def948b9903941388.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/e/ae524c05420e98ff1b2b00c89337a31ec8a34a7e_2_690x236.png)

> **Image Description**: Here's a concise description of the image:

The image shows a Windows file explorer window. The current directory is "Downloads > docker_logs.zip". The content area displays "No items match your search", implying the zip file is either empty or the content is being filtered. The file name "23f1001524" is typed in the search bar at the top-right of the window.
image1912×654 36.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/e/ae524c05420e98ff1b2b00c89337a31ec8a34a7e.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/a/0adbce8db00985ca07a8ad9347c9cb9559139dda_2_690x240.png)

> **Image Description**: The image shows a Windows File Explorer window. The user is viewing the contents of a ZIP archive named "evaluation_logs.zip" located in the Downloads folder. However, the archive appears to be empty, as indicated by the text "No items match your search" in the main panel. The search bar at the top right contains the query "2311001524".
image1899×663 32.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/a/0adbce8db00985ca07a8ad9347c9cb9559139dda.png)

I cannot find my docker_logs nor evaluation_logs and nor anything on the forms . The mail I got says that i received 0 in project tasks but clearly my project is not evaluated. Please look into this. during earlier evaluation i got 7 marks but this time it is 0.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/ef7afffc65533ff5136a0ae3532470957d66bb1b_2_690x386.png)

> **Image Description**: The image shows the results of an automated evaluation of a student's project, specifically focusing on the Github and Docker repositories submitted.

The evaluation includes a pre-requisites check with items related to the Docker and Github repositories. Each item results in a pass or fail (1 or 0, respectively). Based on the output, all 4 pre-requisites tests pass.

There is a table displaying the scores for different test cases: A1-A10, B1-B10, and C1-C5, all of which scored 0.

The final score is calculated based on the formula "MIN (20, (task score + bonus))". The displayed task score is 0, bonus is 1, and P1 score is 1.
image1455×814 38 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/f/ef7afffc65533ff5136a0ae3532470957d66bb1b.png)

My roll number is 23f1001524 .

---

### Post #349 by NK on 2025-04-06T15:10:52.149Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/349

[@carlton](/u/carlton)
 and
[@Jivraj](/u/jivraj)
 , for Task A i had tested before and all the test cases passed, but all my A tasks has failed with 0, In the evaluation logs, i could see that all task A tests failed due to datagen.py not available.

Could you rerun the test ?

---

### Post #350 by Santosh Sharma on 2025-04-06T15:16:52.371Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/350

Respected Sir,

Thank you for your response and for providing the steps to replicate the test environment.

Steps Taken to Replicate the Test Environment

I cloned my repository using:

bash
git clone <my_repo_url>
cd <my_repo_directory>
I built the Docker image using:

bash
docker build -t.
I ran the Docker container with:

bash
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000

I ensured that datagen.py and evaluate.py were placed in the same folder as instructed.

Finally, I ran the evaluation script using:

bash
uvicorn evaluate.py --email=<any_email> --token_counter 1 --external_port 8000

Issue with Original Submission

After reviewing the evaluation logs, I identified that the issue with my original submission was caused by binary incompatibility between pandas (version 2.0.3) and NumPy (version 1.24.3). These versions worked perfectly during development on my local machine and were tested multiple times across both Linux and Windows platforms before submission. Even after pulling the submitted Docker image from Docker Hub post-submission, it worked without any issues locally.

However, during your evaluation, this incompatibility caused the container to fail.

I acknowledge this issue, have fixed it in my updated submission, and previously conveyed this in my earlier message.

Action Taken

To address this issue, I made a small adjustment to my requirements.txt file to explicitly fix these versions for compatibility across all environments. This was the only change made to my submission. After rebuilding the container with this updated file, I tested it again thoroughly in your replicated test environment, and it worked as expected:

The application initializes correctly on port 8000 within 5 minutes.

It responds to requests within the required timeframe.

I have pushed this updated image to Docker Hub under the same repository:

Docker Hub URL: santoshsharma003/tds-project-one-1:latest

Request for Re-Evaluation

I kindly request that you pull the latest version of my Docker image from Docker Hub and re-run the evaluation process. I understand that deployability is being tested, and I have taken every necessary step to ensure that my submission now works in any environment, including replicating your test setup exactly.

Previous Message for Reference

For your convenience, here is my earlier message explaining this issue in detail:

"Greetings, Sir,

I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between pandas and numpy caused the container to fail. To my surprise, the same versions (pandas==2.0.3 and numpy==1.24.3) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.

To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.

I’ve pushed the updated image to Docker Hub (santoshsharma003/tds-project-one-1:latest). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.

Thank you for your assistance!"

---

### Post #351 by MITALI RAJ on 2025-04-06T15:32:18.435Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/351

same for me

my roll number is 23f1003094

---

### Post #352 by  KARTHIK on 2025-04-06T15:35:02.662Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/352

Same with me sir
[@carlton](/u/carlton)

---

### Post #353 by Carlton D'Silva on 2025-04-06T15:39:13.854Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/353

There are no evaluation logs for you, I am not sure which evaluation log you are referring to. Your docker image fails to run the required task because your Dockerfile is misconfigured. Did you follow the test environment setup mentioned in this post before posting your query?

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

[Tools in Data Science](/c/courses/tds-kb/34)

    To replicate the test environment:
Fetch the github repo’s latest commit before 18th feb use below code for that
import requests
import pandas
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try :
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …

Because if you did, you will realise why your evaluation failed.

You must replicate the test environment and then if you submission works, you have a legitimate appeal. Otherwise we will not consider it. Please replicate the issue using the test environment as detailed in the post link.

Kind regards

---

### Post #354 by Carlton D'Silva on 2025-04-06T15:42:44.851Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354

You can take it up with
[@s.anand](/u/s.anand)

I did not come up with the standard.

And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files.

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.

Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand if we could make the allowance. He made the decision to enforce this protocol.

Kindest regards.

---

### Post #355 by D HARICHARAN  on 2025-04-06T15:48:47.772Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/355

[@carlton](/u/carlton)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/f/2fa3b5ca794441978a80d9d1c4e4c850eb67304c_2_690x348.png)

> **Image Description**: The image shows a log file from a data science task, indicating multiple errors. Specifically, tasks B9 and B10 have failed because the system cannot read the files /data/b9.html and /data/b10.csv, respectively. A task is attempting to run a datasette, querying the ticket-sales.db database to count rows where the 'type' is 'Bronze' and save the result to /data/b10.csv. The HTTP request to execute this task resulted in a "400 Bad Request" error. Additionally, an HTTP 400 error with the "Connection refused" message suggests an issue with establishing a connection to localhost on port 8001. A GET request to read /data/b10.csv resulted in a "404 Not Found" error. The current score is 7/20.
image1892×955 130 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/f/2fa3b5ca794441978a80d9d1c4e4c850eb67304c.png)

Respected Sir,

see the above image its from the scores we got from mail just before the latest one, in that I had got 7/20 and now new mail shows I got 0?? how is this possible…

the link for evaluation in which i got 7/20 is :
[23f2001390@ds.study.iitm.ac.in_evaluation.log - Google Drive](https://drive.google.com/file/d/1cNVy9KSfSITZg_KGLF2_wwLWjzNl8mb5/view)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/f/afbded56c295f1e2ff28878559e430ba3ed8244e_2_690x384.png)

> **Image Description**: The image shows a report from an automated system, likely related to a coding assignment or project. 

Key elements:
*   **Repository links**: Includes links to both Github and Docker repositories.
*   **Pre-requisites check**: Indicates whether the submitted code met certain criteria (public repos with timestamps before a certain date, presence of license files, Dockerfile).
*   **Task Score**: Indicates scores related to different tasks:
    *   Task score: 0
    *   Bonus: 1
    *   P1 score: 1
*   **Table of values**:  A table containing labeled cells (A1-A10, B1-B10, C1-C5), each with a value of 0.
*   **Docker logs**: It states that docker logs and evaluation logs are provided for those who passed the pre-requisites.
*   **Evaluation Log**: Indicates that an evaluation log is available only if the API service started working within 5 minutes, otherwise, only a docker log is available.
image1315×732 45.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/f/afbded56c295f1e2ff28878559e430ba3ed8244e.png)

MOST importantly mail shows :

Your final t score
 calculation is based on

MIN (20, (task score + bonus))

Github repo submitted:

[GitHub - 23f2001390/llmagent](https://github.com/23f2001390/llmagent)

Docker repo submitted:
 23f2001390/llmagent

Pre-requisites check: (1 for pass, 0 for fail)

Docker repo exists and is public (should have a timestamp before 18th of Feb): 1

Github repo exists and is public (should have a timestamp before 18th of Feb): 1

Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1

Gihub repo check - Dockerfile exists: 1

Your task score is: 0

Your bonus is: 1

Your P1 score is: 1

So according to the above, I passed the pre-requisites and also in mail u have mentioned that:

We have attached the docker logs and the evaluation logs for everyone who passed the pre-requisites.

but I don’t find my mail id or roll number in the docker_logs.zip or evaluation_logs.zip  that has been given in the mail(latest), if I passed the pre requisites my logs should be there in the zip files included in this latest mail right, my roll number is 23f2001390 and email id is 23f2001390@ds.study.iitm.ac.in

and nor do i find my id in the p1_evaluation_error_logs so please help sir

Thank you

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/1/41513a69b4af93110ad5c7a3717fca9f0fecd63b_2_690x327.png)

> **Image Description**: The image shows a Windows Explorer window, likely from a computer. The directory path is This PC > Downloads > docker_logs.zip. A search bar at the top right contains the text "23f2001390". The window displays column headers "Name," "Type," "Compressed size," and "Password p...", however, "No items match your search" is shown in the file view. A message "Select a file to preview." is at the bottom right of the window.
image1078×511 8.14 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/1/41513a69b4af93110ad5c7a3717fca9f0fecd63b.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/6/d694d88bee053086a294de30c7566ea08dbbf9c0_2_690x336.png)

> **Image Description**: The image shows a Windows file explorer window. The current directory is "This PC > Downloads > evaluation_logs.zip". The window displays "No items match your search." A search box in the upper right corner contains the string "23f2001390". The window has columns for "Name", "Type", "Compressed size", and "Password p..." (truncated). The file preview pane states "Select a file to preview."
image1083×528 8.42 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/6/d694d88bee053086a294de30c7566ea08dbbf9c0.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/2/c2b0b8d98d14050bb8021568b7a3ac7101c7e4df_2_690x351.png)

> **Image Description**: The image shows a Google Sheets document titled "p1_evaluation_error_logs". The sheet contains two columns: "email" and "error_reason". The "email" column lists email addresses, and the "error_reason" column provides descriptions of errors. Examples of errors include missing modules (e.g., "requests module missing", "taskA module missing", "flask_cors module missing") and issues with application execution (e.g., "application running on 5000 port", "error: Failed to spawn: app.py"). One error message indicates a problem with Docker container port accessibility.
image1905×970 78.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/2/c2b0b8d98d14050bb8021568b7a3ac7101c7e4df.png)

---

### Post #356 by D HARICHARAN  on 2025-04-06T16:00:57.299Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/356

[@carlton](/u/carlton)

Same for sir. I have made my post similarly, roll number is 23f2001390 and email is 23f2001390@ds.study.iitm.ac.in

---

### Post #357 by Dipshikha Patel on 2025-04-06T16:04:18.467Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/357

[@carlton](/u/carlton)

i  also not found anything in this form  , but i got mail to score=0

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/e/9e2ca0680b13a927d524fe5883919c8447d0f8e3_2_690x305.png)

> **Image Description**: The image shows a spreadsheet-like interface, likely a Google Sheet, titled "p1_evaluation_error_logs". The sheet contains two columns labeled "email" and "A." The email column displays various email addresses, likely student submissions. Column A displays error messages. Common errors include "taskA module missing," various module import errors, container binding issues (related to Docker), and syntax errors. An error related to installing on Python version 3.12.9 is also present. A search box displays the term "2312001481" with "0 of 0" results, indicating no matching entries were found. The sheet is in "View only" mode.
image1893×837 85.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/e/9e2ca0680b13a927d524fe5883919c8447d0f8e3.png)

![:smiling_face_with_tear:](https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=14)

---

### Post #358 by Carlton D'Silva on 2025-04-06T16:05:27.961Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/358

Hi Hari,

Your docker failed to build.

Did you try to replicate the test environment as mentioned in

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

[Tools in Data Science](/c/courses/tds-kb/34)

    To replicate the test environment:
Fetch the github repo’s latest commit before 18th feb use below code for that
import requests
import pandas
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try :
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …

If you tried you would find that it will not build. Thats why you have no logs.

90 such cases are there where the image could not be built from your repo.

The specific error in your case is:

tried copying requirements.txt which doesn’t exists

Thats why there are no logs.

Kind regards

---

### Post #359 by Santosh Sharma on 2025-04-06T16:11:26.543Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/359

Hello
[@carlton](/u/carlton)
 Sir, please reply to my query

---

### Post #360 by Carlton D'Silva on 2025-04-06T16:13:31.188Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/360

We cannot allow changes to repos. This is a blanket rule for everyone. No exceptions. Since the only way to get your project to work is to make changes to it, we cannot score you for changes.

Kind regards

---

### Post #361 by RAJ K BOOPATHI on 2025-04-06T16:15:38.400Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/361

Thanks for the response. We can go on endless discussions using “nice words” “professionally” with the number of questions we have. Finally we are at the receiving end as students in this setup.

What’s the take away for everyone? Let’s move on. This isn’t the end.

Positive or Negative - Real world outside will make everyone realise and everyone change their opinions (including me) as the time and environment changes.

---

### Post #362 by LAKSHAY on 2025-04-06T16:39:30.463Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/362

What I observed is that most of the repositories appear to be copied from a single source. This original repository contains several issues, such as an incorrectly named Dockerfile and missing instructions to copy all necessary data. Unfortunately, many students seem to have uploaded it blindly without reviewing or fixing these problems.

---

### Post #363 by Siddharth Kaushik on 2025-04-06T16:58:32.449Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/363

Hi I have my Dockerfile saved as dockerfile, given 0 for project 1 due to this. This doesn’t seem to be a big issue to grade me 0 for this. Kindly correct the score please.

---

### Post #364 by Jivraj Singh Shekhawat on 2025-04-06T18:41:59.248Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/364

Most common reason for during running docker image was
taskA module was missing
 which is because a lot of students blindly copied from someone with building and running image, if they would have done that they could have corrected it at early stage.

---

### Post #365 by Jivraj Singh Shekhawat on 2025-04-06T18:52:33.721Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/365

For you check failed because of the naming of Dockerfile(It was named as dockerfile(d in small).

---

### Post #366 by Jivraj Singh Shekhawat on 2025-04-06T18:56:17.830Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/366

This is error that you got while building docker image using docker file in your github repo tried copying requirements.txt which doesn’t exists

In your Dockerfile you are trying to copy requirements.txt but it doesn’t exists in the directory where Dockerfile is located

---

### Post #367 by Jivraj Singh Shekhawat on 2025-04-06T18:59:11.118Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/367

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/mitali_r/48/66886_2.png)
 MITALI_R:

23f1003094

While running docker image create by your github repo, we got following error
taskA module missing

For regenerating it follow steps that are mentioned here :
[Tds-official-Project1-discrepencies - #316](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

### Post #368 by Jivraj Singh Shekhawat on 2025-04-06T19:02:28.148Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/368

For you naming of MIT License was not correct.

This shows naming criteria for adding License.

[Adding a license to a repository - GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)

---

### Post #369 by D HARICHARAN  on 2025-04-06T19:06:07.077Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/369

Sir actually my project doesn’t have requirements.txt, instead it installs automatically

when:

uv run app.py
 is run and for docker image it installs while building and I had submitted the docker image with all libraries required(the dockerfile below, in that it installs while building).

my dockerfile from the repo:

FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn requests python-dateutil pandas db-sqlite3 scipy pybase64 python-dotenv httpx markdown duckdb faker pillow

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app
# Copy application files
COPY *.py /app/
COPY .env /app/

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]

here u can see it installs using pip install …

here it’s requiring
.env
 file to be present in the project folder because my project when I was uploading to both git and docker had
.env
 file for AIPROXY_TOKEN and I uploaded to docker with that
.env
 file but as git doesn’t allow upload of
.env
 file I couldn’t upload
.env
 to git

the project will still work after downloading the repository when we upload AIPROXY_TOKEN as environment variable but to again build the docker image for replicating the test environment, my docker image could not be built because
.env
 file doesn’t upload to GIT, so when I downloaded the repository from the above method, it didn’t have the
.env
 file so it didn’t build so I had to create the
.env
 file now to create the docker image, and for the dockerimage I had submitted, I built it with the
.env
 file(it supports both
.env
 file and environment variable one)

---

### Post #370 by Jivraj Singh Shekhawat on 2025-04-06T19:15:23.872Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/370

After filling form you didn’t double check form.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/abhay222/48/66780_2.png)
 Abhay222:

I kindly request you please consider this correct image ID.

We can’t reconsider it.

---

### Post #371 by Jivraj Singh Shekhawat on 2025-04-06T19:22:42.862Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/371

Yes problem was missing
.env
 file, Your repo, was supposed to run in a test environment.

---

### Post #373 by D HARICHARAN  on 2025-04-06T19:25:48.506Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/373

Yes sir, please help me

---

### Post #374 by Jivraj Singh Shekhawat on 2025-04-06T19:26:27.662Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/374

Sorry We can’t do any help, we won’t be considering for eval.

---

### Post #375 by D HARICHARAN  on 2025-04-06T19:27:12.497Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/375

But sir, It was supposed to run right…

---

### Post #376 by Jivraj Singh Shekhawat on 2025-04-06T19:29:29.774Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/376

It Should build in any test environment using Dockerfile from your github repo.

---

### Post #377 by Aryan Kumar on 2025-04-06T19:30:23.489Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/377

[@Jivraj](/u/jivraj)
 please tell me what was my mistake?

---

### Post #378 by Jivraj Singh Shekhawat on 2025-04-06T19:36:51.088Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/378

It was named wrongly.

You named it LICENCE but it should be LICENSE or LICENSE.md.

---

### Post #379 by D HARICHARAN  on 2025-04-06T19:54:37.949Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/379

But sir, just because the repository doesn’t have .env file it couldn’t build the dockerimage, the docker image will build in any test environment as u said but it requires the .env to be included which the git didn’t have(it doesn’t allow upload of it ofcourse), don’t rerun the evaluation again but please sir atleast give me those 7/20 marks along with the pre-requisite bonus(1mark) that was mailed earlier to me along with logs…this is my primary degree after 12th, I’m also not asking any extra marks just the marks that i got earlier:

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/6/16d50a2f5466ad8d9ed068b4af93899fe3295a4e_2_690x380.png)

> **Image Description**: Here's a concise and factual description of the image for a student in a Tools in Data Science course:

The image displays a log file named "23f2001390@ds.study.iitm.ac.in_evaluation.log". It shows the execution results of a data processing task, likely related to a datasette database. The log indicates several failures: reading data files "data/b9.html" and "data/b10.csv".

The task involves querying a 'ticket-sales.db' database to count rows where the 'type' is "Bronze". The query is constructed using SQL. The log shows HTTP requests to a local server (localhost on ports 8001 and 8369). There are errors related to connection refusal (Errno 111) and "400 Bad Request".

Finally, the image shows the task's score as 7/20 and a successful HTTP request to an embeddings endpoint.
image1850×1021 132 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/6/16d50a2f5466ad8d9ed068b4af93899fe3295a4e.png)

---

### Post #380 by Jivraj Singh Shekhawat on 2025-04-06T21:53:15.006Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/380

Hi
[@23f2002600](/u/23f2002600)

[@21f1005908](/u/21f1005908)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354)

[Tools in Data Science](/c/courses/tds-kb/34)

    You can take it up with
[@s.anand](/u/s.anand)

I did not come up with the standard.
And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files.

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.

Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand i…

---

### Post #381 by Jivraj Singh Shekhawat on 2025-04-06T22:07:19.469Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/381

Runned for you, it A1 Fails.

---

### Post #382 by Jivraj Singh Shekhawat on 2025-04-06T22:10:05.622Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/382

Your docker image and github repo are not consistent,  your docker image was not built with the latest code before 18th feb that’s present in your github repo.

---

### Post #383 by Jivraj Singh Shekhawat on 2025-04-06T22:13:27.848Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/383

We can’t consider any changes after deadline.

---

### Post #384 by Jivraj Singh Shekhawat on 2025-04-06T22:21:06.975Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/384

Your docker image and github repo are not consistent.

While running docker image we got following error:
flask module missing

For regenerating this error follow steps mentioned in below post.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/171141/316)

[Tools in Data Science](/c/courses/tds-kb/34)

    To replicate the test environment:
Fetch the github repo’s latest commit before 18th feb use below code for that
import requests
import pandas
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try :
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …

---

### Post #385 by Jivraj Singh Shekhawat on 2025-04-06T22:29:11.094Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/385

Anything after deadline we can’t consider any changes, it was just a matter of time, you didn’t tests running evaluate.py on docker container that was created, otherwise you would have spotted this mistake and rectified it.

---

### Post #386 by Jivraj Singh Shekhawat on 2025-04-06T22:34:25.989Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/386

In your github repo, Dockerfile should be named as Dockerfile(D caps).

---

### Post #387 by Jivraj Singh Shekhawat on 2025-04-06T22:39:30.596Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/387

I don’t know reason behind it, earlier evaluation was done by pulling docker image.

Latest one was done through github repo, if code in github repo is not consistent with docker image it might cause problems.

LLM won’t provide same results every time, for that reason we have give bonus marks.

---

### Post #389 by Veer Shah on 2025-04-07T01:41:25.976Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/389

[@carlton](/u/carlton)

[@jivraj](/u/jivraj)
 sir it is my humble request to do something. We are losing our marks because of small negligence or mistakes like i fogot to commit my requirements.txt in my github repository. Already the course has taken tolls on our mind. Please give partial marks for the correct run of the docker image or please evaluate my latest commit with the requirements.txt. Because of this project I will lose my cgpa and the hardwork that I have done till this term. A small mistake is causing me my full marks and grades. Atleast consider partial marking for the docker image which does the tasks. I have maintained 9+ cgpa in the diploma and I took other subjects which are easy this term like BDM still is really difficult to cope with the subject. Please consider something. atleast give 50% of the marks for each task which my image passes.

---

### Post #390 by Anisha Seth on 2025-04-07T01:49:33.296Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/390

Sir but i did test my project via evaluate.py and got the 8/10 in my tasks A. A simple port error has resulted in no evaluation at all after all the hardwork.

---

### Post #391 by Bharat Choudhary on 2025-04-07T02:46:43.961Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/391

Sir, how my git repo is not consistent i used the same repo which i have given you in the form even i did not commit any changes after 18th feb also in my docker file there is just a simple mistake that i forgot to add flask dependency just because of that mistake i am losing my marks. I also used same docker image which i have given you through form. Its my humble request please consider or give some solution. It felt like betrayal because we put effort’s.

---

### Post #392 by Afsal on 2025-04-07T04:25:33.067Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/392

Dear Sir,

I understand that this request is coming at a late stage, and I truly apologize for the timing. However, I felt it was important to express how much effort and dedication I have invested in this project and throughout the course. The recent issue has been disheartening for me, especially because the work I submitted was not a blind copy from someone else.

Had it been otherwise, I wouldn’t have had the courage to reach out. I genuinely care about this course and the learning it offers, and I’m proud of the commitment I’ve shown so far.

With utmost respect, I kindly request you to reconsider evaluating my project again, if there’s any possible way to do so. It would mean a lot to me and would really motivate me to keep pushing forward in this subject.

---

### Post #393 by Carlton D'Silva on 2025-04-07T04:51:36.003Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/393

Hi
[@23f1001524](/u/23f1001524)

[@afsalshah](/u/afsalshah)

[@23f1000879](/u/23f1000879)

[@23f1002056](/u/23f1002056)

I understand your situation. We discussed all these scenarios in our weekly meets, and it was decided that we cannot make allowances for these because there was ample time to test your deployments and also ample sessions were conducted to address any difficulties you might have faced. A basic minimum standard was expected and we are unable to relax that threshold because then it would make evaluations meaningless.

We are not just evaluating on your agent functions. We require deployability as a minimum target. If you solution was not deployable and functional then we cannot evaluate the functioning of your application. Once again I sympathise with what might seem minor errors. But they are not minor, even though it may only be a line that needs changing or a spelling mistake. They actually cause a critical failure.

A minor mistake is a function not working that does not prevent other things from working.

Critical failures prevents everything else from working
 and thus most of these what seems like minor failures are missclassified. They are in fact critical failures.

I know its not of much comfort right now, but the learnings from this will be important going forward in your career.

Kindest regards

---

### Post #394 by Telvin Varghese on 2025-04-07T05:54:42.672Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/394

Hi
[@carlton](/u/carlton)
 ,

I couldn’t find my Docker logs or evaluation logs in the latest result mail, even though I had passed the prerequisites. I also tried reproducing the test environment and scored 9/25 (screenshot attached below).

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fd1e9ebbdaabe4f7e853a25f71f645bd06fd0f01.png)

> **Image Description**: The image shows a terminal output. It indicates an HTTP GET request to `http://localhost:8000/read?path=/data/c5.txt` resulted in a `500 Internal Server Error`. It also states "C5 failed: Cannot read /data/c5.txt" and "C5 FAILED" with a red "X" icon. The score is "9/25". An HTTP POST request to `https://aiproxy.sanand.workers.dev/openai/v1/embeddings` resulted in a `200 OK` response.
image1124×268 9.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fd1e9ebbdaabe4f7e853a25f71f645bd06fd0f01.png)

Would really appreciate it if you could take a look. Thanks in advance!

---

### Post #395 by Carlton D'Silva on 2025-04-07T06:01:16.171Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/395

Did you follow these instructions when building the test environment? Our logs indicated that this was the problem:

tried copying multiple files for that you need to give directory name and it should end with a /

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

[Tools in Data Science](/c/courses/tds-kb/34)

    To replicate the test environment:
Fetch the github repo’s latest commit before 18th feb use below code for that
import requests
import pandas
DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")

url = f"https://api.github.com/repos/{owner}/{repo}/commits"
try :
    response = requests.get(url,headers=github_headers, timeout=60)
    fetch_commit = None
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
   …

---

### Post #396 by Telvin Varghese on 2025-04-07T06:04:15.738Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/396

[@carlton](/u/carlton)
  , I followed all the steps instead of
curl -LO https://github.com/<username>/<repo>/archive/<commit_sha>.zip

unzip <path to downloaded zipped repo>
 , I used git clone .

---

### Post #397 by Jayaram on 2025-04-07T06:05:46.668Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/397

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Not able to see the my id in 22f3002723 in evaluation logs or docker logs.. just curious if there was  any issues in creating the image out of github ?

---

### Post #398 by Carlton D'Silva on 2025-04-07T07:27:07.331Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/398

Thanks for the fixes (I have updated the code now). It was put together quickly and not tested before we actually posted it.

---

### Post #399 by Tushar Jalan  on 2025-04-07T07:33:49.534Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/399

Happy to help sir
![:saluting_face:](https://emoji.discourse-cdn.com/google/saluting_face.png?v=14)

(Was expecting some different response from your side,but ig we need to accept our faith
![:upside_down_face:](https://emoji.discourse-cdn.com/google/upside_down_face.png?v=14)
)

Thank you,

(Kindest regards)

Tushar

---

### Post #400 by Carlton D'Silva on 2025-04-07T07:48:28.615Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/400

We are checking you submission. We will get in touch shortly.

---

### Post #401 by Veer Shah on 2025-04-07T09:26:40.790Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/401

[@carlton](/u/carlton)

[@jivraj](/u/jivraj)

[@s.anand](/u/s.anand)
,

I hope you’re doing well. I wanted to humbly request a reconsideration regarding the evaluation of my project submission.

I understand there was an issue with building the Docker image from the repository. However, I had successfully built and pushed the Docker image earlier, and I believe it demonstrates that my solution is deployable. If the final evaluation was solely based on building from the repository, I’m a bit confused about why the Docker image was considered earlier and why we were also asked to upload it to Docker Hub if it wasn’t going to be taken into account later. Also the earlier evaluation score where we got some marks at least and now are hopes are crushed after one night.

I do realize that in the real world, these kinds of errors can be critical, and I truly appreciate that the course is structured to prepare us for such expectations. That said, this course has been quite challenging, and for many students—including myself—it has been a source of considerable stress and demotivation.

I sincerely request that you kindly consider awarding some partial marks for the working Docker image that was built and pushed earlier. It does reflect an understanding of deployable solutions, which I’ve worked hard to demonstrate.

I know you all have our best interests in mind, and I’m grateful for the efforts put into making this a rigorous and enriching course. My only concern is that such harsh penalties—especially for a single oversight—can significantly affect our CGPA and future opportunities. I hope my request can be considered with empathy.

Thank you for your time and understanding.

---

### Post #402 by Jivraj Singh Shekhawat on 2025-04-07T09:55:15.954Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/402

Issues with your submission has been resolved.

Thanks for raising the issue and checking it at your end.

---

### Post #403 by  KARTHIK on 2025-04-07T09:57:43.886Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/403

Sir, I sincerely apologize for the mistake I made in naming the LICENSE file as “LIcense” instead of “LICENSE”. I now understand how important these details are, and it was an unintentional oversight on my part. I had put in a lot of hard work into the project, and it would mean a lot to me if you could kindly consider evaluating it, even though the deadline has passed and results are out. I completely understand if it’s not possible, but I just wanted to request a chance as this project was very important to me and I genuinely learned a lot from it.

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

---

### Post #404 by D HARICHARAN  on 2025-04-07T10:16:46.254Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/404

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/440f4cd9014c4875f88e79b411d5dea05fcd83ec.png)

> **Image Description**: Here's a concise and factual description of the image:

**Content:**

*   **IDE:** The image shows the Visual Studio Code (VS Code) IDE.
*   **Project Directory:** The left sidebar displays a project directory named "llmagent" with files like "app.py", "datagen.py", "Dockerfile", "evaluate.py", "LICENSE", "readme.md", "tasksA.py", and "tasksB.py".
*   **Start Screen:** The main panel shows VS Code's start screen, with options like "New File", "Open File", "Open Folder", and "Clone Git Repository".
*   **Terminal:** The bottom panel shows the VS Code terminal.
*   **Git Clone Command:** The terminal displays a "git clone" command, which is being used to download the "llmagent" project from a GitHub repository.
*   **Git Output:** The terminal shows the progress of the "git clone" operation, including messages related to enumerating, counting, compressing, and receiving objects.
image1188×699 38.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/4/440f4cd9014c4875f88e79b411d5dea05fcd83ec.png)

cloned the repository using

git clone https://github.com/23f2001390/llmagent.git

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/e/0e58db81179e18b5c2b4bd7d75bee3f549d8dac0.png)

> **Image Description**: Here's a concise description of the image:

**Image Summary:**

The image shows a code editor, likely VS Code, displaying a project directory named "llmagent". 

*   The file ".env" is open, which contains an environment variable `AIPROXY_TOKEN` set to a long string (likely a token or key).
*   Other files in the directory include Python scripts (`app.py`, `datagen.py`, `evaluate.py`, `tasksA.py`, `tasksB.py`), a `Dockerfile`, `LICENSE`, and `readme.md`.
*   The terminal is open, showing the output of a `git clone` command that was used to clone a repository (the URL is partially visible).
*   The clone operation appears successful, with messages indicating enumeration, counting, compression, receiving, and resolving of objects.
image1041×721 29.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/e/0e58db81179e18b5c2b4bd7d75bee3f549d8dac0.png)

created the
.env
 for the aiproxy token as its needed to build the docker image as per my Dockerfile and
.env
 file cannot be uploaded to git we have to create it while building docker image

[![evalue](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/4/7451ed8873f25e16cf269a59e4ba5daeba424dc2_2_378x499.png)

> **Image Description**: The image shows a code editor, likely VS Code, with a Python file named "evaluate.py" open within a project called "llmagent". The "evaluate.py" file contains Python code, including import statements for various libraries such as 'sys', 'hashlib', 'httpx', 'io', 'json', 'logging', 'numpy', 'os', 'random', 're', 'subprocess', 'dateutil.parser', 'lxml.html', and 'PIL'. The code also imports several functions from a custom module called "datagen". At the bottom of the code, API keys for OpenAI and Gemini are visible.
evalue752×994 45.3 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/7451ed8873f25e16cf269a59e4ba5daeba424dc2.png)

added the new
evaluate.py
 and
datagen.py
 from the mail, trying to replicate the test environment

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/5/05986eb39e4662742a5fb924ef4199e6b95f37ae.png)

> **Image Description**: The image shows a Visual Studio Code window with a Python file named "app.py" open. The file seems to list dependencies for a project, including libraries such as "requests", "fastapi", "uvicorn", "python-dateutil", "pandas", "db-sqlite3", "scipy", "pybase64", "python-dotenv", "httpx", "markdown", and "duckdb". The project directory, "llmagent", is visible in the file explorer on the left side of the window. Other files in the project include "datagen.py", "Dockerfile", "evaluate.py", "LICENSE", "readme.md", "tasksA.py", "tasksB.py", and ".env". The files "datagen.py" and "evaluate.py" have an 'M' tag, possibly indicating modification. The ".env" file has a "U" tag, which might signify untracked or uncommitted changes in a version control system.
image730×462 21.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/5/05986eb39e4662742a5fb924ef4199e6b95f37ae.png)

moved the new
datagen.py
 and
evaluate.py
 into the project folder

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a5f2b89e834352615300dcbbc2b2d74749da8e2e_2_690x378.png)

> **Image Description**: The image displays a Visual Studio Code (VS Code) window. The left panel, labeled "EXPLORER", shows a directory structure for a project named "llmagent", containing files such as "app.py", "datagen.py", "Dockerfile", "evaluate.py", "readme.md", "tasksA.py", and "tasksB.py". An ".env" file is also present.

The central panel shows the content of "app.py", a Python script, listing dependencies like "requests", "fastapi", "uvicorn", "python-dateutil", "pandas", "db-sqlite3", "scipy", and "pybase64".

The bottom panel displays the VS Code terminal output, indicating a Docker build process. It shows the execution of the command "docker build -t llm-agent .". The output logs steps like loading the build definition from the Dockerfile, downloading base images, adding files, and installing Python packages. The build process is finished and the image is named "docker.io/library/llm-agent". A link to view the build details in the Docker Desktop application is provided.
image1805×989 79.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/5/a5f2b89e834352615300dcbbc2b2d74749da8e2e.png)

docker image built successfully using

docker build -t llm-agent .

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/f/5f6ef64ca044db4f86e841615328f2f0015d6df1_2_690x396.png)

> **Image Description**: Here's a concise and factual description of the image for a Data Science student:

**Overview:**

The image shows a Visual Studio Code (VS Code) environment where Python code is being developed and executed.  The left panel displays the file explorer with project structure.  The central panel shows open files: `.env` and `app.py`. The bottom panel shows the terminal output of running a Python script named `evaluate.py`.

**Key Elements:**

*   **Code:** `app.py` is open in the editor. `env` has an API proxy token.
*   **Terminal Output:** Output of the `uv run evaluate.py` command.
*   **Error Messages:**
    *   An HTTP 400 error: `"detail": "name 'HTTPException' is not defined"` indicating an issue in the API request/response handling.
    *   "A2 failed: \[WinError 2] The system cannot find the file specified" pointing to a file system access problem.
*   **Tasks:**
    * Task to Count the number of Thursdays in the list and write just the number to /data/dates-thursdays.txt"

**Inference:**

*   The student is working on a data science project involving API calls and file processing.
*   Debugging is necessary to address the API error and file access issues.
image1694×974 55.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f6ef64ca044db4f86e841615328f2f0015d6df1.png)

running the evaluate.py using:

 uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/b/6be8a8566f8f3f47a1f052f039130fabd6193c5b.png)

> **Image Description**: The image shows the terminal output of a Python code execution environment, likely VS Code. 

On the left, there is a project folder structure with files like `app.py`, `datagen.py`, `Dockerfile`, `.env`, etc. 

The central part displays the output of a program execution:
*   Task C4 Failed. The task was: "Does the statement 'I hate you' have a positive or negative connotation? Reply as a single string containing 'POSITIVE' or 'NEGATIVE' in uppercase. Save the result to `/data/c5.txt`".
*   An HTTP POST request to `http://localhost:8000/run` resulted in an HTTP 400 error, with the detail message indicating that no connection adapters were found for `data:text/plain; charset=utf-8, NEGATIVE`.
*   An HTTP GET request to `http://localhost:8000/read?path=/data/c5.txt` returned a 200 OK status.
*   The expected result was `NEGATIVE`, but the actual result was `[('NEGATIVE',)]`.
*   Task C5 Failed, with a score of 6/25.
*   An HTTP POST request was made to `https://aiproxy.sanand.workers.dev/openai/v1/embeddings`.

The `.env` file is open, displaying a long string assigned to the `AIPROXY_TOKEN` variable.
image1385×971 46.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/b/6be8a8566f8f3f47a1f052f039130fabd6193c5b.png)

got consistent 6/25 after even running the file 6 times
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@s.anand](/u/s.anand)
 Please sir check this, just because my docker image needs .env, I cannot get full 0…I need to maintain my cgpa (by getting 0 in project my grade is going too close to E grade sir and already in D, already my ROE got bad due to technical issues which on the same day around 6pm after finding way to unlock the input of answers for roe I completed the roe again in short amount of time like 10 or 20 minutes and got 10/10 but still it was rejected because it was late, max 3 minutes after 1:45PM was allowed…I’m not asking to any extra marks, just my marks) I’m trying to improve it already I have 4 subjects in a single term, please give me atleast this marks with the bonus 1 mark for prerequisites (total 7)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/e/8ef5cf5156fdaca65d927edf5d6c2463da4f7052.png)

> **Image Description**: The image shows the submission details and pre-requisite checks for a project. It includes:
- A Github repository URL: https://github.com/23f2001390/lImagent
- A Docker repository name: 23f2001390/lImagent
- A section titled "Pre-requisites check" which indicates that the Docker and Github repositories exist and are public, with a timestamp before Feb 18th. The check also confirms the presence of a LICENSE (or LICENSE.md) file with an MIT License and a Dockerfile in the Github repository. All the checks have passed (indicated by the value '1').
image704×248 20 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/e/8ef5cf5156fdaca65d927edf5d6c2463da4f7052.png)

Thank you

---

### Post #405 by Vaddi Yaswanth on 2025-04-07T10:21:38.581Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/405

Yes,the Same case happend to me also we have put lot of efforts in this project but after seeing that in mail you have no mit licence, I added that license but with name of mit license actually to just name that license file as MIT license but due to this all our hardwork is just an experience but actually we are not awarding any marks in project1 . I request the TDS team to consider this issue.

---

### Post #406 by Sarthak Singh Gaur on 2025-04-07T12:10:25.546Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/406

I have passed the pre requisites, but there is no log file for my email.

At least docker logs should be there, right?

Was it missed by any chance?

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/4/e49661e517e668b1f6055ac2db0b01d1a2a5552a.png)

> **Image Description**: The image shows a checklist labeled "Pre-requisites check: (1 for pass, 0 for fail)". The checklist items are:

*   Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
*   Github repo exists and is public (should have a timestamp before 18th of Feb): 1
*   Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
*   Gihub repo check - Dockerfile exists: 1

All checklist items are marked with "1", indicating they passed the check. The note (1 for pass, 0 for fail) clarifies the significance of the '1' values.
image916×160 14.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/4/e49661e517e668b1f6055ac2db0b01d1a2a5552a.png)

---

### Post #407 by Jayaram on 2025-04-07T12:26:27.239Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/407

Sorry to repeatedly ask
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

couldnt see my id (22f3002723) in any of the logs  evaluation or docker .. was there any issue in building image out of docker file in github

---

### Post #408 by Jivraj Singh Shekhawat on 2025-04-07T12:43:29.133Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/408

Hi
[@22f3002723](/u/22f3002723)

 /bin/sh: 1: uv: not found

This is error that we got on your evaluation while building docker image through github repo.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

[Tools in Data Science](/c/courses/tds-kb/34)

    To replicate the test environment:
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv.
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo

owner = "your_username"  # Replace with your actual GitHub …

---

### Post #409 by Jivraj Singh Shekhawat on 2025-04-07T12:44:40.099Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/409

This was error with your submission.
tried copying file named
app
 which is not there in github repo

---

### Post #410 by S Sharmile on 2025-04-07T12:47:52.725Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/410

Respected Sir ,
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

My roll number is 23f3001688

Pls check my repository properly because I have dockerfile in my repo but it is mentioned that it is not present.

Here is my repository link and screenshot for your reference sir and the dockerfile is present sir

[github.com](https://github.com/Sharmilecholan/tds_project1)

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f4296a48f50a92933eb573695c91faee58b51a1_2_690x344.png)

> **Image Description**: The image shows a GitHub repository named "tds_project1" owned by the user "Sharmilecholan". The repository has 1 contributor, 0 issues, 0 stars, and 0 forks. The repository icon is a stylized letter "H" created from blocks.

[GitHub - Sharmilecholan/tds_project1](https://github.com/Sharmilecholan/tds_project1)

Contribute to Sharmilecholan/tds_project1 development by creating an account on GitHub.

I think the mistake would have been because in my repo the file name is “dockerfile” and you have mentioned it as “Dockerfile” . So is it a mistake to put “D” in lowercase.

Kindly look into this sir because of this I got 0 in project 1 even though many of the tasks of my projects passed the evaluation test.

Regards,

S Sharmile

23f3001688

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/1/014b7a8714c79b6921eb8f8da545286cc6dbedc8_2_690x281.png)

> **Image Description**: The image is a screenshot of a GitHub repository. It shows the repository name and owner, "Sharmilecholan Delete evaluate.py", along with the commit history, "548db37 - 2 months ago" and "4 Commits". The repository file structure is visible, including files such as ".env", ".markdownlint.json", ".prettierrc.json", "LICENSE", "README.md", "app.py", "datagen.py", "dockerfile", "requirements.txt", "tasksA.py", and "tasks8.py". Each file entry includes a brief description of the commit associated with the file (e.g., "Add files via upload", "Initial commit", "Update and rename dockerfile.txt to dockerfile") and the time elapsed since the commit ("2 months ago"). On the right side, the repository's description, website, and topics are stated to be "No description, website, or topics provided." Other repository details like Readme, MIT license, activity, stars, watchers, forks, and a "Report repository" link are displayed. There are also sections for Releases and Packages, both indicating "No releases published" and "No packages published" respectively. Finally, a "Languages" section is visible at the bottom.
image1904×778 83 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/1/014b7a8714c79b6921eb8f8da545286cc6dbedc8.png)

---

### Post #412 by Devanshi  on 2025-04-07T13:37:31.048Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/412

[@carlton](/u/carlton)
 sir, i want to clarify about this. I had got 9/20 in the previous mail in my evaluation log and now the recent mail say i got 1 mark. I want to ask about this. Please help me

[![WhatsApp Image 2025-04-07 at 15.37.17_fb28b652](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/b/4bbeee344dad6a24766c6978889ccd69086dcc6d_2_225x500.jpeg)

> **Image Description**: The image shows a log output indicating a failed task related to running a datasette server. The task involves counting rows in a `tickets` database where the `type` is `Bronze`, saving the result to `/data/b10.csv`, and then stopping the datasette server. The log indicates an "HTTP 500 Internal Server Error" and a subsequent "HTTP/1.1 404 Not Found" error when trying to read the `/data/b10.csv` file.  A later log entry confirms that it "cannot read `/data/b10.csv`" and the task has "FAILED". Finally, a successful HTTP request related to openai embeddings with a 200 OK is shown.
WhatsApp Image 2025-04-07 at 15.37.17_fb28b652720×1600 139 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/b/4bbeee344dad6a24766c6978889ccd69086dcc6d.jpeg)

[![WhatsApp Image 2025-04-07 at 15.39.10_edb0b829](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/3/c342418d20b935d414f96817c92300bcec289598_2_225x500.jpeg)

> **Image Description**: Here's a concise description of the image for a student in a Tools in Data Science course:

The image shows the results of an automated assessment related to a data science task.

**Key elements:**

*   **Repository Submissions:** It indicates that both a GitHub and a Docker repository were submitted.
*   **Pre-requisite Checks:** The image shows successful checks for Docker repo existence, GitHub repo existence, LICENSE file, and Dockerfile existence.
*   **Task Performance Matrix:** The main part displays a grid (A1-A10, B1-B10, C1-C5) filled with zeros, suggesting low scores.
*   **Score Breakdown:** The image shows a task score of 0, a bonus of 1, and a P1 score of 1.
*   **Log Information:** It mentions that docker logs and evaluation logs are attached. Evaluation logs are only present if the API service started working within 5 minutes.
*   **Supporting Files:** It mentions the presence of `evaluate.py` and `datagen.py` for learning purposes.
WhatsApp Image 2025-04-07 at 15.39.10_edb0b829720×1600 125 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/3/c342418d20b935d414f96817c92300bcec289598.jpeg)

---

### Post #414 by Anushka Kumar on 2025-04-07T13:50:15.369Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/414

I don’t know how to check for the errors I made,
[@Jivraj](/u/jivraj)
 sir can you at least show the prerequisite form that I submitted so I can check for myself ?.

---

### Post #415 by Sarthak Singh Gaur on 2025-04-07T14:22:03.831Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/415

[@jivraj](/u/jivraj)

earlier I built the project inside app folder so it was

COPY app /app

it should have been

COPY . /app

Is there anything that can be done on your end now?

All the code is there.

---

### Post #416 by Jivraj Singh Shekhawat on 2025-04-07T14:39:26.569Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/416

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/0/605890bb7fb48c38efa33362d005654d2dd7e765_2_690x86.png)

> **Image Description**: The image shows a table with data related to GitHub repositories and DockerHub images. The table has columns for Timestamp, Email Address, GitHub repository link, and the name of the image published on DockerHub. The first row with index 499 has data from 2/15/2025 with a GitHub repository link to "https://github.com/AnushkaAbhishekKumar/LLM-Project" and a DockerHub image name "coolsisters7/0c8a207a0c7c". The second row with index 1060 has data from 2/16/2025 with a GitHub repository link to "https://github.com/AnushkaAbhishekKumar/LLM-Project/tree/main" and a DockerHub image name "coolsisters7/4a79a3c81cd0". The email addresses associated with both entries are the same: "22f2000559@ds.study.itm.ac.in". There is also a search box at the top with the text "22f2000559".
image1822×229 20.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/0/605890bb7fb48c38efa33362d005654d2dd7e765.png)

Sorry for late reply,These are 2 submissions that you made we are considering the latest one.

---

### Post #417 by Jivraj Singh Shekhawat on 2025-04-07T14:40:37.264Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/417

No we don’t consider any changes after deadline.

---

### Post #418 by Jivraj Singh Shekhawat on 2025-04-07T14:44:08.514Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/418

There was a module missing error while lead the docker image to run.

Follow below steps for replicating test environment.

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

### Post #419 by Jivraj Singh Shekhawat on 2025-04-07T14:49:04.564Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/419

For dockerfile you have in repo, It was named differently, correct naming has to be Dockerfile.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354)

[Tools in Data Science](/c/courses/tds-kb/34)

    You can take it up with
[@s.anand](/u/s.anand)

I did not come up with the standard.
And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files.

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.

Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand i…

---

### Post #420 by Jivraj Singh Shekhawat on 2025-04-07T14:51:31.864Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/420

[@24ds1000119](/u/24ds1000119)
 and
[@YaswanthVaddi](/u/yaswanthvaddi)

We are not considering mismatch in naming for License.

---

### Post #421 by K Senthur Kumaran  on 2025-04-07T14:51:53.998Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/421

Dear
[@carlton](/u/carlton)

This is Senthur. I have reviewed the logs, and it indicates that the

/app/app/main.py
     file is missing. However, in my project directory, the

main.py
   file is located in the
app/
   folder, and the
run.py
   file is in the root folder of the project, which is
LLM_Automation_Agent
  . This structure allows the
run.py
 file to run the project without any issues by calling the appropriate functions from
app/main.py
.

To run the project, the command I used is:

python run.py

Since
run.py
 is placed in the root folder and not in any subfolder, it should properly execute the project without any errors, as it redirects the calls to
app/main.py
.

I believe the evaluation may have been incorrect because the project was not executed in the way it was intended. I kindly request you to re-run the project using the
run.py
 script located in the root folder (
llm-automation-agent
).

For your reference, I have attached screenshots from my local machine where the project was tested successfully, along with my GitHub screenshot.

Here is the GitHub link to my project:

[github.com](https://github.com/ksenthurkumaran18052004/llm-automation-agent)

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/e/ce9394993a2cc41f2a17658d6ed40ff9fff7d6a7_2_690x344.png)

> **Image Description**: The image shows a GitHub repository named "4/llm-automation-agent" owned by user "ksenthurkumaran1805200". The repository has one contributor, zero issues, zero stars, and zero forks. An icon resembling a stylized pixelated face or graphic design is present on the right side of the screen.

[GitHub - ksenthurkumaran18052004/llm-automation-agent](https://github.com/ksenthurkumaran18052004/llm-automation-agent)

Contribute to ksenthurkumaran18052004/llm-automation-agent development by creating an account on GitHub.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/62e7f6525fb97f7d1de84d08cde34b2bf2d5e404_2_255x500.jpeg)

> **Image Description**: Here's a concise description of the image:

The image shows a coding environment. At the top is a code editor, possibly VS Code, displaying Python code. A terminal window underneath shows the output of a script called "run.py", which seems to be starting a Flask development server. Below that, there is a web browser window, probably Chrome, open to a GitHub repository page named "elm-automation-agent." The repository's file structure is visible, showing files and folders.
image1440×2823 252 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/2/62e7f6525fb97f7d1de84d08cde34b2bf2d5e404.jpeg)

Lookig forward towards your support.

With Regards

K Senthur Kumaran

---

### Post #422 by Reva Lakshmy Paul on 2025-04-07T14:53:21.728Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/422

Same here sir, i only changed LICENSE to MIT LICENSE due to the mail i received.

The LICENSE file was already present in the repo as i submitted my project. The change too was made on the 16th of Feb.

Sir, I would highly appreciate if you consider it as the rest of the pre-requisites are working well.Due to this, the project is also not being evaulated.

Thankyou

[@carlton](/u/carlton)

---

### Post #423 by Jivraj Singh Shekhawat on 2025-04-07T15:00:58.659Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/423

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c1d290bffaf6788ece5d9408b1c52566200a8cc9_2_690x149.png)

> **Image Description**: The image shows a terminal session on a system named `root@tds-course-temp-bq`.

The user executes the command `docker images | grep "22f3002902"`, which filters the output of `docker images` for lines containing "22f3002902". The result shows a Docker image with the tag `latest`, ID `c739ff8a3247`, created 6 days ago, and a size of 1.13GB.

Next, the user tries to run a Docker container using the command `docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 c739ff8a3247`. This attempts to run the image with ID `c739ff8a3247`, setting an environment variable `AIPROXY_TOKEN` and mapping port 8000 from the host to the container.

The command fails with the error message `python: can't open file '/app/app/main.py': [Errno 2] No such file or directory`. This indicates that the Python script `/app/app/main.py` is not found within the Docker container.
image1823×395 24.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/1/c1d290bffaf6788ece5d9408b1c52566200a8cc9.png)

Just checked right now. I am getting this error.

Replicate test environment following this post.

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)
0

---

### Post #424 by Mishkat Chougule on 2025-04-07T10:31:33.573Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/424

🟡 Running task: Format `/data/format.md` with `prettier@3.4.2` in-place

HTTP Request: POST http://localhost:8381/run?task=Format+%60%2Fdata%2Fformat.md%60+with+%60prettier%403.4.2%60+in-place "HTTP/1.1 400 Bad Request"

🔴 HTTP 400 {
  "detail": "[Errno 2] No such file or directory: 'C:\\\\Program Files\\\\nodejs\\\\npx.cmd'"
}

HTTP Request: GET http://localhost:8381/read?path=/data/format.md "HTTP/1.1 200 OK"

🔴 /data/format.md
⚠️ EXPECTED:
# Header

| Start | Mid | End |
| :---- | --- | --: |
| 1     | 2   |   3 |

Paragraph has extra spaces and trailing whitespace.

```py
print("23f3003027@ds.study.iitm.ac.in")

[](#p-616683-result-header-1)
![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=14)
 RESULT:

Header

Start

Mid

End

1

2

3

Paragraph has extra   spaces and trailing whitespace.

print("23f3003027@ds.study.iitm.ac.in")

![:cross_mark:](https://emoji.discourse-cdn.com/google/cross_mark.png?v=14)
 A2 FAILED

I am facing Npx error... can I know what went wrong?
@carlton @Jivraj

---

### Post #425 by Jivraj Singh Shekhawat on 2025-04-07T15:11:38.703Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/425

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f300327/48/91361_2.png)
 23F300327:

I am facing Npx error... can I know what went wrong?

This
npx
 error is originating from your Docker container—it’s not being generated by our script. Try to look for what caused this error.

---

### Post #426 by Anushka Kumar on 2025-04-07T16:07:02.249Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/426

[![Screenshot 2025-04-07 213538](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/8/28ee8a9e3739e37d81cedf39142209af2d7f4090_2_690x311.png)

> **Image Description**: The image shows the Docker Hub interface for a user "coolsisters7" viewing the repository "llm". The interface displays repository details like the last push date (about 2 months ago), size (795.7 MB), and includes options to add a description or category. The "General" tab is selected, showing a table of tags for the repository. The table contains one entry with tag "latest", OS identified by an icon, type "Image", pulled "less than 1 day", and pushed "about 2 months" on "Feb 16, 2025 at 11:51 pm". On the right, the interface provides Docker commands for pushing new tags to the repository and information about Docker Build Cloud. The top navigation bar includes "Explore", "My Hub", a search bar, and account-related icons. A left sidebar provides access to "Repositories", "Settings", "Default privacy", "Notifications", "Billing", "Usage", "Pulls", and "Storage".
Screenshot 2025-04-07 2135381868×843 125 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/8/28ee8a9e3739e37d81cedf39142209af2d7f4090.png)

Oh I see what happened, the image names are different, I don’t know how, given I pushed the latest at 11:51pm and submitted the form at 11:59pm. Thank You
[@Jivraj](/u/jivraj)
 for showing me.

Question: Now that I know. how can I test the container myself, if I want to do exactly what you guys are doing?

---

### Post #427 by Mishkat Chougule on 2025-04-07T16:23:03.736Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/427

My code uses
npx
 to format Markdown files using Prettier, specifically via
subprocess.run(["npx", "prettier@3.4.2", "--write", ...])
, which assumes that
npx
 is available in the environment. However, since the Docker container is based on Linux and I didn’t explicitly install Node.js or
npx
, this results in an error during evaluation.

To test the functionality correctly,
npx
 must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:

bash:
 apt-get update && apt-get install -y nodejs npm

Once installed,
npx prettier@3.4.2
 should work as expected.

For reference, this approach worked perfectly when I tested the same task locally on my Windows 11 system, where
npx
 is available by default.

---

### Post #428 by Hilal on 2025-04-07T16:36:21.624Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/428

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

Before the project evaluation, I ran the test script and successfully passed all Task A and Task B checks. I also built the Docker image as required.

But, when you gus evaluated , I get the following error:docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: “uvicorn”: executable file not found in $PATH: unknown.

Could you please help me understand why this is happening even though the evaluation script ran fine?

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/c/9cd9e40f5ec0afeee28e1dcc5ad0340d2e5872d2_2_690x308.png)

> **Image Description**: Here's a concise description of the Docker Hub image:

The image shows a Docker Hub repository page for "hilalazeez/llm-automation-agent."  The "General" tab is selected.  It displays the repository's tags, showing one tag labeled "latest" with associated vulnerability information (1 critical, 4 high, 22 medium), a pull date of "1 day," and a push date of "about 2 months." A command line instruction,  "docker push hilalazeez/llm-automation-agent:t agname" is shown as a command to push a new tag. Finally, a Buildcloud Docker Build Cloud advertisement is present.
image1591×712 123 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/c/9cd9e40f5ec0afeee28e1dcc5ad0340d2e5872d2.png)

[![Screenshot 2025-04-07 192419](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/c/1cc811ef3cd38bebb7a22e0297e57ce6388e5c58_2_690x341.png)

> **Image Description**: The image shows a FastAPI documentation page in a web browser. It displays the available API endpoints: a GET request to "/ask" named "Ask," a POST request to "/run" named "Run Task," and a GET request to "/read" named "Read File." Below the endpoints, the page shows schema definitions for "HTTPValidationError" and "ValidationError," both described as "object." The FastAPI version is labeled as 0.1.0 and uses OAS 3.1.
Screenshot 2025-04-07 1924191534×760 38 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/c/1cc811ef3cd38bebb7a22e0297e57ce6388e5c58.png)

---

### Post #429 by Anushka Kumar on 2025-04-07T17:19:51.228Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/429

Can you tell me what application is this (FastAPI) one ?

---

### Post #430 by Bharat Choudhary on 2025-04-07T18:31:51.760Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/430

idk why i am doing this but this is my last request (for evaluation) with proofs. me and my friend both have same docker file code with missing flask dependency (i will try as much to not reveal his id/name) he got 12/20 even tough i tried same methods given by you and same error popped up flask module not found in his case but you gave him 12/20 marks but for me you gave 0? did i done something wrong? I know in industry level it matters much but right now we are students and for us CGPA matters. i am also uploading his docker file image and mine with 0 commits after 18th feb.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/8/78eaf46821c5af8d1f6844561dc235a1e22f6de7_2_690x377.png)

> **Image Description**: Here is a concise and factual description of the image for a Tools in Data Science student:

The image shows a code editor interface, specifically a Dockerfile open in a GitHub repository. The Dockerfile contains instructions for setting up a Python 3.12 environment with dependencies like SciPy, FastAPI, and other libraries. The code includes commands to install system dependencies, uv for package management, and Python packages using pip. It also sets the PATH environment variable, copies application files, exposes port 8000, and specifies the command to start the FastAPI server using Uvicorn. The interface also shows the repository file structure with a few Python scripts. The code editor's interface indicates that GitHub Copilot is being used and suggests potential code completion, claiming to provide a 55% faster coding experience.
image1670×914 67.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/8/78eaf46821c5af8d1f6844561dc235a1e22f6de7.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/0/300e62ae1bb91e990020843f9db4aab25bd9ac70_2_690x468.png)

> **Image Description**: Here's a concise description of the image for a student in a Data Science course:

The image shows a GitHub repository containing a `Dockerfile`. The `Dockerfile` is for a Python 3.12 application and installs necessary system and Python packages (e.g., `fastapi`, `uvicorn`, `scipy`, `pandas`). The `Dockerfile` also sets up a working directory, copies application files, exposes port 8000, and defines a command to start the FastAPI server using `uvicorn`. A handwritten annotation labels the file as "mine".
image1376×935 60.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/0/300e62ae1bb91e990020843f9db4aab25bd9ac70.png)

---

### Post #431 by Wasim Ansari on 2025-04-07T19:50:31.765Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/431

Dear Sirs,

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

[@carlton](/u/carlton)

As per the Project 1 deliverables, I had submitted my Docker Hub repo, that hosted the Docker image. At the time of submission, the image was running smoothly, was fully accessible, and was successfully handling the API calls as intended.

[![Screenshot 2025-04-07 233513](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7b8a704d618edd74036a95649a83054e29932879.png)

> **Image Description**: Here's a concise and factual description of the image:

The image presents instructions related to Docker and GitHub. It outlines the following steps:
1.  Create a Dockerfile for building an application.
2.  Publish the Docker image publicly to Docker Hub.
3.  Run the Docker image using a podman command:
    ```
    podman run --rm -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 $IMAGE_NAME
    ```
    This command maps port 8000 and passes an environment variable. The image automatically serves an API at the localhost URLs provided.
4.  Submit the GitHub repository URL (github.com/user-name/repo-name) and the Docker image name (user-name/repo-name).
Screenshot 2025-04-07 233513805×197 9.52 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/b/7b8a704d618edd74036a95649a83054e29932879.png)

Github repo submitted:

[GitHub - wasimansari-iitm/Project-AI-Agent](https://github.com/wasimansari-iitm/Project-AI-Agent)

Docker repo submitted:
 wasimansariiitm/my-ai-agent

The previous evaluation was successfully conducted using my Docker image, which was responding as expected. However, during the subsequent evaluation, the image was rebuilt using my GitHub repo link, and unfortunately, the
app.py
 file could not be found. As a result, my evaluation logs are missing from the evaluation logs bundle.

I would like to respectfully bring this to your kind attention that the
app.py
 file does exist in the repository, but it is located inside a subfolder:

[https://github.com/wasimansari-iitm/Project-AI-Agent/app/app.py](https://github.com/wasimansari-iitm/Project-AI-Agent/blob/main/app/app.py)
.

But as per the submission instructions, I provided the GitHub repo link only:
[https://github.com/wasimansari-iitm/Project-AI-Agent](https://github.com/wasimansari-iitm/Project-AI-Agent)
.

Humbly stating, I did not anticipate that the image will be rebuilt from the GitHub repo at a later stage due to some unforeseen circumstances. Had I known this, I would have made sure the project repo was structured appropriately to support that scenario. To be noted, that the earlier evaluation ran smoothly, and the app responded to all queries as expected.

I’m unsure what to expect now or request, but I just wanted to bring this issue to your notice. Even if I manage to get a single answer correct upon a successful evaluation, it would mean a lot to me and contribute meaningfully to my overall score. I would be extremely grateful if you could look into my case and extend your support in this matter.

Thank You and Regards,

24ds3000090

---

### Post #432 by Shivaditya Bhattacharya on 2025-04-07T20:42:10.131Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/432

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Sir, in my docker logs, the datagen script encounters error during creating the credit card image for A8 during which it fails to find both the fonts used in the try and except blocks, resulting in the datagen script to stop abruptly without creating the files for A8 to A10.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a49f182e22015df35039be85cdd26ad71a07f7a3.png)

> **Image Description**: The image shows a traceback error in Python code, likely related to font loading using the PIL (Pillow) library. The error "OSError: cannot open resource" occurs twice, initially when trying to load "arial.ttf" and subsequently when attempting to load "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf". The traceback points to the PIL ImageFont module and specifically the `truetype` and `freetype` functions, suggesting a problem with finding or accessing the specified font files.
image1298×857 29.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a49f182e22015df35039be85cdd26ad71a07f7a3.png)

I actually want to know if this could have been avoided by some changes in my code or is it an issue in the datagen.py script, because as the situation currently stands, my app wasn’t even tested properly for tasks A8 to A10 as the datagen.py script failed to create the required files because it could not find a font which as far as I knew was not specified that it must be included in my own code or image somehow.

Edit 1: I just realized that the datagen script looked for the fonts in python 3.13/site-packages/…

But my docker image is using the python:3.12-slim-bookworm. Could that be an issue? There was nothing specified about required python version or required python image to be used in docker in the project 1 requirements.

Edit 2:

Even if the font not being available is somehow my fault, A9 and A10 still should not be penalized for A8 without proper checking.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f99c9908823f381a7756ba6fe89d4827ca2faf4.png)

> **Image Description**: The image shows Python code, presumably for a data science project. The code begins with a standard `if __name__ == "__main__":` block. It imports the `argparse` module to handle command-line arguments. An `ArgumentParser` is created, and two arguments are added: "email" and "--root" (with a default value of "/data"). The parsed arguments are stored in the `args` variable. A configuration dictionary `config` is created with "email" and "root" keys assigned to values derived from the parsed arguments and the absolute path of the root directory. The `os.makedirs` function is used to create the directory specified in the "root" configuration, with `exist_ok=True` allowing the function to proceed without error if the directory already exists. Two print statements are executed to inform the user about the script's nature and the created files. Finally, a series of function calls like `a2_format_markdown()`, `a3_dates()`, etc., suggest the script performs several data-related tasks, such as formatting markdown, processing dates, working with contacts, logs, documents, emails, credit card images, comments, and ticket sales.
image1027×510 11 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/f/5f99c9908823f381a7756ba6fe89d4827ca2faf4.png)

Though an error occured in A8, A9 and A10 still could have worked if each of these function calls were enclosed in their own try-except blocks, ensuring independent checks for each task. But the current datagen.py script fails as error propagates to main, where it is not handled and causes abnormal termination without executing the functions for creating files for A9 and A10 as well.

Thank you.

Regards,

Shivaditya

---

### Post #433 by Carlton D'Silva on 2025-04-08T05:49:08.592Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/433

Hi Haricharan

Your Dockerfile does not build the repo. Its misconfigured.

This is the error when building it:

=> ERROR [8/8] COPY .env /app/                                                                                                                         0.0s
------
 > [8/8] COPY .env /app/:
------
Dockerfile:20
--------------------
  18 |     # Copy application files
  19 |     COPY *.py /app/
  20 | >>> COPY .env /app/
  21 |
  22 |     # Explicitly set the correct binary path and use `sh -c`
--------------------
ERROR: failed to solve: failed to compute cache key: failed to calculate checksum of ref 468faeeb-6d46-4aeb-a590-25bae24a84d5::y52oingx9lezoq9kjiwp6v58m: "/.env": not found

[![Screenshot 2025-04-08 at 11.12.18 am](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573_2_690x276.png)

> **Image Description**: The image shows code snippets from a `Dockerfile`. It includes commands to set up an application directory and copy files.  Specifically, it sets the working directory to `/app` using the `WORKDIR` command. Then, it copies all Python files (`*.py`) and a `.env` file into the `/app` directory using the `COPY` command.
Screenshot 2025-04-08 at 11.12.18 am754×302 41 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/4/84ca6c44a889d9afdd688d56fd169d99cb74a573.png)

This is because if you look at your Dockerfile .env does not exist in your repo.

Therefore it does not build.

Your docker is supposed to take the AIPROXY token from our environment not from yours.

This is passed dynamically at runtime of the Docker.

Since it fails to build, we cannot evaluate it.

Kind regards

---

### Post #434 by Carlton D'Silva on 2025-04-08T06:01:28.431Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/434

Your docker failed to build from your Dockerfile

 => ERROR [4/7] RUN uv --version                                                                                                                        0.1s
------
 > [4/7] RUN uv --version:
0.078 /bin/sh: 1: uv: not found
------
Dockerfile:25
--------------------
  23 |
  24 |     # Verify uv installation
  25 | >>> RUN uv --version
  26 |
  27 |     # Set working directory inside the container
--------------------
ERROR: failed to solve: process "/bin/sh -c uv --version" did not complete successfully: exit code: 127

Since we cannot build your docker from your Docker manifest file we cannot evaluate it.

---

### Post #435 by Carlton D'Silva on 2025-04-08T06:14:06.484Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/435

Your container failed to run after building it.

docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: exec: "uv": executable file not found in $PATH: unknown

Thats why we cannot evaluate it.

---

### Post #436 by Carlton D'Silva on 2025-04-08T06:29:24.100Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/436

There is
clearly

some difference
 between both the applications. That is up to you to figure out. I can only tell whats wrong with yours. After building it and trying to run it this is the error we get. It fails to run as a result and we cannot evaluate it.

Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 412, in main
    run(
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 579, in run
    server.run()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 999, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/app/app.py", line 23, in <module>
    from tasksB import *
  File "/app/tasksB.py", line 83, in <module>
    from flask import Flask, request, jsonify
ModuleNotFoundError: No module named 'flask'

---

### Post #437 by Carlton D'Silva on 2025-04-08T06:34:10.301Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/437

Noted your concerns wrt Edit 1 and Edit 2 (and datagen.py running latest python version): Will raise it with
[@s.anand](/u/s.anand)
 during our Wednesday meeting. Once we have an update, we will inform you of the outcome.

Kind regards

---

### Post #438 by Swati Kapoor on 2025-04-08T08:52:53.059Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/438

Hi,

Please let me know the reason on why I have not got any bonus marks.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a4b4614f55f231153c89c3de51b0c0ae60d44633.png)

> **Image Description**: The image presents a grading rubric for a project. It includes the submitted GitHub and Docker repositories.  It also displays a "Pre-requisites check" section, awarding 1 point for each passed prerequisite (Docker repo exists, GitHub repo exists, LICENSE file exists, Dockerfile exists). A table with rows A, B and C is used to show individual points given. Some cells are filled with 1's and 0's, indicating pass or fail. There is an entry for "Your task score is: 3", "Your bonus is: 0" and "Your P1 score is: 4". Finally, "Your final t score calculation is based on MIN (20, (task score + bonus))" is explained.
image1310×681 14.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/4/a4b4614f55f231153c89c3de51b0c0ae60d44633.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/40c10210a7c33774133ec99e68ad77a840209387_2_690x297.png)

> **Image Description**: The image shows a GitHub repository named "project1_final". The repository is public, has 2 branches and no tags. The active branch is "master" which is 8 commits ahead of the "main" branch.

The repository contains the following files and directories:
* `._pycache_`
* `data`
* `Dockerfile`
* `LICENSE`
* `app.py`
* `datagen.py`
* `evaluate.py`
* `llm_code.py`

The most recent commit message for the root directory is "last_minut" by "swati-iitm", made 2 months ago with 9 commits in the branch. The "About" section indicates that there is no description, website, or topic provided for the project. It is licensed under MIT license, 0 stars, 1 watcher, and 0 forks. There are no published releases or packages.
image1696×732 59.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/40c10210a7c33774133ec99e68ad77a840209387.png)

---

### Post #439 by Carlton D'Silva on 2025-04-08T09:37:52.730Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/439

We used some internal parameters with weights to auto calculate the bonus. Unless your submission met that threshold of 0.5 after scaling you would not get any bonus. Your score was normalised so instead of 3 you got 4 (3.75 got rounded up). But the metrics used to evaluate the quality of your submission only scored you at 0.007 which is far below the threshold required to get a bonus.

---

### Post #440 by D HARICHARAN  on 2025-04-08T13:24:46.118Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/440

Respected Sir,

Yes Sir, I said the same,
.env
 was not able to be uploaded to repo as .env file was not allowed to be uploaded

when we download the repository it doesn’t have the
.env
 file,

for docker image to build we need to add
.env
 with
AIPROXY_TOKEN

after that docker image will build, I had given about this in previous message

As you said Sir that you will use separate
AIPROXY_TOKEN
…you can put that in
.env
 file and build the docker image

after that Sir its optional to pass
AIPROXY_TOKEN
 again while running the docker Image

just the
.env
 file required, even without token in that it will work as project has support for both AIPROXY token in .env file and as environment variable

and when I uploaded to repository the .env file was not allowed to upload so had submitted that way, I actually forgot to add step for running the docker image in the previous message, the steps which I used:

git clone https://github.com/23f2001390/llmagent.git

adding
.env
 with AIPROXY token and replacing
evaluate.py
 and
datagen.py
 with new ones according to test environment

docker build -t llm-agent .

docker run -p 8000:8000 llm-agent
or
docker run -e AIPROXY_TOKEN=token -p 8000:8000 llm-agent

and in another terminal

uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000

Thank you

Kind regards

---

### Post #441 by S Sharmile on 2025-04-08T15:08:33.577Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/441

Respected sir

I understand it’s my mistake sir and I apologize for that sir, but please consider this time sir since because of this my entire project score went from 9/20 to 0, which would make me difficult to pass this course and continue my diploma.

Please consider this request sir, sorry sir and this would never be repeated in future. My project evaluation was 9/20 initially sir, but later it came down to 0 because of this issue. Kindly consider sir please.

Regards,

S Sharmile

23f3001688

---

### Post #442 by Jayaram on 2025-04-08T18:05:49.832Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/442

Thanks for relentless efforts
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

I tested the docker file in docker playground again.. Please find the screenshot of the docker build command and the log output of the docker build.. It went thru without issues..

Was the latest docker file used from git lab? Because as explained on March 30 i had to remove the hardcoded http/https proxies of  my office environment,

[![image (18)](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d_2_690x363.png)

> **Image Description**: The image shows a web interface from labs.play-with-docker.com, focusing on a specific instance identified as "cvqlfool_cvqlfsol2o9000cd7icg". The instance has an IP address of 192.168.0.13 and allows opening a port. It also displays an SSH connection string: "ssh ip172-18-0-93-cvqlfo012o9000cd7ic0@direct.labs.play-". Options to delete or edit the instance are present. Additionally, a terminal window shows the execution of a Docker command: "docker build -t tdsproject1:latest . > tds-projlbuild.log", suggesting a Docker image is being built.
image (18)1272×671 64.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/9/a90081b731c1b4fd6c4313837b50e3ca062d687d.png)

build output

#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 694B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/python:latest
#2 DONE 0.5s

#3 [internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [1/6] FROM docker.io/library/python:latest@sha256:aaf6d3c4576a462fb335f476bed251511f2f1e61ca8e8e97e9e197bc92a7a1ee
#4 DONE 0.0s

#5 [internal] load build context
#5 transferring context: 33B done
#5 DONE 0.0s

#6 [4/6] RUN uv --version
#6 CACHED

#7 [2/6] RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates &&     apt-get clean && rm -rf /var/lib/apt/lists/*
#7 CACHED

#8 [3/6] RUN curl -sSfL https://astral.sh/uv/install.sh | sh
#8 CACHED

#9 [5/6] COPY execute.py /
#9 CACHED

#10 exporting to image
#10 exporting layers done
#10 writing image sha256:2919fe6ce0097ae2fc33aebaba327dbd6a35d256b6d946c97c310fd992944add done
#10 naming to docker.io/library/tdsproject1:latest done

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59_2_690x54.png)

> **Image Description**: This image shows a commit history on GitHub dated March 30, 2025. The commit message reads, "Update Dockerfile removed hard coded proxies," authored by rsjay1976, verified and committed last week with hash a71e3a8.
image1480×117 9.41 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b8f94b7678326660ebf7803d7c08ae0433b0dd59.png)

---

### Post #443 by Jivraj Singh Shekhawat on 2025-04-08T21:11:14.726Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/443

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd6b7a633fa356674be001b8861629604fb08ea4_2_690x387.png)

> **Image Description**: The image shows a terminal output from a Docker build process. The build fails at step 4/7 with an error indicating that the "uv" command is not found. The Dockerfile, specifically line 25, attempts to execute "uv --version" to verify the uv installation. The output shows that the "uv" command is not recognized, suggesting that it was not successfully installed in the previous steps.
image1919×1079 301 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd6b7a633fa356674be001b8861629604fb08ea4.png)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002723/48/110636_2.png)
 22f3002723:

Was the latest docker file used from git lab

No, we are not allowing any changes to repo after deadline, this is consistent rule for every student. We pulled your github repo latest commit before 18th feb, I am getting following error.

---

### Post #444 by Jivraj Singh Shekhawat on 2025-04-08T21:22:40.342Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/444

follow the steps mentioned in post below
![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=14)

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

### Post #445 by Jivraj Singh Shekhawat on 2025-04-08T21:24:21.083Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/445

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f300327/48/91361_2.png)
 23F300327:

To test the functionality correctly,
npx
 must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:

That destroys the purpose of containerization, your container should run anywhere anytime, all the dependencies must be preinstalled.

---

### Post #446 by Jayaram on 2025-04-09T06:36:56.097Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/446

Thanks
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

As mentioned earlier, the pre Feb 18 dockerFile commited in GIT had  my office proxy url’s set as http_proxy and https_proxy.. It worked in my office envuironment and i tested everything in my office environment but based on the results which came on March last week realised that the proxies were preventing the uv to be installed in other environments.

Post that realised we have cloud based "docker playground’ utility where docker builds can be tested agonistic of any environment.. The good thing with playground is our instances last for only 3 hrs and next day we try we are kind of gauranteed of fresh environment without any caches,

Now after March 30th checkin validated the same in docker playground and ensured that the image got tagged and createdd successfully..

It would be great if the March 30th checkin could be considered, Again appreciate all your help so far.

---

### Post #447 by Saksham on 2025-04-09T08:03:10.683Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447

Subject:
 Request for Verification of Dockerfile and Reevaluation of Marks for Project 1

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Sir,

Regarding the recent feedback on
Project 1
 for
TDS
, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named
dockerfile
 (not
Dockerfile
). Please verify the repository again with this in mind.

Additionally, my Docker image architecture is
linux/amd64
 (64-bit
x86
). I have also filled out the
Architecture Information Collector
 form as requested.

Pre-requisites check: (1 for pass, 0 for fail)

Docker repo exists and is public (should have a timestamp before 18th of Feb): 1

Github repo exists and is public (should have a timestamp before 18th of Feb): 1

Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1

Gihub repo check - Dockerfile exists: 0

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/a/eaea99d88c244f6d9e7407183e4d96e2e1c35d2f_2_690x368.png)

> **Image Description**: Here's a concise description of the image for a Data Science student:

The image is a screenshot of a GitHub repository named "task_agent_api". It shows the repository's file structure in the "Code" tab, displaying files like 'app.py', 'datagen.py', 'dockerfile', 'requirements.txt' and others. The "About" section indicates that there is no description, website or topics provided. The page also shows the number of commits, branches, and other GitHub metrics like "Stars", "Forks", and "Watching". There are no graphs or tables visible.
image1914×1021 91.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/a/eaea99d88c244f6d9e7407183e4d96e2e1c35d2f.png)

Here’s the link to my GitHub repository:

[github.com](https://github.com/23f1001822/Task_agent_api)

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/8/d83b83eaf69931596b2cddbbfea39884f17e047a_2_690x344.png)

> **Image Description**: The image shows a GitHub repository titled "23f1001822/task_agent_api". The repository has 2 contributors, 0 open issues, 0 stars, and 0 forks. The repository's icon is a stylized image of a robot.

[GitHub - 23f1001822/task_agent_api](https://github.com/23f1001822/Task_agent_api)

Contribute to 23f1001822/task_agent_api development by creating an account on GitHub.

Docker repo submitted:

sakshamumate/task_agent_api

I kindly request a
reevaluation of my project marks
 based on these clarifications.

Thank you for your attention to this matter. Please let me know if you need any further information or clarification.

Best regards,

Saksham Umate ,

23f1001822@ds.study.iitm.ac.in

---

### Post #449 by Shivaditya Bhattacharya on 2025-04-09T08:53:21.417Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/449

Sir, I had posted the query on A8 and datagen exception. Is this a reply to that?

---

### Post #450 by Carlton D'Silva on 2025-04-09T09:01:46.982Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/450

oh yeah sorry, hit the reply to the wrong button, but yes its to your post.

---

### Post #451 by Carlton D'Silva on 2025-04-09T09:04:31.776Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/451

I’ve got good news for you and 30 other students. Thanks to your diligent debugging effort that we were able to find this bug. For now the fix is that we will not evaluate you on a8 and catch the datagen exception so as to not cause cascading failures.

Thanks and kind regards.

We will let you know the outcome of the evaluations soon.

---

### Post #452 by Jayaram on 2025-04-09T17:59:34.677Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/452

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

any way out for my earlier query ?

---

### Post #453 by Hilal on 2025-04-09T19:34:31.420Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/453

[@carlton](/u/carlton)

Thank you for the reply .But it was working when i ran the initial evalaute.py .If you don’t  mind could you tell what may have caused this to happen.

---

### Post #454 by Carlton D'Silva on 2025-04-10T05:31:59.952Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/454

Hi Hilal,

You have to recreate the test environment as shown in this post

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

[Tools in Data Science](/c/courses/tds-kb/34)

    To replicate the test environment:
Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can  run this code using uv.
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo
import argparse
import os
import zipfile

parser = argparse.…

That way you will be able to identify why the error was occuring.

The specific error itself means:

Docker is trying to run the command uv inside your container, but it can’t find the uv executable — it’s not installed or not in the system PATH inside the container.

If you did not run evaluate.py as specified in our live sessions by recreating the test environment and then running evaluate.py then it would not have reflected how your dockerised application would work.

Kind regards

---

### Post #455 by SP on 2025-04-10T19:06:44.256Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/455

sir for my project 1 i got a mail stating that the docker file isn’t public and that’s why prerequisite failed. but i checked it and it seemed absolutely perfect to me. Please look into this issue as my docker repo is public and absolutely as per the requirement.
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #456 by Jivraj Singh Shekhawat on 2025-04-10T20:32:26.287Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/456

Hi
[@22f3003083](/u/22f3003083)

Following was your submission, which is not a valid dockerrepo.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/f/cf43ec80b28a06b6a45f49123430da5b2d20bad6_2_690x94.png)

> **Image Description**: Here's a description of the image for a Tools in Data Science student:

The image shows a code repository interface, likely from a platform like GitHub. It displays a table with data related to a project.

*   **Search bar:** A search bar at the top contains the query "22f3003083/v1".

*   **Table headers:** The table has the following columns:
    *   Timestamp
    *   Email Address
    *   Link to the GitHub repository for Project 1
    *   Name of the image published on DockerHub

*   **Table data:** A single row is visible in the table with the following information:
    *   Timestamp: 2/16/2025 23:20:17
    *   Email Address: 22f3003083@ds.study.itm.ac.in
    *   GitHub Repository Link: https://github.com/22f3003083/TDS\_Project\_1
    *   DockerHub Image Name: 22f3003083/v1

The image suggests a connection between a GitHub repository ("TDS\_Project\_1") and a DockerHub image, with both linked to a specific user ("22f3003083"). The file has 1069 lines and a size of 127 KB.
image1829×251 22 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/f/cf43ec80b28a06b6a45f49123430da5b2d20bad6.png)

---

### Post #457 by SP on 2025-04-10T21:08:17.092Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/457

Now I feel so good getting 0.

0 is best.

---

### Post #458 by Jayaram on 2025-04-11T03:28:59.378Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/458

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

As requested earlier, Could you please reevaluate my submission.  The only change that had to be done post Feb 18 checkin was to remove my office proxies on Mar 30 from the docker file  to make it work in all environments.. It  would be great if this could be accomodated..

---

### Post #459 by Carlton D'Silva on 2025-04-11T05:58:23.286Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/459

Hi Jayaram,

Unfortunately, we are not able to relax restrictions on changes to your repo, regardless of the reason. We have kept this rule uniform for everyone. If we allow this change, then everyone has a legitimate reason to request changes and would make the rule meaningless because then everyone will be able to make corrections to their submission. We do not even allow spelling changes.

Kind regards

---

### Post #460 by Jayaram on 2025-04-11T06:10:41.470Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/460

Thanks for the response
[@carlton](/u/carlton)
 ..  just a small suggestion, to avoid scenarios like what i faced and also with softwares like docker/podman not being too windows friendly, i think students can find it easier if a dev/mock  linux env is provided for course term duration, instead of   everyone having to figuring out with AWS/Azure and all providers.. Anyway thanks and appreciate all the help

---

### Post #461 by Mahesh Singh Bohra  on 2025-04-09T03:15:45.709Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/461

Sir, I have done everything for my project, but I am getting zero. I have uploaded my Docker file, but the email says it is not public. Sir, this is affecting my grades — please help me out.
[@Carlton](/u/carlton)

---

### Post #462 by Jivraj Singh Shekhawat on 2025-04-11T09:50:21.807Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/462

These are your project 1 responses,

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/7/a73f7a58a671b757d3df0929df3e0aa912955e6c_2_690x115.png)

> **Image Description**: The image presents a table showing data related to student projects. The columns include Timestamp, Email Address, GitHub repository link for Project 1, and the name of the image published on DockerHub. Three entries are displayed, with email addresses of the form "23f1001236@ds.study.iitm.ac.in." GitHub repository links point to repositories named "tds_proj.git" and "tdsrepos.git" under the GitHub username "MaheshSingh01." The DockerHub image names correspond to the GitHub repository names, as "maheshsingh01/tds-proj" and "maheshsingh01/tdsrepos." The search query in the UI is "23f1001236."
image1737×291 23.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/7/a73f7a58a671b757d3df0929df3e0aa912955e6c.png)

We are considering latest submission which have docker repo
maheshsingh01/tdsrepos

which is not accessible publically.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/7/174c8e4e8ad4c6e537203447df3d370b0efa8782_2_690x350.png)

> **Image Description**: The image shows a 404 error page on Docker Hub. The URL in the address bar is "https://hub.docker.com/r/maheshsingh01/tdsrepos/tags", and the error message "Oops! The page you have requested was not found" is displayed prominently on a blue circle. The page also shows the navigation trail "Explore / maheshsingh01 / tdsrepos". The Docker Hub logo is visible in the top left corner, and the top right corner contains navigation options like "Sign in" and "Sign up".
image1866×949 92.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/7/174c8e4e8ad4c6e537203447df3d370b0efa8782.png)

---

### Post #463 by Mahesh Singh Bohra  on 2025-04-11T11:11:45.772Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/463

Sir, could you please check it once more? I think the issue has been resolved.
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #464 by Jivraj Singh Shekhawat on 2025-04-11T11:35:39.794Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/464

Since repo was not public during evaluation, we won’t be rechecking, or reevaluating.

---

### Post #465 by Farhan Zafar on 2025-04-11T15:22:07.060Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/465

[@Jivraj](/u/jivraj)
 I’ve completed all the required steps, but I’m still getting 0, It was working fine before. Could you please help me identify what might be going wrong?

---

### Post #466 by Jivraj Singh Shekhawat on 2025-04-11T15:56:08.835Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/466

Hi
[@21f3003107](/u/21f3003107)

You need to look it up yourself, We have sent out evaluation log and docker log files, check those out.

Evaluation script and other scripts that we have used are there in github repository over here.

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/1)

If there is some mistake from our end let us know about it.

To replicate test environment follow steps provided below.

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

### Post #467 by WAGISHA TANYA RAI on 2025-04-11T18:16:52.479Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/467

[@carlton](/u/carlton)
 Requested sir

This is to request that in my evaluation a got 0 cause of the use of lowercase d instead of uppercase D but I have already submitted the  docker file in my git hub repo also.

[![WhatsApp Image 2025-04-11 at 23.34.06_a49fd1e5](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/3/1312efae69b50e418bc708a80bd11f752a9be4a5_2_627x500.jpeg)

> **Image Description**: The image shows a GitHub repository listing its files and their commit history. The files include: .dockerignore, .gitattributes, .gitignore, LICENSE, README.md, app.py, datagen.py, dockerfile, evaluate.py, requirements.txt, tasksA.py, and tasksB.py. Most files were "added" two months ago, with ".gitattributes" marked as "Initial commit" also two months ago. The repository is owned by "wag28," with commit ID "eff178a."
WhatsApp Image 2025-04-11 at 23.34.06_a49fd1e5912×727 79.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/3/1312efae69b50e418bc708a80bd11f752a9be4a5.jpeg)

---

### Post #468 by Hilal on 2025-04-12T07:38:59.014Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/468

[@carlton](/u/carlton)

Thank you i found my mistake in my docker file i wrote  this  CMD [“uv”, “run”, “app.py”]  instead of

CMD [“uvicorn”, “main:app”, “–host”, “0.0.0.0”, “–port”, “8000”].Now i think everything works fine

---

### Post #469 by Mahesh Singh Bohra  on 2025-04-14T07:06:19.259Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/469

Sir my repo was public

---

### Post #470 by Shivaditya Bhattacharya on 2025-04-14T10:10:56.167Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/470

Sir any news on this? Did my score increase at all? My dashboard still shows the old score.

---

### Post #471 by Adarsh kumar on 2025-04-14T20:39:18.125Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/471

[@carlton](/u/carlton)
 sir, my project 1 marks have still not increased even though while during evaluation it shows 4/10 for the task 1. It was said that the docker image prerequisite will be removed and without that the evaluation would be done, but there is still no change in my marks. please look into it once, as my dashboard currently reflects 0 for project 1.

---

### Post #472 by Carlton D'Silva on 2025-04-15T07:49:58.000Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/472

These evals are being handled separately. They have not yet been completed. Kindly bear with us till they are complete.

---

### Post #473 by Maulik Dang on 2025-04-15T11:06:47.111Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/473

Same here
[@carlton](/u/carlton)
 in my evaluation logs i have scored 10 while marks being reflected are not the same neither on mail nor on site

---

### Post #474 by Jivraj Singh Shekhawat on 2025-04-15T11:31:06.090Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/474

I looked at your evaluation logs and it says 1 score instead of 10.

---

### Post #475 by Garima on 2025-04-06T15:40:39.389Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/475

Good evening!

[1000092114|690x198](/uploads/short-url/30ijyIo5UiUUEVvnPZklfYVY2mI.jpeg)

I am writing to you to request you please relook into the evaluation.

The docker image which I share is working at my end.  The size of the image is 6 GB which may take more than 5 minutes to load as I wasn’t aware of the infra level restrictions.

I request you to kindly consider my request and please re-evaluate the assignment as I have contributed a lot of effort into it.

Thanks,

Garima

---

### Post #477 by Adarsh kumar on 2025-04-17T04:48:37.091Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/477

Sir, so will my score get updated because now it is marked as 0.

---

### Post #478 by Saksham on 2025-04-17T06:17:58.394Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/478

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Sir,

I am Saksham Umate and my project 1 was to be re-evaluation because of docker file not found in root ,but it was their so you had given me confirmation that it will re-evaluate after end term. I had already shared my docker file systems configuration at docker hub

So, I hope you will look at this and re-evaluate my project as I put lots of efforts to complete it

Tell me if any information is needed about project from my side

Thank you!

Best regards,

Saksham

My docker repo details in previous post:

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001822/48/66833_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447)

[Tools in Data Science](/c/courses/tds-kb/34)

    Subject: Request for Verification of Dockerfile and Reevaluation of Marks for Project 1

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Sir,
Regarding the recent feedback on Project 1 for TDS, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named dockerfile (not Dockerfile). Please verify the repository again with this in mind.
Additionally, my Docker image architecture is linux/amd64 (64-bit x86). I have also filled out the Architecture Information Collector form as requested.
P…

[![IMG_20250417_114002](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f8ee39bed46e6f2a196634ca56106c56c42003d_2_259x500.jpeg)

> **Image Description**: Here's a concise and factual description of the image for a student in the Tools in Data Science course:

The image is an email stating that a student's P1 assignment failed a prerequisite because the script couldn't locate the Dockerfile in the base of the root directory of their GitHub repo. The requirement is being relaxed.  P1 submissions will be looked at separately after the end term only. The email specifies that the instructor will run a script to search the student's GitHub directory tree for the Dockerfile. It also notes that no changes to the GitHub repo after February 18th will be considered and that no spelling deviations will be accepted for the required files.  The Docker image must build without errors from the Dockerfile and become operational within 5 minutes of starting. The email concludes by stating that evaluations will be carried out exactly according to the specified test environment.
IMG_20250417_1140021080×2083 469 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/f/3f8ee39bed46e6f2a196634ca56106c56c42003d.jpeg)

---

### Post #479 by Jivraj Singh Shekhawat on 2025-04-17T06:30:08.297Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/479

Evaluations are done for such cases where Dockerfile(with name of Dockerfile as
Dockerfile
) was present inside other folders than root folder of your github repo.

---

### Post #480 by Shivaditya Bhattacharya on 2025-04-17T06:38:10.952Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/480

[@carlton](/u/carlton)
 sir, any info on outcome of
[this bug in P1 datagen.py](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/451)
 ?

---

### Post #481 by Saksham on 2025-04-17T07:18:36.089Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/481

Did Mark’s are updated or being update for this students ?

---

### Post #482 by Jivraj Singh Shekhawat on 2025-04-17T07:34:59.259Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/482

Hi
[@22f3000819](/u/22f3000819)

We had updated datagen.py(try block for task) which affected 30 students, but scores changed only for 4 students, for others it remained the same.

---

### Post #483 by Jivraj Singh Shekhawat on 2025-04-17T07:35:35.739Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/483

We will be pushing marks today.

---

### Post #484 by Shivaditya Bhattacharya on 2025-04-17T07:40:39.300Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/484

I probably wasn’t 1 of the 4, right? Anyways thanks for paying attention to the matter.

Regards,

Shivaditya

---

### Post #485 by S Sharmile on 2025-04-17T13:58:06.029Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/485

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Respected Sir,

I hope you are doing well.

This is with reference to your confirmation mail that my project 1 will be re-evaluated after end term

I would like to sincerely apologize for the oversight in my Project 1 submission. Upon reviewing my GitHub repository, I realized that the file was named
dockerfile
 (with a lowercase ‘d’) in the Github root repo instead of the required
Dockerfile
 (with an uppercase ‘D’).

While the contents of the file were correct and my project passed several evaluation tests, I understand that the evaluation script could not detect the Dockerfile due to this naming issue. I genuinely did not intend to deviate from the standard, and I now fully understand the importance of following naming conventions precisely.

I humbly request you to kindly consider this as an honest mistake and allow a one-time exception, Please sir. This issue has unfortunately resulted in my project score being reduced to 0, which puts my overall course performance at risk. I assure you that I have learned from this experience and such an error will not occur again in the future.

So, I hope you will look at this and re-evaluate my project as I put lots of efforts to complete it.

Thank you very much for your time and consideration.

Warm regards,

S. Sharmile

Roll No: 23f3001688

---

### Post #486 by Adarsh kumar on 2025-04-17T17:03:34.931Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/486

Sir, my marks still did not get updated, please help me in that regard.

---

### Post #487 by Carlton D'Silva on 2025-04-18T03:36:17.392Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/487

Hi Everyone,

We have sent the updated marks to Operations. At this time of the term they are very busy with lots of updates, so it will take time for them to push it to the dashboard. As soon as they inform us that the scores have been pushed, we will send out a discrepancy form if you find any issues with your score.

Thanks & Kind regards

---

### Post #488 by Adarsh kumar on 2025-04-18T13:54:05.934Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/488

Sir, my project 1 marks are still 0 even though I had passsd few cases. Please help me sir as my final score is coming as 69.8 , it will be very valuable for me if it crosses 70, please sir help me with this regard

---

### Post #489 by Saksham on 2025-04-20T09:05:20.485Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/489

[@carlton](/u/carlton)

Hi Sir,

I hope you’re doing well. I just wanted to let you know that I put a lot of effort into completing
Project1
, but I accidentally named the
Dockerfile
 as
dockerfile
 (with a lowercase ‘d’).

Could you please consider evaluating it with that name? I’d really appreciate it.

Thank you!

My discourse post for more information:

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001822/48/66833_2.png)

[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447)

[Tools in Data Science](/c/courses/tds-kb/34)

    Subject: Request for Verification of Dockerfile and Reevaluation of Marks for Project 1

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

Sir,
Regarding the recent feedback on Project 1 for TDS, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named dockerfile (not Dockerfile). Please verify the repository again with this in mind.
Additionally, my Docker image architecture is linux/amd64 (64-bit x86). I have also filled out the Architecture Information Collector form as requested.
P…

---
