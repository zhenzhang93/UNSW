#!/bin/sh

urlunder="http://legacy.handbook.unsw.edu.au/vbook2018/brCoursesByAtoZ.jsp?StudyLevel=Undergraduate&descr="
urlpost="http://legacy.handbook.unsw.edu.au/vbook2018/brCoursesByAtoZ.jsp?StudyLevel=Postgraduate&descr=" 

wget -q -O- "$urlunder$1" "$urlpost$1"|egrep "$1[0-9]{4}.html"|sed -r "s/.*($1[0-9]{4}).html[^>]*>([^<]*)<.*/\1 \2/"|sed "s/ *$//"|sort|uniq|sort
