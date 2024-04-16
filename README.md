Thank you for taking interest in this model.
It means we share an interest for stroke care and prediction models. Please do not hesitate to reach out if questions or if you are interested in collaboration.

Before running the script, you need to create an excel file with following variables, in this order, one variable each column (here listed in rows to give easier overview):<br>
Brain_Age_Gap : Brain Age estimated from T1 image at admission, minus real age(we used Pyment (https://github.com/estenhl/pyment-public) <br>
Age_0 : Age at admission<br>
Lesion_volume : Lesion volume segmented on DWI takien during acute phase<br>
Gender : 1 is male, 2 is female<br>
Stent : 1 is stent, 0 is no stent<br>
pre_mRS : scale 0 - 6<br>
Ictus_Recanal_sec : Time from ictus to recanalization in seconds<br>
Procedure_sec : Procedure time in seconds (from punctuation of entry artery to recanalization or giving up)<br>
Complication_reperfusion_bleeding : 0 is no, 1 is yes<br>
Atrial_fibrillation : 0 is no, 1 is yes<br>
Kreatinin : value at admission<br>
Territory : 3 for left media, 4 for right media and 5 for posterior arterial circulation.<br>
NIHSS_admission : NIHSS score at admission<br>
NIHSS_discharge : NIHSS score at discharge<br>
mTICI_mod : modified revised mTICI where 0 is 0, 1 is 1, 2A is 2, 2B is 3, 2C is 4 and 3 is 5.<br>
Thrombolysis : 1 is yes and 0 is no<br>
Hypercholesterolemia : 1 is hypercholesterolemia defined for that subjects gender and age, 0 is normal values<br>
Diabetes : 1 is yes, 0 is no<br>
Heart_failure_1 : 1 is yes, 0 is no<br>
Smoking : <br>
Previous_stroke : 2 is previous hemorrhagic stroke, 1 is previous ischemic stroke, 0 is no<br>
Antiplatelets : Use of medication before stroke. 2 is Clopidogrel, 1 is Aspirin. Note: none of paticipants were on DAPT, which is why we do not have code for it.<br>
Anticoagulation : Use of medication before stroke. 7 is reently paused, 6 is LMWH, 5 is Edoxaban, 4 is Dabigatran, 3 is Rivaroxaban, 2 is Apixaban, 1 is Warfaring and 0 is none<br>
Statin : Use of medication before stroke. 1 is yes, 2 is no. <br>
Hb_admission	: values from blood test<br>
TRC_admission	: values from blood test<br>
Troponin_admission	: values from blood test<br>
CRP_admission : values from blood test<br>
Education_years: Years of education<br>


The script makes an excel file that contains the prediction:<br>
1 is predicted to return to work (RTW)<br>
0 is predicted to not return to work (NRTW)<br>
