// Query to create index
CREATE INDEX ON :Transaction(symbol);

// Query to merge transaction nodes
MERGE (t:Transaction {symbol: $symbol})
SET t.total_value = $total_value, t.estimated_tax = $estimated_tax;

// Query to analyze transactions
MATCH (t:Transaction)
RETURN t.symbol AS symbol, t.total_value AS total_value, t.estimated_tax AS estimated_tax
ORDER BY t.total_value DESC
LIMIT 10;
