@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
REM cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites

REM python GenerateExpRangeSitesList.py --config ./configsjm/config_CNN_sep_3l_s2s_JM --bsc --listsites list_sites(JM1).csv --exp JM_CNN_sep_3l
cd E:\Wind\Minotauro
python JM_ExtractConfig.py --exp JM_CNN_sep_3l --bsc --nconfig 230 --machine mino --jph 5
python JM_ExtractConfig.py --exp JM_CNN_sep_3l --bsc --nconfig 230 --machine mino --jph 5
python JM_ExtractConfig.py --exp JM_CNN_sep_3l --bsc --nconfig 230 --machine mino --jph 5
python JM_ExtractConfig.py --exp JM_CNN_sep_3l --bsc --nconfig 230 --machine mino --jph 5
python JM_ExtractConfig.py --exp JM_CNN_sep_3l --bsc --nconfig 230 --machine mino --jph 5
python JM_ExtractConfig.py --exp JM_CNN_sep_3l --bsc --nconfig 230 --machine mino --jph 5
python JM_ExtractConfig.py --exp JM_CNN_sep_3l --bsc --nconfig 230 --machine mino --jph 5
python JM_ExtractConfig.py --exp JM_CNN_sep_3l --bsc --nconfig 230 --machine mino --jph 5
python JM_ExtractConfig.py --exp JM_CNN_sep_3l --bsc --nconfig 160 --machine mino --jph 4

