import sys

from flask import render_template, url_for, redirect, flash, request, \
    jsonify

from app import app
from app.forms import PostForm
from app.utils import get_webpreview


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        flash('Your post is now live!')
        return redirect(url_for('show_post'), code=307)
    return render_template('index.html', title='Create a post',
                           form=form)


@app.route('/show_post', methods=['GET', 'POST'])
def show_post():
    if request.method == 'GET':
        return redirect(url_for('index'))

    text = request.form.get('post')
    embed_tag = request.form.get('embed_tag')
    url = request.form.get('preview_url')
    post_title = request.form.get('preview_title')
    post_description = request.form.get('preview_description')
    post_image = request.form.get('preview_image')

    return render_template('post.html',
                           title='Great post!', post_title=post_title,
                           post_description=post_description, url=url,
                           post_image=post_image, text=text,
                           embed_tag=embed_tag)


@app.route('/preview_url')
def preview_url():
    url = request.args.get('url')
    og = None
    try:
        og = get_webpreview(url)
    except Exception as e:
        print(f'PREVIEW ERROR {e}', file=sys.stderr)
    else:
        if og and og.image:
            html_embed = render_template('embed_preview.html', url=url,
                                         post_title=og.title, post_image=og.image,
                                         post_description=og.description)
            return jsonify({'html_embed': html_embed,
                            'title': og.title , 'description': og.description,
                            'image': og.image, 'url': url})
