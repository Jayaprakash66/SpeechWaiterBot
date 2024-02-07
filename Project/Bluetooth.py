
import multiprocessing
import bluetooth

def run_server():
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_socket.bind(("", 1))  # Replace channel number if needed
    server_socket.listen(1)

    print("Waiting for client connection...")
    client_socket, client_info = server_socket.accept()
    print("Accepted connection from:", client_info)

    # Code logic for server-client interaction
    # Replace with your server code for communication with the client device

    client_socket.close()
    server_socket.close()

def run_client():
    target_address = 'D4:8A:39:45:2B:F7'  # Replace with the Bluetooth device address
    target_port = 1  # Replace with the appropriate channel number

    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect((target_address, target_port))

    # Code logic for client-server interaction
    # Replace with your client code for communication with the server device

    client_socket.close()

if __name__ == '__main__':
    # Create separate processes for server and client
    server_process = multiprocessing.Process(target=run_server)
    client_process = multiprocessing.Process(target=run_client)

    # Start the server and client processes
    server_process.start()
    client_process.start()

    # Wait for the processes to finish
    server_process.join()
    client_process.join()
