import yaml


def get_data_from_md(text):
    _,infos,content = text.split("---",2)
    data = yaml.safe_load(infos)
    return data, content