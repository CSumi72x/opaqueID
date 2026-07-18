from opaque.oprf import OPRFClient, OPRFServer


print("Starting OPRF test")


# Create server
server = OPRFServer()


# Create client
client = OPRFClient()


password = "123456"


# Client blinds password
blinded = client.blind_password(password)

print("\nBlinded:")
print(blinded)


# Server evaluates
evaluated = server.evaluate(blinded)

print("\nEvaluated:")
print(evaluated)


# Client unblinds
result = client.unblind(evaluated)

print("\nOPRF Output:")
print(result)


print("\nOPRF test completed successfully")