from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

annType = 'bbox'

cocoGt=COCO(r'C:\Users\areson\Desktop\Разное\AIRI_2023\проект\restricted_result.json')
cocoDt=cocoGt.loadRes(r'C:\Users\areson\Desktop\Разное\AIRI_2023\проект\owl-vit_result2.json')

imgIds=sorted(cocoGt.getImgIds())

cocoEval = COCOeval(cocoGt,cocoDt, annType)
cocoEval.params.imgIds = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()