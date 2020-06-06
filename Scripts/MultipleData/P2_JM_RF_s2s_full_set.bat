@ECHO OFF. ECHO. 
REM P1 CNN s2s best
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites

REM python GenerateExpRangeSites.py --config /configsjm/config_RF_s2s(JM).json --exp JM_RF_s2s --isite 0 --fsite 126691

REM calcula el numero de jobs maximo son 48h
FOR /L %%A IN (1,1,442) DO (
  ECHO  job %%A
  cd E:\Wind\Minotauro
  python JM_ExtractConfig_all.py --exp JM_RF_s2s_2 --bsc --nconfig 287 --machine mino --jph 7 
)
