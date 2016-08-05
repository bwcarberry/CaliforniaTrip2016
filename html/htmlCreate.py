picList = ["angel_fall|4|Angel Fall, Oakhurst, CA",
           "aquarium|3|Aquarium of the Bay, San Fransciso, CA",
           "beach1|5|Beach Located on South Lake Tahoe, CA",
           "bishop|5|Bishop, CA","bode|29|Bodie State Park, CA",
           "bridalveil|8|Bridalveil Fall, Yosemite National Park, CA",
           "cave_rock|3|Cave Rock State Park, NV",
           "cave_rock_park|8|Cave Rock State Park, NV",
           "cave_rock_trail|4|Cave Rock Trail, NV",
           "china_town|2|San Fransciso, CA",
           "grasslands|1|Outside Oakhurst, CA",
           "halfdome|4|Half Dome, Yosomite National Park, CA",
           "harvey|1|Harvey's Casino, Stateline, NV",
           "i395|13|Along I-395, California",
           "indian_trail|8|Trail Near Bass Lake, Oakhurst, CA",
           "lands_end|12|Lands End National Park, San Francisco,CA",
           "lombard|10|Lomard St, San Francisco, CA",
           "mehlberg|12|Carol's Dad's House, Riverside, CA",
           "misson_inn|5|Mission Inn, Riverside, CA",
           "pier39|11|Pier 39, San Francisco, CA",
           "sanfran_beach|1|Beach in San Franscico, CA",
           "seals|3|Seals near Pier 39, San Francisco, CA",
           "shirley|6|Aunt Shirley's House, Coarse Gold, CA",
           "tea_garden|19|Japanese Tea Garden, San Francisco, CA",
           "trolley|5|Trolley in San Francisco, CA",
           "tunnel_view|4|Tunnel View, Yosemite National Park, CA",
           "van_sickle_park|7|Van Sickle Bi-State Park, South Lake Tahoe, CA",
           "virginia_city|19|Virginia City, NV",
           "yosemite_fall|17|Yosemite Fall, Yosemite National Park, CA",
           "yosemite_valley|3|Yosemite National Park, CA"]

imgPath = "https://bwcarberry.github.io/CaliforniaTrip2016/photo/"
##imgPath = "images/"

thumbPath = "https://bwcarberry.github.io/CaliforniaTrip2016/thumbnail/"
##thumbPath = "thumnails/"

imgPath2 = "https://bwcarberry.github.io/CaliforniaTrip2016/images/"

for img in picList:
    print img
    imgRoot = img.split("|")[0]
    imgNum =  img.split("|")[1]
    imgTitle =img.split("|")[2]

    htmlFile = open("C:\\California_2016\\htmlFiles\\" + imgRoot + ".html", "w")



    htmlFile.write("<!DOCTYPE html>\n")

    htmlFile.write("<html>\n")



    htmlFile.write("<script type=\"text/javascript\">\n")

    htmlFile.write("function showPic(pic)\n")

    htmlFile.write("{\n")


    htmlFile.write("var divShow = document.getElementById(\"divShow\");\n")

    htmlFile.write("var showImg = document.getElementById(\"showIt\");\n")


    htmlFile.write("showImg.src = pic;\n")
    htmlFile.write("}\n")

    htmlFile.write("function showNextPic()\n")
    htmlFile.write("{;\n")
    htmlFile.write("var showImg = document.getElementById(\"showIt\");\n")
    htmlFile.write("src = showImg.src;\n")

    htmlFile.write("srcNum = src.split(\"(\")[1].substring(0, 2);\n")

    htmlFile.write("if (srcNum.slice(-1) == \")\"){;\n")
    htmlFile.write("   srcNum = src.split(\"(\")[1].substring(0, 1);\n")
    htmlFile.write("};\n")

    htmlFile.write("new_srcNum = Number(srcNum) + 1;\n")

    htmlFile.write("new_src = src.split(\"%20\")[0] + \"%20(\" + new_srcNum + \")\" + \".jpg\" ;\n")


    htmlFile.write("showImg.src = new_src;\n")
    htmlFile.write("};\n")

    htmlFile.write("function showLastPic()\n")
    htmlFile.write("{;\n")
    htmlFile.write("var showImg = document.getElementById(\"showIt\");\n")
    htmlFile.write("src = showImg.src;\n")

    htmlFile.write("srcNum = src.split(\"(\")[1].substring(0, 2);\n")

    htmlFile.write("if (srcNum.slice(-1) == \")\"){;\n")
    htmlFile.write("   srcNum = src.split(\"(\")[1].substring(0, 1);\n")
    htmlFile.write("};\n")

    htmlFile.write("new_srcNum = Number(srcNum) - 1;\n")

    htmlFile.write("new_src = src.split(\"%20\")[0] + \"%20(\" + new_srcNum + \")\" + \".jpg\" ;\n")


    htmlFile.write("showImg.src = new_src;\n")
    htmlFile.write("};\n")



    htmlFile.write("</script>\n")
    htmlFile.write("<style>\n")
    htmlFile.write("div.img {    margin: 5px;    border: 1px solid #ccc;     float: left;     width: 180px;     background:white;     }\n")





    htmlFile.write("div.img:hover {\n")

    htmlFile.write("border: 1px solid #777;\n")

    htmlFile.write("}\n")


    htmlFile.write("div.img img {\n")

    htmlFile.write("width: 100%;\n")

    htmlFile.write("height: auto;\n")

    htmlFile.write("}\n")


    htmlFile.write("div.desc {\n")

    htmlFile.write("padding: 5px;\n")

    htmlFile.write("text-align: center;\n")

    htmlFile.write("background:white;\n")

    htmlFile.write("font-family: \"Arial\";\n")

    htmlFile.write("}\n")



    htmlFile.write("p {\n")

    htmlFile.write("font-family: \"Arial Black\";\n")

    htmlFile.write("font-weight: bold;\n")

    htmlFile.write("font-size: 30px;\n")

    htmlFile.write("}\n")



    htmlFile.write(".imageViewer {\n")

    htmlFile.write("width: 50%;\n")

    htmlFile.write("height: auto;\n")


    htmlFile.write("}\n")


    htmlFile.write("#showit {\n")


    htmlFile.write("}\n")




    htmlFile.write("</style>\n")
    htmlFile.write("</head>\n")




    htmlFile.write("<body bgcolor= #dbdbdb>\n")



    htmlFile.write("<div align=\"center\">\n")


    htmlFile.write("<div>\n")
    htmlFile.write("<a name=\"fullImage\"></a>")
    htmlFile.write("<p>" + imgTitle + "</p>\n")


    htmlFile.write("</div>\n")

    htmlFile.write("<div align=\"center\" id=\"divShow\" >\n")
    #htmlFile.write("<button type=\"button\">Back</button>\n")


    htmlFile.write("<a href=\"#fullImage\" onclick='showLastPic()'>")
    htmlFile.write("<img id=\"LastPic\"  src=\"" + imgPath2 + "scroll-left.gif" +"\">\n")
    htmlFile.write("</a>")
    htmlFile.write("<img class=\"imageViewer\" border=\"2\" id=\"showIt\" src=\"" + imgPath + imgRoot + " (1).jpg\">\n")
    htmlFile.write("<a href=\"#fullImage\" onclick='showNexPic()'>")
    htmlFile.write("<img id=\"NextPic\" onclick='showNextPic()' src=\"" + imgPath2 + "scroll-right.gif" +"\">\n")
    htmlFile.write("</a>")

    htmlFile.write("</div>\n")







    for x in range (1, int(imgNum)):

           htmlFile.write("<div class=\"img\">\n")

           htmlFile.write("<a href=\"#fullImage\" onclick='showPic(\"" + imgPath + imgRoot + " (" + str(x) + ").jpg\"" + ")'>\n")

           htmlFile.write("<img src=\"" + thumbPath + imgRoot + " (" + str(x) + ")_thumbnail.jpg\">\n")
           htmlFile.write("</a>\n")

           htmlFile.write("<div class=\"desc\">" + str(x) + "</div>\n")
           htmlFile.write("</div>\n")


    htmlFile.write("</div>")
    htmlFile.write("</div>")
    htmlFile.write("</body>")
    htmlFile.write("</html>")
    htmlFile.close()












