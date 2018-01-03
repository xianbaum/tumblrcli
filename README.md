# tumblr-cli

tumblr-cli is a simple client which makes a post to Tumblr.com given a directory. It is for my personal use but you may use it if you like. It is not meant to be a full-fledged client, but a simple one.

## Dependencies

tumblr-cli requires the following:

1. Python 3.x must be installed for tumblr-cli to run.
2. Tumblpy must be installed in some form. If pip is installed, it can be installed with the following command:

```sh
pip install python-tumblpy
```

## Setup

You will need to register for your own application:

1. Login to Tumblr.com
2. https://www.tumblr.com/oauth/apps. This is easy to do. Name it whatever you want, and put whatever description you want. On the "application website" and "Callback URL", you can put whatever you want.
3. Once it is created, click the "Explore API" link under your application, click "Allow", and then finally click on "Show keys" on the upper right hand corner. Do not show these keys to anyone.
4. Clone this repository.
4. Open the Python file and replace YOUR_CONSUMER_KEY with the Consumer Key with quotes surrounding it, YOUR_CONSUMER_SECRET with the Consumer Secret with quotes surrounding it, OAUTH_TOKEN with the Token with quotes, and OAUTH_TOKEN_SECRET with the Token Secret with quotes. Again, do not show these keys to anyone.

You can test this by entering this command in the cloned directory: Note that it WILL post "test" to your account publicy (I don't know why it won't post privately). It can be deleted any time.
```sh
python tumblr-cli.py test/
```
To install the post into your system, from the directory, simply write "cp tumblr-cli.py /usr/local/bin" and you may call this from anywhere

## Usage

### Text-post editor

To create a titleless text-post in an editor, simply run the command without any parameters. The EDITOR environment variable must be set.

### Other posts

Each API parameter is represented as a file in a directory. The name of the file should be the name of the API parameter. For example, for a text post containing just a title, create a file in a blank directory named "title" and write the title you want in it in utf-8 plain-text.

To post a photo with a caption, have a directory named whatever you want with the following contents:
1. a file named "data" with the image. The file extention must not be present. For example, if it says "data.jpg", remove the ".jpg".
2. a file named "caption" with the caption information in utf-8 plain-text.

There are a lot of possible parameters. See https://www.tumblr.com/docs/en/api/v2#posting for the complete list of parameters and tips for making posts of different types.

If you want to post to a blog different than your primary blog, then your blog URL must be inside of the folder in utf-8 in a file named "blog_url".

### Short-hand

To make a text post directly from command line without opening any editors or anything, use the "-m" argument, followed by the text post. Currently, whitespace is ignored.


## Todo:
- Add support for uploading photo sets. I do not know how to do this
- Add support for post editing and maybe post index listing
- Find out why it always published publicly
- Put on pip
