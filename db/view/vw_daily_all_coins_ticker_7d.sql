USE crypto;
DROP VIEW IF EXISTS vw_daily_all_coins_ticker_7d;

CREATE OR REPLACE VIEW vw_daily_all_coins_ticker_7d
AS

SELECT * 
FROM (
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
        `time`,
        ROW_NUMBER() OVER (PARTITION BY symbol Order by `time` DESC) AS last_7d
    FROM crypto.tbl_daily_all_coins_ticker 
) RNK
WHERE last_7d <= 7