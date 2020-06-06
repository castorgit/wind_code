@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM Paso 1 con selección de sites
REM dir e:/Wind/Scripts/Multipledata/configsjm/config_MLP_s2s.json

python JM_GenerateExpRangeSites.py --config ./configsjm/config_MLP_s2s_cas_best.json --suff 12 --listsites lista_sites_5m.csv --exp JM_MLP_cas_best
