import pandas as pd


class PandasMd(object):
    """
    Parameters
    ---------------
    file_path : str 
        absolute path of the markdown file

    start_line : int
        line number of the header of the table

    end_line : int
        line number of the end of the table
    """
    def __init__(self, file_path, start_line, end_line):
        self.file_path = file_path
        self.start_line = start_line
        self.end_line = end_line
        # self.df = pd.DataFrame()


    def extract_table(self):
        """
        Extract the table with the between the start_line and end_line.
        """
        with open(self.file_path) as f:
            s = f.readlines()
        

        row_idx = 0
        for i, l in enumerate(s):
            if i < self.start_line-1:
                continue
            elif i > self.end_line:
                break
            elif i == self.start_line-1:
                line = l.strip().strip('|')
                # print(line)
                columns = [x.strip() for x in line.split('|')]
                # print(columns)
                self.df = pd.DataFrame(columns=columns)
            elif i==self.start_line:
                continue # for the horizontal line row
            else:
                line = l.strip().strip('|')
                tokens = line.split('|')
                data = [x.strip() for x in tokens]
                # print(data)
                # print(row_idx)
                self.df.loc[row_idx] = data
                row_idx += 1
        
        return self.df



if __name__ == "__main__":
    import os
    FILE_DIR = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(FILE_DIR, "..", "test_data", "tables.md")
    pm = PandasMd(file_path, 1, 5)
    df = pm.extract_table()
    print(df)