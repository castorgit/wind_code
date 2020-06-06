@ECHO OFF. 
SET var='smacCNNjm2'
ECHO %var%
set PYTHONPATH=E:\Wind
ECHO intensify experiment %var%
REM Random
REM python GenerateExpConfPseudoSMAC.py --config config_CNN_s2s.json --pconfig pconfig_CNN_s2s.json --exp smacCNNjm3 --exploit random --npar 400 --nbatches 1 --confexp 600
REM Genetic
python GenerateExpConfPseudoSMAC.py --config config_CNN_s2s.json --pconfig pconfig_CNN_s2s.json --exp smacCNNjm3 --exploit genetic --npar 20 --nbatches 4 --confexp 600 --nbest 10 --cross 0.8 --mutate 0.8

REM incrementa npar hay que hacer como 1000 - 2000 experimentos
