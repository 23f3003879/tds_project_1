---
title: "Sudo permission needed to create data folder in root?"
topic_id: 167072
slug: "sudo-permission-needed-to-create-data-folder-in-root"
original_url: https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072
downloaded_at: "2025-06-18T16:10:18.111857"
---

### Post #1 by Vikram Suriyanarayanan on 2025-02-14T03:57:16.864Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/1

[@Jivraj](/u/jivraj)

[@carlton](/u/carlton)
 sir please help

When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?

needs sudo permission all the time…

[![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f51040627e050b955bb243c23f1f660da36b73ae_2_690x70.png)

> **Image Description**: The image shows a terminal window with the output of the command `ls /`. The command lists the directories present in the root directory of a Linux-based system. The output includes directories such as `bin`, `boot`, `etc`, `init`, `lib`, `media`, `opt`, `root`, `sbin`, `sys`, `tmp`, and `var`. The command was executed by user `vikramjncasr` from the directory `/mnt/c/IIT_Madras/TDS_Project_1`.
image2100×216 100 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f51040627e050b955bb243c23f1f660da36b73ae.png)

---

### Post #2 by Carlton D'Silva on 2025-02-14T04:53:36.939Z
**Post URL**: https://discourse.onlinedegree.iitm.ac.in/t/sudo-permission-needed-to-create-data-folder-in-root/167072/2

Hi Vikram,

This is because (if you watched the session, or examined the code, you would have realised that) datagen.py was designed to run inside your docker container. And datagen.py (or a similar named file which we will not tell you ahead of time and will be provided as the query parameter in task A1) will normally be called by evaluate.py

Inside the docker container, permission for the data folder is set by the Dockerfile

which then allows your application to access the root folder inside your docker image and create the /data folder.

So the workflow is like this (for your internal testing only… please follow the Project page for deliverables and evaluation to submit project successfully):

You create your application server that serves 2 endpoints on localhost:8000

You create a docker image that runs this application server.

You run the docker image using podman as described in the project page.

For mimicking the testing conditions. You need two files:

evaluate.py and datagen.py to be in the same folder where you are running these two scripts.

Run evalute.py using uv.

If your docker image is correctly configured and your application is correctly configured, then all the tasks run by evaluate.py will correctly tell you if the application is producing the right result for each task.

Hope that gives clarity.

Kind regards

---
