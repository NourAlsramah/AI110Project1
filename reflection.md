# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  It looked like a nice website that takes in use input and would compare with the answer that is correct. Can also give hints if the user selects the check box so.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1.The hints were incorrect and was telling the player to do the opposite such as go higher when they actually needed to go lower and vice versa .
  2.The score was not resetting when a new game was played.
  3.The score seemed to start at -5 instead of 0.


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude AI
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
 It suggested to set the history list to empty when the player would start a new game. I verified that this fix would make sense in this state of the game 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  It did not understand when I wanted to make sure the start setting of the score would be 0 instead of -5. I verified by running andhad to ask claude to fix a few times

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I had claude make test cases and make sure that they passed. I also ran the app.py again and tested it myself an made sure that it worked
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran multiple tests for an example i made test cases to test for the correct hint
- Did AI help you design or understand any tests? How?
Yes, I made it make me tests for each bug fix after I had it fix it for me

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  I would explain how streamlit is python code that makes a front end interface without the standard html or javascript. Reruns is used when you interact with the website the whole code file gets re run and not just the specific part of the website/code.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I like how i was making a test case after each bug that claude fixed.
- What is one thing you would do differently next time you work with AI on a coding task?
I think I would be more specifc in my prompts instead of sending multiple prompts
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I think I realized how much the code ouput is depended on how specific the prompt is.

