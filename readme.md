background

i worked on a hackathon this weekend were we experimented in automating `short film content`, we failed but ive thought on. i think we were ambitious, this dramatically scales down the complexity while also experimenting with a potentially exciting project.
we build around the idea of using twelvelabs to be our video agent, which would be a far different result but an exciting result nontheless and could serve as an added future feature.
this approach substitues this with assuming the user already has a video in mind and rather is interested in seeing how else an `intelligence` could see it
i like to watch `https://www.instagram.com/supparay14k?igsh=ZDE1MWVjZGVmZQ==` videos and i think that they can simply be automated, or even other content, applying this to teaching audiences could be a nice idea 

table of contents

    > `prompts` : include prompts to narrate videos
    > `gemini`: include gemini api handling
    > `video`: processing video to frame rate

next steps: 
- tts for the LLM calls to voice over the videos - elevenlabs is expensive for a demo. hoping to get support from resemble for the voice-cloning.
- more prompts
- gui
- gemini api depth

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
