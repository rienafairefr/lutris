# Third Party Libraries
from gi.repository import Gtk


class BaseApplicationWindow(Gtk.ApplicationWindow):
    """Window used to guide the user through a issue reporting process"""

    def __init__(self, application):
        Gtk.ApplicationWindow.__init__(self, icon_name="net.lutris.Lutris", application=application)
        self.application = application
        self.set_show_menubar(False)

        self.set_position(Gtk.WindowPosition.CENTER)

        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12, visible=True)
        self.vbox.set_margin_top(18)
        self.vbox.set_margin_bottom(18)
        self.vbox.set_margin_right(18)
        self.vbox.set_margin_left(18)
        self.add(self.vbox)
        self.action_buttons = Gtk.Box(spacing=6)
        self.vbox.pack_end(self.action_buttons, False, False, 0)

    def get_action_button(self, label, handler=None, tooltip=None):
        """Returns a button that can be used for the action bar"""
        button = Gtk.Button.new_with_mnemonic(label)
        if handler:
            button.connect("clicked", handler)
        if tooltip:
            button.set_tooltip_text(tooltip)
        return button

    def present(self):  # pylint: disable=arguments-differ
        """The base implementation doesn't always work, this one does."""
        self.set_keep_above(True)
        super().present()
        self.set_keep_above(False)
        super().present()
