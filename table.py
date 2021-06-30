
class Table:
    '''
    Class for printing a table.
    '''

    @staticmethod
    def get_table(headers, data, fixed_space=False, separator_between_lines='-',
        separator_around_lines='', separator_between_cols=' ',  separator_around_cols='', separator_for_data=False):
        '''
        Returns the table string.
        '''
        space = Table.get_max_space(headers, data, fixed_space)

        # list with the strings that represent the table
        string = []

        # appends headers and separators around it
        starting_line = Table.get_line_separator(space, separator_around_lines, separator_between_cols, separator_around_cols) 
        string.append(starting_line)
        if starting_line:
            string.append('\n')
        string.append(Table.get_line(headers, space, separator_between_cols, separator_around_cols))
        string.append('\n')
        string.append(Table.get_line_separator(space, separator_between_lines, separator_between_cols, separator_around_cols))
        string.append('\n')

        # appends data and separators around it
        num_lines = len(data)
        for i in range(num_lines):
            string.append(Table.get_line(data[i], space, separator_between_cols, separator_around_cols))
            string.append('\n')
            if i != num_lines - 1:
                if separator_for_data:
                    string.append(Table.get_line_separator(space, separator_between_lines, separator_between_cols, separator_around_cols))
                    string.append('\n')
            else:
                string.append(Table.get_line_separator(space, separator_around_lines, separator_between_cols, separator_around_cols) )

        return "".join(string)

    @staticmethod
    def get_max_space(headers, data, fixed_space):
        '''
        Returns the spaces between columns.
        '''
        space = [len(header) for header in headers]
    
        for col_index in range(len(headers)):
            max_space_data = max([len(val) for val in [line[col_index] for line in data]])
            cur_space = max(max_space_data, space[col_index])
            space[col_index] = cur_space

        if fixed_space:
            max_space = max(space)
            space = [max_space for val in space]
        return space 
    
    @staticmethod
    def get_line(data, space, separator_between_cols, separator_around_cols):
        '''
        returns a data/header line from the table.
        '''
        lst = [data[i] + ' ' * (space[i] - len(data[i])) for i in range(len(data))]
        return separator_around_cols + separator_between_cols.join(lst) + separator_around_cols

    @staticmethod
    def get_line_separator(space, separator, separator_between_cols, separator_around_cols):
        '''
        Returns a line separating different data/header lines from the table.
        '''
        if separator:
            lst = [separator * cur_space for cur_space in space]
            return separator_around_cols + separator_between_cols.join(lst) + separator_around_cols
        else:
            return ''



if __name__ == "__main__":
    # examples of how to use the class
    headers = ['header 1', 'header 2','header 3']
    data = [['data 1.1 ','data 2.1  ','data 3.1   '], ['data 1.1','data 2.2','data 3.2'], ['data 1.3','data 2.3','data 3.3']]

    print("Normal table:\n")
    print(Table.get_table(headers, data))
    print("fixed_space=True:\n")
    print(Table.get_table(headers, data, fixed_space=True))
    print("separator_between_lines='~':\n")
    print(Table.get_table(headers, data, separator_between_lines='~'))
    print("separator_between_cols='|':\n")
    print(Table.get_table(headers, data, separator_between_cols='|'))
    print("separator_around_lines='-':\n")
    print(Table.get_table(headers, data, separator_around_lines='-'))
    print("separator_around_cols='|':\n")
    print(Table.get_table(headers, data, separator_around_cols='|'))
    print("separator_for_data=True:\n")
    print(Table.get_table(headers, data, separator_for_data=True))