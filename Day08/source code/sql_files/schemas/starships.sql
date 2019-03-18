CREATE TABLE IF NOT EXISTS starships(
  id                     INTEGER NOT NULL PRIMARY KEY,
  name                   VARCHAR(128) NOT NULL,
  model                  VARCHAR(128) NOT NULL,
  manufacturer           VARCHAR(128) NOT NULL,
  cost_in_credits        INTEGER  NOT NULL,
  length                 INTEGER  NOT NULL,
  max_atmosphering_speed VARCHAR(128) NOT NULL,
  crew                   INTEGER  NOT NULL,
  passengers             INTEGER  NOT NULL,
  cargo_capacity         INTEGER  NOT NULL,
  consumables            VARCHAR(128) NOT NULL,
  hyperdrive_rating      NUMERIC(3,1) NOT NULL,
  MGLT                   INTEGER  NOT NULL,
  starship_class         VARCHAR(128) NOT NULL,
  created                VARCHAR(128) NOT NULL,
  edited                 VARCHAR(128) NOT NULL,
  url                    VARCHAR(128) NOT NULL
);

