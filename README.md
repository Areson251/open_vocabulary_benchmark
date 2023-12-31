# Open Vocabulary benchmark

Репозиторий содержит в себе код для тестирования существующих моделей (LSeg, OWL-Vit, GroundingDino) поиска объектов по открытому запросу на изображениях по собственных данных в рамках летней школы AIRI 2023.

## Dataset

Данные могут быть получены по запросу к linok.sa@phystech.edu.

## Repo structure

- annotations (содержит GT разметку в формате COCO)
- methods (содержит код для получения результатов нахождения объектов по открытым запросам)
- results (содержит файлы с пердсказаниями для каждого эксперимента)
- metrics.py - код для получения метрик поиска объектов

## mAP evaluation

В качестве метрик использовались map для боксов и map для масок. Для моделей, которые предсказывают только боксы (OWL-Vit, GroundingDino), использовался SAM с промптом бокса для получения маски, для OWL-Vit бокс находился как описывающий прямоугольник предсказанной маски.

Описание экспериментов:
1) **Tag2Text** - описания объектов (с human evaluation, чтобы убедиться в отсутствии мусора), сгенерированные предобученной моделью Tag2Text по кропам боксов из GT разметки, подаются на вход моделям для поиска. Количество фотографий меньше, чем в **Indoor**.
2) **Label*** - текстовый запрос формата "a picture of {gt class name}". Количество фотографий тоже, что и в **Indoor**.
3) **Indoor** - полный набор размеченных данных, текстовый запрос для поиска - это имя класса.

|Модель\Данные| Bbox mAP Tag2Text | Bbox mAP Label* | Bbox mAP Indoor
|------------|-------------------|----------------------|-------------
| **OWL-ViT + SAM** |  0.183  |0.314 | 0.151
|**GroundingDINO + SAM**| 0.484| **0.619**| 0.360|
|**LSeg**|0.002| 0.002| 0.000|


|Модель\Данные| Seg mAP Tag2Text | Seg mAP Label* | Seg mAP Indoor
|------------|-------------------|----------------------|-------------
| **OWL-ViT + SAM** | 0.287   |0.439 | 0.193
|**GroundingDINO + SAM**| 0.568| **0.669**| 0.337|
|**LSeg**|0.001| 0.001| 0.000|

## Research

Дополнительные ислледования по модификации открытых запросов проводились в отдельном репозитории https://github.com/ZoyaV/cunning_manipulator.git. 
