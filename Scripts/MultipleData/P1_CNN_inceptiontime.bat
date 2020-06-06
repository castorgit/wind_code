@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites
cd E:\Wind\Scripts\MultipleData
python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_TimeInception_03 --suff 12 --listsites lista_sites_5m.csv --exp JM_CNN_IT_03
cd E:\Wind\Scripts\MultipleData
