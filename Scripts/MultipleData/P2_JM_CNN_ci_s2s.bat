@ECHO OFF. ECHO. 
REM CNN_CI_s2s P2
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites
REM python GenerateExpRangeSitesList.py --config ./configsjm/config_CI_s2s.json --listsites list_sites(JM1).csv --exp JM_CNN_CI_s2s

cd E:\Wind\Minotauro
python JM_ExtractConfig.py --exp JM_CNN_CI_s2s --nconfig 2000 --machine mino --jph 100

