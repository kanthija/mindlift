from agents.mood_agent import MoodCheckAgent
from agents.wellness_agent import WellnessCoachAgent
from agents.habits_agent import HabitBuilderAgent
from agents.reflection_agent import ReflectionAgent
from agents.calm_agent import CalmAgent

class MindLiftOrchestrator:
    def __init__(self):
        self.mood = MoodCheckAgent()
        self.wellness = WellnessCoachAgent()
        self.habits = HabitBuilderAgent()
        self.reflect = ReflectionAgent()
        self.calm = CalmAgent()

    def run(self, message):
        mood = self.mood.run(message)

        if mood == "stress":
            return self.wellness.run(message) + "\n" + self.calm.run()
        if mood == "sad":
            return self.reflect.run() + "\n" + self.wellness.run(message)
        if mood == "low-energy":
            return self.habits.run()
        if mood == "positive":
            return "You're doing well! Here's a gratitude prompt:\n" + self.reflect.run()
        return self.habits.run()

