@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites

python GenerateExpRangeSitesList.py --config ./configsjm/config_MLP_s2s_b_JM --listsites list_sites(JM1).csv --exp JM_MLP_s2s_b

