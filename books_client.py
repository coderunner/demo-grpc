import grpc
import books_pb2
import books_pb2_grpc

def get_books():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = books_pb2_grpc.BooksServiceStub(channel)
        response = stub.GetBooks(books_pb2.BooksRequest())
    
    for i in response.books: 
        print("{0} {1} {2}".format(i.id, i.title, i.author))

def add_book(title, author):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = books_pb2_grpc.BooksServiceStub(channel)
        response = stub.AddBook(books_pb2.AddBookRequest(book = books_pb2.Book(id = '', title = title, author = author)))
        print("{0} {1} {2}".format(response.book.id, response.book.title, response.book.author))


if __name__ == '__main__':
    get_books()
    add_book('t', 'i')