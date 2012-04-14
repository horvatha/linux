#!/bin/bash
lynx -source http://rss.freshmeat.net/freshmeat/feeds/fm-releases-global | \
while read line; do [[ $line =~ \<title\>(.*?)\</title\> ]] && printf "%s\n" "${BASH_REMATCH[1]}"; done
