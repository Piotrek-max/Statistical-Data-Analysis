# Body performance analysis
multi class classification

[Body performance analysis](https://www.kaggle.com/datasets/kukuroo3/body-performance-data?resource=download) dataset -  Kaggle.
This is data that confirmed the grade of performance with age and some exercise performance data.

## Workflow
1. [Data analysis](data_analysis.ipynb)
   - look at data
   - set proper data types / get dummies
   - fill missing data
   - create train / test split
2. [Feature selection & regularization](feature_selection.ipynb)
   - remove unnecessary / collinear features
   - scale data
   - search outliers
   - create baseline models
3. [Best model selection](model_selection.ipynb)
   - create pipelines
   - run optuna
   - choose best model
4. [Testing & Interpretation](testing.ipynb)
   - test model in order to baseline model
   - calculate model scores

5. [Use & Serve](main.py)

### Additional files
 - [Pipelines](utils/pipelines.py) - created to be optimized in optuna
 - [Serving](utils/serve.py) - contains class to serve model via http

## Data

data shape : (13393, 12)

- age : 20 ~64
- gender : F,M
- height_cm : (If you want to convert to feet, divide by 30.48)
- weight_kg
- body fat_%
- diastolic : diastolic blood pressure (min)
- systolic : systolic blood pressure (min)
- gripForce
- sit and bend forward_cm
- sit-ups counts
- broad jump_cm
- class : A,B,C,D (A: best) / stratified


## Source
[Korea Sports Promotion Foundation](https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=ace0aea7-5eee-48b9-b616-637365d665c1)
Some post-processing and filtering has done from the raw data.

