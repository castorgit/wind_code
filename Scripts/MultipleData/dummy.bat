@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites

python JM_GenerateExpRangeSitesList.py --config ./configsjm/config_sep_2l_s2s_JM --listsites list_sites(JM1).csv --exp JM_MLP_sep_2l
cd E:\Wind\Minotauro
REM python JM_ExtractConfig.py --exp JM_MLP_sep_2l --nconfig 2000 --machine mino --jph 100

