from pandasql import load_births, load_meat, sqldf

pysqldf = lambda q: sqldf(q,globals())
meat = load_meat()
births = load_births()
qr = pysqldf("SELECT * FROM meat LIMIT 20;")

print(qr)