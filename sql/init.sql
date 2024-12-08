DROP TABLE IF EXISTS portfolio_item;
CREATE TABLE portfolio_item(
    portfolio_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    desc VARCHAR,
    photo VARCHAR,
    audio VARCHAR
)
