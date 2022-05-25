"""Data formatter."""
import keyword
import re

import m2r2

KEYWORDS = set(keyword.kwlist)
KEYWORDS.add("property")

PATTERN_DOUBLE_UNDERSCORE = re.compile(r"__+")
PATTERN_LEADING_ALPHA = re.compile(r"(.)([A-Z][a-z]+)")
PATTERN_FOLLOWING_ALPHA = re.compile(r"([a-z0-9])([A-Z])")
PATTERN_WHITESPACE = re.compile(r"\W")


def snake_case(value):
    s1 = PATTERN_LEADING_ALPHA.sub(r"\1_\2", value)
    s1 = PATTERN_FOLLOWING_ALPHA.sub(r"\1_\2", s1).lower()
    s1 = PATTERN_WHITESPACE.sub("_", s1)
    s1 = s1.rstrip("_")
    return PATTERN_DOUBLE_UNDERSCORE.sub("_", s1)


def camel_case(value):
    return "".join(x.title() for x in snake_case(value).split("_"))


def escape_reserved_keyword(word):
    """
    Escape reserved language keywords like openapi generator does it
    :param word: Word to escape
    :return: The escaped word if it was a reserved keyword, the word unchanged otherwise
    """
    if word in KEYWORDS:
        return f"_{word}"
    return word


def attribute_name(attribute):
    return escape_reserved_keyword(snake_case(attribute))


def format_value(value, quotes='"'):
    if isinstance(value, str):
        return f"{quotes}{value}{quotes}"
    elif isinstance(value, bool):
        return "true" if value else "false"
    return value


def get_name(schema):
    if hasattr(schema, "__reference__"):
        return schema.__reference__["$ref"].split("/")[-1]


def attribute_path(attribute):
    return ".".join(attribute_name(a) for a in attribute.split("."))


class CustomRenderer(m2r2.RestRenderer):
    def double_emphasis(self, text):
        if "``" in text:
            text = text.replace("\ ``", "").replace("``\ ", "")
        if "`_" in text:
            return text
        return super().double_emphasis(text)

    def header(self, text, level, raw=None):
        return "\n{}\n".format(self.double_emphasis(text))


def docstring(text):
    return m2r2.convert(text.replace("\\n", "\\\\n"), renderer=CustomRenderer())[1:-1]
