
from concurrent import futures
import logging

import grpc
import books_pb2
import books_pb2_grpc

import uuid

BOOKS = [
    books_pb2.Book(id = str(uuid.uuid4()), title = 'Un livre', author = 'U. Auteur'),
    books_pb2.Book(id = str(uuid.uuid4()), title = 'Un autre livre', author = 'U. A. Auteur')
    ]

class BooksService(books_pb2_grpc.BooksService):

    def GetBooks(self, request, context):
        return books_pb2.BooksResponse(books = BOOKS)

    def AddBook(self, request, context):
        id = str(uuid.uuid4())
        title = request.book.title
        author = request.book.author
        new_book = books_pb2.Book(id = id, title = title, author = author)
        BOOKS.append(new_book)
        return books_pb2.AddBookResponse(book = new_book)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    books_pb2_grpc.add_BooksServiceServicer_to_server(BooksService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()