"""

Listens for messages on the queue.
This process runs continuously. 

Approach
---------
Simple - one producer / one consumer.


Since this process runs continuously, 
if we want to emit more messages, 
we'll need to open a new terminal window.


Terminal Reminders
------------------

- Use Control c to close a terminal and end a process.

- Use the up arrow to get the last command executed.

"""

# you can add multiple imports on one line
# but we don't recommend it for readability
import pika
import sys
import os

# Define a main function to run the program
def main():
    # Create a blocking connection to the RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    
    # Use the connection to create a communication channel
    channel = connection.channel()
    
    # Use the channel to declare a queue
    channel.queue_declare(queue="hello")
    
    # Define a callback function to be called when a message is received
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
    
    # Use the channel to consume messages from the queue
    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)
    
    # Print a message to the console for the user
    print(" [*] Waiting for messages. To exit press CTRL+C")
    
    # Start consuming messages
    channel.start_consuming()

# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
