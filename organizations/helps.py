def get_filter_keys(filter_name):
    if filter_name == "on-progress":
        return {'x2tBdd': 413}
    elif filter_name == "finished":
        return {'x2tBdd': 414}
    elif filter_name == "over-deadline":
        return {'x2tBdd': 415}


def get_page_color(filter_name):
    if filter_name == "on-progress":
        return "warning"
    elif filter_name == "finished":
        return "success"
    elif filter_name == "over-deadline":
        return "danger"
    return 'primary'
