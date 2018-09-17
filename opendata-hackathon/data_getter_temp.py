import requests
import xml.etree.ElementTree as ET

r = requests.get("http://weather.cyi.ac.cy/data/met/CyDoM.xml")


xmparsed = ET.fromstring(r.text)

# def get_temp(station_id):
#
