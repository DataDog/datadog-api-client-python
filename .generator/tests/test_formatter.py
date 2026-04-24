import pytest
from collections import defaultdict
from generator.formatter import _is_valid_identifier, format_data_with_schema


class TestIsValidIdentifier:
    @pytest.mark.parametrize("key,expected", [
        ("valid_key", True),
        ("_valid_key", True),
        ("ValidKey123", True),
        ("key123", True),
        ("key.with.dots", False),
        ("123invalid", False),
        (".starts_with_dot", False),
        ("", False),
        ("key-with-dash", False),
        ("key with space", False),
        ("key@special", False),
    ])
    def test_is_valid_identifier(self, key, expected):
        assert _is_valid_identifier(key) == expected


class TestFormatDataWithSchemaDictWithSpecialChars:
    def test_ocsf_dotted_keys_actual_failing_case(self):
        data = {
            "ocsf.activity_name": "Other",
            "ocsf.activity_id": "99"
        }
        schema = {
            "additionalProperties": {
                "type": "string"
            }
        }

        result, imports = format_data_with_schema(
            data,
            schema,
            version="v1"
        )

        assert result.startswith("{")
        assert result.endswith("}")
        assert '"ocsf.activity_name": \'Other\'' in result
        assert '"ocsf.activity_id": \'99\'' in result
        assert "dict(" not in result

    def test_multiple_dotted_keys(self):
        data = {
            "ocsf.activity_name": "Other",
            "ocsf.activity_id": "99",
            "ocsf.category_name": "System Activity"
        }
        schema = {
            "additionalProperties": {
                "type": "string"
            }
        }

        result, imports = format_data_with_schema(
            data,
            schema,
            version="v1"
        )

        assert result.startswith("{")
        assert result.endswith("}")
        assert '"ocsf.activity_name": \'Other\'' in result
        assert '"ocsf.activity_id": \'99\'' in result
        assert '"ocsf.category_name": \'System Activity\'' in result
        assert "dict(" not in result

    def test_dict_with_valid_identifiers_uses_constructor(self):
        data = {
            "normal_key": "value1",
            "another_key": "value2"
        }
        schema = {
            "additionalProperties": {
                "type": "string"
            }
        }

        result, imports = format_data_with_schema(
            data,
            schema,
            version="v1"
        )

        assert result.startswith("dict(")
        assert result.endswith(")")
        assert "normal_key='value1'" in result
        assert "another_key='value2'" in result


class SchemaWithReference(dict):
    """Dict subclass that carries a __reference__ attribute, mimicking a JsonRef proxy."""
    def __init__(self, data, ref_name):
        super().__init__(data)
        self.__reference__ = {"$ref": f"#/components/schemas/{ref_name}"}


class TestFormatDataWithSchemaNamedNumberType:
    def test_named_number_type_returns_raw_float(self):
        schema = SchemaWithReference({"type": "number", "format": "double"}, "RumRetentionFilterSampleRate")
        result, imports = format_data_with_schema(50.0, schema, version="v2")
        assert result == "50.0"
        assert "RumRetentionFilterSampleRate" not in result
        assert all("rum_retention_filter_sample_rate" not in k for k in imports)

    def test_named_integer_type_still_works(self):
        schema = SchemaWithReference({"type": "integer", "format": "int64"}, "SomeNamedInteger")
        result, imports = format_data_with_schema(42, schema, version="v2")
        assert result == "42"
        assert "SomeNamedInteger" not in result

    def test_named_number_enum_still_uses_constructor(self):
        schema = SchemaWithReference(
            {"type": "number", "enum": [0.5, 1.0], "x-enum-varnames": ["HALF", "ONE"]},
            "SomeNumberEnum",
        )
        result, imports = format_data_with_schema(0.5, schema, version="v2")
        assert result == "SomeNumberEnum.HALF"
