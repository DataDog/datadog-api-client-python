# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.creator import Creator
    from datadog_api_client.v1.model.monitor_overall_states import MonitorOverallStates
    from datadog_api_client.v1.model.monitor_search_result_notification import MonitorSearchResultNotification
    from datadog_api_client.v1.model.monitor_type import MonitorType

    globals()["Creator"] = Creator
    globals()["MonitorOverallStates"] = MonitorOverallStates
    globals()["MonitorSearchResultNotification"] = MonitorSearchResultNotification
    globals()["MonitorType"] = MonitorType


class MonitorSearchResult(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "classification": (str,),
            "creator": (Creator,),
            "id": (int,),
            "last_triggered_ts": (
                int,
                none_type,
            ),
            "metrics": ([str],),
            "name": (str,),
            "notifications": ([MonitorSearchResultNotification],),
            "org_id": (int,),
            "query": (str,),
            "scopes": ([str],),
            "status": (MonitorOverallStates,),
            "tags": ([str],),
            "type": (MonitorType,),
        }

    attribute_map = {
        "classification": "classification",
        "creator": "creator",
        "id": "id",
        "last_triggered_ts": "last_triggered_ts",
        "metrics": "metrics",
        "name": "name",
        "notifications": "notifications",
        "org_id": "org_id",
        "query": "query",
        "scopes": "scopes",
        "status": "status",
        "tags": "tags",
        "type": "type",
    }

    read_only_vars = {
        "classification",
        "id",
        "last_triggered_ts",
        "metrics",
        "name",
        "notifications",
        "org_id",
        "tags",
    }

    def __init__(self, *args, **kwargs):
        """MonitorSearchResult - a model defined in OpenAPI

        Keyword Args:
            classification (str): [optional] Classification of the monitor.
            creator (Creator): [optional]
            id (int): [optional] ID of the monitor.
            last_triggered_ts (int, none_type): [optional] Latest timestamp the monitor triggered.
            metrics ([str]): [optional] Metrics used by the monitor.
            name (str): [optional] The monitor name.
            notifications ([MonitorSearchResultNotification]): [optional] The notification triggered by the monitor.
            org_id (int): [optional] The ID of the organization.
            query (str): [optional] The monitor query.
            scopes ([str]): [optional] The scope(s) to which the downtime applies, for example `host:app2`. Provide multiple scopes as a comma-separated list, for example `env:dev,env:prod`. The resulting downtime applies to sources that matches ALL provided scopes (that is `env:dev AND env:prod`), NOT any of them.
            status (MonitorOverallStates): [optional]
            tags ([str]): [optional] Tags associated with the monitor.
            type (MonitorType): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorSearchResult, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
