@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData

python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_sep_MIMO_5L.json --suff 12 --listsites lista_sites_5m.csv --exp JM_CNN_sep_5L

cd E:\Wind\Scripts\MultipleData