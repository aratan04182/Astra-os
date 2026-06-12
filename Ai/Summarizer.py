class Summarizer:

    def create(self, data):

        summary = ""

        summary += "Word Count: "

        summary += str(data["length"])

        summary += "\n"

        summary += "Keywords:\n"

        for word in data["keywords"]:

            summary += word + "\n"

        return summary
