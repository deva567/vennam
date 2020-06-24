def create_engine(user,
        password,
        host,
        port,
        database):
    import sqlalchemy
    import psycopg2
    import psycopg2.extras

    try:
        connection = psycopg2.connect(user=user,
        password=password,
        host=host,
        port=port,
        database=database)
        print("Database Connection Established.")
    
    except Exception as ex:
        print("An exception occurred..check the provided credentials.",+ex)
    return connection
    
    
def insert_dict(connection,schemaname,tablename,dataframe):
    from vennam import DataFrameToDict 
    import time
    import psycopg2
    try:
        
        start_time=time.time()
        dict_data=DataFrameToDict.dftodict(dataframe)
        cursor=connection.cursor()
        insert_query=f' insert into {schemaname}.{tablename}  values %s'
        psycopg2.extras.execute_values(
                cursor, insert_query, [tuple(d.values()) for d in dict_data]
            )
        connection.commit()
        cnt=len(dict_data)
        end_time=time.time()
        Elapsed_time=end_time-start_time
        info=f' {cnt} Rows loaded into DataBase in : {Elapsed_time} sec'
        print(info)
    except Exception as ex:
        print(ex)
    finally :
        connection.close()