USE crypto;

CREATE TABLE `tbl_daily_all_coins_ticker` (
  `id` varchar(45) NOT NULL,
  `symbol` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `nameid` varchar(45) NOT NULL,
  `rank` varchar(45) DEFAULT NULL,
  `price_usd` varchar(45) DEFAULT NULL,
  `percent_change_24h` varchar(45) DEFAULT NULL,
  `percent_change_1h` varchar(45) DEFAULT NULL,
  `percent_change_7d` varchar(45) DEFAULT NULL,
  `price_btc` varchar(45) DEFAULT NULL,
  `market_cap_usd` varchar(45) DEFAULT NULL,
  `volume24` varchar(45) DEFAULT NULL,
  `volume24a` varchar(45) DEFAULT NULL,
  `csupply` varchar(45) DEFAULT NULL,
  `tsupply` varchar(45) DEFAULT NULL,
  `msupply` varchar(45) DEFAULT NULL,
  `coins_num` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci