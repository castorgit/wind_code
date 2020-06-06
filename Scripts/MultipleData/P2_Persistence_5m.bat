@ECHO OFF. ECHO. 
REM CNN_CI_s2s P1
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1Genera los jobs
REM --bsc pone todo en un mismo directorio

cd E:\Wind\Minotauro
python JM_ExtractConfig.py --exp JM_Persistence_02_5m --bsc --nconfig 2000 --machine mino --jph 50

