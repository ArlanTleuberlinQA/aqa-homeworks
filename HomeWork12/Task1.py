import os


class TxtToHtmlAdapter:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def convert_to_html(self):
        html_output = ''
        for filename in os.listdir(self.file_path):
            if filename.endswith(".txt"):
                absolute_file_path = os.path.join(self.file_path, filename)
                with open(absolute_file_path, 'r') as txt_file:
                    lines = txt_file.readlines()

                headers = lines[0].strip().split(',')
                for line in lines[1:]:
                    values = line.strip().split(',')
                    for header, value in zip(headers, values):
                        html_output += f"<{header}>{value}</{header}>\n"
        return html_output


if __name__ == "__main__":
    html_result = TxtToHtmlAdapter('./.').convert_to_html()
    print(html_result)
