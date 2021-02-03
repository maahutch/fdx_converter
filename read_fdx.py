from lxml import etree

tree = etree.parse(('noDuh.fdx'))

root=tree.getroot()

# get root element
#root = tree.getroot()

#print(root.tag)

#for child in root:
 #   print(child.tag, child.attrib)
    
#[elem.tag for elem in root.iter()]


#for Content in root.iter('Content'):
#    print(Content.attrib)
    
    


#for paragraph in root.findall("./Content/Paragraph[@Type=Scene Heading"):
   # x = paragraph.attrib
   #if x['Type'] == 'Scene Heading':
#   print(x)
   

x= root.xpath("./Content/Paragraph[@Type='Scene Heading']/child::*")
      
print(x[7].attrib)