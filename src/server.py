import grpc
from concurrent import futures
import order_management_pb2
import order_management_pb2_grpc
from datetime import datetime

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer):
    def __init__(self):
        self.server_orders = ['banana', 'apple', 'orange', 'grape', 'red apple', 'kiwi', 'mango', 'pear', 'cherry', 'green apple']
        self.processedShipmentId = 1

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
        confirmation_message = "Updates: "
        
        for request in request_iter:
            for i in range(len(self.server_orders)):
                if self.server_orders[i] == request.old_order_name:
                    self.server_orders[i] = request.new_order_name
                    confirmation_message += f"{request.old_order_name} changed to {request.new_order_name} | "
                    break
            else:
                confirmation_message += f"{request.old_order_name} not found | "

        return order_management_pb2.UpdateOrderResponse(confirmation=confirmation_message)

    def processOrders(self, request_iterator, context):
        shipmentOrders = []
        for request in request_iterator:
            if request.order_name not in self.server_orders:
                continue
            
            shipmentOrders.append(request.order_name)
            if len(shipmentOrders) == 3:
                yield order_management_pb2.ShipmentResponse(id = str(self.processedShipmentId), orders = shipmentOrders)
                shipmentOrders = []
                self.processedShipmentId += 1
        
        if shipmentOrders:
            yield order_management_pb2.ShipmentResponse(id = str(self.processedShipmentId), orders = shipmentOrders)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()

serve()