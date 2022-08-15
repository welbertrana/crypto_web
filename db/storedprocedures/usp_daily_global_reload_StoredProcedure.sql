USE crypto;

DELIMITER //
CREATE PROCEDURE usp_daily_global_reload()
BEGIN
CALL usp_daily_global_views_to_table;
END//