
from adk import Agent

class MoodCheckAgent(Agent):
    def run(self, message):
        msg = message.lower()
        if "stress" in msg or "overwhelm" in msg:
            return "stress"
        if "sad" in msg or "down" in msg:
            return "sad"
        if "tired" in msg or "low" in msg:
            return "low-energy"
        if "happy" in msg or "good" in msg:
            return "positive"
        return "neutral"
