# demo-grpc

Petite démo gRPC.

La première fois, exécuter

```
python3 -m venv venv
. venv/bin/activate
pip install grpcio
```

Pour regénérer le code python correspondant aux définitions protobuf:

```
python3 -m grpc_tools.protoc -Iprotos --python_out=. --grpc_python_out=. protos/books.proto
```

Ensuite, on peut démarrer le serveur avec la commande

```
python3 books_server.py
```

Pour intéragir avec le serveur on peut soit exécuter le script client avec

```
python3 books_client.py
```

ou le démarrer en mode intéractif avec

```
python3 -i books_client.py
```

Une fois dans la console, on peut utiliser les méthodes _get_books()_ et _add_book('titre', 'auteur')_.
