import xml.etree.ElementTree as ET
import csv

tree = ET.parse('C:/Users/maahutch/OneDrive/NoDuh2.1-Copy.fdx')

    # get root element
root = tree.getroot()

print(root)
