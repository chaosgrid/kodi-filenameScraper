#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import urllib.parse as urllib

import xbmcgui
import xbmcplugin


def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?','')
        if params[len(params)-1] == '/':
            params = params[0:len(params)-2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    return param

params=get_params()
action=urllib.unquote_plus(params["action"])
if action == 'find':
    title=urllib.unquote_plus(params["title"])
    liz=xbmcgui.ListItem(title, offscreen=True)
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=title, listitem=liz, isFolder=True)
elif action == 'getdetails':
    url=urllib.unquote_plus(params["url"])
    liz=xbmcgui.ListItem(url, offscreen=True)
    liz.setInfo('video',
        {'title': url
        })
    liz.setArt({'icon': 'DefaultVideo.png'})
    xbmcplugin.setResolvedUrl(handle=int(sys.argv[1]), succeeded=True, listitem=liz)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
