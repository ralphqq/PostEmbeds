from flask import render_template, url_for, redirect, flash, request, \
    jsonify
from webpreview import web_preview, OpenGraph

from app import app
from app.forms import PostForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if form.validate_on_submit():
        post_text = form.post.data
        embed_html = request.form['embed_tag']
        flash('Your status has been updated!')
        return redirect(url_for('aftermath', post_text=post_text,
                                embed_html=embed_html))
    return render_template('index.html', title='Create a post',
                           form=form)


@app.route('/aftermath')
def aftermath():
    post_text = request.args.get('post_text')
    embed_html = request.args.get('embed_html')
    return render_template('aftermath.html',
                           title='Great post!', text=post_text,
                           embed_html=embed_html)


@app.route('/preview_url')
def preview_url():
    url = request.args.get('url')
    og = OpenGraph(url, ['og:title', 'og:description', 
                         'og:site_name', 'og:image'])
    html_embed = render_template('embed_preview.html', og=og, url=url)
    return jsonify({'html_embed': html_embed})