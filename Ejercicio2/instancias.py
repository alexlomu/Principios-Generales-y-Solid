from Authenticator import *
from DataBaseManager import *
from OrderManager import *
from PaymentProcessor import *

# Crear instancias de nuestras dependencias
database_manager = DataBaseManager("my-database-connection-string")
authenticator = Authenticator(database_manager)
payment_processor = PaymentProcessor("my-payment-api-key")

# Crear una instancia de OrderManager, pasando nuestras dependencias
order_manager = OrderManager(database_manager, authenticator, payment_processor)