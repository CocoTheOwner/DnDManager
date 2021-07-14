import json, os, time
class Storage:

    def save(object: object, file: str):

        # Serializing json 
        json_object = json.dumps(object, indent = 4)

        # Writing to sample.json
        with open(file, "w") as outfile:
            outfile.write(json_object)

    def load(file: str, useIfEmpty: dict):

        if not os.path.exists(file):
            print("File: " + file + " does not exist. Creating empty file.")
            os.makedirs("/".join(file.split("/")[:-1]))
            time.sleep(0.1)
            Storage.save(useIfEmpty, file)

        # Writing to sample.json
        with open(file, "r") as outfile:
            return json.loads(outfile.read())