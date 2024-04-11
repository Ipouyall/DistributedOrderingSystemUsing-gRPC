all: server_streaming order_management

deps:
	@echo "Installing needed dependencies to compile project"
	pip install grpcio-tools
	pip install protobuf

order_management:
	@echo "Building Order Management artifacts..."
	python -m grpc_tools.protoc -I=./proto --python_out=./ --grpc_python_out=./ order_management.proto

server_streaming:
	@echo "Building Server Streaming artifacts..."
	python -m grpc_tools.protoc -I=./proto --python_out=. --grpc_python_out=. order_management_serverStreaming.proto
