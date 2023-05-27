import os
from dotenv import load_dotenv

import audiostack

directory = os.path.join('motivation', 'static', 'audio')
os.makedirs(directory, exist_ok=True)

# Then generate the audio file


# Load .env file
load_dotenv()

audiostack.api_key = os.getenv("AUDIO_STACK_DEV_KEY")

def generate_audio(story):
    # Prepare the story for audio generation
    story = story.replace('\n', ' ')
    story = story.replace('\n', ' ')
    story = story.replace('"', '')
    story = story.replace('/', '')
    story = story.replace('{', '')
    story = story.replace('}', '')
    story = story.replace('[', '')
    story = story.replace(']', '')
    text = f"""
    <as:section name="intro" soundsegment="intro">
        Welcome to Celfyre.
    </as:section>

    <as:section name="main" soundsegment="main">
        {story}
    </as:section>

    <as:section name="outro" soundsegment="outro">
        Stay inspired, motivated, and unstoppable – with Celfyre!
    </as:section>
    """

    # Listen and share your audio file
    VOICE = "aria"
    SOUND_TEMPLATE="emptyfaces"
    try:
        script = audiostack.Content.Script.create(scriptText=text,
                                                scriptName="testing")
        scriptId = script.scriptId
        item = audiostack.Speech.TTS.create(scriptItem=script, voice=VOICE)
        # simple syntax, get TTS and then download

        item = audiostack.Speech.TTS.get(item.speechId)

        mix = audiostack.Production.Mix.create(speechItem=item,
                                            #masteringPreset="balanced",
                                            soundTemplate=SOUND_TEMPLATE,
                                            public = True
                                            )
        audio_url = mix.data['files'][0]['url']

        # Return the URL.
        return audio_url
        # encoder = audiostack.Delivery.Encoder.encode_mix(productionItem=mix, preset="mp3")
        # encoder.download(fileName="motivation-track", path=directory)

    except Exception as e:
        print(e)
        print("FAILED GENERATING SCRIPT: ")

    print("Cost for this session: ", audiostack.credits_used_in_this_session())
