USE crypto;

DELIMITER //
CREATE PROCEDURE usp_daily_global_views_to_table()
BEGIN
TRUNCATE TABLE tbl_daily_global_materialized;

INSERT INTO tbl_daily_global_materialized
(
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
)
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
FROM vw_daily_global;
END //