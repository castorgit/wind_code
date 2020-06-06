@ECHO OFF. ECHO. 
REM set variables globales
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData

python JM_GenerateExpRangeSites.py --config ./configsjm/config_MLP_MIMO_1L.json --suff 12 --listsites lista_sites_5m.csv --exp JM_MLP_1L
python JM_GenerateExpRangeSites.py --config ./configsjm/config_MLP_MIMO_2L.json --suff 12 --listsites lista_sites_5m.csv --exp JM_MLP_2L
python JM_GenerateExpRangeSites.py --config ./configsjm/config_MLP_MIMO_3L.json --suff 12 --listsites lista_sites_5m.csv --exp JM_MLP_3L
python JM_GenerateExpRangeSites.py --config ./configsjm/config_MLP_MIMO_4L.json --suff 12 --listsites lista_sites_5m.csv --exp JM_MLP_4L
python JM_GenerateExpRangeSites.py --config ./configsjm/config_MLP_MIMO_5L.json --suff 12 --listsites lista_sites_5m.csv --exp JM_MLP_5L

python JM_GenerateExpRangeSites.py --config ./configsjm/config_MLP_MIMO_1L_cas.json --suff 12 --listsites lista_sites_5m.csv --exp JM_MLP_1L_cas
python JM_GenerateExpRangeSites.py --config ./configsjm/config_MLP_MIMO_2L_cas.json --suff 12 --listsites lista_sites_5m.csv --exp JM_MLP_2L_cas
python JM_GenerateExpRangeSites.py --config ./configsjm/config_MLP_MIMO_3L_cas.json --suff 12 --listsites lista_sites_5m.csv --exp JM_MLP_3L_cas
python JM_GenerateExpRangeSites.py --config ./configsjm/config_MLP_MIMO_4L_cas.json --suff 12 --listsites lista_sites_5m.csv --exp JM_MLP_4L_cas
python JM_GenerateExpRangeSites.py --config ./configsjm/config_MLP_MIMO_5L_cas.json --suff 12 --listsites lista_sites_5m.csv --exp JM_MLP_5L_cas


cd E:\Wind\Scripts\MultipleData