#!/usr/bin/bash
echo "processing $1 and $2"
PNG0=$1 ## png0 <----- first image should be the BLACKEST
PNG1=$2 ## png1 <----- second image should be the WHITEST
#PNG2=$3 ## png2 <----- third - todo - this could be an opaque fg with tranparent bg
bg_size=`identify -format '%wx%h' "$1"`
#echo "bg is $bg_size" 
convert $PNG1 -resize $bg_size $PNG1
convert $PNG0 -channel RGBA -matte -colorspace gray -normalize -ordered-dither o8x8 gray_$PNG0
convert $PNG1 -channel RGBA -matte -colorspace gray -normalize -ordered-dither o8x8 gray_$PNG1
# set transparencies
convert gray_$PNG0 -fuzz 20% -transparent white t_$PNG0
convert gray_$PNG1 -fuzz 20% -transparent black t_$PNG1
# set white to transparency
composite -dissolve 30x30 -gravity South "t_$PNG1" "t_$PNG0" -alpha Set combined.png
rm $PNG0 $PNG1 gray_$PNG0 gray_$PNG1 t_$PNG0 t_$PNG1
