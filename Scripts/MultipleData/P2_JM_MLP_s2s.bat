@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
REM cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites

REM python GenerateExpRangeSitesList.py --config ./configsjm/config_MLP_s2s --listsites list_sites(JM1).csv --exp JM_MLP_s2s
cd E:\Wind\Minotauro
python JM_ExtractConfig.py --exp JM_MLP_s2s --nconfig 2000 --machine mino --jph 60

