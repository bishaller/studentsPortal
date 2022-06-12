from .models import Student, Category


def menu_categories(request):
    cats = Category.objects.all()


    all_posts = Student.objects.all()
    ordered_posts = all_posts.order_by("-views")
    popular_posts = ordered_posts[:5]

    ctx = {
        "category_menu": cats,
        "popular_posts": popular_posts,
    }

    return ctx
