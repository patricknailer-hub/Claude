# Content ideas generator - creates and reads idea files for different platforms

# Define content ideas for each platform
ideas = {
    "tiktok_ideas.txt": [
        "Day in the life of a developer - 60 sec timelapse",
        "3 Python tricks you didn't know existed",
        "POV: Your code works on the first try",
        "Duet this if you can solve this coding challenge",
        "What I earn vs what I spend as a tech worker",
    ],
    "youtube_ideas.txt": [
        "Build a full-stack app from scratch in 1 hour",
        "I tried every AI coding tool so you don't have to",
        "5 side project ideas that actually make money",
        "How I landed a remote dev job with no degree",
        "Beginner to pro: Complete Python roadmap 2026",
    ],
    "cme_ideas.txt": [
        "Newsletter: Top 10 GitHub repos of the month",
        "Blog post: Why every developer needs a personal brand",
        "Twitter thread: Lessons from 5 years of freelancing",
        "Email series: 7-day intro to web development",
        "Case study: How we scaled to 1M users on a budget",
    ],
    "heygen_ideas.txt": [
        "AI avatar product demo for SaaS landing page",
        "Multilingual explainer video for global audience",
        "Personalized sales outreach video at scale",
        "AI spokesperson for weekly company updates",
        "Training video series with custom digital presenter",
    ],
}

# Create and write to each file
for filename, content_list in ideas.items():
    with open(filename, "w") as f:
        for idea in content_list:
            f.write(f"- {idea}\n")

# Read and display all files with formatting
print("=" * 55)
print("         CONTENT IDEAS DASHBOARD")
print("=" * 55)

labels = {
    "tiktok_ideas.txt": "TIKTOK IDEAS",
    "youtube_ideas.txt": "YOUTUBE IDEAS",
    "cme_ideas.txt": "CME IDEAS",
    "heygen_ideas.txt": "HEYGEN VIDEO IDEAS",
}

for filename, label in labels.items():
    with open(filename, "r") as f:
        content = f.read()
    print(f"\n  {label}")
    print("-" * 55)
    print(content)

print("=" * 55)
print(f"  Total: {sum(len(v) for v in ideas.values())} ideas across {len(ideas)} platforms")
print("=" * 55)
