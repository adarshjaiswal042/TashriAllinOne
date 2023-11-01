#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ["API_ID", ""]
    API_HASH = os.environ["API_HASH", ""]
    AUTH_USERS= os.environ["AUTH_USERS", "1112773045,201558573,2015585738"]
