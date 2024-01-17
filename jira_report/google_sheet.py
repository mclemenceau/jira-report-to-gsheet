from typing import List
import gspread


class GoogleSheet:
    def __init__(self, google_sheet):
        gc = gspread.oauth()
        self.google_sheet = gc.open(google_sheet)

    def set_headers(self, headers_name: List[str]):
        self.headers = headers_name

    def update(self, sheet_name: str, data: List[List[str]]):
        if len(data) < 1:
            return

        sheet = self.google_sheet.worksheet(sheet_name)
        last_column = GoogleSheet.column_letter(len(self.headers))
        sheet.clear()

        # We use the first line of the data set as header
        sheet.update(f"A1:{last_column}1", [self.headers])

        sheet.update(
            f"A2:{last_column}{len(data)+1}",
            data)

    @staticmethod
    def column_letter(col_index: int) -> str:
        if col_index < 1:
            raise ValueError("Index is too small for a valid column")

        result = ""
        while col_index > 0:
            col_index, remainder = divmod(col_index - 1, 26)
            result = chr(65 + remainder) + result

        return result.upper()
