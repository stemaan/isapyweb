CREATE TABLE IF NOT EXISTS people(
  id INTEGER NOT NULL PRIMARY KEY,
  name       VARCHAR(14) NOT NULL,
  height     INTEGER  NOT NULL,
  mass       INTEGER  NOT NULL,
  hair_color VARCHAR(128) NOT NULL,
  skin_color VARCHAR(128) NOT NULL,
  eye_color  VARCHAR(128) NOT NULL,
  birth_year VARCHAR(128) NOT NULL,
  gender     VARCHAR(128) NOT NULL,
  homeworld  VARCHAR(128) NOT NULL,
  created    VARCHAR(128) NOT NULL,
  edited     VARCHAR(128) NOT NULL,
  url        VARCHAR(128) NOT NULL
);

