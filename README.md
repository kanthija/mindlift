# MindLift – A Multi-Agent Mental Wellness Assistant

MindLift is a multi-agent system built using the **Google Agent Development Kit (ADK)**.  
It provides mental wellness support through mood detection, calming prompts, tiny habits, and reflection cues.

>  Disclaimer: This is a general wellness tool. It is NOT a medical or diagnostic system.

---

##  Features

- Mood detection (stressed, sad, low energy, neutral, positive)
- Stress-relief & grounding techniques
- 1–3 minute micro-habit recommendations
- Journaling prompts for reflection
- Breathing exercises
- Multi-agent workflow using ADK

---

## Architecture

```
MindLift_Orchestrator
│
├── MoodCheck Agent
├── Wellness Coach Agent
├── Habit Builder Agent
├── Reflection Agent
└── Calm (Breathing) Agent
```

Orchestrator routes user messages and combines responses.

---

## Tools & Utilities

- **Sentiment Analyzer Tool**
- **Habit Library (JSON)**
- **Reflection Prompt Generator**
- **Session Memory Manager**

---

## Project Structure

```
mindlift/
│
├── orchestrator.py
├── agents/
│   ├── mood_agent.py
│   ├── wellness_agent.py
│   ├── habits_agent.py
│   ├── reflection_agent.py
│   └── calm_agent.py
│
├── tools/
│   ├── sentiment_tool.py
│   ├── habit_library.json
│   └── reflection_prompts.json
│
└── README.md
```

---

## Running the Project

```
python orchestrator.py
```

---

## Future Enhancements

- Mood-pattern tracker  
- Celebration agent for achievements  
- Voice-guided breathing  
- Calendar reminders  

---

##  Author

**Kanthija Annamreddi**  
AI & Web Dev Learner  


