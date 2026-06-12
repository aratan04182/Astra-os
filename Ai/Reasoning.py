class Reasoning:

    def analyze(self, code):

        lines = code.split("\n")

        result = {

            "lines": len(lines),

            "imports": [],

            "functions": []

        }

        for line in lines:

            if line.startswith("import"):

                result["imports"].append(line)

            if line.startswith("def"):

                result["functions"].append(line)

        return result
