@ECHO OFF. 
SET var='smacCNNjm2'
ECHO %var%
set PYTHONPATH=E:\Wind
ECHO intensify experiment %var%

python GenerateExpConfPseudoSMAC.py --config config_CNN_s2s.json --pconfig pconfig_CNN_s2s.json --exp smacCNNjm3 --random --npar 50 --nbatches 2


