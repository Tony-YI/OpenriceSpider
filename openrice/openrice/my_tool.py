import json;
import xlsxwriter;
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
