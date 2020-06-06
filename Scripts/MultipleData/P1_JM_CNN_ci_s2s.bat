@ECHO OFF. ECHO. 
REM CNN_CI_s2s P1
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites
python GenerateExpRangeSitesList.py --config ./configsjm/config_CNN_CI_s2s.json --listsites list_sites(JM1).csv --exp JM_CNN_SKIP_2L

REM cd E:\Wind\Minotauro
REM python ExtractConfig.py --exp JM_CNN_CI_s2s --nconfig 2000 --machine mino --jph 42

