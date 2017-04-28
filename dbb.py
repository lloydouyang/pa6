import pymysql.cursors

def accessDatabase(num,question):
    # Connect to the database
    connection = pymysql.connect(host='uvaclasses.martyhumphrey.info',
                             port=3306,
                             user='UVAClasses',
                             passwd='WR6V2vxjBbqNqbts',
                             db='uvaclasses')
    s=""
    try:
        with connection.cursor() as cursor:
        # Read in the following columns and then use python to process
            sql = "SELECT `Number`,`Title`,`Instructor`,`Days`,`EnrollmentLimit` FROM `CS1178Data`"
            cursor.execute(sql)
            result = cursor.fetchall()
            numrows = len(result)    
            

    
            for i in range(0,numrows):
                if (str(result[i][0].number)==num) :
                    if (question==1):
                        s=str(result[i][1])
                    if (question==2):
                        s=str(result[i][3])
                    if (question==3):
                        s=str(result[i][2])
                    if (question==4):
                        s=str(result[i][4])
                    break
                   

    finally:
        connection.close()
    return s

if __name__ == '__main__':
    accessDatabase()
