import grpc
from concurrent import futures
import order_management_pb2
import order_management_pb2_grpc
from datetime import datetime

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer):
    def __init__(self):
        self.server_orders = ['banana', 'apple', 'orange', 'grape', 'red apple', 'kiwi', 'mango', 'pear', 'cherry', 'green apple']

    def getOrder(self, request, context):
        order_name = request.order_name.lower()

        matching_order = None
        for order in self.server_orders:
            if order_name == order.lower():
                matching_order = order
                break

        if matching_order:
            item_name = matching_order
            timestamp = str(datetime.now())
            return order_management_pb2.OrderResponse(item_name=item_name, timestamp=timestamp)
        else:
            return order_management_pb2.OrderResponse(item_name="Item not found", timestamp="")

    def searchOrders(self, request, context):
        order_name = request.order_name.lower()
        matching_orders = [order for order in self.server_orders if order_name in order.lower()]

        if not matching_orders:
            yield order_management_pb2.OrderResponse(item_name="Item not found", timestamp=str(datetime.now()))
        else:
            for order in matching_orders:
                yield order_management_pb2.OrderResponse(item_name=order, timestamp=str(datetime.now()))

    def updateOrders(self, request_iter, context):
        recieved_old_names = []
        recieved_new_names = []

        for request in request_iter:
            recieved_old_names.extend(request.old_order_names)
            recieved_new_names.extend(request.new_order_names)

        confirmation_message = "Updates: "
        for j in range(len(recieved_old_names)):
            for i in range(len(self.server_orders)):
                if self.server_orders[i] == recieved_old_names[j]:
                    self.server_orders[i] = recieved_new_names[j]
                    confirmation_message += f"{recieved_old_names[j]} changed to {recieved_new_names[j]}, "
                    break
            else:
                confirmation_message += f"{recieved_old_names[j]} not found, "
        
        return order_management_pb2.UpdateOrderResponse(confirmation=confirmation_message)

    def processOrders(self, request_iterator, context):
        for request in request_iterator:
            received_message = request.message
            response_message = "Server received: " + received_message
            yield order_management_pb2.ChatMessage(message=response_message)

    # def processOrders(self, request_iterator, context):
    #     try:
    #         for request in request_iterator:
    #             received_message = request.message
    #             response_message = "Server received: " + received_message
    #             yield order_management_pb2.ChatMessage(message=response_message)
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         # Handle any cleanup or error recovery logic here

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


serve()
