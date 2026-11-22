from django.shortcuts import render, redirect

from . import util

import markdown2




def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title,
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": markdown2.markdown(content),
        })

def search(request):
    results = []
    query = request.GET.get("q", "").strip()
    for entry in util.list_entries():
        if query.lower() == entry.lower():
            return redirect("title", title=entry)
        elif query.lower() in entry.lower() and len(query) != 0:
            results.append(entry)
    return render(request, "encyclopedia/search.html", {
        "results": results,
        "query": query,
    })
            
def newpage(request):
    if request.method == "POST":
        entryname, entrytext = request.POST.get("entryname"), request.POST.get("entrytext")
        util.save_entry(entryname, entrytext)
    return render(request, "encyclopedia/newpage.html")

