import oracledb as odb
try:
    conobj = odb.connect("system/1234@localhost/xe")
    curobj = conobj.cursor()
    qry = """drop table anuj"""
    curobj.execute(qry)
    print("Drop table Successfully ")
except odb.DatabaseError as e :
    print("Problem in database ",e)