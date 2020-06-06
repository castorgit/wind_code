@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites
python JM_GenerateExpRangeSites.py --listsites lista_sites_5m.csv --config ./configsjm/config_MLP_5m.json --suff 01 --exp Pollo
cd E:\Wind\Scripts\MultipleData