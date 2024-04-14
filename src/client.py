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
                names = []
                while True:
                    old_name = input("Enter order name (leave empty to stop): ")
                    if not old_name:
                        break
                    new_name = input("Enter new order name: ")
                    names.append((old_name, new_name))
                response = client.updateOrders(iter([order_management_pb2.UpdateOrderRequest(old_order_name=old_name, new_order_name=new_name) for old_name, new_name in names]))
                print(response)
            elif choice == "4":
                order_names = []
                while True:
                    order_name = input("Enter order name (leave empty to start processing): ")
                    if not order_name:
                        break
                    order_names.append(order_name)
                responses = client.processOrders(iter([order_management_pb2.OrderRequest(order_name=order_name) for order_name in order_names]))
                print(responses)
                for response in responses:
                    print(response)
            else:
                print("Invalid choice!")
                continue

run()
