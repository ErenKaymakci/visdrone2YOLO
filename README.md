# VisDrone to YOLO

## VisDrone Format 

<bbox_left> , <bbox_top> , <bbox_width> , <bbox_height> , < score > , <object_category> , < truncation > , < occlusion >
 
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
  1. ignored regions 
  2. pedestrian 
  3. people 
  4. bicycle 
  5. car
  6. van 
  7. truck  
  8. tricycle  
  9. awning-tricycle 
  10. bus 
  11. motor 
  12. others 
 
