USE crypto;

CREATE TABLE `tbl_daily_global_materialized` (
  `coins_count` int DEFAULT NULL,
  `active_markets` int DEFAULT NULL,
  `total_mcap` float DEFAULT NULL,
  `total_volume` float DEFAULT NULL,
  `btc_d` int DEFAULT NULL,
  `eth_d` int DEFAULT NULL,
  `mcap_change` int DEFAULT NULL,
  `volume_change` int DEFAULT NULL,
  `avg_change_percent` int DEFAULT NULL,
  `volume_ath` float DEFAULT NULL,
  `mcap_ath` float DEFAULT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci