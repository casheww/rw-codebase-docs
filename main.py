from docs_generator import ceciljsonparser as cecil_speak
import os
import ujson

"""
For converting the JSON output from thalber's butcher to markdown docs.
"""


ASSEMBLY_PATH = "./assemblies/Assembly-CSharp/"


def json_hunt():
    for root, dirs, files in os.walk(ASSEMBLY_PATH):
        for htmlfile in files:
            if not htmlfile.endswith(".json"):
                continue

            with open(root + htmlfile) as file:
                j = ujson.load(file)
            cecil_md = cecil_speak.json2md(j)

            # placeholder saving for dev:
            with open("test.md", "w+") as file:
                file.write(cecil_md)


if __name__ == "__main__":

    _input = ""

    while _input != "0":
        _input = input("\nmenu\n\t1 : generate html from cecil's json & user's md\n\t0 : exit\n > ")

        if _input == "1":
            json_hunt()
            _input = "0"
