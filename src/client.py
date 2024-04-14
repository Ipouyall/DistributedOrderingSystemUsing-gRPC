import grpc
import order_management_pb2
import order_management_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        client = order_management_pb2_grpc.OrderManagementStub(channel)

        while True:
            print("1. Get Order - Unary")
            print("2. Search Orders - Streaming Server")
            print("3. Update Orders - Client Streaming")
            print("4. Process Orders - Birdirectional Streaming")
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                order_name = input("Enter order name: ")
                response = client.getOrder(order_management_pb2.OrderRequest(order_name=order_name))
                print(response)
            elif choice == "2":
                order_name = input("Enter order name: ")
                responses = client.searchOrders(order_management_pb2.OrderRequest(order_name=order_name))
                for response in responses:
                    print(response)
            elif choice == "3":
                old_names = []
                new_names = []
                while True:
                    old_name = input("Enter order name (leave empty to stop): ")
                    if not old_name:
                        break
                    new_name = input("Enter new order name: ")
                    old_names.append(old_name)
                    new_names.append(new_name)
                response = client.updateOrders(iter([order_management_pb2.UpdateOrderRequest(old_order_names=old_names, new_order_names=new_names)]))
                print(response)
            elif choice == "4":
                messages = []
                while True:
                    message = input("Enter message (leave empty to stop): ")
                    if not message:
                        break
                    messages.append(message)
                responses = client.processOrders(iter([order_management_pb2.ChatMessage(message=message) for message in messages]))
                for response in responses:
                    print(response)
            else:
                print("Invalid choice!")
                continue

run()
