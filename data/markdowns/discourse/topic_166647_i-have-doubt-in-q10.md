---
title: "I have doubt in Q10"
topic_id: 166647
slug: "i-have-doubt-in-q10"
original_url: https://discourse.onlinedegree.iitm.ac.in/t/i-have-doubt-in-q10/166647
downloaded_at: "2025-06-18T16:07:52.277360"
---

### Post #1 by Dhruv Gupta on 2025-02-09T14:51:52.566Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/i-have-doubt-in-q10/166647/1

I have doubt in question 10 to convert pdf to markdown

I am not getting correct markdown

[@pds_staff](/u/pds_staff)

---

### Post #2 by Ashutosh Banerjee  on 2025-02-09T18:15:12.582Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/i-have-doubt-in-q10/166647/2

Try using the pymupdf4llm Library

pip install pymupdf4llm

import pymupdf4llm

md_text = pymupdf4llm.to_markdown(“input.pdf”)

import pathlib

pathlib.Path(“output.md”).write_bytes(md_text.encode())

import pymupdf4llm

llama_reader = pymupdf4llm.LlamaMarkdownReader()

llama_docs = llama_reader.load_data(“input.pdf”)

---
