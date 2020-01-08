from django.shortcuts import render, redirect
from django.contrib import messages
from blog.models import Post
import csv
from django.contrib.auth.decorators import login_required


@login_required
def report_offence(request, **kwargs):
    post = Post.objects.get(id=kwargs["pk"])
    if request.method == "POST" and request.user not in post.reported_by.all():

        post.reported_by.add(request.user)
        post.save()
        reported_by = request.user.username
        csv_file = open("offence_report.csv", "a")
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(
            [post.title, post.content, post.author, post.date_posted, reported_by]
        )

        messages.success(request, f'You have REPORTED blog post "{post.title}"')

        k = Post.objects.filter(author=post.author)
        p = 0

        for post in k:
            p = p + post.reported_by.count()

        if p > 5 and not post.author.is_staff:
            post.author.delete()

        return redirect("blog-home")
    else:
        post = Post.objects.get(id=kwargs["pk"])
        context = {"post": post}
        return render(request, "cyberSecurity/report_offence.html", context)
