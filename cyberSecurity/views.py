from django.shortcuts import render, redirect
from django.contrib import messages
from blog.models import Post
import csv
from django.contrib.auth.decorators import login_required


@login_required
def report_offence(request, **kwargs):
    if request.method == "POST":

        post = Post.objects.filter(id=kwargs["pk"]).first()
        reported_by = request.user.username
        csv_file = open("offence_report.csv", "a")
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(
            [post.title, post.content, post.author, post.date_posted, reported_by]
        )

        messages.success(request, f'You have REPORTED blog post "{post.title}"')
        return redirect("blog-home")
    else:
        post = Post.objects.get(id=kwargs["pk"])
        context = {"post": post}
        return render(request, "cyberSecurity/report_offence.html", context)
