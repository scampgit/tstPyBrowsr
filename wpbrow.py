#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk, WebKit

def on_destroy(win):
    Gtk.main_quit()

def on_entr(urlent):
    url = urlent.get_text()

    if (url == 'about:history'):
        webvw.open('file://history.html')
        return

    hist_file = open('history.html', 'a+')
    hist_file.writelines('* '+url+'<br>')
    hist_file.close()
    webvw.open(url)

def op_page(url):
    entr.set_text(url)
    webvw.load_uri(url)

def op_history(bttn):
    op_page('file://fullhistory.html')

def on_load_changd(webvw, evnt):
    url = webvw.get_uri()
    hist_file = open('/ullhistory.html', 'a+')
    hist_file.writelines('* <a href="' + url + '">' + url + '</a></br>')
    hist_file.close()

def goback(g_b_bttn):
    webvw.go_back()

def goforw(g_f_bttn):
    webvw.go_forward()

win = Gtk.Window()
win.set_title('& now in gUi!')
win.connect('destroy', on_destroy)
win.set_default_size(1024, 768)

headrbar = Gtk.HeaderBar()
headrbar.set_show_close_button(True)
win.set_titlebar(headrbar)

scrld_win = Gtk.ScrolledWindow()

g_b_bttn = Gtk.Button()
g_f_bttn = Gtk.Button()
g_b_arrw = Gtk.Image.new_from_icon_name('go-previous', Gtk.IconSize.SMALL_TOOLBAR)
g_f_arrw = Gtk.Image.new_from_icon_name('go-next', Gtk.IconSize.SMALL_TOOLBAR)
g_b_bttn.add(g_b_arrw)
g_f_bttn.add(g_f_arrw)

headrbar.pack_start(g_b_bttn)
headrbar.pack_start(g_f_bttn)

webvw = WebKit.WebView()
webvw.open('https://gnome.org')

urlent = Gtk.Entry()
urlent.connect('activate', on_entr)
headrbar.set_custom_title(urlent)

scrld_win.add(webvw)
g_b_bttn.connect('clicked', goback)
g_f_bttn.connect('clicked', goforw)

win.add(scrld_win)
#win.add(webvw)

win.show_all()

Gtk.main()

