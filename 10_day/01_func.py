def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    for_f_name = (f_name.title())
    for_l_name = (l_name.title())
    return f"{for_f_name} {for_l_name}"


new_string= format_name("rouank", "mishra")
print(new_string)

