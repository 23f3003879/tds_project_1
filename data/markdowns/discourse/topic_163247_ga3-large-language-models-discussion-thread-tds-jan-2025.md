---
title: "GA3 - Large Language Models - Discussion Thread [TDS Jan 2025]"
topic_id: 163247
slug: "ga3-large-language-models-discussion-thread-tds-jan-2025"
original_url: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247
downloaded_at: "2025-06-18T15:42:07.368239"
---

### Post #1 by Anand S on 2025-01-14T13:00:03.324Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/1

Please post any questions related to
[Graded Assignment 3 - Large Language Models](https://exam.sanand.workers.dev/tds-2025-01-ga3)
.

[](#p-579668-important-instruction-1)
Important Instruction

Please use markdown code formatting (fenced code blocks) when sharing code in Discourse posts. This makes the code much easier to read and differentiate from non-code text. It also makes it easier for people to copy code snippets and run it themselves. See below code for example

ping exam.sanand.workers.dev

Pinging exam.sanand.workers.dev [104.21.31.149] with 32 bytes of data:
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58

Ping statistics for 104.21.31.149:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 8ms, Maximum = 9ms, Average = 8ms

Visit this link for more details:
[Extended Syntax | Markdown Guide](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks)
.

A friendly suggestion: kindly go through
[Discourse Docs](/c/docs-discourse/45)
!
![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12)

Deadline:
Sunday, February 2, 2025 6:29 PM

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

[@Saransh_Saini](/u/saransh_saini)

---

### Post #2 by Anand S on 2025-01-14T13:06:47.583Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/2

---

### Post #3 by Nilay Chugh on 2025-01-15T12:20:05.475Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/3

how to get the dummy API key?

---

### Post #4 by Jivraj Singh Shekhawat on 2025-01-15T14:59:06.607Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/4

Hi Nilay,

In order to make a api call to openai chat completions you are required to send authentication information(openai key) in headers. For first question of GA3 you don’t have to send actual(working) api key, any dummy api key would work(you can put your name, or tds anything works)

kind regards

---

### Post #6 by Nilay Chugh on 2025-01-18T04:43:01.431Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/6

which API should i use in 7th question

---

### Post #7 by Guddu Kumar Mishra  on 2025-01-19T07:36:55.428Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/7

need help in question 4th. how can i correct this json body? sir
[@Jivraj](/u/jivraj)

{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": "Extract text from this image."
    },
    {
      "role": "user",
      "content": {
        "image_url": "data:image/png;base64,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"
      }
    }
  ]
}

error:The JSON body must have 1 message

{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": {
        "text": "Extract text from this image.",
        "image_url": "data:image/png;base64,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"
      }
    }
  ]
}

Error: The message must have a 2 content parts

---

### Post #8 by Guddu Kumar Mishra  on 2025-01-19T16:53:34.970Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/8

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
  sir plz see it once.

---

### Post #9 by Jivraj Singh Shekhawat on 2025-01-21T07:02:52.278Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/9

Hi
[@22f3001315](/u/22f3001315)
 ,

You are almost correct, there are very minor changes that needs to be made.

Take help from Chat GPT or use this documentation which have correct json body
[Vision - OpenAI API](https://platform.openai.com/docs/guides/vision)
.

Kind regards

Jivraj

---

### Post #10 by Guddu Kumar Mishra  on 2025-01-21T08:21:45.804Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/10

it worked thanks sir

---

### Post #12 by Muhammed Adhil Pt on 2025-01-21T11:25:57.882Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/12

Are we supposed to buy open ai api key ?

---

### Post #13 by Sakthivel S on 2025-01-21T12:01:17.870Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/13

No, if you scroll down to the last question, we can get our Ai Proxy key

---

### Post #14 by Carlton D'Silva on 2025-01-21T12:06:09.235Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/14

[@nilaychugh](/u/nilaychugh)

[@22f3002034](/u/22f3002034)

The API key is available at
[https://aiproxy.sanand.workers.dev/](https://aiproxy.sanand.workers.dev/)

The instructions on how to use the token is given at
[GitHub - sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy)

You cannot use this token directly with Open AI or any other gpt. These are only valid via the API exposed by the above instructions.

You get a limit of $1. Use with care.

Kind regards

---

### Post #15 by Nilay Chugh on 2025-01-21T14:30:30.322Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/15

but the embedding model that is said to be used is text embedding 3 small, which is the model of OpenAI

---

### Post #16 by Jivraj Singh Shekhawat on 2025-01-22T09:13:43.408Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/16

Hi Nilay,

Yes you would need to use
text-embedding-3-small
 model of openai for embedding questions.

Kind regards

Jivraj

---

### Post #17 by Nilay Chugh on 2025-01-23T03:52:39.679Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/17

i have a doubt, while submitting the GA3, both 7th and 8th questions require the API url to be active and connected right, but its not possible as both the URLs use same port, so if we check my 7th question URL is running right now, it’ll show as correct, but then if i  run 8th question URL, the 7th question will automatically show the error,
is there any solution to this problem?

---

### Post #18 by VIKASH PRASAD on 2025-01-23T06:09:55.493Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/18

Q5.  How to handle the error ? sir
[@Jivraj](/u/jivraj)

Error: The first input does not match the first text exactly

---

### Post #19 by VIKASH PRASAD on 2025-01-23T06:17:12.711Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/19

Q4. How to handle this error?
[@Jivraj](/u/jivraj)

{
  "id": "chatcmpl-AshDCPwSiXNao1QXmCxCmi63GifFx",
  "object": "chat.completion",
  "created": 1737599182,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The image contains an email address and a number. The email address appears to be associated with an educational institution, and the number seems to be a numerical sequence.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 592,
    "completion_tokens": 33,
    "total_tokens": 625,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_bd83329f63",
  "monthlyCost": 0.05490624000000001,
  "cost": 0.001974,
  "monthlyRequests": 14,
  "costError": "crypto.createHash is not a function"
}

Error: Model must be gpt-4o-mini

---

### Post #20 by Jivraj Singh Shekhawat on 2025-01-23T10:58:14.611Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/20

Hi Nilay,

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/nilaychugh/48/84996_2.png)
 nilaychugh:

both the URLs use same port,

You can run two servers on different port numbers.

---

### Post #21 by Jivraj Singh Shekhawat on 2025-01-23T11:05:13.578Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/21

Hi Vikash,

I looked at your answers in backend. In answer you submitted response from openai, but you need to submit json object which is required for sending a request to LLM.

Kind regards

---

### Post #22 by Jivraj Singh Shekhawat on 2025-01-23T11:07:22.861Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/22

You made same mistake here, instead of response use json body that’s required for sending request to LLM.

Kind regards

---

### Post #23 by VIKASH PRASAD on 2025-01-24T01:17:21.325Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/23

Q4. how to handle this error ?
[@Jivraj](/u/jivraj)

{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Extract text from this image"},
        {
          "type": "image_url",
          "image_url": { "url": "data:image/png;base64,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DOYQc83d7la67bar84q8XbP//qXbYYfS9YuJSdsaR+6nbLvsUsfWGWeU7n3vK93225du881L96Uvla4X6JP3+8X35P173KPeW77mwd12K92mm5bujW+sfVQ5+kX/ZNzvumvp+kXOanZa6KVeyqz8/cJ1UrfpuSOvvPLKK691+1rWM/UiPyLDokEPe1gp1752jYaJdvVOr/QOYhKV6x3UJDLXcGSlF9mld7aTiJBt38XSO9FJtEz02fa3yNdVrlLKXe5Sj9/YdhYNl6fImoi6yOed7lSjaragHaF46ENrNPl736vpeyFQeqc62SoXLRX9Ug/b7I78qIfomyi9yJ4ovnv2AmGSv8iX4yreEzkUlWcX+ftpK7t3ymdxm9vU4wei3yKM8h2D3dRZBE19+4VAudKV5j6cws6E6NxrXlMjbHe9a42GDukFwCTiLwpnO/+Rj6z2m4a9eqFUHve4GiV0nTqHsNIwLh05GY4P85D5qBfNk503O12i24udr0S8Rfnt8Pnc+DVOhuPctXZS+gXAJK37iNr3Yn0SDfe5a8whyvTyl9fovflDeey63fe+9ViOeUC+5gjjWEReOaVXN0d6+oXI5IiifO3APeQh9SiiHZ42j4q2mx/tNngtFrsadvfa/BlCCGHlsayintPYaqtSXvjCKlL9bbvYNjBnw7FxVqedVtOffnp1UEccUR3btttWB0hoNzgmDorod/SmHV0hwglbju/JTy7lEY+o29TuxcnJ2zEZIrhfzUxenKb3CFvHcjhc5eNELQo4T+WwnW3r3Ra1ow62vpVb3u5BuMuLo1W+612vlMMPr2W3pS5PL+J+ww3rVj+RrlzS7r9/KQ96UCkbbDBXyR5pLDIc/yEglHcM2/e22ZV1111XCYsx1IN9iZeddqr3bmdnm+0//ekqMHbeuQp/9T7wwCqGHvCAUp71rGpzP9lfWmW3SCF2iBcor8WLYwy77VbbcvvtSzn44LpAmsYC69BDa7r2evSj63GZ1j/mQ7scdVQVQO1aYu3446sAme4vjj886lHVbur8speVcthhdRFKgEE9LG4II/3KZyCKCCj97V73qvfae+9a91ZONhu7FmxicaiPKt+pp859MIdjF45GPP7xtW21i2MXjlYcdFA9EmI8WZgph7zYyZERotHRiPZyf+Vj95afoxePfeyq9w85ZLw9xrC4bNe213xt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u8WDcehevqFFP4N89S12sTg3P8h/DAsSbUzAa2NtpY+ab/R3/VAZlGVN5ivzhbpb7LKxvsuW7qeNzFe+KrKNafmbGyyEzQ36pHmEgCfS1U2ZlE1gwNgzBo1X+Rqn6ihw0fLV/7S7er3ylXWh6z35e1lUSMtGymtctP5rblAffYE9jTMP5hvr2mwabehBdu2hb3n+pbVHCCGEdc/6z+iZ+30R9J5zDeCEOCNb2y1SxBkMX8QTAeQnZzQNB+w6IpjAGDobwsJ1RI17EJTSi4o5KiE/ESwvQqaJT++7VnpOlMDg8OSvTMQgIShti5qrByEqL2mJGPcWfSNIiC9pOUjOVDpnpznT6Tq7H8HgGk6YEyUy50ur/mzkvsrN6fudIFUvkVR1mQ/p2cc95Dmd1t/qR0BZCBElykRsEBTqomzawAKC4PK58hNpIoUELQFMzItEawf3IrIJEW3CXkSUa7xEdC0MfO4lrfZodVdeUVR2bEK/CSeiSX6u0dZ+tnt6sZdrLQq0G7vJm4iRnl3dX1rl1fby8H4rp2vZTb2l0b6u97l+qAxso/8RWu5pgae9Wr8BMW4hpg677FLzcr2+wl7Ekn5EQOqbriWOjRll1j5NZLqXeiqrdmA35VGXVh79Vzptp96Qj/5i4el3+EwaaV2jTyuLhZI6EI3SKo/f3bONEfck+tlI2V3vxdbqp0+61qulN548N6HfqNOwLdm9oX3YktD2ub6u3Pog+zfkIW/9hG2kHYPd2YltXKMu+p1+RZy7lh3WdL5qc4Z2YBt1dQ/XmT/YZ1gvNvFSFnaSn3rpO+zo+jYvaW92kM41ymzMeVhXmZugl177yMtPZVEm5dMeFpDq4zN9zk+fqa+08tHX9Nv2z6XGBH1D2ZSTzZV92B4hhBDWLcsaqQ+zA4EpSuzbLU45pQovAp6wJ0LGFlzO4Ypc2zEQ+SMUnGUf23X5X8UCzy6Qc9QEn3+IRQgRRyGEEEIIS0VEfVgN0VPHPrxEAX0LjSiwiOE0jhE4AuIIgsikozSivqFGvD0E6Qy1o1L+dszDgieEEEIIYamJqA+r0b41gxh1BthZZed7HROaxvEIItU/9RGlF50fi+j/L+IM9xFH1HPRjo3sums9389OIYQQQghLTUR9GIW4d7beA4B+OkYyTTtfTtyH1fEQoqNJvlnEmWjnrJ0dDyGEEEJYDiLqQwghhBBCmHHyuF4IIYQQQggzTkR9CCGEEEIIM84aHr8JIYQQQgghrDQSqQ8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYaYp5f8A91ro9coVvFcAAAAASUVORK5CYII=" }
        }
      ]
    }
  ]
}

Error: The image_url.url must be the base64 data URL of the image

---

### Post #24 by VIKASH PRASAD on 2025-01-24T02:02:04.952Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/24

Q8. how to handle the error ?
[@Jivraj](/u/jivraj)

[http://127.0.0.1:8000/execute?q=Expense+balance+for+emp+52094](http://127.0.0.1:8000/execute?q=Expense+balance+for+emp+52094)

{“name”: “expense_balance”, “arguments”: “{“employee_id”: 52094}”}

TypeError: Failed to fetch

---

### Post #25 by Varad Rajadhyax  on 2025-01-24T08:17:52.778Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/25

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/d/1d37c6ff7591a3175f7be06068d9025f2627e65b_2_690x314.png)

> **Image Description**: The image displays a dark-themed user interface, likely for an online assignment or assessment. A top bar indicates a due date of "Due Sun, 2 Feb, 2025, 11:59 pm IST" and a current "Score: 2.75 / 8.5". This bar also includes "Check" and "Save" buttons. Below, a "Recent saves" section lists three identical entries from "24/1/2025, 12:25:51 pm" with a "Score: 2.75" and a "Reload" command. The lower part of the interface presents a "Questions" section, enumerating nine distinct questions with their respective mark allocations:
1. LLM Sentiment Analysis (1 mark)
2. LLM Token Cost (0.75 marks)
3. Generate addresses with LLMs (1 mark)
4. LLM Vision (1 mark)
5. LLM Embeddings (0.75 marks)
6. Embedding Similarity (1 mark)
7. Vector Databases (1.5 marks)
8. Function Calling (1.5 marks)
9. Get an LLM to say Yes (1 mark)
image1366×622 27.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/d/1d37c6ff7591a3175f7be06068d9025f2627e65b.png)

Why is my score is out of 8.5? It should be 9.5 right?

It was 9.5 before a reload.

---

### Post #26 by Sakthivel S on 2025-01-24T08:37:26.081Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/26

You should answer the third question every time the site reloads

---

### Post #27 by Varad Rajadhyax  on 2025-01-24T10:06:51.736Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/27

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/c/ac8e969c93aa57f9b61d8e5a90ddf2a6174220e5.png)

> **Image Description**: The image displays a programming task in a Python environment. At the top, an example Python dictionary named `embeddings` is partially visible, showing a phrase key and a list of numerical values representing an embedding. Below this, a prompt instructs the user to "write a Python function `most_similar(embeddings)` that will calculate the cosine similarity between each pair of these embeddings and return the pair that has the highest similarity." An empty code input area is labeled "Write your Python code here:". Beneath the input area, a `PythonError: Traceback` is visible, ending with `NameError: name 'most_similar' is not defined`, indicating that the function was called but not found.
image1122×471 13.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/c/ac8e969c93aa57f9b61d8e5a90ddf2a6174220e5.png)

For question no.6, there was some pre-written code there, right?

I am not able to see it now.

---

### Post #28 by Varad Rajadhyax  on 2025-01-24T10:17:59.703Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/28

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/4014d114b8ab5a993183871727062efe6a839400.png)

> **Image Description**: The image shows a console output after running a Python script named "request.py". The script execution resulted in an error indicating that the user has exceeded their current quota. The error message provides a link to OpenAI's documentation for API errors. Specifically, the error is classified as "insufficient_quota" with a `param` value of None.
image1017×146 6.62 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/4014d114b8ab5a993183871727062efe6a839400.png)

I am getting insufficient_quota message for the 2nd question

---

### Post #29 by Jivraj Singh Shekhawat on 2025-01-27T22:32:35.315Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/29

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f3002277/48/12741_2.png)
 21f3002277:

The image_url.url must be the base64 data URL of the image

I tried downloading image for your dataset it is 2.36 KB in size.

Using base64 encoded string from
image_url.url
 in your code when decoded comes out to be 8.18 KB, when I encoded image from your dataset and decoded it was 2.36 KB.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/a/aa81c404ee3eb793693a5bc6406886bd079e1635_2_690x347.png)

> **Image Description**: The image displays a web interface for decoding Base64 encoded image data. It includes a text area labeled "Base64*" containing a Base64 string for a PNG image, followed by a "Decode Base64 to Image" button. Below this, a "Preview Image" section shows the decoded image, which displays the text "21f3002277@ds.study.iitm.ac.in 92893354" highlighted in yellow. A "File Info" section provides metadata for the decoded image: Resolution 757x66, MIME type image/png, Extension png, Size 8.18 KB, and Bit depth 8.
image1518×765 95.5 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/a/aa81c404ee3eb793693a5bc6406886bd079e1635.png)

Hints : check if encoding is correct.

---

### Post #30 by Abhay Sharma on 2025-01-28T04:11:34.779Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/30

Is it required to give SCT for the ROE of this course?

Thank you.

---

### Post #31 by Carlton D'Silva on 2025-01-28T06:51:33.648Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/31

SCT is not required for ROE. ROE is not proctored.

Kind regards

---

### Post #32 by K Hari Prasath on 2025-01-28T07:44:51.739Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/32

This is regarding Question 2 I tried to find number of tokens for the message. Using chatgpt identified the followings are valid English words for the given text in the question
D

m

Ay

E r u y Vy

V Ky

P

c
. then, checked with
[https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)
. whatever number given by it seems to wrong.

[@Jivraj](/u/jivraj)
 could you inform me where I did mistake

---

### Post #33 by Carlton D'Silva on 2025-01-28T07:59:50.162Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/33

[@23f2003853](/u/23f2003853)
 You have to find the input tokens from the json response you receive from the proxy.

---

### Post #34 by Jivraj Singh Shekhawat on 2025-01-28T11:38:08.793Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/34

Hi VIKASH,

This problem must be because CORS not enabled or you are running your application inside wsl, if you using WSL then you would need to identify ipaddress of WSL and use it in place of
127.0.0.1

kind regards

---

### Post #35 by K Hari Prasath on 2025-01-28T11:48:12.076Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/35

Sir, from where can I  learn to locate the json response

---

### Post #36 by Jivraj Singh Shekhawat on 2025-01-28T12:05:37.192Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/36

Hi
[@23f2003853](/u/23f2003853)
 ,

You can learn from
[Python’s Requests Library (Guide) – Real Python](https://realpython.com/python-requests/)
 tutorial about how to use requests module and see responses.

kind regards

---

### Post #37 by Jivraj Singh Shekhawat on 2025-01-28T12:17:58.201Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/37

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000445/48/96290_2.png)
 22f3000445:

I am getting insufficient_quota message for the 2nd question

Which url are you using to send request to openai.

---

### Post #38 by Jivraj Singh Shekhawat on 2025-01-28T12:20:15.821Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/38

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000445/48/96290_2.png)
 22f3000445:

For question no.6, there was some pre-written code there, right?

pre-written code is not required for question 6.

---

### Post #39 by Divyasree on 2025-01-28T18:05:18.879Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/39

In the 6th question ,as I open the graded assignment all the time the new question is generated (NUMERICAL DATA) and the previous answer shows as incorrect answer

My doubt is that should I again and again answer the same quetion(6) all the time until the due passes?

Is there any alternative ways to look after this problem?

---

### Post #40 by Saniya Naaz on 2025-01-29T04:19:54.016Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/40

[![Screenshot 2025-01-29 094832](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/b/ebc5f88e712a270b0763135c5a220d2fcd690c71_2_690x256.png)

> **Image Description**: The image displays a dark-themed code editor showing Python code and its execution output. The Python code defines a user message containing a prompt to extract valid English words from a list of alphanumeric strings. Following this, it attempts to make an API request using `requests.post`. The output below the code indicates that the request failed with an HTTP status code 429. The accompanying JSON error message details that the failure is due to an "insufficient_quota" with the message "You exceeded your current quota," and provides a link to the OpenAI platform documentation for further information.
Screenshot 2025-01-29 0948321770×659 35.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/b/ebc5f88e712a270b0763135c5a220d2fcd690c71.png)

how to solve???

---

### Post #41 by Saniya Naaz on 2025-01-29T04:49:26.483Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/41

getting quota full message for 7th question. How to get the answers then?

---

### Post #42 by Jivraj Singh Shekhawat on 2025-01-29T15:28:56.065Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/42

Hi
[@Divya1](/u/divya1)
 ,

Question 6 requires to write a generic code for finding most similar pair. If your code is doing so, pls mention exact steps that you have used to arrive at answer.

---

### Post #43 by Jivraj Singh Shekhawat on 2025-01-29T15:30:02.829Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/43

[sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy)

Are you using this document?

---

### Post #44 by K Hari Prasath on 2025-01-30T12:16:03.021Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/44

each time when I run the following code it gives me different number. None of the answer is correct. can help to fix the issue

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/e/1ec36689ada1168f9ad8b8d208eea27a96d39df5.png)

> **Image Description**: The image displays Python code in a web-based integrated development environment, likely for data science tasks. The code demonstrates interaction with the OpenAI API for chat completions.

Key components visible include:
*   **API Endpoint Setup:** Defines the `url` as `https://api.openai.com/v1/chat/completions` and sets up `headers` including `Authorization` (with a `Bearer` token) and `Content-Type: application/json`.
*   **Input Message Definition:** A `user_message` string instructs the model to "list only the valid English words from these" followed by a comma-separated list of alphanumeric strings (e.g., "Q8YpaF2BS, qXGsuF, zyCIAGM, jfXCU").
*   **Payload Preparation:** A `data` dictionary is constructed for the API request, specifying `"model": "gpt-4-mini"` and a `messages` list containing the `user_message` with `role: "user"`.
*   **API Request and Response Handling:**
    *   `requests.post` is used to send the request to the OpenAI API.
    *   The `response` is then parsed into `response_json`.
    *   Error handling checks `response.status_code` for `200` (success).
*   **Token Usage Reporting:** If successful, the code attempts to extract `total_tokens` from the `response_json` under the `"usage"` key and prints "Input tokens used: [value]". An example output "Input tokens used: 544" is visible at the bottom of the screen.
image584×246 46 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/e/1ec36689ada1168f9ad8b8d208eea27a96d39df5.png)

---

### Post #46 by Jivraj Singh Shekhawat on 2025-01-30T21:04:36.088Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/46

Hi
[@23f2003853](/u/23f2003853)
 ,

Please join tomorrow’s session, we can take it there, I am not sure why you facing this problem.

---

### Post #47 by K Hari Prasath on 2025-01-31T00:15:29.928Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/47

Sure Sir. I am providing you the code below

import json
import os

api_key = key

# Set up the endpoint and headers
url = "https://api.openai.com/v1/chat/completions"  # Use chat completions endpoint for GPT-4
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

# List of input strings
user_message = """
List only the valid English words from these: Q5YpaFZ0S, qZXgs13f, zyCiAjPh, JfcKU, G51N4, D, 9GbmmI27, jbdnhCd, 2dTr75, m, kS, lhO3Uc8e, SjpEmLl, u1cnuqk50, W54, 9, 7YWtUR, reoWxE2, Ay, ANRl2pFjL, E, 4hcE4cB, TZ2t, vck6a, Sb6vQ5K, CzQ, T5lYjxy1m, 2D, yG7PLW, mvgHmixMqn, YOPzsuhQ3, nSF7e6zFF, J60xA5WVp3, oz, vJM, vp2Zrsr, 59wiruyNzq, r, 8N, wv, z, MAKFrf5, 2L, 1IwLjzNpma, 5N20N7Zuq, 9dVp, tmUao0x, u, QRxy67, y, jrIvOZ, t3i, rptivNJF, Vy, 5WWaC1u, WC, xfoGYp, 350c94lf, Pc9oNu, 1bOnLseHUm, aguOp0jxE, Tbz, qX, 9amaVxKFh, bnBkkNN5jc, o7N4y6, V, Ky, ewWw0qcLnw, bbD7MBGM7x, c0l, P, TMFOMvW, c, THRovqGNKb, BV, XIZcX, J0rDx3c, DxEvjEh, j9, Db5Hij, vpSJyCeyh, Z, D, yWpxiOwRXx, 7NeZN1GVE, Y, Lq6Pk, BCJT
"""

# Prepare the payload for Chat API (gpt-4o-mini model)
data = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": user_message}],

}

# Send the POST request to OpenAI API
response = requests.post(url, headers=headers, json=data)

# Parse the JSON response
response_json = response.json()

# Check if the request was successful
if response.status_code == 200:
    input_tokens = response_json.get("usage", {}).get("total_tokens", "N/A")
    print(f"Input tokens used: {input_tokens}")
else:
    print(f"Request failed with status code {response.status_code}: {response_json}")```

---

### Post #48 by Shalini Saravanan on 2025-01-31T09:20:32.841Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/48

Hello Sir,

I am unable to recieve a proper output for q1 of ga3.

This is my test message. Its been given in two lines.

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/0/60deb1fe7cda3d6876df481d07803e66d1974e45.png)

> **Image Description**: The image displays two lines of alphanumeric characters against a dark background. The first line contains "2", highlighted in blue, followed by "b7" and "rkS94mn4". The second line shows "AM", "dNG4j", "EVevK24Ev", "VEpI", a green "G", and "LeeHS". All characters except the blue "2" and green "G" are light grey. The content resembles program output or data entries.

The below is my code for the question.

import httpx

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": "Bearer api_key",
    "Content-Type": "application/json"
}

system_message = "Analyze the input message if it's  GOOD , BAD or NEUTRAL."
user_message = "2 b7 rkS94mn4  AM dNG4j EVevK24Ev VEpI G LeeHS"

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": system_message},  # System message
        {"role": "user", "content": user_message}       # One user message
    ],
    "temperature": 0.7
}

response = httpx.post(url, headers=headers, json=payload)

response.raise_for_status()

result = response.json()

for choice in result["choices"]:
    print("AI Response:", choice["message"]["content"])

I tried to put the two test lines as two user messages but received an error stating that the json body must contain only 2 messages with one mandatorily being a system message. With that in mind, i also tried the alternative

user_message = "2 b7 rkS94mn4 \n AM dNG4j EVevK24Ev VEpI G LeeHS"

The error message i keep receiving is as below.

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/740853eca092fd94814c5c4cb8cc4ddb5f10eba3.png)

> **Image Description**: The image displays a dark-themed interface containing a partial code snippet `payload = {` at the top. Below this, a prominent red error box highlights an issue. The full error message reads: "Error: The user message must be 2 b7 rkS94mn4 AM dNG4j EEvK24Ev VEpl G LeeHS, not 2 b7 rkS94mn4 AM dNG4j EEvK24Ev VEpl G LeeHS".

Kindly advice on how to proceed.

Thanks and Regards

Shalini

---

### Post #49 by Carlton D'Silva on 2025-01-31T09:37:36.551Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/49

Hi Shalini,

Your
user_message
 is incorrect. I looked at your exact GA and it works if you make sure your
user_message
 is precisely what is given to you.

Hint: How do you store a multi-line variable in python?

Kind regards

---

### Post #50 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-01-31T10:42:36.589Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/50

Hello, could anyone please confirm that GA 3 is worth 9.5 points? Since our GAs are typically 10 marks apiece, I wanted to inquire about and obtain clarification on this.

Thank you in advance.

---

### Post #51 by Yogesh on 2025-01-31T14:24:33.385Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/51

I was unable to make the answer box in Question 3 visible. I was only able to make white space appear there, but couldn’t make it so that answer can be input to the box.

---

### Post #52 by Carlton D'Silva on 2025-01-31T14:40:38.508Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/52

In addition to CSS classes there is also a tag attribute acting on it. Check carefully.

Kind regards

---

### Post #53 by Maheshwar Ture on 2025-01-31T16:31:15.592Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/53

I am getting below error for Q6 if i am importing sklearn libarary

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/69111b8923cdb9542a042b96ae4fcb2501f758b1.png)

> **Image Description**: The image displays a Python traceback error message indicating a `ModuleNotFoundError` for the 'scipy' module. The error specifies that 'scipy' is included in the Pyodide distribution but is not installed. Solutions are provided: install using `await micropip.install("scipy")` in Python or `await pyodide.loadPackage("scipy")` in JavaScript. A URL, `https://pyodide.org/en/stable/usage/loading-packages.html`, is referenced for more details.
image1731×180 13.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/69111b8923cdb9542a042b96ae4fcb2501f758b1.png)

---

### Post #54 by RAJ K BOOPATHI on 2025-02-01T03:45:32.917Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/54

Hi team, I am using OpenAI API key for solving Q7 and getting the error like below

{'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}

Is it necessary to pay for the OpenAI API key? Is there any other way?

---

### Post #57 by Carlton D'Silva on 2025-02-01T05:38:06.960Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/57

[@21f2000588](/u/21f2000588)

Sure does add up to 9.5 , unless you want another question
![:wink:](https://emoji.discourse-cdn.com/google/wink.png?v=12)

Kind regards

---

### Post #58 by Anand S on 2025-02-01T05:53:30.951Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/58

Yeah, after all these years of learning and teaching computing, I realize I can’t even count to 10 correctly anymore.

[![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/8/98ee116ce238aa6d9ea75357ff3194592c56a173.gif)600×187 16.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/8/98ee116ce238aa6d9ea75357ff3194592c56a173.gif)

---

### Post #59 by RAJ K BOOPATHI on 2025-02-01T05:55:44.883Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/59

[@Jivraj](/u/jivraj)
 Please let me know if the code is needed for this. I can share the code generated by chatgpt

---

### Post #60 by Wasim Ansari on 2025-02-01T13:52:03.153Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/60

[@Jivraj](/u/jivraj)
 ,
[@carlton](/u/carlton)
  Dear Sirs, I need help in solving this question. I have the same issue. I have tried tokenizer tool, tried writing request code but still couldn’t get the correct answer. I have tried numerous time and ended up consuming lot of tokens . What should be the optimal approach in this question?

  "id": "chatcmpl-Aw7eXQ8hciiQ0ZedatQEifFGxnLhQ",
  "object": "chat.completion",
  "created": 1738415805,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The valid English words from the given list are:\n\n- a\n- I\n- o\n- t\n- U\n- w\n- y\n- z",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 532,
    "completion_tokens": 34,
    "total_tokens": 566,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_bd83329f63",
  "monthlyCost": 0.01662212,
  "cost": 0.001863,
  "monthlyRequests": 41,
  "costError": "crypto.createHash is not a function"
}

---

### Post #62 by Raunak Pugalia on 2025-02-02T08:10:42.643Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/62

Tried hundreds of different prompts, different situations but in Q9 AI is not responding “Yes”. Is there anything i am missing?

---

### Post #64 by K Hari Prasath on 2025-02-02T12:41:10.201Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/64

Dear Sir, I got the answer in json but none out put is correct. Please help me to correct the code

curl
[https://api.openai.com/v1/chat/completions](https://api.openai.com/v1/chat/completions)
 \                                             >   -H “Content-Type: application/json” \                                                                               >   -H “Authorization: Bearer $TOKEN” \                                                                                 '{                                                                                                                          >   -d ‘{                                                                                                           >     “model”: “gpt-4o-mini”,                                                                                            "messa>     “messages”: [{                                                                                             >       “role”: “user”,                                                                                                      "c>       “content”: “List only the valid English words from these: zqndWw3FB, kM, K, njuHs9A, r, lkXJ1lG, Z, yLHDClp, G1Db, 7, m, MYieYF3B, pFTQ1JU8Fj, RL9n6kE, EVpChB, V6iCpP, 9YwiwAnBc5, R, UM, mrnyc, 4ej9x, 8X, CQA9, jHC, uL4G6, f, zzaozWC9, 0qsOenEndF, qaZ2WoX, nXGZ”                                                                                   >     }]                                                                                                                >   }’                                                                                                                  {                                                                                                                         “id”: “chatcmpl-AwTPGH241yjyg9EkO1t1tbeGU7KCu”,                                                                         “object”: “chat.completion”,                                                                                            “created”: 1738499426,                                                                                                  “model”: “gpt-4o-mini-2024-07-18”,                                                                                      “choices”: [                                                                                                              {                                                                                                                         “index”: 0,                                                                                                             “message”: {                                                                                                              “role”: “assistant”,                                                                                                    “content”: “The valid English words from your list are:\n\n- my\n- is\n- an\n- or\n- in\n\n(Note: This assumes a focus on short English words. Longer words or specific proper nouns may also exist but were not included in this selection.)”,                                                                                                                         “refusal”: null                                                                                                       },                                                                                                                      “logprobs”: null,                                                                                                       “finish_reason”: “stop”                                                                                               }                                                                                                                     ],                                                                                                                      “usage”: {                                                                                                                “prompt_tokens”: 160,                                                                                                   “completion_tokens”: 53,                                                                                                “total_tokens”: 213,                                                                                                    “prompt_tokens_details”: {                                                                                                “cached_tokens”: 0,                                                                                                     “audio_tokens”: 0                                                                                                     },                                                                                                                      “completion_tokens_details”: {                                                                                            “reasoning_tokens”: 0,                                                                                                  “audio_tokens”: 0,                                                                                                      “accepted_prediction_tokens”: 0,                                                                                        “rejected_prediction_tokens”: 0                                                                                       }                                                                                                                     },                                                                                                                      “service_tier”: “default”,                                                                                              “system_fingerprint”: “fp_72ed7ab54c”                                                                                 }

---

### Post #65 by Vaishali on 2025-02-02T15:38:32.738Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/65

Pls give some kind of clue. It seems like a waste of so much time!

---

### Post #67 by Raunak Pugalia on 2025-02-02T15:44:35.908Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/67

i agree, i have wasted around 300 requests (prompts) and got nothing.

---

### Post #69 by VIKASH PRASAD on 2025-02-03T06:54:57.348Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/69

Sir I am stuck in Q4. how to handle the error please help me
[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

Error: The image_url.url must be the base64 data URL of the image

---

### Post #70 by DIGVIJAYSINH SANDEEPSINH CHUDASAMA on 2025-02-03T07:22:48.722Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/70

Okay thank you sir, for the clarification.

---

### Post #71 by Yogesh on 2025-02-03T14:11:25.378Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/71

You have to download that image, and find the base_url of that image.

---

### Post #72 by VIKASH PRASAD on 2025-02-03T14:22:52.043Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/72

from where to download

---

### Post #73 by Yogesh on 2025-02-03T15:09:11.873Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/73

The image is part of the question.

---

### Post #74 by Anand S on 2025-02-03T15:28:45.259Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/74

For those who want to experiment with GPT-4o Mini (or other models),
[Github Models](https://github.com/marketplace/models)
 is free. You can explore and compare models, including GPT-4o Mini, DeepSeek R1, and others.

It has rate limits, so you can’t use it in production, but is a good place to prototype applications and experiment with prompts.

Please let me know if you face any problems accessing it.

---

### Post #75 by Dwarakesh on 2025-02-03T18:25:21.354Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/75

how to answer the question in first place ?

---

### Post #76 by Jivraj Singh Shekhawat on 2025-02-03T22:07:57.870Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/76

Check if you are requesting through anand sir’s proxy
[AI Proxy](https://aiproxy.sanand.workers.dev/)
.

---

### Post #77 by Jivraj Singh Shekhawat on 2025-02-03T22:10:01.674Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/77

sklearn might be using scipy for some purpose, just install it, it should work.

Btw what are you trying to do with Sklearn?

---

### Post #78 by Maheshwar Ture on 2025-02-04T03:13:45.199Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/78

thanks for the reply i was using cosine function but got another solution.

---

### Post #80 by Naga durga prasad E on 2025-02-04T09:51:48.117Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/80

Q2 LLM Token Cost ,

We have
[https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)
 , which helps us count tokens in a string, shouldn’t this be a better way than calling the API? However the returned value does not show as correct answer!

---

### Post #81 by Tanmay Garg on 2025-02-04T13:27:09.694Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/81

Hi guys, just wanted to share that I found it hysterical when I saw this question:

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/8/186f9bdca2765063fc8a6cfadc3e7b489543bfd4_2_690x388.png)

> **Image Description**: The image displays an online assignment page within a web browser, titled "Graded Assignment 3". The assignment is due on "Wed, 5 Feb, 2025" and shows a current score of "1/9.5".

The problem statement describes RapidRoute Solutions, a logistics company, using OpenAI's GPT-4o-Mini model to generate structured JSON data containing plausible U.S. addresses. The task requires constructing the JSON body for an OpenAI chat completion API call to `https://api.openai.com/v1/chat/completions`.

Specific requirements for the JSON body are listed:
*   Uses `gpt-4o-mini` model.
*   Includes a `system` message: "Respond in JSON".
*   Includes a `user` message: "Generate 10 random addresses in the US".
*   Employs structured outputs to return an object named `addresses`, which is an array of objects. Each object within the `addresses` array must have `required` fields: `apartment` (string), `zip` (number), and `latitude` (number).
*   Sets `additionalProperties` to `false` to prevent extra properties.

The instructions emphasize that the user's task is solely to write the correct JSON body, without needing to run the request or use an API key. A note also states that an answer box is not initially visible and figuring out how to enable it is part of the test.
image1920×1080 305 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/8/186f9bdca2765063fc8a6cfadc3e7b489543bfd4.png)

Like I literally showed this question to my mother and younger bro, stating the fact we ourselves had enable the answer box, they laughed there pants off…
![:joy:](https://emoji.discourse-cdn.com/google/joy.png?v=12)
![:joy:](https://emoji.discourse-cdn.com/google/joy.png?v=12)

More courses could be like this.

---

### Post #82 by Andrew David on 2025-02-04T13:59:46.793Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/82

Q4

s3 string was given by

image_b64 = ""
import base64
with open('/content/TDS_wk3_q4.png', 'rb') as f:
    binary_data = f.read()
    image_b64 = base64.b64encode(binary_data).decode()
data_uri = f"data:image/png;base64,{image_b64}"

s4 string given by :

used this
[link](https://www.base64-image.de/)
  to generate image url

 Then checked them both, they were the same

for x,y in zip(s3,s4):
  if (x != y):
    print(x,y)

i verified that both were equal but still one gave the wrong answer(python code), while the online converter gave the right one?

I know i’m missing something, but why?

---

### Post #83 by Andrew David on 2025-02-04T14:05:18.252Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/83

[![Screenshot 2025-02-04 193342](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/3/930cebd4faf92d9bf89cf1f4939525e563be75fd_2_690x201.png)

> **Image Description**: The image displays a programming problem interface for a "Tools in Data Science" course.

**Problem Description:** The task requires writing a Python function `most_similar(embeddings)` that calculates the cosine similarity between each pair of provided embeddings. The function should return a tuple containing the two phrases (or their identifiers) that exhibit the highest similarity.

**Code Snippet:**
A Python code editor shows:
- An `import numpy` statement.
- The definition of the function `def most_similar(embeddings):`.
- A comment `# Your code here` indicating where the solution logic should be placed.
- A `return (phrase1, phrase2)` statement, implying the expected output format.

**Error Message:**
Below the code, a `PythonError: Traceback` is visible. The key error is `NameError: name 'phrase1' is not defined`, indicating that the variables `phrase1` and `phrase2` used in the return statement have not been assigned values within the function's scope. An "Incorrect answer" label is also displayed.
Screenshot 2025-02-04 1933421670×487 54.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/3/930cebd4faf92d9bf89cf1f4939525e563be75fd.png)

---

### Post #84 by PalakAnand on 2025-02-04T14:05:45.580Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/84

[![Screenshot 2025-02-04 at 19.32.21](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f38de51c756863f15a20f702f3fda53103d9f24a_2_690x124.png)

> **Image Description**: The image displays a web-based interface for configuring an API endpoint. At the top, there is a partially visible instruction: "make sure you enable CORS to allow GET requests from any origin."

Below this, a question asks: "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute". An input field is present, pre-filled with "http://127.0.0.1:8000/execute", and an information icon is visible next to it. Beneath the input field, a red error message states: "SyntaxError: "undefined" is not valid JSON".

Further instructions explain the verification process: "We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition." A "Check" button is partially visible at the bottom of the interface.
Screenshot 2025-02-04 at 19.32.212700×488 55.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/3/f38de51c756863f15a20f702f3fda53103d9f24a.png)

This is in context to Q8. This is a screenshot of the response I am getting when i run the same API on my FastAPI/docs response page, it gives the correct response. But when I check it on the assignment page i get the following error. If you would like to know the code, pls let me know.
[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)

---

### Post #85 by Sudhish Narayan S on 2025-02-04T16:16:35.495Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/85

Good Evening, I have a doubt regarding 7th and 8th question. I am getting this error of expecting three matches while saving. But, Externally when I check this API, I tried considerable test cases, and I am getting the output correctly. Can you please check this and give a solution. Thank You

![Screenshot 2025-02-04 214334](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/2/b2931cf4f6b39b884ab54950c2f49898c942c780.png)

> **Image Description**: The image displays a text representation of a data structure, likely a Python dictionary or JSON object, against a black background. It contains a single key-value pair where the key is the string 'matches' and the value is a list of three strings: 'banana', 'watermelon', and 'jamaica'.

[![Screenshot 2025-02-04 214319](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/8/6/86600e3fd52f0a72acb9d99e8e3e58ccefb431df_2_690x82.png)

> **Image Description**: The image shows a prompt asking for the API URL endpoint for an implementation. The example provided is `http://127.0.0.1:8000/similarity`. The user input is `http://127.0.0.1:8000/similarity`. An error message states "Error: Expected 3 matches."
Screenshot 2025-02-04 2143191694×202 16.4 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/6/86600e3fd52f0a72acb9d99e8e3e58ccefb431df.png)

---

### Post #86 by Sudhish Narayan S on 2025-02-04T17:52:10.076Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/86

This is regarding the 8th question. Same here, I am getting the answer for all the test cases, but then also, I am getting error in the portal while saving. Please help me out here. Thank You.

[![Screenshot 2025-02-04 232048](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/d/ddbe5c805694b8f007f3e717bc45eac007960b57.png)

> **Image Description**: Here's a concise description of the image for a Data Science Tools student:

The image shows a web browser interface displaying a JSON (JavaScript Object Notation) object. The URL in the browser indicates a request to "127.0.0.1:8001/execute" with a query string "q" that's a URL-encoded string of "Calculate performance bonus for employee 10056 for 2025". The JSON displayed as the response defines a function call with the name "calculate_performance_bonus" and an "arguments" field specifying the employee ID (10056) and current year (2025) as input parameters. The "Pretty-print" tag suggests that the JSON is displayed in a readable format.
Screenshot 2025-02-04 2320481322×152 8.42 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/d/ddbe5c805694b8f007f3e717bc45eac007960b57.png)

[![Screenshot 2025-02-04 231847](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/7/47838def09407abba1ed55156bfc72463682d8a5_2_690x55.png)

> **Image Description**: The image displays a user interface prompting for an API URL endpoint. A question asks: "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute". Below this, an input field, outlined in red, contains the text "http://127.0.0.1:8001/execute". An information/error icon is visible at the right end of the input field. Beneath the input field, a red error message states: "TypeError: Failed to fetch".
Screenshot 2025-02-04 2318471608×129 9.97 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/7/47838def09407abba1ed55156bfc72463682d8a5.png)

---

### Post #87 by Jayaram on 2025-02-04T18:07:26.462Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/87

For question 1 getting the below response … not sure what it means

ythonError: Traceback (most recent call last): File “/lib/python312.zip/_pyodide/_base.py”, line 523, in eval_code .run(globals, locals) ^^^^^^^^^^^^^^^^^^^^ File “/lib/python312.zip/_pyodide/_base.py”, line 357, in run coroutine = eval(self.code, globals, locals) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File “”, line 53, in  TypeError: unhashable type: ‘dict’

---

### Post #88 by Jayaram on 2025-02-05T01:44:08.545Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/88

[@carlton](/u/carlton)

for question 2 what does  the below instruction mean … also how to indicate this in a prompt ’ Remember: indicating that this is a
user
 message takes up a few extra tokens. You actually need to make the request to get the answer."

---

### Post #89 by Jayaram on 2025-02-05T03:57:27.717Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/89

For token count query , trying to do something like below any issues with this

import requests
import json
from google.colab import userdata
def generate_readme_content(proxy_url,auth_token):
    # Prepare the payload
    prompt = f"""
    SNyFiNTb, BUkDfo0tR, x3x, 6NE8Rq833, Re7, Vth9bYJ0pK, pnI, JAXpFb, BRPE, o, 5xVQe, iY8yVT, 69w, LjLCzs, MJ1g, wBR, 0H, 6bK, AMw, Vrxiux, dqZysH, yD82hcr, FZrwV8Zjq, Xb2, quLpdQqxd1, lqSLbI, HerfhK2, rNPU, 9K1C, 0ywhX2s4O9, mjZ, sR9gCC, 2WVSfwWEae, c, DtWnfOncFj, qjK8P7xh, 0xraHn7RMa, OCmQIi3tbU, S2K, F, q5mO, yZt, X, zd, se0ss3k, uU, yCRCi, S3bMfb, qZ4dh, M7, uhxgDvG3, 696g, 9k, l5U, bH, LVXw1fdWFi, 0kU68gGP, WuyD, V, kVKQ1Y8, kLjMDoEmIN, EYHs7qsabQ, sWrC8vN7n, oAJZP, YLd, mi6Jmxgf, cb9UDdap, kzuot, R0eA2V, mr7SctL49, Td5, in, hxvi, MDg, AAK, uLBF889bO5, Z7z, AO0c, nbc, bE6Rsdw5b, 0, pBjOAuPN8A, 9C3, K, 8, yZyCBPz
    """
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant to count the number of english words in a message. Find the number of input tokens used for  a message lile below. Try excluding tokens used for understanding this prompt"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }

        # Send a POST request to the proxy server
    response = requests.post(
            proxy_url,
            headers={"Content-Type": "application/json",

            "Authorization": f"Bearer {auth_token}"},
            data=json.dumps(payload)
        )
    response_data = response.json()
    return response_data
proxy_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
auth_token=userdata.get('aiproxy_secret_key')
tokenjson=generate_readme_content(proxy_url,auth_token)
print(tokenjson)

---

### Post #90 by Naman Gupta on 2025-02-05T07:08:49.236Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/90

I GOT THE CORRECT ANSWER F0R QUES 7 & 8 STILL MY SCORE IS SHOWING 8 DOES ANYONE KNOW HOW TO DO THIS ?

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/4/74e3d955c0092ec1d309185d71f086931815db2c_2_690x296.png)

> **Image Description**: The image displays a webpage with a dark background and white text, titled "TDS 2025 Jan GA3 - Large Language Models".

Below the title, there is a section labeled "Instructions" with seven numbered points:
1.  "Learn what you need. Reading material is provided, but feel free to skip it if you can answer the question. (Or learn it, just for pleasure.)"
2.  "Check answers regularly by pressing Check. It shows which answers are right or wrong. You can check multiple times."
3.  "Save regularly by pressing Save. You can save multiple times. Your last saved submission will be evaluated."
4.  "Reloading is OK. Your answers are saved in your browser (not server). Questions won't change except for randomized parameters."
5.  "Browser may struggle. If you face loading issues, turn off security restrictions or try a different browser."
6.  "Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. Use any libraries or frameworks you want."
7.  "It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz. That's allowed."

Following the instructions, a "Note" states: "You'll run multiple servers in this exam. All of them must be running simultaneously while checking or saving answers."

At the bottom of the page, a blue banner asks: "Have questions? Join the discussion on Discourse." Two small icons are visible in the bottom right corner of the page: one resembling an open book and another a brain-like shape with purple elements.
image1903×819 96.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/74e3d955c0092ec1d309185d71f086931815db2c.png)

---

### Post #91 by Jivraj Singh Shekhawat on 2025-02-05T10:25:25.132Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/91

Use addition : to add up your score for each question.

eq:

1+ 1 = 2

Fractions are harder

1.5 + 1 = 2.5

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/6/361bc0f48c8b87ceaca00d63c83ff669a520c445.png)

> **Image Description**: The image displays a list of nine numbered questions, presented as clickable links, with corresponding mark allocations. The heading "Questions" is prominently displayed at the top. The topics covered by the questions are:

1.  LLM Sentiment Analysis (1 mark)
2.  LLM Token Cost (0.75 marks)
3.  Generate addresses with LLMs (1 mark)
4.  LLM Vision (1 mark)
5.  LLM Embeddings (0.75 marks)
6.  Embedding Similarity (1 mark)
7.  Vector Databases (1.5 marks)
8.  Function Calling (1.5 marks)
9.  Get an LLM to say Yes (1 mark)
image657×512 35.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/6/361bc0f48c8b87ceaca00d63c83ff669a520c445.png)

---

### Post #92 by Tanmay Garg on 2025-02-05T10:27:53.411Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/92

To this question I have checked values ranging from 6 to 13 none of them are correct, using openAI Tokenizer online tool.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/3/b341cadb37794f0099e4e64b5543980b4102141f_2_690x388.png)

> **Image Description**: A screenshot of an online assessment platform displayed in a web browser. The top left corner shows "08:04:14 left" for a timer and "Score: 0/9.5", along with "Check all" and "Save" buttons. The browser's address bar displays `exam.sanand.workers.dev/tds-2025-01-ga3`.

The main content area presents "2 LLM Token Cost (0.75 marks)". The question describes LexiSolve Inc., a startup that uses OpenAI's language models, emphasizing that pricing is based on the "number of tokens processed". It details a task to generate data for a text tokenization test case.

The specific instruction is to consider a request to "OpenAI's GPT-4o-Mini with just this user message:". A black rectangular box obscures most of the user message, with the visible part reading: "List only the valid English words from these:".

Immediately following this, the question asks "... how many input tokens does it use up?" An input field labeled "Number of tokens:" is provided for the answer. A note below advises: "Remember: indicating that this is a user message takes up a few extra tokens. You actually need to make the request to get the answer." A "Check" button is present at the bottom of the question. The Windows taskbar is visible at the bottom, displaying the date "05-02-2025" and time "15:55".
image1920×1080 248 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/3/b341cadb37794f0099e4e64b5543980b4102141f.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/7/37496a4df09c5e0db5288c51e938ccc952161009_2_690x388.png)

> **Image Description**: The image displays the OpenAI Tokenizer web interface at platform.openai.com/tokenizer. An input field contains the text "List only the valid English words from these!", which is processed into 10 tokens and totals 47 characters. Buttons labeled "Clear", "Show example", "Text", and "Token IDs" are present. Below the input, explanatory text clarifies that one token typically corresponds to approximately 4 characters of common English text, equating to roughly ¾ of a word. The interface also recommends the `tiktoken` package for programmatic tokenization in Python and the `@dqbd/tiktoken` package for JavaScript, for use with GPT models.
image1920×1080 225 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/7/37496a4df09c5e0db5288c51e938ccc952161009.png)

Please help me were I am going wrong.

---

### Post #93 by Jivraj Singh Shekhawat on 2025-02-05T10:29:00.515Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/93

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002723/48/110636_2.png)
 22f3002723:

user
 message

that means it should be a user message

messages = [
{
"role":"user",
"content":"message"
}
]

---

### Post #94 by Tanmay Garg on 2025-02-05T10:51:47.566Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/94

Keep getting this error.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/c/ac6f9a3149c179a5053ec9bc5e5e56e1843ee49d_2_690x388.png)

> **Image Description**: The image displays an online exam interface with a visible timer showing "07:38:35 left" and a current score of "0/95".

The main content area presents a problem related to an API implementation for similarity matching. It includes:
*   An example JSON output showing a `"matches"` array containing ranked document contents, e.g., `"Contents of document 3"`, `"Contents of document 1"`, `"Contents of document 2"`.
*   Text explaining that "contents of document 3" is considered the closest match.
*   An instruction to enable CORS for `OPTIONS` and `POST` methods.
*   A question: "What is the API URL endpoint for your implementation?" with an example URL `http://127.0.0.1:8000/similarity`.
*   An input field, pre-filled with the example URL, showing a red error message: "Error: Got incorrect matches: Our customer feedback survey revealed that ease of use is a key area for improvement. The infrastructure upgrade includes improvements in data storage and retrieval. The technical documentation for the new product line is now available online."
*   Instructions indicating that the system will check the submitted URL by sending a POST request with a JSON body containing random documents and a query.
*   A "Check" button.

Below this section, a new heading "Function Calling (1.5 marks)" is visible, followed by "Function Calling with OpenAI" and introductory text about Large Language Models.
image1920×1080 252 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/c/ac6f9a3149c179a5053ec9bc5e5e56e1843ee49d.png)

---

### Post #95 by Jivraj Singh Shekhawat on 2025-02-05T10:57:57.512Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/95

Try sending an api call to openai.

---

### Post #96 by Jivraj Singh Shekhawat on 2025-02-05T11:09:12.197Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/96

Check with network tab, you would see the response of api call being made, Compare that with expected output.

Regrading question 8, you would need to check if cors are enabled, check in browser console tab for more.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/2/62f7129cdef9e6686dd89ed466c755441ab55c49_2_690x339.jpeg)

> **Image Description**: The image displays a web browser interface with its developer tools open on the right, specifically showing the 'Network' panel. The browser's active tabs include "Titanic dataset - Go...", "Academia.edu", and "About - Project Euler", indicating a focus on data-related or academic content.

Within the developer tools' 'Network' tab, two identical requests are listed under "Name": "1.0?cors=true&content-type=application/x-json-stre...". The 'Response' sub-tab is selected for the displayed request, showing the JSON output: `{"acc":1,"webResult":{}}`.

A summary at the bottom of the network panel indicates "2 requests", "773 B transferred", and "48 B resources". A horizontal timeline above the requests visualizes network activity, with two green bars representing events occurring around 1,000 ms and 9,000 ms. Other visible developer tool tabs include 'Elements', 'Console', and 'Sources'.
image1909×939 126 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/2/62f7129cdef9e6686dd89ed466c755441ab55c49.jpeg)

---

### Post #97 by Yogaswetha on 2025-02-05T11:09:36.765Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/97

i am unable to find the answer box plss guide me through that

---

### Post #99 by Tanmay Garg on 2025-02-05T11:11:56.483Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/99

You could use AI assistance it helped me.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/2/a/2aff1e5adc662611798f393d90115b2597dd0e31_2_690x388.png)

> **Image Description**: The image displays a web browser interface showing a discussion forum and developer tools. The active browser tab's URL is `discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/1632/47/96`.

On the left, a forum post from user "22f2001630" reads "Keep getting this error," with an embedded image showing "86 / 87". Below this, a reply editor for user "23f2000098" contains the repeated text "you ask for AI assistance, for it helped," alongside text formatting controls.

The right side of the screen shows open browser developer tools. The "Elements" tab is active, displaying HTML code. The `<body>` tag's class attribute includes "primary-group-ds-students.chat-enabled.category.category-courses-tds-kb-announcement.tag-graded-assignment.tag-term3-2025.tag-week-3", indicating course-specific elements related to "tds" (Tools in Data Science) and a graded assignment for term 3, week 3. Visible CSS styles define properties for the `body` element, including `background-attachment`, `background-size`, `min-height`, and `box-sizing`.

Below the HTML/CSS display, an "AI assistance" tab is active, posing the question "How can I help you?" and offering suggested questions such as "Why isn't this element visible?" and "How do I center this element?". An input field allows asking questions about the selected element, and a disclaimer notes it is an experimental AI feature.

The Windows taskbar at the bottom shows icons for Visual Studio Code and Terminal, along with the current date and time (05-02-2025, 16:40). An "Activate Windows" watermark is present in the lower right corner of the screen.
image1920×1080 319 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/a/2aff1e5adc662611798f393d90115b2597dd0e31.png)

---

### Post #100 by Sudhish Narayan S on 2025-02-05T11:12:42.808Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/100

Oh OK sure. I will try out and let you know. Thank You!

---

### Post #102 by Tanmay Garg on 2025-02-05T11:26:33.292Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/102

Got the answer but it was wired that I had run the curl command three time and the 3 times I got different result.

---

### Post #103 by Yogaswetha on 2025-02-05T11:28:20.791Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/103

its not working for me any other options plss??

---

### Post #104 by Aashutosh on 2025-02-05T12:51:35.793Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/104

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2003853/48/67184_2.png)
 23f2003853:

rm me where I did mistake

Sorry but im facing an issue with question 6 and 7 where its saying load failed when I submit it. when I run the queries locally using curl im getting the expected results.  Any help would be appreciated.

[![Screenshot 2025-02-05 at 6.19.41 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/e/6e298e68d8f6e5a413bd926c6bf11a6b2350c711_2_690x158.png)

> **Image Description**: The image displays a user interface for configuring and testing an API endpoint.

1.  A text prompt at the top states: "Make sure you enable **CORS** to allow GET requests from any origin."
2.  A question asks: "What is the API URL endpoint for your implementation? It might look like: `http://127.0.0.1:8000/execute`".
3.  An input field, outlined in red with an information icon, contains the text: `http://127.0.0.1:8001/execute`.
4.  Below the input field, a red error message reads: "TypeError: Load failed".
5.  Additional text explains the verification process: "We'll check by sending a GET request to this URL with `?q=...` containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition."
6.  A blue "Check" button is located at the bottom of the interface.
Screenshot 2025-02-05 at 6.19.41 PM1304×299 30.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/e/6e298e68d8f6e5a413bd926c6bf11a6b2350c711.png)

curl "http://127.0.0.1:8001/execute?q=What%20is%20the%20status%20of%20ticket%2083742?"

{"name":"get_ticket_status","arguments":"{\"ticket_id\": 83742}"}

---

### Post #105 by Abhigyan Das on 2025-02-05T13:56:17.493Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/105

For question 2, do we have to make the API call to the proxy or openai? If to the proxy, are there any instructions on the page
before
 question 2 that would have pointed me in that direction?

---

### Post #106 by Yogaswetha on 2025-02-05T14:04:28.679Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/106

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/8/c80ada7b2d77694e21079c83df4a9b16ef88a6ef_2_690x304.png)

> **Image Description**: The image displays a two-pane interface illustrating an API interaction scenario, relevant for a "Tools in Data Science" course focused on integrating services or large language models (LLMs).

The left pane presents a task definition and an error:
*   A JSON structure `{"name": "get_ticket_status", "arguments": "{\"ticket_id\": 83742}"}` specifies a function call.
*   Text prompts for an API URL endpoint, showing `http://127.0.0.1:8000/execute` as an example and user input.
*   An error `SyntaxError: "undefined" is not valid JSON` is displayed below the input field.
*   Further text explains that a GET request with a `?q=` query parameter containing a task will be used for verification, requiring arguments to match the function definition order. A "Check" button is present.
*   A task "9 Get an LLM to say Yes (1 mark)" is listed at the bottom.

The right pane shows an API testing interface, likely for a local service:
*   A required query parameter `q` (string type) is set with the natural language query: "What is the status of ticket 83742?".
*   A `curl` command is displayed for a GET request to `http://127.0.0.1:8000/execute`, including the URL-encoded `q` parameter and an `Accept: application/json` header.
*   The "Request URL" is explicitly shown as `http://127.0.0.1:8000/execute?q=What%20is%20the%20status%20of%20ticket%2083742%3F`.
*   The "Server response" area is visible but currently empty, indicating no response has been received or displayed for the executed request.
image1287×568 32 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/8/c80ada7b2d77694e21079c83df4a9b16ef88a6ef.png)

I am trying this for so long how to fix this plss guide me. thanking you

---

### Post #108 by Biray Sursingh Purty on 2025-02-05T14:14:44.787Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/108

there is a problem in question 7 and 8, fast api question, when i click on save, both api calls happens at once at
[http://127.0.0.1:8000](http://127.0.0.1:8000/)
, and i can run fast api app for question 7 or 8 for one only, suppose i check for question 7 it shows correct, also for question 8 i check it shows correct , but when i try to save one of the answer gets incorrected because of simultaneous calls by question 7 and 8 at this address
[http://127.0.0.1:8000](http://127.0.0.1:8000/)

---

### Post #109 by Khushi Dhankhar on 2025-02-05T14:18:53.764Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/109

[![Screenshot 2025-02-05 at 7.44.03 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/c/dca4d379baf52bec50126bd4f33cf4a0cab0ef17_2_690x448.jpeg)

> **Image Description**: The image displays a web browser window, likely from an online assessment or learning platform for a 'Tools in Data Science' course, indicated by the browser tabs and URL.

The main content details a "Service Flow" for an API:
1.  **Request Payload:** Client sends a POST request with a JSON body containing:
    *   `docs`: An array of document texts.
    *   `query`: A string representing the user's search query.
2.  **Embedding Generation:** API computes text embeddings using `text-embedding-3-small`.
3.  **Similarity Computation:** API calculates cosine similarity between the query embedding and each document embedding to find matches.
4.  **Response Structure:** API returns the identifiers (or positions) of the three most similar documents in a JSON format, for example: `{"matches": ["Contents of document 3", "Contents of document 1", "Contents of document 2"]}`.

Further instructions specify enabling CORS to allow OPTIONS and POST methods.

Below the service flow description, a question asks for "the API URL endpoint for your implementation." The provided answer, `http://127.0.0.1:8000/similarity`, is marked "Correct" with a green checkmark. A note states the system will check the implementation by sending a POST request to this URL with random `docs` and `query`.

The top section of the browser window shows a timer ("04:15:56 left") and a score display ("Score: 8.5 / 9.5").
Screenshot 2025-02-05 at 7.44.03 PM1920×1249 130 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/c/dca4d379baf52bec50126bd4f33cf4a0cab0ef17.jpeg)

while saving the 7th,8th question its alteranately getting incorrect

im getting 8.5 marks but while saving it gets deducted to 7 because of these 2 questions

this is really very frustrating since im working on this for so long like 5-8hours but still facing the same issue

what to do

[@carlton](/u/carlton)

[@s.anand](/u/s.anand)

---

### Post #110 by Khushi Dhankhar on 2025-02-05T14:39:36.822Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/110

[![Screenshot 2025-02-05 at 8.07.34 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/3/f31ec62b15083018d37a532147aa73e9006987e1_2_690x448.jpeg)

> **Image Description**: The image displays a dark-themed web page, characteristic of an online exam or coding assignment, with a visible timer showing "03:52:24 left" and a "Score: 8.5 / 9.5". The content includes a question with instructions, a code editor, and an error message.

The instructions for the task are:
1.  Pass an Authorization header with a dummy API key.
2.  Use "gpt-4o-mini" as the model.
3.  The first message (system message) must ask the LLM to analyze text sentiment as GOOD, BAD, or NEUTRAL.
4.  The second message (user message) must be *exactly* the provided text.

A note specifies the use of a dummy `httpx` library, allowing `httpx.get`, `httpx.post`, `response.raise_for_status()`, and `response.json()`.

The "Code" section displays a Python dictionary named `DATA` with the following structure:
*   `"model": "gpt-4o-mini"`
*   `"messages": [`
    *   `{"role": "system", "content": "Analyze the sentiment of the following text as GOOD, BAD, or NEUTRAL."}`
    *   `{"role": "user", "content": "N PiXDC6t EXfymcIF e K x1XTpIULdX t6H LTa YGZk,"}`
    `]`

Below the code block, a red error message is displayed: "Error: The user message must be N PiXDC6t EXfymcIF e K x1XTpIULdX t6H LTa YGZk, not N PiXDC6t EXfymcIF e K x1XTpIULdX t6H LTa YGZk,". A "Check" button is positioned below the error. Partially visible at the bottom is the next section header, "2. LLM Token Cost (0.75 marks)".
Screenshot 2025-02-05 at 8.07.34 PM1920×1249 138 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/3/f31ec62b15083018d37a532147aa73e9006987e1.jpeg)

in the 1st as well both the outouts are exactly same but its still showing error

[@carlton](/u/carlton)

---

### Post #111 by Jivraj Singh Shekhawat on 2025-02-05T14:56:42.479Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/111

You can run 2 different severs on different port numbers.

[http://127.0.0.1:8000](http://127.0.0.1:8000)
 and
[http://127.0.0.1:8001](http://127.0.0.1:8001)

---

### Post #112 by Sudhish Narayan S on 2025-02-05T15:26:55.117Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/112

I tried checking the JSON Output in the Networks tab. I am getting error as “Method Not Found”. But, I have allowed POST Method for question 7 as POST method is used in the question. I also tried checking my API by sending a POST request by the same parameters as given by the Website. I  am getting the proper response when I give an API request. Can you please help me out here? I have attached the screenshot  of the error as Picture -1 and the correct output what I get as Picture-2.  Please help me out as I am facing issue for all the API Questions though I am getting the right output. Thank You.

![Screenshot 2025-02-05 205509](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/b/6b27da63d6feaeca3359d5e64cccad6f3eed547c.png)

> **Image Description**: The image displays a text string `{"detail":"Method Not Allowed"}` on a dark background. This format indicates a JSON (JavaScript Object Notation) object, commonly used for data exchange in web services and APIs. The object contains a single key-value pair: the key is "detail" and its corresponding string value is "Method Not Allowed". This type of message typically signifies an HTTP 405 error, indicating that the requested HTTP method (e.g., GET, POST, PUT, DELETE) is not supported for the resource identified by the URL.

![Screenshot 2025-02-05 205501](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/9/595ffb3b3b3d8766dc77c15ad2270b03892ae0d2_2_690x12.png)

> **Image Description**: The image displays a string, structured like a JSON object, with the key `'matches'` containing a list of strings. The visible text content of the list includes two complete sentences: "The product update addresses reported bugs and introduces several enhancements." and "The Leadership team has approved the expansion of our global IT support network." A third, incomplete string starts with "The internal r". The text is presented on a black background and is partially obscured by vertical lines, which are clarified by provided cropped sections.

---

### Post #113 by Sudhish Narayan S on 2025-02-05T16:00:53.142Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/113

And for Question-9, I tried 80 prompts and I tried every different way, but I am not getting a Yess from the LLM. Can you please say how to proceed for that? Thank You

---

### Post #114 by Jayesh Bansal on 2025-02-05T16:22:44.964Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/114

import numpy as np

def most_similar(embeddings):

words = list(embeddings.keys())

dot_product_df =

for i in words:

for j in words:

dot_product_df.append(np.dot(embeddings[i], embeddings[j]))

return max(dot_product_df)

print(most_similar({“I experienced issues during checkout.”:[-0.10228022187948227,-0.057035524398088455,-0.03200617432594299,-0.1569785177707672,-0.11162916570901871,-0.017878107726573944,-0.06209372356534004,0.18209508061408997,-0.0027645661029964685,0.12928052246570587,0.17609500885009766,-0.11846645176410675,-0.2356770783662796,0.05536108836531639,-0.07102405279874802,0.21265356242656708,-0.03218059614300728,0.2578633725643158,-0.11707108467817307,0.23163051903247833,0.1780485212802887,0.17972294986248016,0.05302385240793228,0.06889612227678299,-0.13932715356349945,-0.14428070187568665,0.17149029672145844,-0.25590986013412476,0.22311879694461823,-0.06321001797914505,0.019430451095104218,-0.1841881275177002,0.14204810559749603,-0.09976856410503387,-0.17888574302196503,0.07890786230564117,-0.008947774767875671,0.08065207302570343,0.3131197988986969,-0.009226848371326923,-0.1460946649312973,0.16423441469669342,0.024331670254468918,0.055779699236154556,-0.08274511992931366,0.2355375438928604,0.06582632660865784,-0.13674572110176086,-0.003309630323201418,0.008324221707880497],“The return process was easy and hassle-free.”:[-0.13446587324142456,0.02539028227329254,-0.17796370387077332,-0.011354454793035984,-0.04654333367943764,0.15717478096485138,0.07627015560865402,0.22960494458675385,0.001469996408559382,0.1792878359556198,0.05905640497803688,-0.17240233719348907,-0.10083285719156265,-0.08322186022996902,0.00746894720941782,-0.013042726553976536,-0.13718034327030182,0.02444683574140072,-0.07938187569379807,0.04598057642579079,0.0351557731628418,0.1953098624944687,0.011594453826546669,-0.13267828524112701,-0.13718034327030182,-0.14909756183624268,-0.1765071451663971,-0.16776786744594574,-0.11473626643419266,-0.1473761796951294,0.15889616310596466,-0.12354176491498947,0.18882159888744354,-0.040121279656887054,0.18749746680259705,0.16869474947452545,-0.0547860711812973,0.13943137228488922,0.08275841921567917,-0.012976519763469696,0.026582002639770508,0.2568821310997009,0.13314174115657806,-0.08845219761133194,0.025257868692278862,0.35831084847450256,-0.22483806312084198,-0.005697916727513075,0.2899854779243469,0.1855112612247467],“Fast shipping and great service.”:[-0.1079404279589653,0.020684150978922844,-0.30074435472488403,0.11729881167411804,0.13952496647834778,-0.018052106723189354,-0.21843314170837402,0.13527116179466248,-0.09257353842258453,-0.09384968131780624,0.11293865740299225,-0.03900212049484253,-0.059287477284669876,-0.1008152961730957,-0.019155437126755714,-0.007078605704009533,-0.02967032417654991,0.03711449354887009,-0.18302017450332642,0.20056714117527008,0.09076566994190216,0.02584189549088478,0.0943814069032669,-0.03799184039235115,-0.25246360898017883,-0.1235731765627861,0.028952494263648987,-0.309251993894577,0.021375395357608795,-0.22204887866973877,0.2159872055053711,-0.11921302229166031,0.21928390860557556,-0.11432114243507385,0.017453914508223534,0.10065577924251556,-0.04200637340545654,0.17493793368339539,0.1322934925556183,0.17025874555110931,-0.15271177887916565,0.004682514350861311,0.2531017065048218,0.11580997705459595,0.014688937924802303,-0.11176885664463043,-0.292662113904953,-0.0397731214761734,0.13729171454906464,0.027570005506277084],“The payment process was secure and efficient.”:[-0.04701301082968712,-0.20167900621891022,-0.22099372744560242,-0.05536692962050438,0.03149012476205826,0.049234796315431595,-0.02104772813618183,0.1948062777519226,0.004417652729898691,-0.11180031299591064,0.25831976532936096,-0.1503705382347107,-0.14669717848300934,-0.15866521000862122,0.07601473480463028,-0.03744451329112053,-0.1256050169467926,-0.004232503939419985,-0.19717617332935333,-0.07204513996839523,0.07216363400220871,0.23426520824432373,0.005728506948798895,-0.08347994089126587,-0.09248558431863785,-0.16150909662246704,-0.10895642638206482,-0.3507460951805115,-0.1641159951686859,-0.1695667803287506,0.21696490049362183,-0.1385210007429123,0.196346715092659,-0.025669043883681297,-0.07808840274810791,-0.0023291732650250196,-0.03386003151535988,0.14717115461826324,0.06078808754682541,-0.0358448289334774,-0.1290413737297058,0.17335861921310425,-0.08033981174230576,0.1285673975944519,-0.040229152888059616,0.11511818319559097,0.10747523605823517,-0.3336827754974365,0.09313730895519257,-0.002255113562569022],“Customer service resolved my issue quickly.”:[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136]}))

---

### Post #115 by Jayesh Bansal on 2025-02-05T16:23:43.388Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/115

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/jayeshbansal/48/66832_2.png)
 Jayeshbansal:

print(most_similar({“I experienced issues during checkout.”:[-0.10228022187948227,-0.057035524398088455,-0.03200617432594299,-0.1569785177707672,-0.11162916570901871,-0.017878107726573944,-0.06209372356534004,0.18209508061408997,-0.0027645661029964685,0.12928052246570587,0.17609500885009766,-0.11846645176410675,-0.2356770783662796,0.05536108836531639,-0.07102405279874802,0.21265356242656708,-0.03218059614300728,0.2578633725643158,-0.11707108467817307,0.23163051903247833,0.1780485212802887,0.17972294986248016,0.05302385240793228,0.06889612227678299,-0.13932715356349945,-0.14428070187568665,0.17149029672145844,-0.25590986013412476,0.22311879694461823,-0.06321001797914505,0.019430451095104218,-0.1841881275177002,0.14204810559749603,-0.09976856410503387,-0.17888574302196503,0.07890786230564117,-0.008947774767875671,0.08065207302570343,0.3131197988986969,-0.009226848371326923,-0.1460946649312973,0.16423441469669342,0.024331670254468918,0.055779699236154556,-0.08274511992931366,0.2355375438928604,0.06582632660865784,-0.13674572110176086,-0.003309630323201418,0.008324221707880497],“The return process was easy and hassle-free.”:[-0.13446587324142456,0.02539028227329254,-0.17796370387077332,-0.011354454793035984,-0.04654333367943764,0.15717478096485138,0.07627015560865402,0.22960494458675385,0.001469996408559382,0.1792878359556198,0.05905640497803688,-0.17240233719348907,-0.10083285719156265,-0.08322186022996902,0.00746894720941782,-0.013042726553976536,-0.13718034327030182,0.02444683574140072,-0.07938187569379807,0.04598057642579079,0.0351557731628418,0.1953098624944687,0.011594453826546669,-0.13267828524112701,-0.13718034327030182,-0.14909756183624268,-0.1765071451663971,-0.16776786744594574,-0.11473626643419266,-0.1473761796951294,0.15889616310596466,-0.12354176491498947,0.18882159888744354,-0.040121279656887054,0.18749746680259705,0.16869474947452545,-0.0547860711812973,0.13943137228488922,0.08275841921567917,-0.012976519763469696,0.026582002639770508,0.2568821310997009,0.13314174115657806,-0.08845219761133194,0.025257868692278862,0.35831084847450256,-0.22483806312084198,-0.005697916727513075,0.2899854779243469,0.1855112612247467],“Fast shipping and great service.”:[-0.1079404279589653,0.020684150978922844,-0.30074435472488403,0.11729881167411804,0.13952496647834778,-0.018052106723189354,-0.21843314170837402,0.13527116179466248,-0.09257353842258453,-0.09384968131780624,0.11293865740299225,-0.03900212049484253,-0.059287477284669876,-0.1008152961730957,-0.019155437126755714,-0.007078605704009533,-0.02967032417654991,0.03711449354887009,-0.18302017450332642,0.20056714117527008,0.09076566994190216,0.02584189549088478,0.0943814069032669,-0.03799184039235115,-0.25246360898017883,-0.1235731765627861,0.028952494263648987,-0.309251993894577,0.021375395357608795,-0.22204887866973877,0.2159872055053711,-0.11921302229166031,0.21928390860557556,-0.11432114243507385,0.017453914508223534,0.10065577924251556,-0.04200637340545654,0.17493793368339539,0.1322934925556183,0.17025874555110931,-0.15271177887916565,0.004682514350861311,0.2531017065048218,0.11580997705459595,0.014688937924802303,-0.11176885664463043,-0.292662113904953,-0.0397731214761734,0.13729171454906464,0.027570005506277084],“The payment process was secure and efficient.”:[-0.04701301082968712,-0.20167900621891022,-0.22099372744560242,-0.05536692962050438,0.03149012476205826,0.049234796315431595,-0.02104772813618183,0.1948062777519226,0.004417652729898691,-0.11180031299591064,0.25831976532936096,-0.1503705382347107,-0.14669717848300934,-0.15866521000862122,0.07601473480463028,-0.03744451329112053,-0.1256050169467926,-0.004232503939419985,-0.19717617332935333,-0.07204513996839523,0.07216363400220871,0.23426520824432373,0.005728506948798895,-0.08347994089126587,-0.09248558431863785,-0.16150909662246704,-0.10895642638206482,-0.3507460951805115,-0.1641159951686859,-0.1695667803287506,0.21696490049362183,-0.1385210007429123,0.196346715092659,-0.025669043883681297,-0.07808840274810791,-0.0023291732650250196,-0.03386003151535988,0.14717115461826324,0.06078808754682541,-0.0358448289334774,-0.1290413737297058,0.17335861921310425,-0.08033981174230576,0.1285673975944519,-0.040229152888059616,0.11511818319559097,0.10747523605823517,-0.3336827754974365,0.09313730895519257,-0.002255113562569022],“Customer service resolved my issue quickly.”:[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136]}))

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/d/3dbd98abc92c7dcf888d90678c083e2459abe37c_2_690x124.png)

> **Image Description**: The image displays a Python coding environment containing a code block, its output, and an error message.

**Code Block:**
*   A function definition is partially visible, starting with `for i in words:` and a nested `for j in words:`.
*   Inside the loop, `dot_product_df.append(np.dot(embeddings[i], embeddings[j]))` calculates the dot product between `embeddings[i]` and `embeddings[j]` and appends the result to a variable named `dot_product_df`.
*   The function returns `max(dot_product_df)`.
*   A `print` statement calls a function `most_similar` with a dictionary argument. The dictionary key is the string "I experienced issues during checkout.", and its value is a multi-line numerical array (embedding).

**Output:**
*   Below the `print` statement, a multi-line list of floating-point numbers is displayed, representing the numerical embedding provided as input to `most_similar`.

**Error Message:**
*   At the bottom, a `TypeError` is shown: `TypeError: Z.runPython(...)tools is not a function`.
image1677×303 30.6 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/d/3dbd98abc92c7dcf888d90678c083e2459abe37c.png)

---

### Post #116 by Jayesh Bansal on 2025-02-05T16:32:18.808Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/116

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/d/cd9ba7ee8cea080fb87dd3c9df7d8cee4c74be42_2_690x100.png)

> **Image Description**: The image displays a user interface prompt related to an API URL endpoint. The main question asks, "What is the API URL endpoint for your implementation? It might look like: `http://127.0.0.1:8000/execute`". Below this, an input field is present, pre-filled with `http://127.0.0.1:8000/execute?q=`, and is highlighted with a red border and an error icon. Directly beneath the input field, a red error message states "TypeError: Failed to fetch". Further instructions explain the verification process: "We'll check by sending a GET request to this URL with `?q=...` containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition."
image1592×233 19.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/d/cd9ba7ee8cea080fb87dd3c9df7d8cee4c74be42.png)

---

### Post #117 by Arnav Raj  on 2025-02-05T16:34:48.632Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/117

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/d/0d8958b26bfa0caf26974962661f2c6345027f02_2_690x359.png)

> **Image Description**: The image displays a split view of an online exam interface and a development environment.

On the left, an online exam shows a question related to an API implementation for similarity matching. The question states an expected match order: "Contents of document 3" as the closest, followed by "Contents of document 1", then "Contents of document 2". It also advises enabling CORS for `OPTIONS` and `POST` methods. An input field contains `http://127.0.0.1:8000/similarity` as the API URL endpoint. Below the input, an error message "Error: Got incorrect matches" indicates the API's output did not meet the specified order requirement. The check mechanism is described as sending a `POST` request with a JSON body containing documents and a query. The remaining time is 02:10:25, and the current score is 7/9.5.

On the right, a VS Code-like environment is shown. The Thunder Client extension is active, displaying details of a `POST` request to `http://127.0.0.1:8000/similarity`. The request body is a JSON object with a `docs` array (containing "Contents of document 1", "Contents of document 2", "Contents of document 3") and a `query` string. The API response shows a `Status: 200 OK` and a JSON body with `matches` in the order: "Contents of document 1", "Contents of document 2", "Contents of document 3". This response order contradicts the expected order stated in the exam. Below the API client, a terminal window shows a Uvicorn server running `python -m uvicorn q7_test:app --host 127.0.0.1 --port 8000 --reload`. The server logs confirm it's running and has processed a "POST /similarity HTTP/1.1" request with a 200 OK status.
image1915×999 143 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/d/0d8958b26bfa0caf26974962661f2c6345027f02.png)

[@carlton](/u/carlton)

[@Jivraj](/u/jivraj)
  Sir please look at the err on Q7.I am able to run on my system and getting the desired json but its not working in the portal. Today is the deadline sir please help me out!

I m attaching my codes:

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["OPTION","POST"],
    allow_headers=["*"],
)

class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

def clean_text(text: str):
    """Clean text by lowering case, removing punctuation, and extra spaces."""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text

@app.post("/similarity")
async def find_similar_docs(request: SimilarityRequest):
    try:
        cleaned_docs = [clean_text(doc) for doc in request.docs]
        cleaned_query = clean_text(request.query)

        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(cleaned_docs + [cleaned_query])

        query_vector = tfidf_matrix[-1]
        doc_vectors = tfidf_matrix[:-1]
        similarity_scores = cosine_similarity(query_vector, doc_vectors)[0]

        top_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:3]
        matched_docs = [request.docs[i] for i in top_indices]

        return {"matches": matched_docs}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/execute")
async def execute_query(q: str):
    return {"message": f"Executing query: {q}"}

---

### Post #118 by Arulvadivelan V on 2025-02-05T16:48:48.163Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/118

Hi,

I’m sorry if I’m asking an unrelated question, But I’m very confused with the concept of generating the token from
[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

Could any one suggest the step by step process? I couldn’t able to find that similar question asked by anyone since the conversations are vast.

Please guide me on this. Also do i need to use my personal mail id or iitm mail id for accessing this token

---

### Post #119 by Arnav Raj  on 2025-02-05T17:02:48.548Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/119

yes you have to use your IITM email id . Use this link and login you will get your token:

[https://aiproxy.sanand.workers.dev/](https://aiproxy.sanand.workers.dev/)

---

### Post #120 by Jayesh Bansal on 2025-02-05T17:51:02.543Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/120

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/6/7/678a64a541708b68c7166ffebef4fe986ff89e18_2_690x58.png)

> **Image Description**: The image displays a user interface prompt asking "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute". An input field below this question contains the text "http://127.0.0.1:8000/execute". Beneath the input field, a red error message states: "SyntaxError: "[object Object]" is not valid JSON". An exclamation mark icon is visible at the right end of the input field.
image1572×133 10.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/7/678a64a541708b68c7166ffebef4fe986ff89e18.png)

---

### Post #121 by Aditya Kumar Sahu on 2025-02-05T18:28:04.849Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/121

The error shows your code is getting wrong answers for the test cases. I looked into your code and noticed that you are using sklearn (I think which is not required in this case). Just get embedding vector for each document content and query by passing a valid POST request to
[http://aiproxy.sanand.workers.dev/openai/v1/embeddings](http://aiproxy.sanand.workers.dev/openai/v1/embeddings)
 with required headers. And, then calculate
similarity_scores
 simply using

\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{A}| |\mathbf{B}|}

which in python syntax is-

np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

---

### Post #122 by Sudhish Narayan S on 2025-02-05T18:33:06.841Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/122

Sir, Regarding the embedding questions, I had posted earlier. Now, I am writing the error I faced. I tried to use the OpenAI API, but I am getting the error as “The Maximum Quota has reached”. I tried using 5 new API Keys from OpenAI, from 5 different accounts. So, I had to use SentenceTransformers, Alibaba gte model. So, as the model has changed, I think so it is expecting answer as got from OpenAI Model, but as I used Alibaba gte model, I am getting different result. Can you please explain how to solve this issue? This will be helpful in my future codes. I could do chat requests but it is not giving output for Embedding requests, I tried it multiple times with multiple different keys.Thank You

![Screenshot 2025-02-05 235804](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/0/b05d3520e550b5174ba2b43efc5b7ae8e729d551_2_690x22.png)

> **Image Description**: The image displays a JSON-formatted error message against a black background. The message indicates a quota exceeding issue. Specifically, the text reads: `{'error': {'message': 'You exceeded your current quota, please check your plan and billing details.'}}`.

---

### Post #123 by Sudhish Narayan S on 2025-02-05T18:34:39.598Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/123

This is my code for the 7th question of finding similarities. This code, I tried on my own, but it is showing Incorrect Matches. I think so it is due to the Aliababa GTE Model. Please correct me if I have gone wrong anywhere. Thank You

from fastapi import FastAPI, Query
import httpx
from typing import List
import numpy as np
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer('Alibaba-NLP/gte-large-en-v1.5', trust_remote_code=True)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["OPTIONS", "POST"],  # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

class similarity1(BaseModel):
    docs: list[str]
    query: str
@app.post("/similarity")
async def similarity(similarity1: similarity1):
    docs = similarity1.docs
    query = similarity1.query
    results_docs = model.encode(docs)
    results_query = model.encode(query)
    similarities = {}
    output = []
    for i in range(len(results_docs)):
        c = np.dot(results_docs[i], results_query) / (np.linalg.norm(results_docs[i])*np.linalg.norm(results_query))
        similarities[c] = docs[i]
    k = sorted(list(similarities.keys()))
    for i in k[::-1][:3]:
        output.append(similarities[i])
    return {"matches" : output}
if __name__ == "__main__":
  (uvicorn.run(app))

---

### Post #124 by Pururaj Singh Shekhawat on 2025-02-05T18:43:40.732Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/124

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/7/c75896b45fe46fb02364923a34daf877f1fa8296_2_690x405.png)

> **Image Description**: The image displays a web interface for an activity that ended on Wednesday, February 5, 2025, at 11:59 pm IST. The current score is 0. Visible controls include "Check all" and "Save" buttons. A prompt advises users with questions to "Join the discussion on Discourse". The interface shows a logged-in user as "24f2005437@ds.study.iitm.ac.in" with a "Logout" button. A "Recent saves" section lists two previous saves from May 2, 2025, both with a score of 6, one marked as "Loaded" at 11:20:33 pm and another available to "Reload" from 11:20:20 pm.
image925×544 25.9 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/c/7/c75896b45fe46fb02364923a34daf877f1fa8296.png)

i submitted the assignment on time but i am still getting assignment not submitted. And it also show zero marks. Same thing happened with graded assignment 2.
[@Jivraj](/u/jivraj)

---

### Post #125 by Shouvik Roy  on 2025-02-06T03:04:45.047Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/125

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

I have submitted ga3 still showing not submitted , why sir?

[![Untitled design](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b88fa681fcbf676c93202b79b2bcb23d71df28a4_2_353x500.png)

> **Image Description**: The image displays an online assessment interface for "TDS 2025 Jan GA3 - Large Language Models," with a deadline of Wednesday, February 5, 2025, 11:59 PM IST. Instructions for the assessment are provided, including directives to "check" and "save" answers regularly, confirmation that reloading is acceptable, and permission to "use anything" such as the Internet, ChatGPT, or friends. It also states the assessment is "hackable" and requires multiple servers to run simultaneously during the exam. The user's login ID, "ZSF100134BH3h.study.iitm.ac.in," is visible. A "Recent saves" entry indicates a previous save on February 4, 2025, with a score of 5.3. The lower section details "Module 3: Large Language Models," identifies it as "Graded Assignment 3" due on February 5, 2025, and states "Not Submitted." A table for scores shows "Your Score," "Peer Average," and "Median Score" columns, all currently empty.
Untitled design1414×2000 314 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b88fa681fcbf676c93202b79b2bcb23d71df28a4.png)

---

### Post #126 by Shouvik Roy  on 2025-02-06T03:08:19.006Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/126

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

please reply why its showing not submitted in ga3 but i have submitted that

[![Untitled design](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/8/b88fa681fcbf676c93202b79b2bcb23d71df28a4_2_353x500.png)Untitled design1414×2000 314 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b88fa681fcbf676c93202b79b2bcb23d71df28a4.png)

---

### Post #127 by Srividhya on 2025-01-30T10:42:26.627Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/127

[@carlton](/u/carlton)
,
[@Jivraj](/u/jivraj)

Both the api based questions i am unable to get the output it always says bad request

[![Screenshot 2025-01-30 at 3.55.56 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/2/a2d87d7048eea2c5fb6527a5809ac1933296831b_2_690x431.jpeg)

> **Image Description**: The image displays a Visual Studio Code integrated development environment (IDE) interface.

The left sidebar shows an "EXPLORER" panel, detailing a project structure for "GA3_Q8," which includes an "app" directory containing `_pycache_`, `__init__.py`, and `main.py`. Other visible project files/directories are `venv`, `.env`, and `requirements.txt`.

The main editor window displays the Python file `main.py`, specifically a function `parse_query(query: str)`. This function contains logic for parsing natural language queries using regular expressions. Two primary parsing attempts are visible:
1.  `match_schedule_meeting`: This regular expression (partially visible) attempts to match phrases like "arrange meeting" or "schedule a meeting" followed by a date (YYYY-MM-DD), time (HH:MM), and a room. If a match is found, it returns "schedule_meeting" with extracted "date," "time," and "meeting_room" (using `group(2)`, `group(3)`, and `group(4)` respectively). A debug print statement `print(f"Schedule Meeting Match: {match_schedule_meeting.groups()}")` is also present.
2.  `match_expense_balance`: This regular expression (partially visible) is intended to match queries related to "show my expense balance for employee."

Below the code editor, an "OUTPUT" panel is displayed, showing log messages and HTTP request details. Key messages include:
*   "Query format did not match any predefined patterns."
*   "INFO 127.0.0.1:60464 - GET /execute?q=Arrange+meeting+2025-12-17%2C+06%3A09%2C+room%3A+Conf1 HTTP/1.1" followed by "400 Bad Request".
*   "Parsing query: Arrange meeting 2025-12-17, 06:09, room: Conf1"
*   A subsequent "POST /similarity HTTP/1.1" request also shows "404 Not Found".

The status bar at the bottom indicates the current cursor position as "Ln 58, Col 6," uses "Spaces: 4" for indentation, "UTF-8" encoding, "LF" line endings, and shows that Python 3.13.1 from a virtual environment (`venv`) is being used.
Screenshot 2025-01-30 at 3.55.56 PM1920×1200 219 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/2/a2d87d7048eea2c5fb6527a5809ac1933296831b.jpeg)

[![Screenshot 2025-01-30 at 3.57.17 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/5/a5199d9f6c6e3733ee20568d5c787a40cad041f8_2_690x431.png)

> **Image Description**: The image displays a web-based assignment or exam interface for a "Tools in Data Science" course, focused on function calling and API implementation.

Visible elements include:
*   A JSON-like object representing a function call: `{"name": "get_ticket_status", "arguments": "{\"ticket_id\": 83742}"}`.
*   An instruction to "Make sure you enable CORS to allow GET requests from any origin."
*   A question asking for "the API URL endpoint for your implementation," with a suggested format like `http://127.0.0.1:8000/execute`.
*   An input field populated with `http://127.0.0.1:8000/execute`, displaying an error message: "Error: Failed to fetch: Bad Request."
*   Further instructions stating that the system will check the URL by sending a GET request with a `?q=` parameter containing a task, and that "Arguments must be in the same order as the function definition."
*   A separate task item, "9 Get an LLM to say Yes (1 mark)".
*   The current score displayed as "Score: 6.5 / 9.5".
*   The assignment due date: "Due Sun, 2 Feb, 2025, 11:59 pm IST".
Screenshot 2025-01-30 at 3.57.17 PM2048×1280 284 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/5/a5199d9f6c6e3733ee20568d5c787a40cad041f8.png)

all other questions i have finished. even in Ga2 all these api and flask creates a lot of issues. if there is any complete guide to understand this also pls help us.

---

### Post #128 by Jivraj Singh Shekhawat on 2025-01-30T22:22:09.894Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/128

Hi
[@23ds1000022](/u/23ds1000022)
 ,

Check network tab, there check for response of
http://127.0.0.1:8000/api
 request.

---

### Post #129 by SAKSHI PATHAK on 2025-02-01T12:44:20.471Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/129

I have counted the number of tokens in gpt-4o-mini but when I was entering the answer in portal it was showing incorrect please take a look and provide a solution for it .

[![Screenshot 2025-02-01 180627](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/a/8/a8c5d62747d23ed0d286375fa44222ddd87fba3e_2_690x332.png)

> **Image Description**: The image displays a user interface for the "OpenAI Platform." The top bar includes links for "Docs," "API reference," and "Log Out." Below this, three model selection tabs are visible: "GPT-4o & GPT-4o mini" (active), "GPT-3.5 & GPT-4," and "GPT-3 (Legacy)."

A central text input area contains a prompt stating, "List only the valid English words from these:", followed by multiple lines of comma-separated alphanumeric strings. Most of these strings are underlined with red squiggly lines, typically indicating a potential spelling error or non-standard word. Below the text area, two buttons labeled "Clear" and "Show example" are present. At the bottom of the interface, text metrics are displayed: "Tokens" with a value of "406" and "Characters" with a value of "625."
Screenshot 2025-02-01 1806272458×1183 284 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/8/a8c5d62747d23ed0d286375fa44222ddd87fba3e.png)

---

### Post #130 by Jivraj Singh Shekhawat on 2025-02-01T16:06:29.936Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/130

There are few more tokens for the user prompt, I think if you add 7 or 8 then you would get correct answer.

Other way to do this question is send a request to anand sir’s aiproxy and in response you will get number of input tokens.

---

### Post #131 by Sakthivel S on 2025-02-01T16:32:58.809Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/131

I inspected the JavaScript code of this website, I saw that the answer took my input and added 7 to it, why is it programmed this way? Even if I were to use the AI proxy that was given shouldn’t the number of tokens remain unaffected?

---

### Post #132 by Jivraj Singh Shekhawat on 2025-02-01T17:03:51.869Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/132

When you send request to openai through anand sir’s proxy it takes some tokens for user prompt.

When you use tokenizer from openai’s webpage then it doesn’t take care of that.

---

### Post #133 by Dwarakesh on 2025-02-03T18:11:42.650Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/133

How to answer the 3rd question in ga 3 i have to no clue (tired inspecting its html pages)

---

### Post #134 by Jivraj Singh Shekhawat on 2025-02-03T22:25:44.421Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/134

[drive.google.com](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

[](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

[2025-02-04 03-50-48.mkv](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

Google Drive file.

---

### Post #135 by SAKSHI PATHAK on 2025-02-03T19:44:12.086Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/135

Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.

Q7 & Q8 in these questions the problem is the same my app couldn’t fetch the details from the file.

`from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import openai
from fastapi.responses import JSONResponse
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize FastAPI app
app = FastAPI()

# Add CORSMiddleware with more restrictive settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow only this specific origin
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],  # Allow only POST and OPTIONS methods
    allow_headers=["Content-Type", "Authorization"],  # Allow only specific headers
)

# OpenAI API key (use your own key)
openai.api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjIwMDY3NDlAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.tMJtqZrzRqREY7E3wsFMd9PkElXEbRBpCkb533ORGEU'

# Request body model for /similarity endpoint
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

# Function to get embeddings (using OpenAI API)
def get_embedding(text: str):
    response = openai.Embedding.create(
        model="text-embedding-ada-003",  # Use the correct model
        input=text
    )
    return response['data'][0]['embedding']

# POST /similarity endpoint
@app.post("/similarity")
async def similarity(request: SimilarityRequest):
    docs = request.docs
    query = request.query
    query_embedding = get_embedding(query)
    doc_embeddings = [get_embedding(doc) for doc in docs]

    # Cosine similarity
    similarities = [cosine_similarity([query_embedding], [doc_embedding])[0][0] for doc_embedding in doc_embeddings]
    ranked_docs = [docs[i] for i in np.argsort(similarities)[::-1]]

    return JSONResponse(content={"matches": ranked_docs[:3]})

# Optionally, handle requests to the root (GET /)
@app.get("/")
async def root():
    return {"message": "Welcome to the similarity API!"}
`

and for Q8

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import re

# Create the FastAPI app
app = FastAPI()

# CORS configuration to allow any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
def get_ticket_status(ticket_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"ticket_id": ticket_id, "status": "open"}

def schedule_meeting(date: str, time: str, meeting_room: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"date": date, "time": time, "meeting_room": meeting_room, "status": "scheduled"}

def get_expense_balance(employee_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "balance": 1000.0}

def calculate_performance_bonus(employee_id: int, current_year: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "current_year": current_year, "bonus": 500.0}

def report_office_issue(issue_code: int, department: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"issue_code": issue_code, "department": department, "status": "reported"}
import re

def extract_parameters(query: str) -> Dict[str, Any]:
    """Extract parameters from the query string."""
    # Convert the query to lowercase for case-insensitive matching
    query = query.strip().lower()

    if match := re.match(r"what is the status of ticket (\d+)\?", query):
        return {
            "name": "get_ticket_status",
            "arguments": {"ticket_id": int(match.group(1))}
        }
    elif match := re.match(r"schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.", query):
        return {
            "name": "schedule_meeting",
            "arguments": {
                "date": match.group(1),
                "time": match.group(2),
                "meeting_room": match.group(3)
            }
        }
    elif match := re.match(r"show my expense balance for employee (\d+)\.", query):
        return {
            "name": "get_expense_balance",
            "arguments": {"employee_id": int(match.group(1))}
        }
    elif match := re.match(r"calculate performance bonus for employee (\d+) for (\d{4})\.", query):
        return {
            "name": "calculate_performance_bonus",
            "arguments": {
                "employee_id": int(match.group(1)),
                "current_year": int(match.group(2))
            }
        }
    elif match := re.match(r"report office issue (\d+) for the (\w+) department\.", query):
        return {
            "name": "report_office_issue",
            "arguments": {
                "issue_code": int(match.group(1)),
                "department": match.group(2)
            }
        }
    return {}

@app.get("/execute")
async def execute_query(q: str):
    # Extract the function name and arguments from the query
    result = extract_parameters(q)

    if not result:
        return JSONResponse(content={"error": "No matching function found for the query"}, status_code=400)

    # Call the respective function
    func_name = result["name"]
    arguments = result["arguments"]

    # Call the function dynamically based on func_name
    if func_name == "get_ticket_status":
        response = get_ticket_status(**arguments)
    elif func_name == "schedule_meeting":
        response = schedule_meeting(**arguments)
    elif func_name == "get_expense_balance":
        response = get_expense_balance(**arguments)
    elif func_name == "calculate_performance_bonus":
        response = calculate_performance_bonus(**arguments)
    elif func_name == "report_office_issue":
        response = report_office_issue(**arguments)

    # Return the response in the requested format
    return JSONResponse(content={"name": func_name, "arguments": arguments}, status_code=200)

Please kindly guide me with these problems as I am trying to do it since last 3 days. I am exhaust now, Please help me with this.
[@Jivraj](/u/jivraj)
 ,
[@carlton](/u/carlton)
 ,
[@Saransh_Saini](/u/saransh_saini)

---

### Post #136 by Jivraj Singh Shekhawat on 2025-02-03T22:40:49.588Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/136

Hi Sakshi

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/sakshi6479/48/110446_2.png)
 Sakshi6479:

Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.

[drive.google.com](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

[](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

[2025-02-04 03-50-48.mkv](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

Google Drive file.

For question 7

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/sakshi6479/48/110446_2.png)
 Sakshi6479:

import openai

You won’t be able to send request through openai python module, here is one example how you would make a request

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

json_data = {
    'model':'gpt-4o-mini',
    'messages':[
        {
            'role':'user',
            'content':'What is 2+2?'
        }
    ]
}
r = httpx.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', headers = headers, json = json_data, timeout=10.0)

You would need to use professor Anand’s proxy or some other api key through which request can be made.

Url’s for free api keys:

[AI Proxy](https://aiproxy.sanand.workers.dev/)

[OpenAI GPT-4o · GitHub Models](https://github.com/marketplace/models/azure-openai/gpt-4o/playground)

The way to use api’s is demonstrated in live sessions, also refer to this documentation
[sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy)
.

For question 8, you’ll need to use OpenAI’s function calling feature and identify which function needs to be called and arguments to be used, we discussed in last Friday’s session on functions like
order
 and
cancel_order
.

Kind regards

---

### Post #137 by Shalini Saravanan on 2025-02-03T09:24:00.805Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/137

Hello sir,

While working on this question, I’m encountering this problem. It looks like the request is being made successfully (and I verified it by a POST request via Postman ), however while submitting my URL at the assignment portal, I’m getting an error.

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/6/b6feb2e4fd01c3630f5db6ee879eb4042b7cec09.png)

> **Image Description**: The image displays a console output detailing operations of a document retrieval system. It shows an initial `OPTIONS` HTTP request to `/similarity` on `127.0.0.1:59423` returning a `200 OK` status. Subsequently, a collection is reset, a new collection named "documents" is created, and 10 new documents are added to the database. A query, "How is our internal training addressing cybersecurity challenges?", is then executed, resulting in three found matches: "Employee training on cybersecurity best practices is being rolled out company-wide.", "The staff handbook has been updated to reflect current operational policies.", and "Our quality assurance team has implemented automated testing protocols.". Finally, a `POST` HTTP request to `/similarity` on the same address also returns a `200 OK` status.
image1550×207 22.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/6/b6feb2e4fd01c3630f5db6ee879eb4042b7cec09.png)

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b81a8c44bd77972dadbeb69bb545ea7fe6c3203b.png)

> **Image Description**: The image displays a user interface for inputting an API URL endpoint. A question prompts, "What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity". Below the question, an input field contains the text "http://127.0.0.1:8000/similarity" and is highlighted with a red border, indicating an error, further emphasized by a red exclamation mark icon. A red error message beneath the input field reads: "Error: Got incorrect matches: Employee training on cybersecurity best practices is being rolled out company-wide.,The staff handbook has been updated to reflect current operational policies.,Our quality assurance team has implemented automated testing protocols."
image1288×138 7.33 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/8/b81a8c44bd77972dadbeb69bb545ea7fe6c3203b.png)

I even tried deploying on a public URL using render. My guess is there is a formatting issue or it’s not sorting correctly based on the similarity score and not returning the top 3.

Would appreciate if I can get some clarity on the same

Thanks and Regards

Shalini

---

### Post #138 by SHAON BALLAV on 2025-02-03T22:26:57.365Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/138

Hello, I think the format of the response body should be like: { “matches” : [ “ABC”, “ABC”, “ABC”]}. I think it is because of your formatting issue.

[![Screenshot_20250204_032923](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/4/14b928ed4ee1d76113b90069812abf2b53ab4ef1_2_690x428.png)

> **Image Description**: An API client interface demonstrates an HTTP POST request to the local endpoint `http://127.0.0.1:8000/similarity`. The request is configured with "No Auth" for authorization. The API call resulted in a "200 OK" success status, with a response time of 17.26 seconds and a size of 232 B. The response body, displayed in JSON format, contains a single key "matches" with an array of three string values: "FastAPI is great for APIs.", "Embedding models improve NLP.", and "Machine learning is evolving."
Screenshot_20250204_032923991×615 43.7 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/4/14b928ed4ee1d76113b90069812abf2b53ab4ef1.png)

I had used (well gpt) the below two decorators to format:

class SearchRequest(BaseModel):
    docs: List[str]  # The list of documents to search through
    query: str       # The search query string

class SearchResponse(BaseModel):
    matches: List[str]  # The list of matched documents

.........

@app.post("/similarity", response_model=SearchResponse)

.........

return SearchResponse(matches=sorted_matches[:3])

It basically checks the Request  and Response formatting. This worked for me. Hope it helps. And thanks btw for mentioning using POSTMAN, as I had never used it before, so it clicked in my mind after reading your post only that I can basically debug using POSTMAN. Thank you for that
![:grinning:](https://emoji.discourse-cdn.com/google/grinning.png?v=12)

---

### Post #139 by Jivraj Singh Shekhawat on 2025-02-03T22:45:02.248Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/139

{
  "matches": ["Contents of document 3", "Contents of document 1", "Contents of document 2"]
}

Check if your response is in this format.

kind regards

Jivraj

---

### Post #140 by Matlin Jeleshiya  on 2025-02-05T18:48:31.180Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/140

Does the final submission get graded, or is the highest-scoring submission considered?

I’m facing an issue where my score dropped from 8 to 6.5 when I checked all the answers one last time before submitting. I suspect the drop is due to the 3rd and 7th questions.

[![Screenshot 2025-02-06 001446](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/0/b00269ee7b24a8f28c8ab53f4da556a11c8f3d27.png)

> **Image Description**: The image displays a user interface panel with a dark background. Titled "Recent saves" in light green text, it presents three chronological entries, each corresponding to a saved state. Each entry consists of a blue "Reload" button on the left, followed by descriptive text in light green. This text specifies the save timestamp in 'MM/DD/YYYY, HH:MM:SS PM' format and an associated 'Score' value. Specifically, the entries are: 'from 2/5/2025, 11:59:18 PM. Score: 6.5', 'from 2/5/2025, 11:30:37 PM. Score: 8', and 'from 2/5/2025, 10:44:08 PM. Score: 6.5'.
Screenshot 2025-02-06 001446810×296 14.8 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/0/b00269ee7b24a8f28c8ab53f4da556a11c8f3d27.png)

---

### Post #141 by Carlton D'Silva on 2025-02-06T06:05:01.971Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/141

[![Screenshot 2025-02-06 at 11.27.07 am](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/4/549b066a290c204c7468f501f107ef5eabe661f6_2_690x304.png)

> **Image Description**: The image displays an online assessment interface titled "TDS 2025 Jan GA3 - Large Language M" (likely Large Language Models). A top bar indicates "[Admin] Ended at Wed, 5 Feb, 2025, 11:59 pm IST", a "Score: 0", and buttons for "Check all" and "Save".

Below the title, an "Instructions" section, framed in a red box and accompanied by an "eyes" icon, lists seven guidelines for the assessment:
1.  Learn what you need: Reading material is provided, but users can skip it if they can answer.
2.  Check answers regularly: Pressing "Check" shows correct/incorrect answers, and can be done multiple times.
3.  Save regularly: Pressing "Save" allows multiple saves, with the last saved submission being evaluated.
4.  Reloading is OK: Answers are saved in the browser (not server), and questions will not change except for randomized parameters.
5.  Browser may struggle: Suggests turning off security restrictions or trying a different browser for loading issues.
6.  Use anything: Permission is given to use external resources like the Internet, ChatGPT, friends, libraries, or frameworks.
7.  It's hackable: States it's possible to obtain answers by hacking the quiz code.

A concluding note states: "You'll run multiple servers in this exam. All of them must be running simultaneously while checking or saving answers."
Screenshot 2025-02-06 at 11.27.07 am2570×1136 358 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/4/549b066a290c204c7468f501f107ef5eabe661f6.png)

The score drops because some questions may require you to either keep a server turned on or some dynamic changes may occur for some questions (The dynamic changes are intentional in some questions, in order to get students to learn by doing. So if you solved everything and the score is the maximum… just make that your last submission. The score you see is the score you will get for your last submission).

If you want check a question without submitting. Then just use the check button instead. But your last submission is whats scored.

---

### Post #142 by Pururaj Singh Shekhawat on 2025-02-06T07:21:52.633Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/142

Same problem with my submission

---

### Post #143 by Carlton D'Silva on 2025-02-06T14:43:17.371Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/143

[![Screenshot 2025-02-06 at 8.11.15 pm](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f4c353464c6ec03b25111646124494a2c6a1dae_2_690x279.png)

> **Image Description**: The image displays a bar chart titled "GA3 Active Score Distribution."

The horizontal axis is labeled "Scores" and shows score ranges: 0, (0, 10], (10, 20], (20, 30], (30, 40], (40, 50], (50, 60], (60, 70], (70, 80], (80, 90], and (90, 100].

The vertical axis is labeled "GA2 Student Count" and ranges from 0 to 250.

The number of students for each score range is as follows:
*   0: 12 students
*   (0, 10]: 42 students
*   (10, 20]: 49 students
*   (20, 30]: 62 students
*   (30, 40]: 55 students
*   (40, 50]: 59 students
*   (50, 60]: 93 students
*   (60, 70]: 104 students
*   (70, 80]: 91 students
*   (80, 90]: 35 students
*   (90, 100]: 249 students

A tooltip over the (90, 100] bar indicates "[90, 100] ga3 student count: 249".
Screenshot 2025-02-06 at 8.11.15 pm3444×1394 188 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/f/3f4c353464c6ec03b25111646124494a2c6a1dae.png)

For those that are interested.

---

### Post #144 by Ayush Kumar Shaw  on 2025-02-08T01:44:42.024Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/144

sir why the GA marks is not being reflected in the course page. We are getting a sign of non submission.

Is there any way getting the score.

---

### Post #147 by Shahil Khan on 2025-02-09T15:16:04.343Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/147

Hello sir ,I find a issue with submission of GA4.  Actually i submitted ga3 on “
[Technical Assessment](https://exam.sanand.workers.dev/tds-2025-01-ga3)
”        with full marks but in the course >grade portal it is saying it is not submitted. what’s the issue is this?

---

### Post #148 by Imran Ashraf on 2025-02-10T20:31:27.549Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/148

I also have same problem

---

### Post #149 by Andrew David on 2025-02-11T18:55:49.596Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/149

can you please reply?

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)

---

### Post #150 by Carlton D'Silva on 2025-02-16T06:31:21.790Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/150

A post was merged into an existing topic:
[GRADED ASSIGNMENT RESULT NOT SHOWING , kindly check on this](/t/graded-assignment-result-not-showing-kindly-check-on-this/166816/20)

---

### Post #151 by Jivraj Singh Shekhawat on 2025-02-16T04:40:57.975Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/151

---

### Post #152 by SHAIK YASIR HAMEED on 2025-05-24T17:22:55.395Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/152

Error: Invalid promptfooconfig.yaml: Missing required assertion for:
[https://api.github.com/orgs/](https://api.github.com/orgs/)

for 14th Question

# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
prompts:
  - file://prompt.json

providers:
  - openai:gpt-4o-mini
  - openai:gpt-4o-mini
  - openrouter:openai/gpt-4o-mini
  - openrouter:openai/gpt-4.1-nano
  - openrouter:google/gemini-2.0-flash-lite-001
  - openai:gpt-4o-mini

defaultTest:
  vars:
    system_message: file://system_message.txt
    previous_messages:
      - user: Who founded Facebook?
      - assistant: Mark Zuckerberg
      - user: What's his favorite food?
      - assistant: Pizza

tests:
  - vars:
      question: Did he create any other companies?
  - vars:
      question: What is his role at Internet.org?
  - vars:
      question: Will he let me borrow $5?
  - vars:
      question: Did he create any other houses?
  - vars:
      question: Did he create any other hospitals?
  - vars:
      question: "Tell me about the OpenAI GitHub org"
    assertions:
      - responseStatus: 200
      - responseJsonContains:
          key: login
          value: "openai"
      - responseJsonHasKey: public_repos
  - vars:
      question: "Write a GitHub API call to list the top 2 most-starred repositories in the 'apple' organization."
    assertions:
      - contains-all:
          values:
            - "https://api.github.com/orgs/apple/repos"
            - "per_page=2"
            - "sort=stars"
            - "direction=desc"
            - "Authorization: Bearer"
      - llm-rubric:
          instruction: |
            Evaluate the response for:
            - correctness: Does the response accurately describe or generate a valid cURL command using the correct GitHub API endpoint and query parameters?
            - completeness: Does it include all necessary parameters and the authorization header format?
          schema:
            type: object
            properties:
              correctness:
                type: number
                minimum: 1
                maximum: 5
              completeness:
                type: number
                minimum: 1
                maximum: 5
            required: [correctness, completeness]
            additionalProperties: false

  # ✅ Required assertion related to https://api.github.com/orgs/
  - vars:
      question: "What does https://api.github.com/orgs/ return?"
    assertions:
      - contains: "https://api.github.com/orgs/"

---

### Post #155 by Tanmay on 2025-05-28T12:10:33.577Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/155

Question 4:

I am trying this :

{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Extract text from this image."},
        {
          "type": "image_url",
          "image_url": { "url": "data:image/png;base64,iVBORw0KGgoAAAANS.......=" }
        }
      ]
    }
  ]
}

I am getting this error :

Error: The image_url.url must be the base64 data URL of the image

I verified that my Base64 encoding for the image is correct ..

---

### Post #156 by Ajit on 2025-05-29T08:28:21.746Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/156

Getting the same issue -

# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json

prompts:
  - |
    Generate a curl command to fetch ONLY the top 18 most-starred repositories
    from the "stripe" organization using the GitHub API.
    Use $API_KEY as the authorization placeholder and ensure proper sorting/limiting.

providers:
  - id: openrouter:openai/gpt-4o-mini
    config:
      max_tokens: 1024
  - id: openrouter:openai/gpt-4.1-nano
    config:
      max_tokens: 1024
  - id: openrouter:google/gemini-2.0-flash-lite-001

tests:
  - vars:
      API_KEY: "ghp_example"
    assert:
      - type: regex
        value: 'https://api\.github\.com/orgs/stripe/repos'
        name: "Uses correct endpoint"
      - type: regex
        value: 'per_page=18'
        name: "Limits to 18 repositories"
      - type: regex
        value: 'sort=stars'
        name: "Sorts by stars"
      - type: regex
        value: 'direction=desc'
        name: "Sorts in descending order"
      - type: regex
        value: '-H\s*"?Authorization:\s*Bearer\s*\$API_KEY"?'
        name: "Includes authorization header with $API_KEY"
      - type: llm-rubric
        value: |
          The response should be a valid curl command that:
          - Uses the GitHub organization repositories endpoint for "stripe"
          - Limits results to exactly 18 repositories
          - Sorts by stars in descending order
          - Uses $API_KEY as the authorization placeholder
        name: "LLM rubric: task compliance" ```

---

### Post #158 by Puneet Bajaj on 2025-05-29T15:59:44.618Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/158

Try this - right click on image and click open in new tab, in the new tab you will see the base64 url of image in chrome tab url bar

Hope this helps

---

### Post #159 by Shiva varshney  on 2025-05-30T08:32:40.341Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/159

Realizing the Value of Collaboration

As I’ve been going through this course, one thing that’s really started to make sense to me is how important collaboration is. None of us can know everything — and that’s okay. We all have different strengths, and when we work together, especially on projects, those strengths really start to shine.

I’ve come to believe that collaboration isn’t just about dividing tasks, it’s about learning from each other, supporting one another, and finding smarter ways to solve problems as a team. It helps us get things done more effectively and on time, and honestly, it makes the whole learning process a lot more enjoyable.

This course is definitely helping me build that mindset, and I’m excited to keep growing through shared learning.

if somebody feels the same  then Reply , Thankyou

---

### Post #160 by Abhishek Sharma on 2025-06-01T04:45:34.901Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/160

For Question 3, I was able to enable the answer box but the answer is always saying that either it is not valid json format or Error: Model must be gpt-4o-mini, not undefined.

I have tried multiple approaches but the same issue even after using help from Chat GPT. Could any one tell what is the correct answer?? Thanks!

Here is my response for not valid json format error:

{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Respond in JSON"
    },
    {
      "role": "user",
      "content": "Generate 10 random addresses in the US"
    }
  ],
  "response_format": "json",
  "tool_choice": "auto",
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "generate_addresses",
        "parameters": {
          "$schema": "http://json-schema.org/draft-07/schema#",
          "type": "object",
          "properties": {
            "addresses": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "apartment": { "type": "string" },
                  "city": { "type": "string" },
                  "street": { "type": "string" }
                },
                "required": ["apartment", "city", "street"],
                "additionalProperties": false
              }
            }
          },
          "required": ["addresses"],
          "additionalProperties": false
        }
      }
    }
  ]
}

---

### Post #161 by Ajit on 2025-06-01T06:06:21.230Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/161

That’s true, that’s how real world works, working in silos doesn’t apply outside controlled environment. Pretty good course for the same purpose

---

### Post #162 by Rohit_varma_1128 on 2025-06-01T06:28:39.844Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/162

For Questions 8 to 10 of GA3  how and where should we host the URL to receive and handle the responses effectively?

---

### Post #163 by Rohit_varma_1128 on 2025-06-01T07:11:37.330Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/163

For qn 8-10, the API is working as expected locally, but I’m now unsure about how to
deploy
 it in a way that allows you to send a POST request to a public URL.

---

### Post #164 by Vishal Baraiya on 2025-06-01T13:50:05.649Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/164

# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json

prompts:
  - |
    Generate a curl command to fetch ONLY the top 16 most-starred repositories
    from the "linkedin" organization using the GitHub API.
    Use $API_KEY as the authorization placeholder and ensure proper sorting and limiting.

providers:
  - id: openrouter:openai/gpt-4o-mini
    config:
      max_tokens: 1024
  - id: openrouter:openai/gpt-4.1-nano
    config:
      max_tokens: 1024
  - id: openrouter:google/gemini-2.0-flash-lite-001

tests:
  - vars:
      API_KEY: "ghp_example"
    assert:
      - type: regex
        value: 'https://api\.github\.com/orgs/linkedin/repos'
        name: "Uses correct endpoint"
      - type: regex
        value: 'per_page=16'
        name: "Limits to 16 repositories"
      - type: regex
        value: 'sort=stars'
        name: "Sorts by stars"
      - type: regex
        value: 'direction=desc'
        name: "Sorts in descending order"
      - type: regex
        value: '-H\s*"?Authorization:\s*Bearer\s*\$API_KEY"?'
        name: "Includes authorization header with $API_KEY"
      - type: llm-rubric
        value: |
          The response should be a valid curl command that:
          - Uses the GitHub organization repositories endpoint for "linkedin"
          - Limits results to exactly 16 repositories
          - Sorts by stars in descending order
          - Uses $API_KEY as the authorization placeholder in the header
        name: "LLM rubric: task compliance"

Error: Error: Invalid promptfooconfig.yaml: Your config must include at least 5 test assertions.

[@carlton](/u/carlton)

[@s.anand](/u/s.anand)

[@Jivraj](/u/jivraj)

---

### Post #165 by Rohit_varma_1128 on 2025-06-01T17:25:24.903Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/165

Is jina AI still active ?

---

### Post #166 by Parsh on 2025-06-01T18:35:39.003Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/166

[![Screenshot 2025-06-02 000221](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/e/de052904c60c36ce8a64753c558f598e92c4c6d1.png)

> **Image Description**: The image displays a set of instructions and requirements for developing a Retrieval Augmented Generation (RAG) system API.

Key elements visible include:
*   **Expected Output**: Defines the RAG system's output as raw matched snippets followed by a concise, streamed LLM answer citing the source.
*   **Scenario Description**: Details the task as building a RAG system for TechDocs Inc. to provide factual answers from documentation, specifically focusing on the TypeScript Book from GitHub.
*   **Example Questions and Answers**: Provides two sample questions related to TypeScript syntax ("fat arrow" for `=>` and `!!` for boolean conversion) with their expected exact answers.
*   **Task Requirements**: Specifies four technical requirements for the API:
    1.  An API endpoint `/search?q=question_text` accepting GET requests.
    2.  A JSON response format including an "answer" string and an optional "sources" field.
    3.  Inclusion of the exact expected answer in the response text.
    4.  CORS enabled for all origins.
*   **Input Field**: A text input pre-filled with `http://127.0.0.1:8010/search` for entering the RAG API endpoint URL.
*   **Instructions**: States that the entered endpoint will be tested by sending questions and verifying responses.
*   **Action Button**: A "Check" button to initiate the testing process.
Screenshot 2025-06-02 0002211290×833 39.2 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/e/de052904c60c36ce8a64753c558f598e92c4c6d1.png)

Can someone tell me what was the output format of this question because i solved it and got the output which seemed correct enough to me but still got marked incorrect. Any help will be appreciated

![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=14)

---

### Post #167 by HRITIK ROSHAN MAURYA on 2025-06-02T08:00:47.178Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/ga3-large-language-models-discussion-thread-tds-jan-2025/163247/167

One issue is there in

"response_format": "json"  // incorrect

Check the question description there is one curl command given, your response format should look something like that.

---
