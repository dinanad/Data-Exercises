# Diabetes-Type-II-Risk-Prediction

In general this project divided into 5 parts.

1. Preparation Data

   This project use data from National Health and Nutrition Examination Surveys 2017 - 2018.
   - Demographic Data
   - Examination Data
   - Laboratory Data
   - Questioner Data
   Source Data : https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx
   
   The next step are define target and features, for target use questioner and data laboratory which respondent have  diabetes & prediabetes risk. After fill missing value in dataset that might be done from remining data, we exploratory data analysis and prepare data for the next stage (case I and case II).
   
2. Prediction Risk Diabetes (Case I)

  For prediction risk diabetes Data Biochemistry Profile not include in analysis because objective model. The model will be used for screening so that features are selected based on the ease of filling by user. Check percentage missing value features, association and correlation target with features. This process can help the researcher to find features which will be used in modelling. The next stage is modelling with some algorithm classifier and evalute preformance model.

3. Prediction Risk Prediabetes (Case II)

  For prediction risk prediabetes we use all features. Check percentage missing value features, association and correlation target with features. The process same with case I, we evalute preformance model and choose best model for predicting prediabetes.

4. Dashboard

  From the analysis of existing data and models, a predicting risk diabetes is compiled which consists of 3 parts, namely home, additional test and about Diabetes Risk. In the about section, you can analyze the description risk status by health weight . In the home section, you can Calculate Risk Diabetes, new data can be analyzed regarding the risk diabetes of user. And the additioanl test, you can Calculate Risk Prediabetes, new data can be analyzed regarding the risk diabetes of user.

5. Deck Presentation

  Diabetes Prediction file is a presentation deck for this project which contains an overview and a summary of how this project is carried out.
