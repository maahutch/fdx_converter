from lxml import etree

from scene_class import scene

tree = etree.parse(('noDuh.fdx'))

root=tree.getroot()


   

scene_number = root.xpath("./Content/Paragraph[@Type='Scene Heading']")
      
all_scenes = []

for i in range(0, len(scene_number)):
    
    no = scene_number[i].attrib['Number']
    
    tmp_scene = scene(scene_no = no)
    
    all_scenes.append(tmp_scene)
    

print(all_scenes)