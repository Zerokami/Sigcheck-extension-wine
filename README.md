# Sigcheck-extension-wine
Nautilus File Manager property extension that checks and shows signatures of Windows executables by running sigcheck.exe using wine

Nemo not yet implemented.

# Requirements
Nautilus

Wine to run sigcheck.exe

sigcheck.exe by Sysinternals https://docs.microsoft.com/en-us/sysinternals/downloads/sigcheck

First download Sigcheck from Sysinternals and place sigcheck.exe in `~/.sigcheck`. The script runs `~/.sigcheck/sigcheck.exe` using wine.

Place the extension script in this location `/home/design/.local/share/nautilus-python/extensions/`. The final location should look like this `/home/design/.local/share/nautilus-python/extensions/sigcheck-property-page.py`.

# Checking signature
Open the properties of Windows executables using Nautilus. You should see a Sigcheck tab in the Properties menu. Now click the button which should read something like `Click to get Sigcheck data!`.

If everything is setup correctly you should see the signature details of the executable.
