try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote

from os.path import expanduser, join

import subprocess

from gi.repository import Nautilus, Gtk, GObject

sigcheckexe_path = join(expanduser("~"), ".sigcheck/sigcheck.exe") #If you want to set a custom sigcheck.exe path replace everything after = with sigcheck path as a python strings


class ButtonPropertyPage(GObject.GObject, Nautilus.PropertyPageProvider):
    def __init__(self):
        pass

    def get_property_pages(self, files):

        if len(files) != 1:
            return

        file = files[0]
        if file.get_uri_scheme() != 'file':
            return

        if file.is_directory():
            return

        self.filename = unquote(file.get_uri()[7:])

        self.property_label = Gtk.Label('Sigcheck')
        self.property_label.show()


        self.boxy = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.boxy.show()

        self.button = Gtk.Button(label="Click to get Sigcheck data!")
        self.button.connect("clicked", self.get_sigcheck)
        self.button.show()

        self.sw = Gtk.ScrolledWindow()

        self.texty = Gtk.TextView()

        self.sw.add(self.texty)
        self.sw.show()
        self.texty.show()

        self.boxy.pack_start(self.button, False, False, 0)
        self.boxy.pack_end(self.sw, True, True, 0)

        self.textbuffer = self.texty.get_buffer()

        return Nautilus.PropertyPage(name="NautilusPython::sigcheck_wine_button",
                                     label=self.property_label, page=self.boxy),

    def get_sigcheck(self, widget):

        try:
            output = subprocess.check_output(["wine", sigcheckexe_path, str(self.filename).replace("/", "\\"), "-nobanner"])
        except subprocess.CalledProcessError as e:
            output = e.output

            if "wine: cannot find" in str(output):
                output = """"Failed to find sigcheck.exe!
Did you place sigcheck.exe in '~/.sigcheck' directory?
First Download sigcheck from Sysinternals and extract the zip to find sigcheck.exe and then copy it to '~/.sigcheck'.
The full path of sigcheck.exe should be '~/.sigcheck/sigcheck.exe' where ~/ is the home directory of the current user"""

        finally:
            self.textbuffer.set_text(self.filename + "\n"*2 + output)
