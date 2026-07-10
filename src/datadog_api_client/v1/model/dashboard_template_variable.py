# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.dashboard_template_variable_available_values_query import (
        DashboardTemplateVariableAvailableValuesQuery,
    )
    from datadog_api_client.v1.model.dashboard_available_values_events_query import DashboardAvailableValuesEventsQuery
    from datadog_api_client.v1.model.dashboard_available_values_metrics_query import (
        DashboardAvailableValuesMetricsQuery,
    )


class DashboardTemplateVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dashboard_template_variable_available_values_query import (
            DashboardTemplateVariableAvailableValuesQuery,
        )

        return {
            "available_values": ([str], none_type),
            "available_values_query": (DashboardTemplateVariableAvailableValuesQuery,),
            "data_source_mappings": ({str: (str,)},),
            "default": (str, none_type),
            "defaults": ([str],),
            "name": (str,),
            "prefix": (str, none_type),
            "type": (str, none_type),
        }

    attribute_map = {
        "available_values": "available_values",
        "available_values_query": "available_values_query",
        "data_source_mappings": "data_source_mappings",
        "default": "default",
        "defaults": "defaults",
        "name": "name",
        "prefix": "prefix",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        available_values: Union[List[str], none_type, UnsetType] = unset,
        available_values_query: Union[
            DashboardTemplateVariableAvailableValuesQuery,
            DashboardAvailableValuesEventsQuery,
            DashboardAvailableValuesMetricsQuery,
            UnsetType,
        ] = unset,
        data_source_mappings: Union[Dict[str, str], UnsetType] = unset,
        default: Union[str, none_type, UnsetType] = unset,
        defaults: Union[List[str], UnsetType] = unset,
        prefix: Union[str, none_type, UnsetType] = unset,
        type: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Template variable.

        :param available_values: The list of values that the template variable drop-down is limited to.
        :type available_values: [str], none_type, optional

        :param available_values_query: A query that dynamically computes the list of values available for this template variable.
        :type available_values_query: DashboardTemplateVariableAvailableValuesQuery, optional

        :param data_source_mappings: A mapping from data source type to the variable value to use for that data source.
        :type data_source_mappings: {str: (str,)}, optional

        :param default: (deprecated) The default value for the template variable on dashboard load. Cannot be used in conjunction with ``defaults``. **Deprecated**.
        :type default: str, none_type, optional

        :param defaults: One or many default values for template variables on load. If more than one default is specified, they will be unioned together with ``OR``. Cannot be used in conjunction with ``default``.
        :type defaults: [str], optional

        :param name: The name of the variable.
        :type name: str

        :param prefix: The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.
        :type prefix: str, none_type, optional

        :param type: The type of variable. This is to differentiate between filter variables (interpolated in query) and group by variables (interpolated into group by).
        :type type: str, none_type, optional
        """
        if available_values is not unset:
            kwargs["available_values"] = available_values
        if available_values_query is not unset:
            kwargs["available_values_query"] = available_values_query
        if data_source_mappings is not unset:
            kwargs["data_source_mappings"] = data_source_mappings
        if default is not unset:
            kwargs["default"] = default
        if defaults is not unset:
            kwargs["defaults"] = defaults
        if prefix is not unset:
            kwargs["prefix"] = prefix
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.name = name
