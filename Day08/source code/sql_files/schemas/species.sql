CREATE TABLE IF NOT EXISTS species(
  id               INTEGER NOT NULL PRIMARY KEY,
  name             VARCHAR(128) NOT NULL,
  classification   VARCHAR(128) NOT NULL,
  designation      VARCHAR(128) NOT NULL,
  average_height   INTEGER  NOT NULL,
  skin_colors      VARCHAR(128) NOT NULL,
  hair_colors      VARCHAR(128) NOT NULL,
  eye_colors       VARCHAR(128) NOT NULL,
  average_lifespan INTEGER  NOT NULL,
  homeworld        VARCHAR(128) NOT NULL,
  language         VARCHAR(128) NOT NULL,
  created          VARCHAR(128) NOT NULL,
  edited           VARCHAR(128) NOT NULL,
  url              VARCHAR(128) NOT NULL
);

