@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites

cd E:\Wind\Minotauro
python JM_ExtractConfig.py --exp JM_MLP_s2s_b --nconfig 700 --bsc --machine mino --jph 15
python JM_ExtractConfig.py --exp JM_MLP_s2s_b --nconfig 700 --bsc --machine mino --jph 15
python JM_ExtractConfig.py --exp JM_MLP_s2s_b --nconfig 600 --bsc --machine mino --jph 15

