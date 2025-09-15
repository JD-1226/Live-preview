from django.shortcuts import render
from django.http import JsonResponse
from .models import Snippet

# Create your views here.
def index(request):
    snippets = Snippet.objects.all().order_by("-created_at")
    return render(request, "preview/index.html", {"snippets": snippets})

def live_update(request):
    html_code = request.POST.get("html_code", "")
    return JsonResponse({"html": html_code})

def save_snippet(request):
    title = request.POST.get("title")
    code = request.POST.get("code")

    if not title or not code:
        return JsonResponse({"status": "error", "message": "Title and code required"})

    snippet, created = Snippet.objects.update_or_create(
        title=title,
        defaults={"content": code}
    )
    return JsonResponse({"status": "success", "message": "Saved!"})

def load_snippet(request):
    snippet_id = request.GET.get("id")
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        return JsonResponse({"status": "success", "content": snippet.content})
    except Snippet.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Snippet not found"})

