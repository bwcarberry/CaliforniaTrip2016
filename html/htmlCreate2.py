picList = ["angel_fall|4|Angel Fall, Oakhurst, CA",
           "aquarium|3|Aquarium of the Bay, San Fransciso, CA",
           "beach1|5|Beach Located on South Lake Tahoe, CA",
           "bishop|5|Bishop, CA","bode|29|Bodie State Park, CA",
           "bridalveil|8|Bridalveil Fall, Yosemite National Park, CA",
           "Cal_Science|9|California Academy of Sciences, San Fransciso, CA",
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
           "lombard|10|Lombard St, San Francisco, CA",
           "mehlberg|20|Carol's Dad's House, Riverside, CA",
           "misson_inn|5|Mission Inn, Riverside, CA",
           "pier39|11|Pier 39, San Francisco, CA",
           "sanfran_beach|1|Beach in San Franscico, CA",
           "seals|3|Seals near Pier 39, San Francisco, CA",
           "shirley|6|Aunt Shirley's House, Coarse Gold, CA",
           "tea_garden|19|Japanese Tea Garden, San Francisco, CA",
           "trolley|5|Trolley in San Francisco, CA",
           "tunnel_view|4|Tunnel View, Yosemite National Park, CA",
           "van_sickle_park|7|Van Sickle Bi-State Park, South Lake Tahoe, CA",
           "virginia_city|15|Virginia City, NV",
           "wagon_train|9|Wagon Train",
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
    htmlFile.write("var arrowNext = document.getElementById(\"NextPic\");\n")
    htmlFile.write("src = showImg.src;\n")

    htmlFile.write("srcNum = src.split(\"(\")[1].substring(0, 2);\n")

    htmlFile.write("if (srcNum.slice(-1) == \")\"){;\n")
    htmlFile.write("   srcNum = src.split(\"(\")[1].substring(0, 1);\n")
    htmlFile.write("};\n")

    htmlFile.write("new_srcNum = Number(srcNum) + 1;\n")


    srcNum2 = str(int(imgNum) + 1)
    htmlFile.write("if (new_srcNum < " + srcNum2 +  ")\n")
    htmlFile.write("{;\n")
    #htmlFile.write("alert(new_srcNum)\n")
    htmlFile.write("arrowNext.style.visibility = 'visible';\n")

    htmlFile.write("new_src = src.split(\"%20\")[0] + \"%20(\" + new_srcNum + \")\" + \".jpg\" ;\n")


    htmlFile.write("showImg.src = new_src;\n")
    htmlFile.write("};\n")
    htmlFile.write("if (new_srcNum >= " + imgNum + ") {\n")
    #htmlFile.write("alert(\"test\");\n")
    #htmlFile.write("alert(" + imgPath + "\"end.jpg\");\n")
    #htmlFile.write("alert(\"" +  imgPath +"\"end.jpg\");\n")
    htmlFile.write("arrowNext.style.visibility = 'hidden';\n")

    #htmlFile.write("alert(""https://bwcarberry.github.io/CaliforniaTrip2016/photo/end.jpg);\n")

    htmlFile.write("new_src = src.split(\"%20\")[0] + \"%20(\" + new_srcNum + \")\" + \".jpg\" ;\n")
    #htmlFile.write("arrowNext.src = \"https://bwcarberry.github.io/CaliforniaTrip2016/photo/end.jpg\";\n")
##    htmlFile.write("};\n")
    htmlFile.write("}\n")
    htmlFile.write("if (new_srcNum > 1){\n")
    htmlFile.write("LastPic.style.visibility = 'visible';\n")
    #htmlFile.write("LastPic.src = \"https://bwcarberry.github.io/CaliforniaTrip2016/photo/left.jpg\";\n")
    htmlFile.write("}\n")
    htmlFile.write("if (new_srcNum == 1){\n")
    htmlFile.write("LastPic.style.visibility = 'hidden';\n")
    #htmlFile.write("LastPic.src = \"https://bwcarberry.github.io/CaliforniaTrip2016/photo/end.jpg\";\n")
    htmlFile.write("}\n")




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

    htmlFile.write("if (new_srcNum <= " + imgNum + ") {\n")
    htmlFile.write("NextPic.style.visibility = 'visible';\n")
    #htmlFile.write("LastPic.src = \"https://bwcarberry.github.io/CaliforniaTrip2016/photo/right.jpg\";\n")
    htmlFile.write("}\n")
    htmlFile.write("if (new_srcNum == 1){\n")
    htmlFile.write("LastPic.style.visibility = 'hidden';\n")
    #htmlFile.write("LastPic.src = \"https://bwcarberry.github.io/CaliforniaTrip2016/photo/end.jpg\";\n")

    htmlFile.write("}\n")






    htmlFile.write("};\n")



    htmlFile.write("</script>\n")
    htmlFile.write("<style>\n")
    htmlFile.write("div.img {    margin: 5px;    border: 1px solid #ccc;     float: center;     width: 180px;     background:white;     }\n")





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

    htmlFile.write("width: 65%;\n")

    htmlFile.write("height: auto;\n")


    htmlFile.write("}\n")


    htmlFile.write("#showit {\n")


    htmlFile.write("}\n")

    htmlFile.write("#LastPic{\n")
    htmlFile.write(  " width:50%;\n")
    htmlFile.write("}\n")
    htmlFile.write("#NextPic{\n")
    htmlFile.write(  " width:50%;\n")
    htmlFile.write("}\n")
    htmlFile.write("#ExitPic{\n")
    htmlFile.write(  " width:10%;\n")
    htmlFile.write("}\n")

    htmlFile.write("#picTitle{\n")
    htmlFile.write("border: 5px solid white;\n")
    htmlFile.write("border-radius: 10px;\n")
    htmlFile.write("background-color: #308446;\n")
    htmlFile.write("color: white;\n")
    htmlFile.write("width: 35%;\n")

    htmlFile.write("padding: 5px 0px 5px 0px;\n")


    htmlFile.write("}\n")








    htmlFile.write("</style>\n")
    htmlFile.write("</head>\n")




    htmlFile.write("<body bgcolor= #dbdbdb>\n")



    htmlFile.write("<div align=\"center\">\n")


    htmlFile.write("<div>\n")
    htmlFile.write("<a name=\"fullImage\"></a>")
    htmlFile.write("<p id=\"picTitle\">" + imgTitle + "</p>\n")
    htmlFile.write("<a href=\"#fullImage\" >\n")
    #htmlFile.write("<a href=\"#fullImage\" onclick=\"self.close()\"\n>")
    htmlFile.write("<img  onclick='alert(\"To return to the map tour, close this picture viewer page.  Do not click the back button.\")'  title=\"Return to the map tour\"   id=\"ExitPic\"  src=\"" + imgPath + "exit.jpg" +"\">\n")
    htmlFile.write("</a>\n")




    #htmlFile.write("<input type=\"button\" value=\"Click Here to return to the map tour\" onClick=\"self.close()\">\n")

    htmlFile.write("</div>\n")
    htmlFile.write("<table align=\"center\" id=\"divShow\" >\n")
    #htmlFile.write("<div align=\"center\" id=\"divShow\" >\n")
    #htmlFile.write("<button type=\"button\">Back</button>

    htmlFile.write("<tr align=\"center\">\n")
    htmlFile.write("<td align=\"center\">\n")
    htmlFile.write("<a href=\"#fullImage\" onclick='showLastPic()'>\n")
    htmlFile.write("<img  title=\"Click to go back\"style=\"visibility:hidden\"  id=\"LastPic\"  src=\"" + imgPath + "left.jpg" +"\">\n")
    #htmlFile.write("<img  title=\"Click to go back\"style=\"display:none\"  id=\"LastPic\"  src=\"" + imgPath2 + "scroll-left.gif" +"\">\n")
    htmlFile.write("</a>\n")
    htmlFile.write("</td>\n")


    htmlFile.write("<td align=\"center\">\n")
    htmlFile.write("<img class=\"imageViewer\" border=\"2\" id=\"showIt\" src=\"" + imgPath + imgRoot + " (1).jpg\">\n")
    htmlFile.write("</td>\n")
    htmlFile.write("<td align=\"center\">\n")
    htmlFile.write("<a href=\"#fullImage\" onclick='showNextPic()'>")
    htmlFile.write("<img title=\"Click to Advance\" id=\"NextPic\"  src=\"" + imgPath + "right.jpg" +"\">\n")
    htmlFile.write("</a>")
    htmlFile.write("</td>\n")
    htmlFile.write("</tr>\n")
    htmlFile.write("<tr align=\"center\">\n")
    htmlFile.write("<td align=\"center\">\n")
    htmlFile.write("</td>\n")
    htmlFile.write("<td valign=\"top\" align=\"center\">\n")
    htmlFile.write("<h4></h4>\n")
    htmlFile.write("</td>\n")
    htmlFile.write("<td align=\"center\">\n")
    htmlFile.write("</td>\n")
    htmlFile.write("</tr>\n")
    htmlFile.write("</table>\n")





##    for x in range (1, int(imgNum)):
##
##           htmlFile.write("<div class=\"img\">\n")
##
##           htmlFile.write("<a href=\"#fullImage\" onclick='showPic(\"" + imgPath + imgRoot + " (" + str(x) + ").jpg\"" + ")'>\n")
##
##           htmlFile.write("<img src=\"" + thumbPath + imgRoot + " (" + str(x) + ")_thumbnail.jpg\">\n")
##           htmlFile.write("</a>\n")
##
##           htmlFile.write("<div class=\"desc\">" + str(x) + "</div>\n")
##           htmlFile.write("</div>\n")


    htmlFile.write("</div>")
    htmlFile.write("</div>")
    htmlFile.write("<div>\n")


    htmlFile.write("</body>")
    htmlFile.write("</html>")
    htmlFile.close()












