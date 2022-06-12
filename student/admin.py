from django.contrib import admin

from .models import Student, Category

admin.site.register(Category)

class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "views", "created_at"]
    search_fields = ["name", "content"]
    list_per_page = 30
    # date_hierarchy = "created_at"
    # list_editable = ["views"]
    list_filter = ["category"]
    save_on_top = True

    fieldsets = (
        (
            "Post",
            {
                "fields": (("title", "views"), "content"),
            },
        ),
        (
            "test",
            {
                "fields": ["category", "image", "created_at"],
            },
        ),
    )

    readonly_fields = ["views", "created_at"]


admin.site.register(Student, StudentAdmin)