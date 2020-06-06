@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData

python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_7L_residual.json --suff 12 --listsites lista_sites_5m.csv --exp JM_CNN_7L_residual
python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_8L_residual.json --suff 12 --listsites lista_sites_5m.csv --exp JM_CNN_8L_residual
python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_sep_MIMO_7L.json --suff 12 --listsites lista_sites_5m.csv --exp JM_CNN_7L_MIMO
python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_sep_MIMO_8L.json --suff 12 --listsites lista_sites_5m.csv --exp JM_CNN_8L_MIMO
python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_7L_skip.json --suff 12 --listsites lista_sites_5m.csv --exp JM_CNN_7L_skip
python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_8L_skip.json --suff 12 --listsites lista_sites_5m.csv --exp JM_CNN_8L_skip
python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_sep_MIMO_7L.json --suff 12 --listsites lista_sites_5m.csv --exp JM_CNN_sep_7L
python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_sep_MIMO_8L.json --suff 12 --listsites lista_sites_5m.csv --exp JM_CNN_sep_8L

cd E:\Wind\Scripts\MultipleDat7