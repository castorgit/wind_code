@ECHO OFF. ECHO. 
REM P1 CNN s2s best
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites

python GenerateExpRangeSites.py --config /configsjm/config_RF_s2s(JM).json --exp JM_RF_s2s_2 --isite 0 --fsite 126691
REM cd E:\Wind\Minotauro
REM python ExtractConfig.py --exp JM_CNN_s2s_best --nconfig 2500 --machine mino --jph 46

