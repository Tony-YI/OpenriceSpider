#!/bin/bash

unit=50
if [ -n "$1" ]; then
	start_at=$1
else 
	start_at=2350000
fi

if [ -n "$2" ]; then
	num=$2
else
	num=50
fi

num_of_file=$(expr $num / $unit)

echo "starting at $start_at"
echo "collecting $num info" 
echo "storing into $num_of_file files"

count=0
while [ $count -lt $num_of_file ]
	do
		echo "count is $count"
		current=$(expr $start_at + $count \* $unit)
		echo "current is $current"
		count=$(expr $count + 1)
		filename=data_$current;
		echo "filename is $filename";
		#echo "scrapy crawl openrice -a start_at=$current -o $filename -t json" 
		scrapy crawl openrice -a start_at=$current -o $filename -t json
	done
