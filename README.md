tumblelog
=============================

This is a project for learning MongoDB and Python.

Following the tutorial:
http://docs.mongodb.org/ecosystem/tutorial/write-a-tumblelog-application-with-flask-mongoengine/




WTForm
1. in the blueprint, create the Form class from the model automatically, like the following:
```
PostForm = model_form(Post, exclude=['comments', 'created_at', 'slug'])
```
The PostForm is a class.

2. create an instance of the Form class and sent it to the template
```
form = self.PostForm(request.form)
...
context = {
  "form": form,
  ...
}
return render_template('posts/list.html', **context)
```
3. in the template, render the form instance
```
  <form action="." method="post">
    {{ forms.render(form) }}
    <div class="actions">
        <input type="submit" class="btn primary" value="Post"/>
    </div>
  </form>
```

4. when submitted, in the blueprint, save the submitted new post
```
  form = self.PostForm(request.form)
  post = Post()
  form.populate_obj(post)
  post.save()
```




