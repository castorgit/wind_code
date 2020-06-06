@ECHO OFF. ECHO. 
REM MLP_fut STEP 2
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites
REM python GenerateExpRangeSitesList.py --config ./configsjm/config_MLP_s2s_future --listsites list_sites(JM1).csv --exp JM_MLP_fut

cd E:\Wind\Minotauro
python JM_ExtractConfig.py --exp JM_MLP_fut --nconfig 2000 --machine mino --jph 100

