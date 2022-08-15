USE crypto;

DELIMITER //
CREATE PROCEDURE usp_daily_all_coins_ticker_views_to_table()
BEGIN
TRUNCATE TABLE tbl_daily_all_coins_ticker_materialized;

INSERT INTO tbl_daily_all_coins_ticker_materialized
(
	id, 
	symbol, 
    `name`, 
    nameid, 
    `rank`, 
    price_usd, 
    percent_change_24h, 
    percent_change_1h, 
    percent_change_7d, 
    price_btc, 
    market_cap_usd, 
    volume24, 
    volume24a, 
    csupply, 
    tsupply, 
    msupply, 
    coins_num, 
    `time`
)
SELECT
	id, 
	symbol, 
    `name`, 
    nameid, 
    `rank`, 
    price_usd, 
    percent_change_24h, 
    percent_change_1h, 
    percent_change_7d, 
    price_btc, 
    market_cap_usd, 
    volume24, 
    volume24a, 
    csupply, 
    tsupply, 
    msupply, 
    coins_num, 
    `time`
FROM vw_daily_all_coins_ticker;
END //