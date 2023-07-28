from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import argparse

def load_files(annFile, resFile):
    cocoGT = COCO(annFile)
    cocoDT = cocoGT.loadRes(resFile)
    return cocoGT, cocoDT

def calculate_metrics(annFile, resFile):
    cocoGT, cocoDT = load_files(annFile, resFile)
    
    annType = ['bbox', 'segm']
    
    for ann in annType:
        cocoEval = COCOeval(cocoGT, cocoDT, ann)
        cocoEval.evaluate()
        cocoEval.accumulate()
        cocoEval.summarize()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_gt", help="add path to gt")
    parser.add_argument("path_to_result", help="add path to result")
    args = parser.parse_args()
    calculate_metrics(args.path_to_gt, args.path_to_result)
