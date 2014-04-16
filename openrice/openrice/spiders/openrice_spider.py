from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from openrice.items import OpenriceItem
import time

class OpenriceSpider(Spider):
	name = "openrice";
	allowed_domains = "openrice.com";
	num_of_recom = 0;
	locate = 0;
	num_of_com = 50;

	start_urls = [];
	
	dataset = [];

	def __init__(self,name=None,**kwargs):
		self.comment_id = kwargs["start_at"];
		for count in range(0, self.num_of_com):
			self.start_urls.append("http://www.openrice.com/restaurant/commentdetail.htm?commentid=" + str(int(self.comment_id) + count));

	def parse(self,response):
		local_comment_id = response.url[len(response.url) - 7:len(response.url)];
		local_keyword = "<span class=\"recom_" + local_comment_id + " \">";
		local_keyword2 = "<div class=\"FL ML5 txt_18\">";
		if(str(response.status) == "503"):
			time.sleep(3);
		
		date = "";
		#try to retrieve the date information
		try:
			locate = response.body.index("date_lower");
			#cut the data before the 'date_lower'
			sub_str = response.body[locate:];
			
			locate = sub_str.index("display:none");
			#cut the data before the "display:none"
			sub_str_date = sub_str[locate:];
			#cut the data after the </span>
			end = sub_str_date.index("</span>");
			sub_str_date = sub_str_date[:end];
			locate = sub_str_date.index("2");
			sub_str_date = sub_str_date[locate:];
			date = sub_str_date;
		except:
			date = "";

		#try to retrieve the data about number of reader of the review.
		try:
			locate = response.body.index(local_keyword2);
			sub_str = response.body[locate + len(local_keyword2):];
			end = sub_str.index("</div>");
			num_of_view = sub_str[:end];
		except:
			sub_str = response.body;
			num_of_view = "0";


		#try to retrieve the data about number of recommend of the review.
		try:
			locate = sub_str.index(local_keyword);
		except:
			num_of_recom = "0";
			item = OpenriceItem();
			item["comment_id"] = local_comment_id;
			item["num_of_recom"] = num_of_recom;
			item["num_of_view"] = num_of_view;
			item["ratio"] = float(num_of_recom)/float(num_of_view);
			item["date"] = date;
			return item;
		
		sub_str = sub_str[locate + len(local_keyword):];
		sub_str = sub_str[:sub_str.index("</span>")];
		num_of_recom = sub_str;
		#print "comment_id:" + local_comment_id + ", num_of_recom:" + str(num_of_recom) + ", num_of_view:" + str(num_of_view);
		item = OpenriceItem();
		item["comment_id"] = local_comment_id;
		item["num_of_recom"] = num_of_recom;
		item["num_of_view"] = num_of_view;
		item["ratio"] = float(num_of_recom)/float(num_of_view);
		item["date"] = date;
		return item;



