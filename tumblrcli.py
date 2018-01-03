#!/usr/bin/env python

import sys, tempfile, os
from subprocess import call
from tumblpy import Tumblpy

t = Tumblpy(YOUR_CONSUMER_KEY, YOUR_CONSUMER_SECRET,
            OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def read_tumblr_api_parameter( file_dir, param_name ):
    try:
        f = open(file_dir+param_name, 'r')
    except FileNotFoundError:
        return None
    return f.read()

def append_tumblr_api_parameter(file_dir, param_name, dict_to_append):
    value = read_tumblr_api_parameter( file_dir, param_name)
    if value != None:
        dict_to_append[param_name] = value
    
def get_tumblr_blog_url( file_dir = "" ):
    url = read_tumblr_api_parameter( file_dir, 'blog_url')
    if url != None:
        return url
    else:
        blog_url = t.post('user/info')
        return blog_url['user']['blogs'][0]['url']

def get_all_tumblr_api_params( file_dir ):
    #Defining params
    primary_params = ( 'type', 'state', 'tags', 'tweet', 'date', 'format', 'slug', 'type', 'native_inline_images')
    post_type = read_tumblr_api_parameter( file_dir, 'type')
    secondary_params = ('text','body')
    if post_type == 'photo':
        secondary_params = ('caption', 'link', 'source', 'data', 'data64')
    elif post_type == 'quote':
        secondary_params = ('quote', 'source')
    elif post_type == 'link':
        secondary_params = ('title', 'url', 'description', 'thumbnail', 'excerpt', 'author')
    elif post_type == 'chat':
        secondary_params = ('title', 'conversation')
    elif post_type == 'audio':
        secondary_params = ('caption', 'external_url', 'data')
    elif post_type == 'video':
        secondary_params = ('caption', 'embed', 'data')
    #Creating a dict with all params and checking for each param
    all_params = {}
    for i,param in enumerate( primary_params ):
        append_tumblr_api_parameter(file_dir, param, all_params)
    for i,param in enumerate( secondary_params ):
        append_tumblr_api_parameter(file_dir, param, all_params)
    return all_params

def post_from_dir(file_dir):
    post = t.post('post',
                  get_tumblr_blog_url(file_dir),
                  params=get_all_tumblr_api_params(file_dir))
    print("Success.")

def post_from_string( string_to_post):
    post = t.post('post',
                  get_tumblr_blog_url(),
                  params={'body' : string_to_post})
    print("Success.")

def post_from_temp_file():
    editor_envvar = os.environ.get('EDITOR','vim')
    with tempfile.NamedTemporaryFile(suffix=".tmp", delete=False) as temp_file:
        temp_file.write(b'')
        temp_file.flush()
        temp_file.close()
        call([editor_envvar, temp_file.name])
        with open(temp_file.name, temp_file.mode) as temp_file_read:
            post_from_string(temp_file_read.read())

def print_usage():
    print("Usage: tumblr <argument or file path> <post string>\nArguments:\n -h: Prints this help message\n -m \"Text post message NOT wrapped in quotes\"\n\nIf no arguments are present, this application will open the default $EDITOR and begin work on a title-less text post.")

if len(sys.argv) == 1:
    post_from_temp_file()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        print_usage()
    else:
        path = os.path.join( sys.argv[1], '') #Add a slash if not there
        post_from_dir( path)
else:
    if sys.argv[1] == "-m":
        string_to_post = ""
        for argument_index in range(2,len(sys.argv)):
            string_to_post = string_to_post +" " + sys.argv[argument_index]
        
        post_from_string( string_to_post)
    else:
        print_usage()
