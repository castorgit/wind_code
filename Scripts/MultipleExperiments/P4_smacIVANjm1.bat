@ECHO OFF. 
SET var='smacCNNjm2'
ECHO %var%
set PYTHONPATH=E:\Wind
ECHO intensify experiment %var%

python GenerateExpConfPseudoSMAC.py --config config_crazyivan_JM.json --pconfig pconfig_crazyivan_JM.json --exp smacIVANjm1 --random --npar 50 --nbatches 2

