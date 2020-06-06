@ECHO OFF. ECHO. 
REM CNN_CI_s2s P1
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleExperiments
REM Inicializa pseudoSMAC
python GenerateExpConfPseudoSMAC.py --config config_CNN_s2s.json --pconfig pconfig_CNN_s2s.json --init 2000 --exp smacCNNjm3 
