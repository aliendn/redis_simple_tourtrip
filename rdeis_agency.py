import redis

connection = redis.Redis(db=0)


class Travel:

    user_id = 0
    trip_id = 0
    tour_id = 0

    def __init__(self, name, phone , age):
        self.name = name
        self.phone = phone
        self.age = age



    def user(self):
        self.user_id += 1
        connection.hset(f"{self.user_id}", mapping={"name": self.name, "age":self.age, "phone":self.phone})
    
    def user_list(self,name):
        return self.connection.hgetall(name)
    
    def trip(self, user, time,  departure, destination, vehicle_type, user_id):
        users = {}
        for elm in user_id:
            user = self.connection.hgetall(elm)
            for elm1 in user:
                user[elm1.decode('utf-8')] = user.pop(elm1).decode('utf-8')
            users[elm] = user
        
        connection.hset(f"trip:{ departure}:{destination}:{time}:{vehicle_type}",mapping={"beginning": departure,"destination":destination,
        "time":time,"vehicle":vehicle_type,"passenger":users})

        self.trip_id += 1

    def trip_list(self, begin,destination, time):
        return (connection.hgetall(f"trip:{begin}:{destination}:{time}"))

    
    def tour_create(self, leader, user, price , departure, destination, details, pass_id, days):
        users={}

        for elm in pass_id:
            user = self.connection.hgetall(elm)
            for elm1 in user:
                user[elm1.decode('utf-8')] = user.pop(elm1).decode('utf-8')
            users[elm] = user


        connection.hset(f"tour:{leader}:{ departure}:{destination}",mapping={"leader":leader,"passenger": users,"days":days,"price":price,
        "beginning": departure,"destination":destination,"details":details})

        self.tour_id+=1
    

    def show_tour(self, trip_id):
        return self.r.hgetall(f"tour: {trip_id}")