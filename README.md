btools (Current: 1.24)

Just some Python helper methods for GPT API, Stable Diffusion API, html, strings, and more.


------------------------------------------------------------------
- B-TOOLS-AUDIO v0.24
-
- Audio:
- play_audio(path, speed (float, optional))
-
------------------------------------------------------------------

------------------------------------------------------------------
- B-TOOLS-GOOGLE v0.24
-
- Google:
- google(query (string)) - returns a Google CSE (Custom Search Engine) JSON object - rtfm (hint: print(json.dumps(data, indent=4)) )
- Set GOOGLE_API_KEY and GOOGLE_SEARCH_ENGINE_ID in your env
-
------------------------------------------------------------------

------------------------------------------------------------------
- B-TOOLS-GPT v0.24
-
- GPT:
- gpt(prompt (req), model, messages, temperature, top_p, presence_penalty, frequency_penalty, user)
- Set OPENAI_API_KEY in your env
-
------------------------------------------------------------------

------------------------------------------------------------------
- B-TOOLS-GPT4FREE v0.24
-
- GPT4FREE:
- gpt_you(prompt) - GPT4FREE (Limited, unreliable, wysiwyg)
- 
------------------------------------------------------------------

------------------------------------------------------------------
- B-TOOLS-NET v0.24
-
- Net:
- GetHTML(url)
-
------------------------------------------------------------------

------------------------------------------------------------------
- B-TOOLS-NEWSDATA v0.24
-
- NewsData.io API:
- latest_news(query (string - optional)) - returns a JSON object with current weather
- Set NEWSDATA_API_KEY in your env
------------------------------------------------------------------

------------------------------------------------------------------
- B-TOOLS-OPENWEATHER v0.24
-
- OpenWeather:
- current_weather(city (string)) - returns a JSON object with current weather
- Set OPENWEATHER_API_KEY in your env
------------------------------------------------------------------

------------------------------------------------------------------
- B-TOOLS-SD v0.24
-
- Stable Diffusion:
- sd(prompt, save=False, save_path, negative_prompt="", steps, sampler_name,  width, height, cfg_scale,enable_hr=False, denoising_strength, 
-      hr_scale, hr_upscaler, hr_second_pass_steps, url)
- upscale(image:str, resize_factor, save=False, save_path, upscaler_1, upscaler_2, upscaler_2_visibility, width, height, url)
- load_image_as_base64() - Utility function for SD methods
-
------------------------------------------------------------------

------------------------------------------------------------------
- B-TOOLS-STRING v0.24
-
- String:
- GetStringsBetween(string, opening, close) - returns a list of strings
- GetRight(string, div) - returns a string
- GetLeft(string, div) - returns a string
- write(path, content) - Write txt to file
- read(path) - Read txt from file
- Wild2Reg(wildcard) - Input wildcard, Output RegEx
- WildcardMatch() - Utility function used by Wild2Reg()
- truncate(text, size) - Truncate to the final n characters (size = int)
-
------------------------------------------------------------------

------------------------------------------------------------------
- B-TOOLS-TRANSLATE v0.24
-
- Translate:
- translate(text, from_language, to_language, style)
-
- style = enum. Valid values: "ANTIQUATED, MODERN_LITERAL, MODERN_READABLE, MODERN_PARAPHRASE"
------------------------------------------------------------------

------------------------------------------------------------------
- B-TOOLS-TTS v0.24
-
- TTS:
- talk(text, voice_id=2 [Default: C-3PO], play=True)
-
- VOICE ID'S:
- DISNEY VOICES
'en_us_ghostface',            - 0. Ghost Face
'en_us_chewbacca',            - 1. Chewbacca
'en_us_c3po',                 - 2. C3PO
'en_us_stitch',               - 3. Stitch
'en_us_stormtrooper',         - 4. Stormtrooper
'en_us_rocket',               - 5. Rocket

- ENGLISH VOICES
'en_au_001',                  - 6. English AU - Female
'en_au_002',                  - 7. English AU - Male
'en_uk_001',                  - 8. English UK - Male 1
'en_uk_003',                  - 9. English UK - Male 2
'en_us_001',                  - 10. English US - Female (Int. 1)
'en_us_002',                  - 11. English US - Female (Int. 2)
'en_us_006',                  - 12. English US - Male 1
'en_us_007',                  - 13. English US - Male 2
'en_us_009',                  - 14. English US - Male 3
'en_us_010',                  - 15. English US - Male 4

- EUROPE VOICES
'fr_001',                     - 16. French - Male 1
'fr_002',                     - 17. French - Male 2
'de_001',                     - 18. German - Female
'de_002',                     - 19. German - Male
'es_002',                     - 20. Spanish - Male

- AMERICA VOICES
'es_mx_002',                  - 21. Spanish MX - Male
'br_001',                     - 22. Portuguese BR - Female 1
'br_003',                     - 23. Portuguese BR - Female 2
'br_004',                     - 24. Portuguese BR - Female 3
'br_005',                     - 25. Portuguese BR - Male

- ASIA VOICES
'id_001',                     - 26. Indonesian - Female
'jp_001',                     - 27. Japanese - Female 1
'jp_003',                     - 28. Japanese - Female 2
'jp_005',                     - 29. Japanese - Female 3
'jp_006',                     - 30. Japanese - Male
'kr_002',                     - 31. Korean - Male 1
'kr_003',                     - 32. Korean - Female
'kr_004',                     - 33. Korean - Male 2

- SINGING VOICES
'en_female_f08_salut_damour',  - 34. Alto
'en_male_m03_lobby',           - 35. Tenor
'en_female_f08_warmy_breeze',  - 36. Warmy Breeze
'en_male_m03_sunshine_soon',   - 37. Sunshine Soon
'en_female_ht_f08_glorious',   - 38. Glorious
'en_male_sing_funny_it_goes_up',- 39. It Goes Up
'en_male_m2_xhxs_m03_silly',   - 40. Chipmunk
'en_female_ht_f08_wonderful_world',- 41. Dramatic

- OTHER
'en_male_narration',           - 42. Narrator
'en_male_funny',               - 43. Wacky
'en_female_emotional'          - 44. Peaceful
------------------------------------------------------------------
