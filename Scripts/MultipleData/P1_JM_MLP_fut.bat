@ECHO OFF. ECHO. 
REM P1 JM_MLP_fut 
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites
python GenerateExpRangeSitesList.py --config ./configsjm/config_MLP_s2s_future --listsites list_sites(JM1).csv --exp JM_MLP_fut

REM cd E:\Wind\Minotauro
REM python ExtractConfig.py --exp JM_MLP_fut --nconfig 2000 --machine mino --jph 100

