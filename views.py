from flask import render_template, request, redirect
import os
import json
from datetime import date
import warnings
from utils import find_sugg, fetch_sugg

warnings.filterwarnings("ignore")

# put your views here.


def index():
    if request.method == "POST":
        return render_template("upload.html")

    return render_template("index.html")


def complete(host):
    if host.lower() == "google":
        query = request.args.get("q")
        count = request.args.get("count")

        if query == None:
            return "No query found"
        else:
            if count != None:
                if count != "all":
                    try:
                        count = int(count)
                    except:
                        return (
                            "error : count : {} is not all or a integer value".format(
                                count
                            )
                        )
            else:
                count = "all"

            data = fetch_sugg(query, count)
            return json.dumps(data)
    else:
        return "no valid host found."
