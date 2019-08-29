#!/bin/sh

cat $1 | cut -d ':' -f2|cut -d ',' -f1|egrep '"'|cut -d '"' -f2|sort|uniq|sort
