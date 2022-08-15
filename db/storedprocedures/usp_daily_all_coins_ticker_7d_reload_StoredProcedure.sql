USE crypto;

DELIMITER //
CREATE PROCEDURE usp_daily_all_coins_ticker_7d_reload()
BEGIN
CALL usp_daily_all_coins_ticker_7d_views_to_table;
END//