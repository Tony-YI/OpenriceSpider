#!/usr/bin/python

import sys;

print "Number of arguments: ", len(sys.argv), 'arguments';
print "Argument List: ", str(sys.argv);

start_at = sys.argv[1];
file_list = [];
file_list.append("data_" + start_at);