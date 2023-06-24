##################################################################
# B-TOOLS-TTS v0.24
#
# TTS:
# talk(text, voice_id=2 [Default: C-3PO], play=True)
#
##################################################################

import requests
import base64
import json
import datetime
import btools_audio


def talk(text, voice_id=2, name=None, play=True):
        
    voices = [
        # DISNEY VOICES
        'en_us_ghostface',            # 0. Ghost Face
        'en_us_chewbacca',            # 1. Chewbacca
        'en_us_c3po',                 # 2. C3PO
        'en_us_stitch',               # 3. Stitch
        'en_us_stormtrooper',         # 4. Stormtrooper
        'en_us_rocket',               # 5. Rocket

        # ENGLISH VOICES
        'en_au_001',                  # 6. English AU - Female
        'en_au_002',                  # 7. English AU - Male
        'en_uk_001',                  # 8. English UK - Male 1
        'en_uk_003',                  # 9. English UK - Male 2
        'en_us_001',                  # 10. English US - Female (Int. 1)
        'en_us_002',                  # 11. English US - Female (Int. 2)
        'en_us_006',                  # 12. English US - Male 1
        'en_us_007',                  # 13. English US - Male 2
        'en_us_009',                  # 14. English US - Male 3
        'en_us_010',                  # 15. English US - Male 4

        # EUROPE VOICES
        'fr_001',                     # 16. French - Male 1
        'fr_002',                     # 17. French - Male 2
        'de_001',                     # 18. German - Female
        'de_002',                     # 19. German - Male
        'es_002',                     # 20. Spanish - Male

        # AMERICA VOICES
        'es_mx_002',                  # 21. Spanish MX - Male
        'br_001',                     # 22. Portuguese BR - Female 1
        'br_003',                     # 23. Portuguese BR - Female 2
        'br_004',                     # 24. Portuguese BR - Female 3
        'br_005',                     # 25. Portuguese BR - Male

        # ASIA VOICES
        'id_001',                     # 26. Indonesian - Female
        'jp_001',                     # 27. Japanese - Female 1
        'jp_003',                     # 28. Japanese - Female 2
        'jp_005',                     # 29. Japanese - Female 3
        'jp_006',                     # 30. Japanese - Male
        'kr_002',                     # 31. Korean - Male 1
        'kr_003',                     # 32. Korean - Female
        'kr_004',                     # 33. Korean - Male 2

        # SINGING VOICES
        'en_female_f08_salut_damour',  # 34. Alto
        'en_male_m03_lobby',           # 35. Tenor
        'en_female_f08_warmy_breeze',  # 36. Warmy Breeze
        'en_male_m03_sunshine_soon',   # 37. Sunshine Soon
        'en_female_ht_f08_glorious',   # 38. Glorious
        'en_male_sing_funny_it_goes_up',# 39. It Goes Up
        'en_male_m2_xhxs_m03_silly',   # 40. Chipmunk
        'en_female_ht_f08_wonderful_world',# 41. Dramatic

        # OTHER
        'en_male_narration',           # 42. Narrator
        'en_male_funny',               # 43. Wacky
        'en_female_emotional'          # 44. Peaceful
    ]

    url = "https://tiktok-tts.weilnet.workers.dev/api/generation"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'text': text,
        'voice': voices[voice_id]  # the voice id
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        resp_json = response.json()
        audio_data = base64.b64decode(resp_json['data'])
        
        # Get the current date and time
        now = datetime.datetime.now()

        # Format the date and time as a string
        timestamp = now.strftime("%Y-%m-%d %H-%M-%S")
        filename = "output-" + timestamp if name is None else name

        with open(filename + ".mp3", "wb") as f:
            f.write(audio_data)
        
        if play:
            btools_audio.play_audio("output-" + timestamp + ".mp3")

        return filename
    else:
        print(f"Request failed with status code {response.status_code}")
