from .models import Category


def show_categories(request):
    categories = {}
    for category in Category.objects.all():
        categories[category] = []
        subcategories = category.subcategory_set.all()
        idx = category.subcategory_set.count() // 3 + 1
        for i in range(idx):
            categories[category].append(subcategories[i * 3: (i + 1) * 3])

    return {
        "categories": categories,
    }
