# Menulock

### Menulock is a MacOS menu bar application that is used to invoke the screen saver.

---

# I. Installation and Prerequisites

- The only prerequisites for Menulock are Python 3.8+, the rumps module, and py2app

- 
1. Run `python3 setup.py py2app`

2. Move the generated .app package from the "dist" directory ""to `/Applications` (or elsewhere, as desired.)

3. Add menulock.app as a login item in System Preferences

---

## II. Notes

- I wrote the earliest versions of Menulock on MacOS Mojave, and checked for dark mode to determine whether to use a black or a white icon. Under MacOS Big Sur and later, the wallpaper - rather than the theme - determines the color of the menu bar; this method is unreliable. There are ways of fixing this using an icon template, but rumps (as far as I can tell from its documentation) doesn't support this directly; it would require some more complicated work directly with the Python bindings to the Objective-C functions. At present, that is not supported.

- Menulock will only lock the screen after the amount of time specified in System Preferences that the system should wait to lock the screen after the screen saver starts.

- One could achieve essentially the same result with hot corners, but I find those more of a nuisance than anything else (one has to be very careful to avoid inadvertently activating them).
