# VisDrone to YOLO

## VisDrone Format 

<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,<score>,<object_category>,<truncation>,<occlusion>

| Value  | Explanation |
| ------------- | ------------- |
| bbox_left  | Sınırlayıcı kutunun sol-üst koordinatının x değeri |
| bbox_top  | Sınırlayıcı kutunun sol-üst köşesinin y değeri  |
| bbox_width  | Sınırlayıcı kutunun genişliği  |
| bbox_height  | Sınırlayıcı kutunun yüksekliği  |
| score | _ |
| object_category | nesnenin sınıf indeksi | 
| truncation | _ |
| occlusion | _ |
  
**VisDrone sınıfları:** 
  - ignored regions (0) 
  - pedestrian (1) 
  - people (2)
  - bicycle (3)
  - car (4)
  - van (5)
  - truck (6) 
  - tricycle (7) 
  - awning-tricycle (8)
  - bus (9)
  - motor (10)
  - others (11)
 
