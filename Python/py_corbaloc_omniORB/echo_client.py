#!/usr/bin/env python

import sys
from omniORB import CORBA
import Example

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# ior = sys.argv[1]
# obj = orb.string_to_object(ior)

ref = 'corbaloc::localhost:5678/ExampleEcho';
obj = orb.string_to_object(ref)

eo = obj._narrow(Example.Echo)

if eo is None:
    print "Object reference is not an Example::Echo"
    sys.exit(1)

message = "Hello from Python"
result  = eo.echoString(message)

print "I said '%s'. The object said '%s'." % (message,result)
