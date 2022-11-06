import urllib.parse

def load_css() -> str:
    """ Return all css styles. """
    common_tag_css = """
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: .15rem .40rem;
                position: relative;
                text-decoration: none;
                font-size: 95%;
                border-radius: 5px;
                margin-right: .5rem;
                margin-top: .4rem;
                margin-bottom: .5rem;
                background-color: rgb(240, 242, 246);
    """
    return f"""
        <style>
            #tags {{
                {common_tag_css}
                color: rgb(88, 88, 88);
                border-width: 0px;
                background-color: rgb(240, 242, 246);
            }}
            #tags:hover {{
                color: blue;
                box-shadow: 0px 5px 10px 0px rgb(255, 165, 0);
            }}
            #active-tag {{
                {common_tag_css}
                color: rgb(246, 51, 102);
                border-width: 1px;
                border-style: solid;
                border-color: rgb(246, 51, 102);
            }}
            #active-tag:hover {{
                color: blue;
                border-color: blue;
                background-color: rgb(188, 203, 232);
                box-shadow: 0px 5px 10px 0px rgb(255, 165, 0);
            }}
        </style>
    """

def number_of_results(total_hits: int, duration: float) -> str:
    """ HTML scripts to display number of results and duration. """
    return f"""
        <div style="color:pink;font-size:95%;">
            {total_hits} results ({duration:.2f} seconds)
        </div><br>
    """

def search_result(i: int, url: str, title: str, id: str, score: str, **kwargs) -> str:
    """ HTML scripts to display search results. """
    return f"""
        <div style="color:blue;font-size:120%;">
            {i + 1}.
            <a href="{url}">
                {title}
            </a>
        </div>
        <div style="font-size:95%;">
            <div style="color:pink;font-size:95%;">
                {url[:40] + '...' if len(url) > 50 else url}
            </div>
            <div>
            <a href="?recursive={id}&search-term={kwargs["search_term"]}">
            <img alt="{id}" src="{url}" width="224" height="224">
            </a>
            </div>
            
        </div>
    """

def tag_boxes(tags: list) -> str:
    """ HTML scripts to render tag boxes. """
    html = ''
    for tag in tags.split(","):
        html += f"""
            <a id="tags">
                {tag.replace('-', ' ')}
            </a>
            """
    html += '<br><br>'
    return html

def no_result_html() -> str:
    """ """
    return """
        <div style="color:pink;font-size:95%;margin-top:0.5em;">
            No results were found.
        </div><br>
    """
    
def one_type_html() -> str:
    """ """
    return """
        <div style="color:pink;font-size:95%;margin-top:0.5em;">
            Please select either an image or image link.
        </div><br>
    """

def pagination(total_pages: int, search: str, current_page: int, recursive=None,ty=None, files=None) -> str:
    """ Create and return html for pagination. """
    # search words and tags
    print("hna",files)
    params = f'?search-term={search}&ty={ty}'
    if recursive:
        params = f'{params}&recursive={recursive}'

    # avoid invalid page number (<=0)
    if (current_page - 5) > 0:
        start_from = current_page - 5
    else:
        start_from = 1

    hrefs = []
    if current_page != 1:
        hrefs.append(f'<a href="{params}&page={1}">&lt&ltFirst</a>')
        hrefs.append(f'<a href="{params}&page={current_page - 1}">&ltPrevious</a>')

    for i in range(start_from, min(total_pages + 1, start_from + 10)):
        if i == current_page:
            hrefs.append(f'{current_page}')
        else:
            hrefs.append(f'<a href="{params}&page={i}">{i}</a>')

    if current_page != total_pages:
        hrefs.append(f'<a href="{params}&page={current_page + 1}">Next&gt</a>')

    return '<div>' + '&emsp;'.join(hrefs) + '</div>'