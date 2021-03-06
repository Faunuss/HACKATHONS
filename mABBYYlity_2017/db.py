import MySQLdb


class Review:
    def __init__(self, user_id, product_id, rating, price, text, image_id):
        self.user_id = user_id
        self.product_id = product_id
        self.rating = rating
        self.price = price
        self.text = text
        self.image_id = image_id
        
    def __str__(self):
        return "%s (%s) \n%s:\n\t%s\n\n%s" % (self.rating, self.price, self.user_id,  self.text,  self.image_id)
    
    def write_to_db(self):
        db = MySQLdb.connect("us-cdbr-iron-east-05.cleardb.net","ba7573e0732fc6","ab97d8e2", "heroku_054bdca41772a64", charset="utf8")
        cursor = db.cursor()
        cursor.execute("insert into reviews (user_id, product_id, rating, price, text, image_id) values (%s, %s, %s, %s, %s, %s)",
            (self.user_id, self.product_id, self.rating, self.price, self.text, self.image_id))
        db.commit()
        db.close()

def get_reviews(product_id):
    db = MySQLdb.connect("us-cdbr-iron-east-05.cleardb.net","ba7573e0732fc6","ab97d8e2", "heroku_054bdca41772a64", charset="utf8")
    cursor = db.cursor()
    cursor.execute("select * from Reviews where product_id = %s limit 5" % product_id)
    answer = []
    for row in cursor:
        answer.append(Review(row[0], row[1], row[2], row[3], row[4], row[5]))
    return answer
    db.close()
        
def get_score(product_id):
    db = MySQLdb.connect("us-cdbr-iron-east-05.cleardb.net","ba7573e0732fc6","ab97d8e2", "heroku_054bdca41772a64", charset="utf8")
    cursor = db.cursor()
    cursor.execute("select avg(rating) from Reviews where product_id = %s" % product_id)
    return cursor.fetchone()[0]
    db.close()
