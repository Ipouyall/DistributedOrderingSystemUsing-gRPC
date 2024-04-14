all: order_management

ifeq ($(OS),Windows_NT)
    RM = del /q
else
    RM = rm -f
endif

deps:
	@echo "Installing needed dependencies to compile project"
	pip install grpcio-tools -q
	pip install protobuf -q
	@echo "Please install 'protoc' from https://github.com/protocolbuffers/protobuf/releases"

order_management:
	@echo "Building Order Management artifacts..."
	python -m grpc_tools.protoc -I=./proto --python_out=./ --grpc_python_out=./ order_management.proto

clean:
	@echo "Cleaning up..."
	$(RM) *_pb2.py *_pb2_grpc.py