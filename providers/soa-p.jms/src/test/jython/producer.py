from javax.naming import InitialContext 
from javax.jms import *
from java.util import Properties

numberOfMessage = 10
messageText = "hello"

properties = Properties()
properties.put("java.naming.factory.initial","org.jnp.interfaces.NamingContextFactory")
properties.put("java.naming.provider.url","jnp://localhost:1099")
properties.put("java.naming.factory.url.pkgs","org.jboss.naming:org.jnp.interfaces")

context = InitialContext(properties)
factory =context.lookup("ConnectionFactory")
destination = context.lookup("queue/DemoJMSProviderGW")

connection =  factory.createConnection()
session = connection.createSession(False, Session.AUTO_ACKNOWLEDGE)
producer = session.createProducer(destination)

for i in range(numberOfMessage):
  producer.send(session.createTextMessage(messageText+' ' + `i`))



