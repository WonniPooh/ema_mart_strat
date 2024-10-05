import time
import json
import threading
import websockets.sync.server
from common import *
from websockets.exceptions import ConnectionClosed

VALID_PASSWORD = "secret_password"
ACTIVE_CONNECTIONS_COUNT = 0

def handle_client_output(websocket, output_cmd_queue):
    try:
        print("Connection start output")
        while websocket.is_active:
            try:
                message = output_cmd_queue.get_nowait()
                print(f"Sending: {message}")
                websocket.send(message)
            except:
                time.sleep(0.5)

    except Exception as e:
        handle_exception(e)
    finally:
        print("Connection closed output")

def handle_client_input(websocket, 
                        input_cmd_queue,
                        output_cmd_queue):
    try:
        password = websocket.recv()
        websocket.is_active = True
        print(f"Received password attempt: {password}")

        if password != VALID_PASSWORD:
            websocket.send(json.dumps({"type": "error", "msg":"Invalid password. Connection closed."}))
            print("Connection closed due to invalid password.")
            return

        if ACTIVE_CONNECTIONS_COUNT > 1:
            websocket.send(json.dumps({"type": "error", "msg":"Only 1 active connection allowed."}))
            print("Connection closed due to 1 active connection already present.")
            return
        
        websocket.send(json.dumps({"type": "info", "msg":"Password accepted. Welcome!"}))

        forward_msg_client = threading.Thread(target=handle_client_output, 
                                              args=(websocket, output_cmd_queue))
        forward_msg_client.start()

        while True:
            try:
                message = websocket.recv(timeout=5)
            except TimeoutError:
                continue
            except ConnectionClosed:
                print("Connection closed input")
                websocket.is_active = False
                break
            except Exception as e:
                print(e)
                handle_exception(e)
            print("process msg")
            try:
                input_cmd_queue.put_nowait(message)
            except Exception as e:
                handle_exception(e)
            print(f"Received: {message}")          

    except Exception as e:
        handle_exception(e, "Connection closed")


# Function to start WebSocket server
def start_server(input_cmd_queue, output_cmd_queue):
    # Define a handler for the single WebSocket connection
    def ws_handler(ws_socket):
        with ws_socket:
            global ACTIVE_CONNECTIONS_COUNT
            ACTIVE_CONNECTIONS_COUNT += 1
            try:
                handle_client_input(ws_socket, 
                                    input_cmd_queue,
                                    output_cmd_queue)
            finally:
                ACTIVE_CONNECTIONS_COUNT -= 1

    # Create a WebSocket server and bind it to a host and port
    with websockets.sync.server.serve(ws_handler, "localhost", 8877) as server:
        print("WebSocket server is running on ws://localhost:8877")
        server.serve_forever()

# Create a single-threaded WebSocket server
def run_single_thread_server(input_cmd_queue, output_cmd_queue):  
    # Start the WebSocket server to handle this single client
    server_thread = threading.Thread(target=start_server,
                                     args=(input_cmd_queue, output_cmd_queue))
    server_thread.start()
    return server_thread

if __name__ == "__main__":
    run_single_thread_server()
