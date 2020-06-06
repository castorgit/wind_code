@ECHO OFF. ECHO. 
REM CNN_CI_s2s P1
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites
python GenerateExpRangeSitesList.py --config ./configsjm/config_CNN_sep_2l_s2s_GB_JM.json --listsites list_sites(JM1).csv --exp JM_CNN_sep_2l_GB1

REM cd E:\Wind\Minotauro
REM python ExtractConfig.py --exp JM_CNN_CI_s2s --nconfig 2000 --machine mino --jph 42

