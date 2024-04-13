import grpc
import order_management_pb2
import order_management_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = order_management_pb2_grpc.OrderManagementStub(channel)

        while True:
            print("1. Get Order - Unary")
            print("2. Search Orders - Streaming Server")
            print("3. Update Orders - Client Server")
            print("4. Process Orders - Birdirectional Streaming")
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                order_name = input("Enter order name: ")
                response = stub.getOrder(order_management_pb2.OrderRequest(order_name=order_name))
                print(response)
            elif choice == "2":
                num_messages = int(input("Enter number of messages: "))
                responses = stub.searchOrders(order_management_pb2.ReceiveMessagesRequest(num_messages=num_messages))
                for response in responses:
                    print(response)
            elif choice == "3":
                messages = []
                while True:
                    message = input("Enter message (leave empty to stop): ")
                    if not message:
                        break
                    messages.append(message)
                response = stub.updateOrders(iter([order_management_pb2.UploadMessagesRequest(messages=messages)]))
                print(response)
            elif choice == "4":
                messages = []
                while True:
                    message = input("Enter message (leave empty to stop): ")
                    if not message:
                        break
                    messages.append(message)
                responses = stub.processOrders(iter([order_management_pb2.ChatMessage(message=message) for message in messages]))
                for response in responses:
                    print(response)
            else:
                print("Invalid choice!")
                continue

run()
