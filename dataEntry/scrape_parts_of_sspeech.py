#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 19:02:56 2019

@author: jacobsolinsky
"""
import os
import json
import requests
from lxml import html
from lxml.cssselect import CSSSelector
doc = html.fromstring(requests.get("https://ojibwe.lib.umn.edu/help/ojibwe-parts-of-speech").text)
def scrape_parts_of_speech(doc):
    selector = CSSSelector(("div.container-fluid"
                            " div.row.content-container"
                            " div.col-md-9.col-sm-9.content"
                            " div.view-content"
                            " table.table.table-hover tr"))
    abbreviation_selector = CSSSelector(("td.views-field.views-field-field-lookup-abbreviation-value"
                                         " a:not([name])"))
    label_selector = CSSSelector("td.views-field.views-field-field-label-value")
    description_selector = CSSSelector("td.views-field.views-field-field-lookup-description-value")
    retval = []
    rows = selector(doc)[1:]
    for row in rows:
        abbrev = abbreviation_selector(row)[0].text
        abbrevurl = abbreviation_selector(row)[0].attrib['href']
        label = label_selector(row)[0].text.strip()
        description = description_selector(row)[0].text.strip()
        retval.append({
                "abbrev": abbrev,
                "abbrevurl": abbrevurl,
                "label": label,
                "description": description,
                })
    return retval
parts_of_speech = scrape_parts_of_speech(doc)
os.chdir("/Users/jacobsolinsky/programming/ojibwe")
with open("parts_of_speech.json", "w+") as f:
    json.dump(parts_of_speech, f)