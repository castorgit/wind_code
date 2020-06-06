@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
REM cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites

REM python GenerateExpRangeSitesList.py --config --bsc ./configsjm/config_CNN_sep_JM --listsites list_sites(JM1).csv --exp JM_CNN_sep_b
cd E:\Wind\Minotauro
python JM_ExtractConfig.py --exp JM_CNN_sep_b --nconfig 700 --bsc --machine mino --jph 20
python JM_ExtractConfig.py --exp JM_CNN_sep_b --nconfig 700 --bsc --machine mino --jph 20
python JM_ExtractConfig.py --exp JM_CNN_sep_b --nconfig 600 --bsc --machine mino --jph 20

