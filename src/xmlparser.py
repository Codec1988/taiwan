#/usr/bin/python

from  traffic_dataset_setter import traffic_dataset_setter

import sys
import xml.sax
import csv


newrow = []

class xmlparser(xml.sax.ContentHandler):


        """

                XML_Head [(u'listname', u'VD\u4e94\u5206\u9418\u52d5\u614b\u8cc7\u8a0a'), (u'updatetime', u'2015/04/01 00:33:00'), (u'version', u'1.1'), (u'interval', u'300')]


                lane [(u'vsrdir', u'0'), (u'laneoccupy', u'2'), (u'speed', u'85'), (u'vsrid', u'1')]

                cars [(u'volume', u'19'), (u'carid', u'S')]

                cars [(u'volume', u'0'), (u'carid', u'T')]

                cars [(u'volume', u'0'), (u'carid', u'L')]

                lane [(u'vsrdir', u'0'), (u'laneoccupy', u'0'), (u'speed', u'0'), (u'vsrid', u'2')]

                cars [(u'volume', u'0'), (u'carid', u'S')]

                cars [(u'volume', u'0'), (u'carid', u'T')]

                cars [(u'volume', u'0'), (u'carid', u'L')]

        """

	vehcount=0

        def __init__(self):

                self.traffic_controller = None



        def startElement(self, tag, attributes):

                '''

                        parse xml's

                '''

               # if str(tag).lower() ==  'xml_head':

               #         print "New xml came\n\n"


                if str(tag).lower() == 'info':

                        vd_id =  attributes.get('vdid','')

                        collect_time = attributes.get('datacollecttime','')


			global newrow 
			
			#wr.writerow(newrow)
			self.writenewline(newrow)
			newrow = []
                        newrow.append(collect_time)
			newrow.append(vd_id)


                if str(tag).lower() == 'lane':

			self.vehcount = 0 
	
                        key1 = attributes.get('vsrdir','')
			key2 =  attributes.get('vsrid','')
			newrow.append(key1)
			newrow.append(key2)
			
			

                        lane_data = attributes.get('laneoccupy','')
			newrow.append(lane_data)

			lane_data2 = attributes.get('speed','')
			newrow.append(lane_data)



                if str(tag).lower() == 'cars':

                        car_data = attributes.get('volume','')

                        newrow.append(car_data)
			self.vehcount += 1


        def parse_attributes(self,attributes):

                pass


        def endElement(self, tag):

		pass

	def writenewline(self, newrow):
		count = (len(newrow) - 2)/(self.vehcount + 4)
		timestamp = newrow[0]
		vdid = newrow[1]
		i = 2
		for datathing in range(count):
			templine = [timestamp,vdid]
			elements = self.vehcount + 4 
			while (elements > 0):
				templine.append(newrow[i])
				i += 1
				elements -= 1	
			wr.writerow(templine)
			
						
			
		
	

def parse(xml_file):

        parser = xml.sax.make_parser()

        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        Handler = xmlparser()

        parser.setContentHandler( Handler )

        parser.parse(xml_file)

xmlname = sys.argv[1]
lanecounter = 0
csvname = xmlname + ".csv"
try:
    myfile = open(csvname,'wb')
    wr = csv.writer(myfile,delimiter=";")
    newrow =  ("timestamp","vdid")
    parse(xmlname)
except:
    print "Error encountered while parsing " + xmlname


	
