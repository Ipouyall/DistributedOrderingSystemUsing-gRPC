import grpc
from concurrent import futures
import order_management_pb2
import order_management_pb2_grpc
from datetime import datetime

class OrderManagementServicer(order_management_Unary_pb2_grpc.OrderManagementServicer):
    def getOrder(self, request, context):
        serverOrders = ['banana', 'apple', 'orange', 'grape', 'red apple', 'kiwi', 'mango', 'pear', 'cherry', 'green apple']
        order_name = request.order_name.lower()
        matching_orders = [order for order in serverOrders if order_name in order.lower()]

        if matching_orders:
            item_name = matching_orders[0]
            timestamp = str(datetime.now())
            return order_management_Unary_pb2.OrderResponse(item_name = item_name, timestamp = timestamp)
        else:
            return order_management_Unary_pb2.OrderResponse(item_name = "Item not found", timestamp = "")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_management_Unary_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
