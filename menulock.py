#!/usr/bin/env python3
# menulock.py
# Robert Ryder, 12 February 2022
# This script creates a macOS menu bar icon that, when clicked, creates a menu from which
# the screen saver can be activated. It requires that rumps be installed.
import rumps
import subprocess
import time
import os
import sys

class InvokeScreenSaverApplication(rumps.App):
    @rumps.clicked("Lock")
    def enterScreenSaver(self, _):
        time.sleep(1)  # wait one second to give user time to release the mouse; otherwise, that movement will exit the screen saver
        subprocess.Popen(['/System/Library/CoreServices/ScreenSaverEngine.app/Contents/MacOS/ScreenSaverEngine'], stdout=None, stdin=None, stderr=None)  # Set standard streams to None so as to hide console output

    @rumps.clicked("Screen Saver Preferences")
    def enterPreferencePane(self, _):
        subprocess.Popen(['open', '-b', 'com.apple.systempreferences', '/System/Library/PreferencePanes/DesktopScreenEffectsPref.prefPane'],
            stdout=None, stdin=None, stderr=None)

application = InvokeScreenSaverApplication("Menulock")

if '-d' in sys.argv:  # Enable debug mode with -d on the command line
    rumps.debug_mode(True)
elif len(sys.argv) > 1:
    sys.stderr.write("Unrecognized option %s. The only option is -d, which enables debug mode" % sys.argv[1])


# This only checks for light vs. dark mode. Under Big Sur and later versions of MacOS, light mode can have a dark menu bar. I don't quite know how to deal with that. Dark mode, it seems, can also have a light menu bar.
try:
    subprocess.check_output(['defaults', 'read', '-g', 'AppleInterfaceStyle'])
    # Dark mode is enabled if the above succeeds
    application.icon = 'menuicon-dark.png'
except subprocess.CalledProcessError:
    # UI is in light mode, and the key pair read by defaults thus does not exist.
    application.icon = 'menuicon-light.png'

application.run()
