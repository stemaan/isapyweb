CREATE TABLE IF NOT EXISTS planets(
  id              INTEGER NOT NULL PRIMARY KEY,
  name            VARCHAR(128) NOT NULL,
  rotation_period INTEGER  NOT NULL,
  orbital_period  INTEGER  NOT NULL,
  diameter        INTEGER  NOT NULL,
  climate         VARCHAR(128) NOT NULL,
  gravity         VARCHAR(128) NOT NULL,
  terrain         VARCHAR(128) NOT NULL,
  surface_water   BIT  NOT NULL,
  population      INTEGER  NOT NULL,
  created         VARCHAR(128) NOT NULL,
  edited          VARCHAR(128) NOT NULL,
  url             VARCHAR(128) NOT NULL
);

