@ECHO OFF. ECHO. 
REM P1 CNN s2s best
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
REM cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites

REM python GenerateExpRangeSitesList.py --config ./configsjm/config_CNN_s2s_best --listsites list_sites(JM1).csv --exp JM_CNN_s2s_best
cd E:\Wind\Minotauro
python JM_ExtractConfig.py --exp JM_CNN_s2s_best --nconfig 2000 --machine mino --jph 44

