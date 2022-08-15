USE crypto;
DROP VIEW IF EXISTS vw_daily_global;

CREATE OR REPLACE VIEW vw_daily_global
AS

SELECT 
  `coins_count`,
  `active_markets`,
  `total_mcap`,
  `total_volume`,
  `btc_d`,
  `eth_d`,
  `mcap_change`,
  `volume_change`,
  `avg_change_percent`,
  `volume_ath`,
  `mcap_ath`,
  `date`
FROM crypto.tbl_daily_global
WHERE `date` = (SELECT MAX(`date`) FROM crypto.tbl_daily_global);