import grpc
from concurrent import futures
import order_management_pb2
import order_management_pb2_grpc
from datetime import datetime

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer):
        
    def getOrder(self, request, context):
        server_orders = ['banana', 'apple', 'orange', 'grape', 'red apple', 'kiwi', 'mango', 'pear', 'cherry', 'green apple']
        order_name = request.order_name.lower()
        matching_orders = [order for order in server_orders if order_name in order.lower()]

        if matching_orders:
            item_name = matching_orders[0]
            timestamp = str(datetime.now())
            return order_management_pb2.OrderResponse(item_name=item_name, timestamp=timestamp)
        else:
            return order_management_pb2.OrderResponse(item_name="Item not found", timestamp="")

    def searchOrders(self, request, context):
        server_orders = ['banana', 'apple', 'orange', 'grape', 'red apple', 'kiwi', 'mango', 'pear', 'cherry', 'green apple']
        order_name = request.order_name.lower()
        matching_orders = [order for order in server_orders if order_name in order.lower()]

        if not matching_orders:
            yield order_management_pb2.OrderResponse(item_name="Item not found", timestamp=str(datetime.now()))
        else:
            for order in matching_orders:
                yield order_management_pb2.OrderResponse(item_name=order, timestamp=str(datetime.now()))

    def updateOrders(self, request_iterator, context):
        received_messages = []
        for message in request_iterator:
            received_messages.extend(message.messages)
        confirmation_message = f"Received {len(received_messages)} messages."
        return order_management_pb2.UploadMessagesResponse(confirmation=confirmation_message)

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
