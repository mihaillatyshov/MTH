from RedisLogin import RedisLogin

RL = RedisLogin()

RL.AddUser("Test1", {"name" : "Михаил", "userName" : "LM", "password" : "123"})
print(RL.GetUser("Test1"))
print(RL.GetUser("Test2"))
