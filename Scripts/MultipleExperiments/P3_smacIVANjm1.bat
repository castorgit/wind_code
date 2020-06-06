@ECHO OFF. ECHO. 
REM CNN_CI_s2s P1
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleExperiments
REM Inicializa pseudoSMAC
python GenerateExpConfPseudoSMAC.py --config config_crazyivan_JM.json --pconfig pconfig_crazyivan_JM.json --init 2000 --exp smacIVANjm1 
