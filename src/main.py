from src.search import generate_search_file, perform_search, manual_search
import sys


def main():
    """
    queries whether we want to immediately perform a search, calling a file or using existing defaults
    or
    generate search
    """

    """ OUTLINE
    
    A - perform default search (default api token and default params)
        invokes perform_search()
            *** date/time to filepath
    or
    B - generate simple search
        invokes generate_search(adv=false)
    or
    C - generate advanced (option at end to save as default?)?
        invokes generate_search(adv=true)
    or
    D - perform search
        manual file entry for search file
            use default api token (.env)
            or
            enter new api token
    or
    E - list history
        select from history of search_queries
            use default api token (.env)
            or
            enter new api token

    """
    while True:
        title_line = "\n       JOBSCOUT\n"
        selection_message = """
        S - generate search file (simple options)\n
        A - generate search file (advanced options)\n
            D - Default search (default api token and default params)\n
            L - Perform search (from file list)\n
            M - Manual file search\n
                    X - Quit\n\n"""
        user_message = "Please enter selection:"
        user_input = input(title_line + selection_message + user_message)
        match user_input.upper().strip():
            case "S":
                generate_search_file()
            case "A":
                generate_search_file(advanced=True)
            case "D":
                perform_search()
            case "L":
                perform_search()
            case "M":
                manual_search()
            case "X":
                sys.exit()
            case _:
                print("\n\n\n Please Enter A Valid Selection (case insensitive)\n\n")


if __name__ == "__main__":
    main()
