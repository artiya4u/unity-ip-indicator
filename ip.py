#!/usr/bin/python
import os
import appindicator
import gtk

ICON = os.path.abspath("./images/icon.png")


def get_ip():
    import requests

    url = "https://httpbin.org/ip"

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers)

    re = response.json()
    return re['origin']


class IPIndicator:
    def __init__(self):
        self.ip = ""
        self.ind = appindicator.Indicator("ip-indicator", ICON,
                                          appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.update()
        self.ind.set_menu(self.setup_menu())

    def setup_menu(self):
        menu = gtk.Menu()

        refresh = gtk.MenuItem("Refresh")
        refresh.connect("activate", self.on_refresh)
        refresh.show()
        menu.append(refresh)

        return menu

    def update(self):
        """
        
        Update the IP address.
        
        """
        ip = get_ip()
        if ip != self.ip:
            self.ip = ip
            self.ind.set_label(ip)

    def on_refresh(self, widget):
        self.update()


if __name__ == "__main__":
    i = IPIndicator()
    gtk.main()
