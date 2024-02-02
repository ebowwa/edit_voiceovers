# automating influencers

background

i worked on a hackathon this weekend where we toy'd with automating `short film content`, we failed but ive thought on. i think we were ambitious, this dramatically scales down the complexity while also experimenting with a potentially exciting project.

we built around the idea of using twelvelabs to be our video agent, which would be a far different result and could serve as an added future feature.

this approach substitues this with assuming the user already has a video in mind and rather is interested in seeing how else an `intelligence` could see it. Audiences like content in third-person; see sports, podcasts, talkshow hosts, tiktok edits, etc

on the importance of edits see
[https://x.com/julesterpak/status/1749205480931557710?s=20]
    
## goal: 
shorts are a great medium to getting people's attention, given the attention economy any means to further attention is valuable. Shorts a great way to capture this value,some types of shorts like `narrated edits`, `commedy-reactions`, etc can simply be automated, or even other content, applying this to teaching audiences could be a great resource. 

## influencers to clone:

[https://www.instagram.com/supparay14k?igsh=ZDE1MWVjZGVmZQ==]            # our instagram download sample

[https://www.tiktok.com/@tanaradoublechocolate?_t=8jTZfv1GsLG&_r=1]      # our tiktok download sample

[(https://youtube.com/@WISEspade7?si=vMCCcuO5WCSVEPdS)]                  # our youtube download sample

## table of contents

    > `examples` : gemini api functions
    
    > `prompts` : include prompts to narrate videos
    
    > `gemini`: include gemini api handling
    
    > `video`: processing video to frame rate
    
    > `tts`: resemble text-to-speech api
    
    > `retrieval_sources`: download content via urls from social platforms

### next steps: 
- perfect llm generating & gen. sequence
  **current bug is gemini safety~ism** & **frame rates per vision preview**

- implement `retrieval_sources` into the workflow
- voice cloning
- more prompts
- gui
- gemini api depth
- ollama, together.ai, perplexity support
- more calc diff btwn frames / scrutiny
- toggable whisper/equivalent transcriptions with timestamps used in the input prompt

for installation check
``` 
requirements.txt
```

once dependencies are installed 
add your api key and rename `env.example` to `.env`
then run
```
python video-gemini.py # will send the video for gemini narration
```

gemini docs https://cloud.google.com/vertex-ai/docs/generative-ai/migrate/migrate-google-ai

```
No matter how much you test and mitigate, you can never guarantee perfection, so plan upfront how you'll spot and deal with problems that arise. Common approaches include setting up a monitored channel for users to share feedback (e.g., thumbs up/down rating) and running a user study to proactively solicit feedback from a diverse mix of users — especially valuable if usage patterns are different to expectations.
```
