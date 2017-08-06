#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2, GLib

HISTORY_FILE = '/home/' + GLib.get_user_name() + '/.fullhistory.html'
HOME_PAGE = "https://ya.ru"

def on_destroy(win):
    Gtk.main_quit()

def op_page(url):
    urlent.set_text(url)
    webvw.load_uri(url)

def op_history(bttn):
    op_page('file://' + HISTORY_FILE)

def on_load_changed(webvw, event):
    url = webvw.get_uri()
    hist_file = open(HISTORY_FILE, 'a+')
    hist_file.writelines('* <a href="' + url + '">' + url + '</a></br>')
    hist_file.close()

def on_entr(urlent):
    url = urlent.get_text()
    webvw.load_uri(url)
    if (url == 'about:history'):
        op_history(webvw)
        return

    op_page(url)

def goback(g_b_bttn):
    webvw.go_back()

def goforw(g_f_bttn):
    webvw.go_forward()

win = Gtk.Window()
win.set_title('now in gUiBrows')
win.connect('destroy', on_destroy)
win.set_default_size(1024, 600)

headrbar = Gtk.HeaderBar()
headrbar.set_show_close_button(True)
win.set_titlebar(headrbar)

#scrld_win = Gtk.ScrolledWindow()

g_b_bttn = Gtk.Button()
g_f_bttn = Gtk.Button()
g_b_arrw = Gtk.Image.new_from_icon_name('go-previous', Gtk.IconSize.SMALL_TOOLBAR)
g_f_arrw = Gtk.Image.new_from_icon_name('go-next', Gtk.IconSize.SMALL_TOOLBAR)
g_b_bttn.add(g_b_arrw)
g_f_bttn.add(g_f_arrw)

hist_bttn = Gtk.Button()
hist_bttn_img = Gtk.Image.new_from_icon_name('document-open', Gtk.IconSize.SMALL_TOOLBAR)
hist_bttn.add(hist_bttn_img)
hist_bttn.connect('clicked', op_history)

headrbar.pack_start(g_b_bttn)
headrbar.pack_start(g_f_bttn)
headrbar.pack_start(hist_bttn)

webvw = WebKit2.WebView()

urlent = Gtk.Entry()
urlent.connect('activate', on_entr)
headrbar.set_custom_title(urlent)
op_page(HOME_PAGE)

#scrld_win.add(webvw)
g_b_bttn.connect('clicked', goback)
g_f_bttn.connect('clicked', goforw)

#win.add(scrld_win)
win.add(webvw)

webvw.connect('load-changed', on_load_changed)

win.show_all()

Gtk.main()

