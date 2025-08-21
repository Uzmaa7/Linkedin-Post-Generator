import random
import json

# Seed data from your examples (themes + tones)
themes = [
    "LinkedIn influencer sarcasm",
    "Jobseekers struggle & motivation",
    "LinkedIn scams & fakeness",
    "Corporate humor / toxic workplace",
    "Ghosting & rejection",
    "Company vs talent value",
    "Funny one-liners on LinkedIn culture",
    "Life lesson style stories"
]

# Example post templates
templates = [
    "Just saw a LinkedIn Influencer with '{buzzword}' written in the profile and {followers} followers claiming to {claim}, while actually {expose}.",
    "Jobseekers, this one’s for you. Every {step} feels like {pain}. Remember: {lesson}.",
    "Looking for jobs on LinkedIn is like {metaphor}, full of {false_promise}, but in the end {outcome}.",
    "LinkedIn scams be like: 'Congratulations, you’ve been selected for a role you didn’t apply for!' The catch? Pay {amount} for the honor.",
    "Sometimes we forget that {common_belief}, but actually {truth}.",
    "When I left a toxic workplace, I told my manager: '{savage_line}' — the silence was priceless.",
    "Next time I read an Influencer’s post, I’ll start from the last line. If there’s {giveaway}, it’s probably fake.",
    "To everyone still looking for a job: You’re not alone. {statistic}% of seekers feel {emotion}, but remember {advice}.",
    "Rejections sting, but sometimes they’re the {hidden_blessing} leading to {better_outcome}.",
    "sapne dekhna achi baat hai, lekin {sarcasm} yeh toh achi baat nahi hai na?"
]

# Word banks
buzzwords = ["Organic Growth", "Thought Leader", "Visionary", "AI Expert", "Crypto Enthusiast"]
claims = ["help you grow", "change your career", "scale your network", "teach you success"]
exposes = ["copying others", "selling courses", "resharing old tweets", "using ChatGPT badly"]
steps = ["application", "interview", "follow-up", "cold email"]
pains = ["a punch in the gut", "never-ending stress", "soul-crushing", "mentally draining"]
lessons = ["your mental health matters", "the system is broken, not you", "rejection ≠ your worth"]
metaphors = ["online dating", "a lottery", "a never-ending Netflix series"]
false_promises = ["dreams", "opportunities", "promises"]
outcomes = ["you get ghosted", "no reply comes", "silence wins"]
amounts = ["₹50,000", "$200", "₹1 lakh"]
common_beliefs = ["big company = big talent", "title defines success"]
truths = ["skills matter more", "growth > brand name", "happiness > title"]
savage_lines = [
    "Hope your son gets a manager like you",
    "May your kids experience the 'great leadership' you gave me"
]
giveaways = ["a link", "a WhatsApp number", "an affiliate link"]
statistics = [60, 70, 80, 90]
emotions = ["anxiety", "self-doubt", "hopelessness"]
advices = ["take breaks", "keep going", "don’t lose yourself"]
hidden_blessings = ["redirection", "protection", "a hidden blessing"]
better_outcomes = ["better roles", "healthier workplaces", "true growth"]
sarcasms = ["‘interested’ likhna", "‘will DM you’ likhna"]

# Function to generate a post
def generate_post():
    template = random.choice(templates)
    text = template.format(
        buzzword=random.choice(buzzwords),
        followers=random.randint(10, 500),
        claim=random.choice(claims),
        expose=random.choice(exposes),
        step=random.choice(steps),
        pain=random.choice(pains),
        lesson=random.choice(lessons),
        metaphor=random.choice(metaphors),
        false_promise=random.choice(false_promises),
        outcome=random.choice(outcomes),
        amount=random.choice(amounts),
        common_belief=random.choice(common_beliefs),
        truth=random.choice(truths),
        savage_line=random.choice(savage_lines),
        giveaway=random.choice(giveaways),
        statistic=random.choice(statistics),
        emotion=random.choice(emotions),
        advice=random.choice(advices),
        hidden_blessing=random.choice(hidden_blessings),
        better_outcome=random.choice(better_outcomes),
        sarcasm=random.choice(sarcasms)
    )
    engagement = random.randint(50, 1500)  # engagement number
    return {"text": text, "engagement": engagement}

# Generate dataset
data = [generate_post() for _ in range(1000)]

# Save to JSON
with open("linkedin_posts.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✅ Generated 1000 LinkedIn-style posts and saved to linkedin_posts.json")