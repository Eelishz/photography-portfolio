#!/bin/python3
import json
import sys

N_COLS = 2

site_data = None
with open("site.json", "r") as f:
    site_data = json.load(f)

html_base = \
"""<!DOCTYPE html>
<html>
    <head>
        <title>Eelis Holmstén</title>
        <script scr="index.js"></script>
        <link rel="stylesheet" href="style.css">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
    </head>
    <body>
        <header>
            <div class="flex-row">
                <h1>{header_title}</h1>
            </div>
            <div class="flex-row">
                {menu_items}
            </div>
        </header>
        <div class="portfolio-container">
            <div class="flex-col">
                {col_0}
            </div>
            <div class="flex-col">
                {col_1}
            </div>
        </div>
        <footer>
            <p>Copyright © 2024 Eelis Holmstén</p>
        </footer>
    </body>
</html>"""

header_title = site_data["header_title"]



cols = ["", ""]

picture_prefix = site_data["picture_prefix"]
preview_prefix = site_data["preview_prefix"]

for i, picture in enumerate(site_data["pictures"]):
    file = picture["file"]
    caption = picture["caption"]
    col = i % N_COLS
    html_picture = f"""
            <img
                data-src={picture_prefix + file}
                srcset="{preview_prefix + file} 800w, {picture_prefix + file} 1920w"
                id={file}
                class="portfolio-image"
                loading="lazy"
            >
            """
    cols[col] += html_picture

menu_items = ""

for item in site_data["menu_items"]:
    text = item["text"]
    href = item["href"]
    menu_items += f"""
        <a href={href}>{text}</a>"""

html_output = html_base.format(
    col_0 = cols[0],
    col_1 = cols[1],
    header_title = header_title,
    menu_items = menu_items
)

print(html_output)
