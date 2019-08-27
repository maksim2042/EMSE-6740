# EMSE-6740 Syllabus

### Course and Contact Information
Course: EMSE 6740: Systems Thinking and Policy Modeling I
Semester: Fall 2019
Meeting time: THURSDAYS 6:10-8:40 PM
Location: PHIL 348

### Instructor
Name: Maksim Tsvetovat
Campus Address: ???
Phone: 412-519-4304
E-mail: maksim@tsvetovat.org
Office hours: THURSDAYS 4:00-6:00pm or by appointment

## Bulletin Course Description
Introduction to systems thinking and the system dynamics approach to policy analysis, with applications to business management and public policy. Causal-loop and stock and flow models of business growth, technology adoption, and marketing. Use of role-based games to explain key principles of systems. Use of simulation software to model problems and case studies.

## Detailed Course Information:
This course serves as an introduction to methods of policy modeling in the systems engineering and public health domains. Specific techniques to be covered include systems dynamics, agent-based modeling, and network analysis.   We will cover key concepts such as system boundary definition, complexity, uncertainty, model verification, and model validation. We will discuss the utility of models for exploring behavioral and social aspects of population health and engineering design. We will note the variety of ways models can be formulated. Some extant models will be explored in depth. Models will range from individual interactions to international policy formulation. We will indicate how to apply models to situations of interest. Choice of model strategy will be addressed including whether new models should be developed. We will discuss how to allocate efforts and resources appropriately. The course will provide an opportunity for students to create and present conceptual models in problems that involve their personal research interests. The course describes different worldviews adopted by various modeling platforms. 

This course is NOT deep -- we will skim the surface of three distinct areas of system modeling, each worthy of its own semester and a few Ph.D. dissertations. The goal is not to make you an instant expert, but to give you a high-level understanding of the field. 

The central questions I will be asking are -- in order of importance:
*“WHY do we model?”* -- Are we trying to understand a phenomenon? Are we trying to demonstrate our theory of how something works? Are we trying to predict and control the future?  Are we trying to persuade a policy maker? Or are we pointlessly gazing at our navels and wasting time?

*“WHAT do we model?”* -- What are the boundaries of the problem? What is the unit of analysis and unit of time? Do we have sufficient data or are we trying to generate data? 

and only then… we get to …

*“HOW do we model?”* -- What are the appropriate methods and techniques, and how do we get down to brass tacks and get this thing running.

This course will be largely taught using open source software based on Python programming language. I strongly encourage these not familiar with Python to take a crash course at LearnPython.org or DataCamp.com or many other free online courses. I will have many live-code exercises where I will talk through and code an entire problem from scratch as you watch; it’s not as hard as you may think. 

## Assignments

This class has 3 homework assignments, roughly covering the 3 major areas of study we’ll be talking about. Each HW is split into two sections -- mindless repetition and creative improvisation 

Section 1 should be easy to anyone that didn’t sleep through all the classes and knows how to search Wikipedia.

Section 2 will ask you to synthesize, think a bit outside the box and apply what you’ve learned. I will pull ideas for these problems from the news -- I’ll make it fun and relevant. 

Section 2 will be graded on a “valiant attempt” scale -- I am looking for evidence of clear thinking and synthesizing ideas from the class with ideas from other fields and publications, not for a finished research paper. 

Note on collaboration: I encourage you to bounce ideas off of each other, especially on creative problems. However, if you receive a lot of help from someone, please thank them in a footnote. It’s good karma, and reinforces proper academic citation practice.

## FINAL PROJECT
Ideally, this will be a group project covering your area of personal interest. In the past, projects ranged from baseball to politics, and from public health to the social dynamics of the Insane Clown Posse (I’m NOT kidding). 

Your project should include 3 major components:
WHAT -- Proper definition of the problem. 
WHY -- What can be accomplished by using system thinking on your domain?  (note: “to get an A in Max’s class” is NOT a good answer)
HOW -- the projects should include a mixture of empirical data collection, modeling, coding, validation and verification, and result interpretation

I would love to see all projects presented as Jupyter Notebooks on a Github page. 

## Prerequisites
None -- but if you have never programmed in your life, PLEASE take a free Python online class. 
Learn how to use Jupyter Notebook
Learn how to post files on GitHub
Install Slack

## Class Schedule [week-by-week]

### Aug 27
Introduction to Systems Thinking:.

Why do we model? -- Modeling to study, modeling to discover, modeling to experiment and test, modeling to persuade, modeling to navel-gaze pointlessly and waste perfectly good research funding.

What do we model? -- Open systems vs. closed-loop systems, large-scale systems, emergent properties, complexity. 

How do we model? -- Levels of model quality. Face validity, distributional validity, numeric validity. Model complexity -- useless toys vs. ungodly messes.

*To do:* Python Crash course Part 1-- do it now! 

### Sep 3
System Dynamics I - Intro to SD: Stocks & Flows, causal diagrams, system boundaries, introduction to Vensim and PySD; Building an SD Model: Feedback, policy resistance, transparent modeling.

In class exercise (live-code): system dynamics model of a flushing toilet. It’s more complicated than you think.

Python crash course
HW 1 assigned
Python Crash Course, Part 2

### Sep 10
System Dynamics II – Interpreting SD Model Output: Inferring dynamics from data, feedback control, targeting policy interventions 

In-class live-code: Use SD model of a flushing toilet to optimize water consumption at the Nationals stadium during a baseball game. How would a hot dog tax affect it? (also -- watching a clean model devolve into an ungodly mess, or things NOT to do)


### Sep 17
GUEST LECTURE -- Bayesian Causal Networks -- non-deterministic system dynamics -- mixing deterministic and non-deterministic models -- Markov Chains and hidden Markov models

Also, happy birthday to me :) I’m presenting a paper at Stanford

### Sep 24
Optimization algorithms. Gradient ascent/descent, simulated annealing. Local and global maxima. Genetic algorithms. Optimization is not magic, but still a bit of a Dark Art.

Live-code -- Simulated annealing 

### Oct 1
Micro-simulation and emergent complexity in simple problems -- NK Model. Modeling field hospital supply and labor. Optimization on complex domains. Interdependence as complexity driver. 

(BONUS: Software drinking game. Don’t try this at home)

Final project idea presentation + group formation 
*HW1 due*

### Oct 8
Agent-Based Modeling I – Introduction to ABM: Emergence and Complexity; Agents and Rule-Sets; Zero intelligence still leads to emergence. Introduction to Mesa; 

Live-code -- Schelling’s Segregation Model and Health Deserts

*HW2 assigned; Final Project topic due*

### Oct 15
<<<< GUEST LECTURE TBD >>>>

### Oct 22
Agent-Based Modeling II – Coevolution, predator and prey models. System Dynamics agent-based model to simulate heart disease progression. 

Live-code -- health deserts meet somewhat intelligent agents 


### Oct 29
Agent-Based Modeling III – Interpreting ABMs: Introduction to Model evaluation – sensitivity analysis and parameter setting; Model verification and validation AXTELL 


### Nov 5
Network Analysis I – Introduction to Network Analysis: Guest Lecturer, Dr. Diane Cline (TBD); Networks as graphs; Combinatorial complexity and random graphs; Node degree; What are network data? Measures of centrality; Introduction to NetworkX; 
*HW2 due*

### Nov 12
Network Analysis II – Milgram and Kevin Bacon; Degree distributions, power laws, and small worlds; Directed network metrics (prestige); In-class exploration of network data;
HW3 assigned; 

*FINAL PROJECT PROCRASTINATION CHECK-IN*

### Nov 19
<<< GUEST LECTURE ON NETWORKS >>> 

### Nov 26

Network Analysis III – Coping with Very Large Networks: Network motifs and architecture; Network partitioning; Abstraction; Canonical system architectures and their relationship to flexibility; 


### Dec 3
Putting it all together -- revisiting rhyme and reason for modeling; picking the right techniques; drawing boundaries; validating results
*HW3 due*

### Dec 12
Final project presentations 
Final Projects Due
