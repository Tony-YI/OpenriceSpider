#!/usr/bin/python

import sys;
import json;
import xlsxwriter;
import my_tool;

def read_file_as_string(filename):
	file_string = "";
	try:
		fd = open(filename,"r");
	except(IOError):
		print "ERROR: read_file_as_string -> cannot open file ";
		return "";
	file_string = fd.read();
	return file_string;

def write_to_excel(json_object):
	return ;

print "Number of arguments: ", len(sys.argv), 'arguments';
print "Argument List: ", str(sys.argv);

if(len(sys.argv) == 1):
	start_at = "2350000";
	number_of_file = 1;

if(len(sys.argv) > 2):
	start_at = sys.argv[1];
	number_of_file = sys.argv[2];
else:
	number_of_file = 1;

file_list = [];
DIR = "spiders/"
for count in range(0,int(number_of_file)):
	file_list.append("data_" + str(int(start_at) + count * 50) );
print str(file_list);

workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

count_row = 1;
worksheet.write_string(count_row,0,"comment_id");
worksheet.write_string(count_row,1,"number of recommend");
worksheet.write_string(count_row,2,"number of reviews");
worksheet.write_string(count_row,3,"date");
worksheet.write_string(count_row,4,"ratio");
count_row = count_row + 1;

for count in range(0,int(number_of_file)):
	input_string = read_file_as_string(DIR + file_list[count]);	
	record_json = json.loads(input_string);
	for count_record in range(0,len(record_json)):
		worksheet.write_number(count_row,0,int(record_json[count_record]["comment_id"]));
		worksheet.write_number(count_row,1,int(record_json[count_record]["num_of_recom"]));
		worksheet.write_number(count_row,2,int(record_json[count_record]["num_of_view"]));
		worksheet.write_date(count_row,3,record_json[count_record]["date"]);
		worksheet.write_number(count_row,4,float(record_json[count_record]["ratio"]));
		count_row = count_row + 1;

workbook.close();
