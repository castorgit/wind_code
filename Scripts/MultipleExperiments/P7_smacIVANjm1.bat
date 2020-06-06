@ECHO OFF. 
SET var='smacCNNjm2'
ECHO %var%
set PYTHONPATH=E:\Wind
ECHO intensify experiment %var%
REM Intensify
REM Genera mas experimentos de los npar mejores
python GenerateExpConfPseudoSMAC.py --config config_crazyivan_JM.json --pconfig pconfig_crazyivan_JM.json --exp smacIVANjm1 --intensify --npar 50 --nbatches 6
REM incrementa npar hay que hacer como 1000 - 2000 experimentos

