import os

class Parser:

    def read(self, folder):

        texts = []

        for root, dirs, files in os.walk(folder):

            for file in files:

                if file.endswith((
                    ".py",
                    ".cpp",
                    ".c",
                    ".h",
                    ".js",
                    ".java"
                )):

                    path = os.path.join(root, file)

                    with open(
                        path,
                        "r",
                        encoding="utf8",
                        errors="ignore"
                    ) as f:

                        texts.append(
                            f.read()
                        )

        return texts
