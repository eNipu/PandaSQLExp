import duckdb
conn = duckdb.connect('shinkansen.duckdb')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE shinkansen(
   Station_Name          varchar 
  ,Shinkansen_Line       varchar 
  ,Year                  int 
  ,Prefecture            varchar 
  ,Distance_from_Tokyo_st double 
  ,Company            varchar
)
"""
 )

# cursor.execute("COPY shinkansen FROM 'shinkansen.csv' (HEADER)")

# print(cursor.execute('select count(*) from shinkansen').fetchall())

cursor.close()
conn.close()
