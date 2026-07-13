import json

from datadog_api_client.configuration import Configuration
from datadog_api_client.model_utils import validate_and_convert_types, model_to_dict

from datadog_api_client.model_utils import UnparsedObject
from datadog_api_client.v1.model.synthetics_api_wait_step import SyntheticsAPIWaitStep
from datadog_api_client.v1.model.synthetics_api_test import SyntheticsAPITest
from datadog_api_client.v1.model.synthetics_browser_test import SyntheticsBrowserTest
from datadog_api_client.v1.model.synthetics_assertion import SyntheticsAssertion
from datadog_api_client.v2.model.downtime_response import DowntimeResponse
from datadog_api_client.v2.model.logs_aggregate_response import LogsAggregateResponse
from datadog_api_client.v2.model.logs_archive import LogsArchive
from datadog_api_client.v2.model.logs_archive_destination import LogsArchiveDestination
from datadog_api_client.v2.model.user_response import UserResponse
from datadog_api_client.v1.model.formula_and_function_event_query_definition import (
    FormulaAndFunctionEventQueryDefinition,
)
from datadog_api_client.v1.model.formula_and_function_event_query_group_by import (
    FormulaAndFunctionEventQueryGroupBy,
)
from datadog_api_client.v1.model.formula_and_function_event_query_group_by_config import (
    FormulaAndFunctionEventQueryGroupByConfig,
)


def test_unknown_nested_oneof_in_list():
    body = """{
        "status": "paused",
        "public_id": "jv7-wfd-kvt",
        "tags": [],
        "locations": [
            "pl:pl-kevin-y-6382df0d72d4588e1817f090b131541f"
        ],
        "message": "",
        "name": "Test on www.example.com",
        "monitor_id": 28558768,
        "type": "api",
        "created_at": "2021-01-12T10:11:40.802074+00:00",
        "modified_at": "2021-01-22T16:42:10.520384+00:00",
        "subtype": "http",
        "config": {
            "request": {
                "url": "https://www.example.com",
                "method": "GET",
                "timeout": 30
            },
            "assertions": [
                {
                    "operator": "lessThan",
                    "type": "responseTime",
                    "target": 1000
                },
                {
                    "operator": "is",
                    "type": "statusCode",
                    "target": 200
                },
                {
                    "operator": "A non existent operator",
                    "type": "body",
                    "target": {
                        "xPath": "//html/head/title",
                        "operator": "contains",
                        "targetValue": "Example"
                    }
                }
            ],
            "configVariables": []
        },
        "options": {
            "monitor_options": {
                "notify_audit": false,
                "locked": false,
                "include_tags": true,
                "new_host_delay": 300,
                "notify_no_data": false,
                "renotify_interval": 0
            },
            "retry": {
                "count": 0,
                "interval": 300
            },
            "min_location_failed": 1,
            "min_failure_duration": 0,
            "tick_every": 60
        }
    }"""
    config = Configuration()
    deserialized_data = validate_and_convert_types(
        json.loads(body), (SyntheticsAPITest,), ["received_data"], True, True, config
    )
    assert isinstance(deserialized_data, SyntheticsAPITest)
    assert len(deserialized_data.config.assertions) == 3
    assert deserialized_data.config.assertions[2].operator == "A non existent operator"
    assert deserialized_data.config.assertions[2]._composed_instances[0]._unparsed
    assert not deserialized_data.config.assertions[1]._composed_instances[0]._unparsed


def test_unknown_nested_enum_in_list():
    body = """{
    "data": {
        "type": "downtime",
        "attributes": {
            "mute_first_recovery_notification": false,
            "schedule": {
                "end": null,
                "start": "2024-11-10T03:12:35.223223+00:00"
            },
            "notify_end_types": [
                "expired"
            ],
            "status": "active",
            "monitor_identifier": {
                "monitor_tags": [
                    "*"
                ]
            },
            "display_timezone": "UTC",
            "notify_end_states": [
                "warn",
                "alert",
                "not an end state"
            ],
            "created": "2024-11-10T03:12:35.241213+00:00",
            "modified": "2024-11-10T03:12:35.241213+00:00",
            "canceled": null,
            "message": null,
            "scope": "host:java-hostsMuteErrorsTest-local-1731208355"
        },
        "id": "a5546ef7-fea3-4a1b-b82e-04f8067f655a"
    }
}"""
    config = Configuration()
    deserialized_data = validate_and_convert_types(
        json.loads(body), (DowntimeResponse,), ["received_data"], True, True, config
    )
    assert isinstance(deserialized_data, DowntimeResponse)
    assert len(deserialized_data.data.attributes.notify_end_states) == 3
    assert str(deserialized_data.data.attributes.notify_end_states[2]) == "not an end state"
    assert deserialized_data.data.attributes.notify_end_states[2]._unparsed


def test_unknown_top_level_enum():
    body = """{
        "status": "live",
        "public_id": "g6d-gcm-pdq",
        "tags": [],
        "locations": [
            "aws:eu-central-1",
            "aws:ap-northeast-1"
        ],
        "message": "",
        "name": "Check on www.10.0.0.1.xip.io",
        "monitor_id": 7464050,
        "type": "A non existent test type",
        "created_at": "2018-12-07T17:30:49.785089+00:00",
        "modified_at": "2019-09-04T17:01:09.921070+00:00",
        "subtype": "http",
        "config": {
            "request": {
                "url": "https://www.10.0.0.1.xip.io",
                "method": "GET",
                "timeout": 30
            },
            "assertions": [
                {
                    "operator": "is",
                    "type": "statusCode",
                    "target": 200
                }
            ]
        },
        "options": {
            "tick_every": 60
        }
    }"""
    config = Configuration()
    deserialized_data = validate_and_convert_types(
        json.loads(body), (SyntheticsBrowserTest,), ["received_data"], True, True, config
    )
    assert isinstance(deserialized_data, SyntheticsBrowserTest)
    assert str(deserialized_data.type) == "A non existent test type"


def test_unknown_nested_enum():
    body = """{
        "status": "live",
        "public_id": "g6d-gcm-pdq",
        "tags": [],
        "locations": [
            "aws:eu-central-1",
            "aws:ap-northeast-1"
        ],
        "message": "",
        "name": "Check on www.10.0.0.1.xip.io",
        "monitor_id": 7464050,
        "type": "api",
        "created_at": "2018-12-07T17:30:49.785089+00:00",
        "modified_at": "2019-09-04T17:01:09.921070+00:00",
        "subtype": "http",
        "config": {
            "request": {
                "url": "https://www.10.0.0.1.xip.io",
                "method": "GET",
                "timeout": 30
            },
            "assertions": [
                {
                    "operator": "not-an-operator",
                    "type": "statusCode",
                    "target": 200
                }
            ]
        },
        "options": {
            "tick_every": 60
        }
    }"""
    config = Configuration()
    deserialized_data = validate_and_convert_types(
        json.loads(body), (SyntheticsAPITest,), ["received_data"], True, True, config
    )
    assert isinstance(deserialized_data, SyntheticsAPITest)
    assert isinstance(deserialized_data.config.assertions[0], SyntheticsAssertion)
    assert str(deserialized_data.config.assertions[0].operator) == "not-an-operator"
    assert deserialized_data.config.assertions[0]._unparsed


def test_unknown_nested_one_of():
    body = """{
        "data": {
            "type": "archives",
            "id": "n_XDSxVpScepiBnyhysj_A",
            "attributes": {
                "name": "my first azure archive",
                "query": "service:toto",
                "state": "UNKNOWN",
                "destination": {
                    "container": "my-container",
                    "storage_account": "storageaccount",
                    "path": "/path/blou",
                    "type": "A non existent destination",
                    "integration": {
                        "tenant_id": "tf-TestAccDatadogLogsArchiveAzure_basic-local-1624981538",
                        "client_id": "testc7f6-1234-5678-9101-3fcbf464test"
                    }
                },
                "rehydration_tags": [],
                "include_tags": false
            }
        }
    }"""
    config = Configuration()
    deserialized_data = validate_and_convert_types(
        json.loads(body), (LogsArchive,), ["received_data"], True, True, config
    )
    assert isinstance(deserialized_data, LogsArchive)
    assert isinstance(deserialized_data.data.attributes.destination, LogsArchiveDestination)
    assert deserialized_data.data.attributes.destination.type == "A non existent destination"
    assert deserialized_data.data.attributes.destination._composed_instances[0]._unparsed


def test_one_of_primitive_types():
    body = """{"data": {"buckets": [{"by": {}, "computes": {"c0": 435.3}}]}}"""
    config = Configuration()
    deserialized_data = validate_and_convert_types(
        json.loads(body), (LogsAggregateResponse,), ["received_data"], True, True, config
    )
    assert isinstance(deserialized_data, LogsAggregateResponse)
    assert deserialized_data.data.buckets[0].computes["c0"] == 435.3


def test_unknown_model_value():
    body = """{
        "data": {
            "type": "users",
            "id": "6d716162-8b48-11ec-8120-da7ad0900002",
            "attributes": {
                "name": null,
                "created_at": "2022-02-11T14:39:33.168622+00:00",
                "modified_at": "2022-02-11T14:39:33.210204+00:00",
                "title": "user title",
                "verified": false,
                "service_account": false,
                "disabled": false,
                "allowed_login_methods": [],
                "status": "Pending"
            },
            "relationships": {
                "roles": { "data": [] },
                "org": {
                    "data": { "type": "orgs", "id": "4dee724d-00cc-11ea-a77b-570c9d03c6c5" }
                }
            }
        }
    }"""
    config = Configuration()
    deserialized_data = validate_and_convert_types(
        json.loads(body), (UserResponse,), ["received_data"], True, True, config
    )
    assert isinstance(deserialized_data, UserResponse)
    serialized = model_to_dict(deserialized_data)
    assert "allowed_login_methods" in serialized["data"]["attributes"]
    assert serialized["data"]["attributes"]["allowed_login_methods"] == []


def test_get_api_test():
    value = [
        {
            "name": "Wait",
            "id": "rjn-fmj-sqw",
            "value": 1,
        },
    ]
    required_types_mixed = ([SyntheticsAPIWaitStep],)
    path_to_item = ["received_data", "config", "steps"]
    converted_value = validate_and_convert_types(value, required_types_mixed, path_to_item, True, True, Configuration())
    assert isinstance(converted_value[0], UnparsedObject)


def test_additional_properties_preserve_integer_precision():
    """JSON integers above 2^53 must survive deserialization into a model's
    additionalProperties without being silently rounded to float64."""
    from datadog_api_client.v1.model.usage_summary_response import UsageSummaryResponse

    # 2^53 + 1 — the smallest integer not exactly representable in float64.
    edge = 9007199254740993
    # A real byte-count value seen in /api/v1/usage/summary at large orgs.
    realistic = 56355942906113522

    body = json.dumps({"some_unknown_field": edge, "another_unknown_field": realistic})
    config = Configuration()
    deserialized = validate_and_convert_types(
        json.loads(body), (UsageSummaryResponse,), ["received_data"], True, True, config
    )

    v_edge = deserialized["some_unknown_field"]
    v_real = deserialized["another_unknown_field"]
    assert type(v_edge) is int and v_edge == edge, f"expected int {edge}, got {type(v_edge).__name__} {v_edge!r}"
    assert (
        type(v_real) is int and v_real == realistic
    ), f"expected int {realistic}, got {type(v_real).__name__} {v_real!r}"


def test_schema_declared_float_still_upconverts_int_input():
    """Regression guard: when the schema explicitly declares a field as float,
    an integer JSON value must still upconvert to float."""
    converted = validate_and_convert_types(3, (float,), ["received_data"], True, True, Configuration())
    assert type(converted) is float and converted == 3.0


def test_one_of_list_branch_rejected_when_element_unparsed():
    """A oneOf list branch must reject the whole value when any element fails to
    parse, rather than silently dropping the bad element and accepting a
    truncated list. ``FormulaAndFunctionEventQueryGroupByConfig`` is a oneOf
    whose first branch is ``[FormulaAndFunctionEventQueryGroupBy]``."""
    value = [
        {"facet": "@geo.country_iso_code", "sort": {"aggregation": "count", "order": "desc"}},
        # Unknown aggregation enum -> this element is unparsed.
        {"facet": "@http.status_code", "sort": {"aggregation": "a non existent aggregation"}},
    ]
    config = Configuration()
    deserialized = validate_and_convert_types(
        value, (FormulaAndFunctionEventQueryGroupByConfig,), ["received_data"], True, True, config
    )
    # The whole value is unparsed rather than a one-element list of the valid item.
    assert isinstance(deserialized, UnparsedObject)


def test_one_of_list_branch_all_valid_yields_objects():
    """When every element of a oneOf list branch parses, the value deserializes
    to a list of model objects (not raw dicts)."""
    config = Configuration()

    valid = [
        {"facet": "@geo.country_iso_code", "limit": 250, "sort": {"aggregation": "count", "order": "desc"}},
    ]
    group_by = validate_and_convert_types(
        valid, (FormulaAndFunctionEventQueryGroupByConfig,), ["received_data"], True, True, config
    )
    assert isinstance(group_by, list)
    assert isinstance(group_by[0], FormulaAndFunctionEventQueryGroupBy)
    assert group_by[0].facet == "@geo.country_iso_code"
    assert str(group_by[0].sort.order) == "desc"


def test_one_of_list_branch_unparsed_propagates_to_enclosing_model():
    """An unparsed element inside a oneOf list branch must propagate ``_unparsed``
    up to the containing model, rather than being silently dropped so the model
    looks fully parsed."""
    config = Configuration()
    body = {
        "data_source": "logs",
        "name": "my_query",
        "compute": {"aggregation": "count"},
        "group_by": [
            {"facet": "@geo.country_iso_code", "sort": {"aggregation": "count", "order": "desc"}},
            # Unknown aggregation enum -> this element is unparsed.
            {"facet": "@http.status_code", "sort": {"aggregation": "a non existent aggregation"}},
        ],
    }
    definition = validate_and_convert_types(
        body, (FormulaAndFunctionEventQueryDefinition,), ["received_data"], True, True, config
    )
    assert isinstance(definition, FormulaAndFunctionEventQueryDefinition)
    assert definition._unparsed


def test_one_of_empty_list_branch_accepted():
    """An empty array for a oneOf list branch is valid: every element parses
    vacuously, so the value deserializes to an empty list rather than falling
    through to ``UnparsedObject`` and marking the enclosing model unparsed."""
    config = Configuration()
    group_by = validate_and_convert_types(
        [], (FormulaAndFunctionEventQueryGroupByConfig,), ["received_data"], True, True, config
    )
    assert group_by == []
