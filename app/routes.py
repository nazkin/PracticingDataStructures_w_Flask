import random
from app import app, db
from flask import request, jsonify
from datetime import datetime
from app.models import User, BlogPost
from app.linked_list import LinkedList
from app.hash_table import HashTable
from app.binary_search_tree import BinarySearchTree

@app.route('/')
@app.route('/index')
def root_route():
    return "<h1> This is the root route </h1>"
#################### User routes ###########################
@app.route('/api/user', methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        name = data["name"],
        email = data["email"],
        address = data["address"],
        phone = data["phone"],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Success: User created !"})

@app.route('/api/user/descending_id', methods=["GET"])
def fetch_all_users_descending():
    users = User.query.all()
    users_list = LinkedList()

    for user in users:
        data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone,
        }
        # inserting in the beginning of the linked list to create a list
        # of ascending objects
        users_list.insert_beginning(data)
    return jsonify(users_list.to_array_list())

@app.route('/api/user/ascending_id', methods=["GET"])
def fetch_all_users_ascending():
    users = User.query.all()
    users_list = LinkedList()

    for user in users:
        data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone,
        }
        users_list.insert_end(data)
    return jsonify(users_list.to_array_list())

@app.route('/api/user/<user_id>', methods=["GET"])
def fetch_user(user_id):
    users = User.query.all()
    users_list = LinkedList()

    for user in users:
        data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "address": user.address,
            "phone": user.phone,
        }
        users_list.insert_beginning(data)
    return jsonify(users_list.get_user_by_id(user_id))

@app.route('/api/user/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({
        "message": "User deleted successfully"
    }), 200

#################### User routes ###########################

#################### BlogPost routes ###########################
@app.route('/api/blog_post/<user_id>', methods=["POST"])
def create_blog_post(user_id):
    blog_data = request.get_json()
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"message": f"user with id = {user_id} does not exist"}), 400

    ht = HashTable(10)
    ht.add_key_value_pair("title", blog_data["title"])
    ht.add_key_value_pair("body", blog_data["body"])
    ht.add_key_value_pair("date", datetime.now())
    ht.add_key_value_pair("user_id", user_id)

    new_blog = BlogPost(
        title = ht.retrieve_value("title"),
        body = ht.retrieve_value("body"),
        date = ht.retrieve_value("date"),
        user_id = ht.retrieve_value("user_id")
    )
    db.session.add(new_blog)
    db.session.commit()

    return jsonify({
        "message": "successfully added blog",
        "title": ht.retrieve_value("title")
    }), 200

@app.route('/api/blog_post/<user_id>', methods=["GET"])
def get_users_blog_posts(user_id):
    blog_posts = BlogPost.query.filter_by(user_id=user_id)
    return jsonify({
        "message": "Success, all blogs retrieved",
        "blogs": blog_posts
    })

@app.route('/api/blog_post/<blog_post_id>', methods=["GET"])
def get_blog_post(blog_post_id):
    all_posts = BlogPost.query.all()
    random.shuffle(all_posts)

    bst = BinarySearchTree()
    for post in all_posts:
        bst.insert_value({
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "user_id": post.user_id
        })
    post = bst.search_node(blog_post_id)
    if not post:
        return jsonify({
            "message": 'Post could not be found'
        })
    return jsonify({
        "message": "Post found successfully",
        "post": post
    })

@app.route('/api/blog_post/<blog_post_id>', methods=["DELETE"])
def delete_blog_post(blog_post_id):
    pass

#################### BlogPost routes ###########################