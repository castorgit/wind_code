@ECHO OFF. ECHO. 
REM CNN s2s P1
set PYTHONPATH=E:\Wind
ECHO lanza programa 1
cd E:\Wind\Scripts\MultipleData
REM 1 Crear la lista de ejecuciones para un experimento con lista sites
python JM_GenerateExpRangeSites.py --config ./configsjm/config_CNN_sep_5m_12h_05 --suff 01 --listsites lista_sites_5m.csv --exp JM_CNN_sep_5m_05

