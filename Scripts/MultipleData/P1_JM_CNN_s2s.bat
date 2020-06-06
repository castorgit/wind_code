@ECHO OFF. ECHO. 
REM CNN s2s P1
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites
python GenerateExpRangeSitesList.py --config ./configsjm/config_CNN_s2s_JM --listsites list_sites(JM1).csv --exp JM_CNN_C

