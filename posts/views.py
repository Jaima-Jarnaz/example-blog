from django.shortcuts import render
import requests


# POSTS VIEW ENDPOINT
def posts(request):
    response=requests.get('https://jsonplaceholder.typicode.com/posts').json()
    return render(request, 'blog-listing.html',{'response':response})


# POST DETAILS VIEW ENDPOINT
def post_details(request,post_id):
    comment_response=requests.get('https://jsonplaceholder.typicode.com/posts/1/comments').json()
    singlepost=requests.get('https://jsonplaceholder.typicode.com/posts/1').json()
    details={
        'comment_response':comment_response,
        'singlepost':singlepost

    }
    return render(request, 'blog-post.html',details)