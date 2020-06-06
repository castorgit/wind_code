@ECHO OFF. ECHO. 
REM CNN_CI_s2s P1
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites
python GenerateExpRangeSitesList.py --config ./configsjm/config_CNN_Skip_2l_s2s_1.json --listsites list_sites_500.csv --exp JM_CNN_SKIP_B1
python GenerateExpRangeSitesList.py --config ./configsjm/config_CNN_Skip_2l_s2s_2.json --listsites list_sites_500.csv --exp JM_CNN_SKIP_B2
python GenerateExpRangeSitesList.py --config ./configsjm/config_CNN_Skip_2l_s2s_3.json --listsites list_sites_500.csv --exp JM_CNN_SKIP_B3
python GenerateExpRangeSitesList.py --config ./configsjm/config_CNN_Skip_2l_s2s_4.json --listsites list_sites_500.csv --exp JM_CNN_SKIP_B4
python GenerateExpRangeSitesList.py --config ./configsjm/config_CNN_Skip_2l_s2s_5.json --listsites list_sites_500.csv --exp JM_CNN_SKIP_B5

