import os


__version__ = '0.1.3'


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir


def setup(app):
    cur_dir = get_html_theme_path()
    app.add_html_theme('murray', cur_dir)
