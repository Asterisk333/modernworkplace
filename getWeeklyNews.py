import openApiCaller
import prompts
import json
import slaves as slave


prompt = prompts.prompt_weekly(kalenderwoche=slave.get_calendar_week(), quellen="srf.ch")

data = openApiCaller.fetch_news(prompt)

with open("xWeeklyNews.json", "w") as f:
    json.dump(data, f, indent=2)

print(prompt)
