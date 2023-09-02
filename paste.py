import sys


def preprocess_data(f1, f2):
    """read and return data from files as lists and make them 
    equally long by adding empty string entries
    """
    rows_f1 = f1.read().splitlines()
    rows_f2 = f2.read().splitlines()
    delta_column_length = len(rows_f1) - len(rows_f2)

    if delta_column_length > 0:
        rows_f2 += delta_column_length * [""]
    elif delta_column_length < 0:
        rows_f1 += abs(delta_column_length) * [""]
    return rows_f1, rows_f2


def paste(rows_f1, rows_f2):
    """horizontal output of two files side by side"""
    max_row_len_f1 = len(max(rows_f1, key=len))
    for left, right in zip(rows_f1, rows_f2):
        print(f"{left:{max_row_len_f1}} {right}")


def paste_d(seperator, rows_f1, rows_f2):
    """usage of specific seperator in-between, e.g. ':'"""
    for left, right in zip(rows_f1, rows_f2):
        print(f"{left}{seperator}{right}")


def paste_s(rows_f1, rows_f2):
    """vertical output of two files below each other"""
    output_f1 = ""
    output_f2 = ""
    for row1, row2 in zip(rows_f1, rows_f2):
        output_f1 += row1 + " "
        output_f2 += f"{row2:{len(row1)}} "
        if max(len(output_f1), len(output_f2)) > 70:
            print(output_f1 + "\n" + output_f2 + "\n")
            output_f1 = output_f2 = ""
    print(output_f1 + "\n" + output_f2)


def main(*args):
    usage_text = f"""

        Usage: python3 paste.py [-d "<seperator>" | -s] filename1 filename2
        for linewise horizontal output of two text files to the console.
        
        positional parameters:
        filename1       : textfile
        filename2       : textfile
        
        optional parameters:
        -d "<separator>": {paste_d.__doc__ }
        -s              : {paste_s.__doc__}
    """
    if (len(args) < 2 
        or (len(args) == 2 and "-" in args) 
        or any("-" in arg for arg in args[-2:])):
        raise SystemExit(
            "\nError, wrong number of command line parameters.\n"
            + usage_text
        )

    paste_opts = {"-d": paste_d, "-s": paste_s, "w/o": paste}
    try:
        with open(args[-2], "r") as file_1, \
             open(args[-1], "r") as file_2:
            data_1, data_2 = preprocess_data(file_1, file_2)
            params = [arg for arg in args[1:-2]] + [data_1, data_2]
            action = (
                paste_opts.get(args[0], None)
                if ("-" in args[0])
                else paste_opts.get("w/o")
            )
            if action:
                action(*params)
            else:
                print(
                    "Error, given command line parameters are not available: ",
                    args[0],
                    usage_text
                )
                return
    except FileNotFoundError as e:
        print("Error while opening the files: ", e)
        return
    except TypeError as e:
        print("Error, wrong number of command line parameters.", usage_text)
        return
    except Exception as e:
        print("Unexpected error: ", e)
        return


if __name__ == "__main__":
    main(*sys.argv[1:])
