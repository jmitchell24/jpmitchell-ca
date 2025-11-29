---
title: "Why I learned how UTF-8 works"
author: "James Mitchell"
draft: true
tags: [guide, code, c++]
date: 2025-11-28
updated: 2025-11-28
---

Something something LZON 

```c++
void printBanner(color const& c1, color const c2)
{
    cstrview banner = R"(
         # #### ####
       ### \/#|### |/####
      ##\/#/ \||/##/_/##/_#
    ###  \/###|/ \/ # ###
  ##_\_#\_\## | #/###_/_####
 ## #### # \ #| /  #### ##/##
  __#_--###`  |{,###---###-~  █████       ███████████    ███████    ██████   █████
            \ }{             ░░███       ░█░░░░░░███   ███░░░░░███ ░░██████ ░░███
             }}{              ░███       ░     ███░   ███     ░░███ ░███░███ ░███
             }}{              ░███            ███    ░███      ░███ ░███░░███░███
             {{}              ░███           ███     ░███      ░███ ░███ ░░██████
       , -=-~{ .-^- _         ░███      █  ████     █░░███     ███  ░███  ░░█████
             `}               ███████████ ███████████ ░░░███████░   █████  ░░█████
              {              ░░░░░░░░░░░ ░░░░░░░░░░░    ░░░░░░░    ░░░░░    ░░░░░
    )"_sv;

    vector<vector<strview>> lines;

    int maxx =0;
    int maxy =0;

    for (auto&& it: banner.split("\n"))
    {
        auto line = it.splitUtf8();
        lines.push_back(line);
        maxx = max(maxx, (int)line.size());
    }

    maxy = lines.size();

    for (size_t y = 0; y < lines.size(); ++y)
    {
        for (size_t x = 0; x < lines[y].size(); ++x)
        {

            cout << color::gradientXY(c1, c2, c2, c1,
                (float)x / maxx,
                (float)y / maxy).toFgEscCode();
            cout << lines[y][x];
        }
        cout << "\n";
    }
}


```