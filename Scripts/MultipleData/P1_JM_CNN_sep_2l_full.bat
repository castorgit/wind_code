@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites

python GenerateExpRangeSites.py --config ./configsjm/config_CNN_sep_2l_s2s_JM  --exp JM_CNN_sep_2l_FULL --isite 0 --fsite 126691

