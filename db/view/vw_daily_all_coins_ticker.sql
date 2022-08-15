USE crypto;
DROP VIEW IF EXISTS vw_daily_all_coins_ticker;

CREATE OR REPLACE VIEW vw_daily_all_coins_ticker
AS

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
FROM crypto.tbl_daily_all_coins_ticker
WHERE `time` = (SELECT MAX(`time`) FROM crypto.tbl_daily_all_coins_ticker);