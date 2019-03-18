CREATE TABLE IF NOT EXISTS films(
  id            INTEGER NOT NULL PRIMARY KEY,
  title         VARCHAR(128) NOT NULL,
  episode_id    INTEGER  NOT NULL,
  opening_crawl VARCHAR(1282) NOT NULL,
  director      VARCHAR(128) NOT NULL,
  producer      VARCHAR(128) NOT NULL,
  release_date  DATE  NOT NULL,
  created       VARCHAR(128) NOT NULL,
  edited        VARCHAR(128) NOT NULL,
  url           VARCHAR(128) NOT NULL
);
