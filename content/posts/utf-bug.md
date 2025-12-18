---
title: "Why I learned how UTF-8 works"
author: "James Mitchell"
draft: true
tags: [guide, code, c++]
date: 2025-11-28
updated: 2025-11-28
---

Here's how I finally learned how utf-8 works. I'm choosing to ignore the fact that I've been programming for over 20 years and just now decided to actually read the [specification.](https://www.ietf.org/rfc/rfc3629.txt)

The story begins with some code, as always. I was working on a new project and as I was wasting time printing the introductory text. I used ASCII art. I used escape sequence colors. I was having a lot of fun! 

{% code() %} ```c++
void printBanner(color const& c1, color const& c2)
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

    for (auto&& it: bannerf.split("\n"))
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
``` {% end %}

So far so good. The code looked right. I smashed the build button. And then saw this. 

{% code() %} ```

sad trombone... 

``` {% end %}