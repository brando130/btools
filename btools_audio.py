##################################################################
# B-TOOLS-AUDIO v0.24
#
# Audio:
# play_audio(path, speed (float, optional))
#
##################################################################

import pyglet

def play_audio(file_path, speed=1.0):
    player = pyglet.media.Player()
    source = pyglet.media.load(file_path)
    player.queue(source)

    # Set the playback speed
    player.pitch = speed

    player.play()

    def on_audio_end(dt):
        pyglet.app.exit()

    # schedule the on_audio_end function to run after the audio finishes
    pyglet.clock.schedule_once(on_audio_end, source.duration)

    # this will block until all scheduled functions have run
    pyglet.app.run()