@ECHO OFF. ECHO. 
REM CNN_CI_s2s P1
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_2L_GB.json --suff 12 --listsites lista_sites_5m.csv --exp JM_CNN_2L_GB_01
cd E:\Wind\Scripts\MultipleData

