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
