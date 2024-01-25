from main.models.problem_model import ProblemSheetModel


def get_filter_keys(filter_name):
    if filter_name == "no-date-given":
        return {'x2tBdd': 412}
    elif filter_name == "on-progress":
        return {'x2tBdd': 413}
    elif filter_name == "finished":
        return {'x2tBdd': 414}
    elif filter_name == "over-deadline":
        return {'x2tBdd': 415}
    elif filter_name == "for-verify":
        return {'x2tBdd': 416}


def get_page_color(filter_name):
    if filter_name == "no-date-given":
        return "dark"
    elif filter_name == "on-progress":
        return "warning"
    elif filter_name == "finished":
        return "success"
    elif filter_name == "over-deadline":
        return "danger"
    elif filter_name == "for-verify":
        return "info"


def get_list_sectors(filter_name, code=None):
    filters = get_filter_keys(filter_name) or {}
    if code:
        filters['Ue07qV'] = code
    sections = {}

    for obj in ProblemSheetModel.objects.filter(**filters):
        all_ = list(obj.n4jAme.all())
        if all_:
            section_number = int(all_[0].cAdagL.A3EIK9)
            if section_number not in sections:
                sections[section_number] = []
            sections[section_number].append(obj)
        else:
            obj.delete()

    return sections
