from src.search import generate_search_file, perform_search




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