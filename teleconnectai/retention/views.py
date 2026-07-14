from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from langchain_core.messages import HumanMessage
from retention.forms import ChatForm
from retention.agent.graph import graph_app
from retention.services.customer_repository import CUSTOMERS
import json


def chat_page(request):
    ai_recipe = request.session.get('ai_recipe', '')
    form = ChatForm()
    return render(request, "retention/home.html", {'form': form, 'ai_recipe': ai_recipe})


def chat_api(request):

    if request.method != "POST":
        redirect('/')

    # message = request.POST.get("message")
    form = ChatForm(request.POST)
    if form.is_valid():
        message = form.cleaned_data['chat_message']
        result = graph_app.invoke(
            {
                "messages": [
                    HumanMessage(content=message)
                ]
            }
        )
        response = result["messages"][-1].content

        # return JsonResponse({"response": response})
        request.session['ai_recipe'] = {"user_message": message, "ai_res": response}
            
    form = ChatForm()
    return redirect('/')







def get_customer_repo(request):
    response = json.dumps(CUSTOMERS, indent=4)
    html_content = f"""
    <html>
        <head>
            <title>Customer Repository JSON Viewer</title>
            <style>
                body {{
                    padding: 20px; 
                    font-family: monospace; 
                }}
                pre {{
                    white-space: pre-wrap;       /* Tells browser to wrap text */
                    white-space: -moz-pre-wrap;  /* Fix for older Firefox versions */
                    white-space: -webkit-pre-wrap; /* Fix for Safari and Chrome */
                    word-wrap: break-word;       /* Breaks long words or values if needed */
                }}
            </style>
        </head>
        <body>
            <pre>{response}</pre>
        </body>
    </html>
    """
    # return JsonResponse({"response": response})
    return HttpResponse(html_content)