# Learning MongoDB

## Install With Brew

```bash
brew install mongosh
```

## Commands In The Shell

What db we are using:
```shell
db
```
Show all db:
```shell
show dbs
```
Switch or create a new db:
```shell
use <db-name>
```
Create a new collection:
```shell
db.createCollection("posts")
```
Create ot insert the docs we can use insert-one or insert-many methods:
```shell
db.posts.insertOne({
  title: 'Post 1', 
  body: 'Body post', 
  category: 'News', 
  likes: 1, 
  tags: ['news', 'events'], 
  date: Date()
})
```

```shell
db.posts.insertMany([
  {title: 'Post 2', body: 'Body post', category: 'News', likes: 1, tags: ['news', 'events'], date: Date()}, 
  {title: 'Post 3', body: 'Body post', category: 'News', likes: 1, tags: ['news', 'events'], date: Date()}, 
  {title: 'Post 4', body: 'Body post', category: 'News', likes: 1, tags: ['news', 'events'], date: Date()}
])
```
How to look what is inside:
```shell
db.posts.find()
```
According to some parameter:
```shell
db.posts.find({category: "News"})
```
We can sort (1 -ascending order, -1 - descending order):
```shell
db.posts.find().sort({title:-1})
```

```shell

```

```shell

```

```shell

```

```shell

```

```shell

```

## Credits

- [youtube | MongoDB Crash Course 2022](https://www.youtube.com/watch?v=2QQGWYe7IDU&ab_channel=TraversyMedia)