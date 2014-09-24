from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from tumblelog.models import Post, Comment

from flask.ext.mongoengine.wtf import model_form

posts = Blueprint('posts', __name__, template_folder='templates')


class ListView(MethodView):

    #PostForm is a class. It's the form generated from the model, Post
    PostForm = model_form(Post, exclude=['comments', 'created_at', 'slug'])
    
    def get(self):
        form = self.PostForm(request.form)
        posts = Post.objects.all()
        context = {
            #"post": Post(),
            "form": form,
            "posts": posts  
        }


        return render_template('posts/list.html', **context)#posts=posts)

    
    def post(self):

        form = self.PostForm(request.form)

        context = {
            #"post": Post(),
            "form": form,
            #"posts": Post.objects.all() 
        }

        if form.validate():
            post = Post()
            form.populate_obj(post)
            post.slug = post.title.replace(" ", "")
            post.save()

            return redirect(url_for('posts.list'))

        return render_template('posts/list.html', **context)



class DetailView(MethodView):

    form = model_form(Comment, exclude=['created_at'])
    
    
    def get_context(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context

    def get(self, slug):
        post = Post.objects.get_or_404(slug=slug)
        return render_template('posts/detail.html', post=post)


    
    def post(self, slug):
        context = self.get_context(slug)
        form = context.get('form')

        if form.validate():
            comment = Comment()
            form.populate_obj(comment)

            post = context.get('post')
            post.comments.append(comment)
            post.save()

            print 1
            return redirect(url_for('posts.detail', slug=slug))

        print 2
        return render_template('posts/detail.html', **context)


# Register the urls
posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/<slug>/', view_func=DetailView.as_view('detail'))
