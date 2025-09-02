import openApiCaller
import prompts
import json
import slaves as slave


prompt = prompts.prompt_daily(datum=slave.get_yesterday(), quellen="srf.ch")

data = openApiCaller.fetch_news(prompt)

with open("xDailyNews.json", "w") as f:
    json.dump(data, f, indent=2)

print(prompt)
