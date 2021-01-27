import re
from typing import Dict, List


_DROPDOWN_MD = "<details>\n<summary><code>.name.</code>\n</summary>\n\n.content.\n</details>"


def _format_method_name(method: Dict) -> str:
    name = ("static" if method['IsStatic'] else "") + method['Name']    # static?
    name = re.sub(r"\w*[./]*\w* \w*::", "", name)                   # remove return type
    name = re.sub(r"\w*\.+(\w*\()", r"\1", name)
    name = re.sub(r"(\(.*\w*)/(\w*.*\))", r"\1.\2", name)           # swap / in param types for .
    name = name.replace(",", ", ")                                  # add spaces after commas
    return name


def _make_method_list(methods: List[Dict]) -> str:
    md = ""
    for method in methods:
        method_str = _DROPDOWN_MD.replace(".name.", _format_method_name(method))

        method_details = "**Parameters** :\n"
        method_details += "\n".join([f"  - **{p['Name']}** (`{p['ParameterType']}`)" for p in method['Parameters']])
        method_details += f"\n\n**Returns** : `{method['ReturnType']}`\n"

        md += method_str.replace(".content.", method_details)

    return md


def _format_attribute_name(prop: str) -> str:
    name = ("static" if prop['IsStatic'] else "") + prop['Name']
    name = re.sub(r"\w*[./]*\w* \w*::", "", name)
    name = name.replace("()", "")
    return name


def _make_properties_list(properties: List[Dict]) -> str:
    md = ""
    for prop in properties:
        prop_str = _DROPDOWN_MD.replace(".name.", _format_attribute_name(prop))

        if prop['HasGetter'] and prop['HasSetter']:
            prop_details = "`{ get; set; }`\n\n"
        else:
            prop_details = "`{ get; }`\n\n"

        prop_details += f"**Type** : {prop['PropertyType']}"

        md += prop_str.replace(".content.", prop_details)

    return md


def _make_fields_list(fields: List[Dict]) -> str:
    md = ""
    for field in fields:
        field_str = _DROPDOWN_MD.replace(".name.", _format_attribute_name(field))

        md += field_str.replace(".content.", f"**Type** : {field['FieldType']}")

    return md


def json2md(j: Dict, nested: bool = False) -> str:
    """
    Convert Cecil's output JSON to pretty markdown.
    """
    md = f"## {j['Name']}\n"

    if not nested:
        md = f"*Namespace : {j['Namespace'] if j['Namespace'] != '' else 'none'}*\n" + md

    if j['BaseClassName'] != "":
        md += f"**Base class** : {j['BaseClassName']}\n"
    if j['IsSealed']:
        md += "\n*sealed class*\n"

    md += "\n\n**Methods** :\n" + _make_method_list(j['Methods'])
    md += "\n\n**Properties** : \n" + _make_properties_list(j['Properties'])
    md += "\n\n**Fields** : \n" + _make_fields_list(j['Fields'])

    if len(j['NestedTypes']) > 0:
        md += "\n\n---\n\n### Nested types\n\n" + \
            "\n\n".join([json2md(nt, True) for nt in j['NestedTypes']])

    return md
