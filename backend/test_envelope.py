from opaque.envelope import (
    create_envelope,
    open_envelope
)


print("Creating envelope...")


oprf_output = "test_oprf_result"


envelope = create_envelope(
    oprf_output
)


print("\nEnvelope:")
print(envelope)



secret = open_envelope(
    envelope
)


print("\nRecovered secret:")
print(secret)



print("\nEnvelope working successfully")