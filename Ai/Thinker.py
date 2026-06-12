class Thinker:

    def analyze(self, text):

        words = text.split()

        result = {

            "length": len(words),

            "keywords": words[:20]

        }

        return result
