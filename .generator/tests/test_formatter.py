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
