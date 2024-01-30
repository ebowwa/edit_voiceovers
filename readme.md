# automating influencers

background

i worked on a hackathon this weekend where we toy'd with automating `short film content`, we failed but ive thought on. i think we were ambitious, this dramatically scales down the complexity while also experimenting with a potentially exciting project.

we built around the idea of using twelvelabs to be our video agent, which would be a far different result and could serve as an added future feature.

this approach substitues this with assuming the user already has a video in mind and rather is interested in seeing how else an `intelligence` could see it. Audiences like content in third-person; see sports, podcasts, talkshow hosts, tiktok edits, etc

on the importance of edits see
[https://x.com/julesterpak/status/1749205480931557710?s=20]
    
goal: i like to watch [https://www.instagram.com/supparay14k?igsh=ZDE1MWVjZGVmZQ==] videos and i think that they can simply be automated, or even other content, applying this to teaching audiences could be a nice idea 

table of contents

    > `prompts` : include prompts to narrate videos
    > `gemini`: include gemini api handling
    > `video`: processing video to frame rate
    > `tts`: resemble text-to-speech api

next steps: 
- add the tts download as video overlay
- perfect llm generating & gen. sequence
- more prompts
- gui
- gemini api depth
- ollama, together.ai, perplexity support

**current bug is gemini safety~ism**

for installation check
``` 
requirements.txt
```

once dependencies are installed 
add your api key and rename `env.example` to `.env`
then run
```
python main.py
```
## note to LARGE PROVIDERS plz dont release a vision llm video model this week
