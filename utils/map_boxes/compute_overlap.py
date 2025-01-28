def compute_overlap(boxes, query_boxes):
  ### boxes: Ground Truth Box
  ### query_boxes: Predicted Box

  N = boxes.shape[0] # Image 하나당 속해있는 GT Boxes 갯수
  overlaps = np.zeros((N,),dtype=np.float64) # 빈 Iou 배열 생성
  box_area = (
    (query_boxes[2] - query_boxes[0]) * 
    (query_boxes[3] - query_boxes[1])
  for n in range(N):
      ## iw: query_box랑 box의 겹치는 width 길이
      iw = (
          min(boxes[n,2], query_boxes[2] - 
          max(boxes[n,0], query_boxes[0])
      )
      if iw > 0:
         ## ih: query_box랑 box의 겹치는 height 길이
         ih = (
            min(boxes[n,3], query_boxes[3]) -
            max(boxes[n,1], query_boxes[1])
         )
         if ih > 0: 
           ## ua: 두 상자의 전체 합집합 - 교집합 
           ua = np.float64(
              (boxes[n,2] - boxes[n,0) * (boxes[n,3] - boxes[n,1]) + 
              box_area - iw*ih
            )
            overlaps[n] = iw * ih / ua ## Iou
   return overlaps
           
  
