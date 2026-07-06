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
    from datadog_api_client.v1.model.notebook_template_variable_available_values_query import (
        NotebookTemplateVariableAvailableValuesQuery,
    )
    from datadog_api_client.v1.model.notebook_template_variable_available_values_query_log_rum_spans import (
        NotebookTemplateVariableAvailableValuesQueryLogRumSpans,
    )
    from datadog_api_client.v1.model.notebook_template_variable_available_values_query_metrics import (
        NotebookTemplateVariableAvailableValuesQueryMetrics,
    )


class NotebookTemplateVariable(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notebook_template_variable_available_values_query import (
            NotebookTemplateVariableAvailableValuesQuery,
        )

        return {
            "available_values": ([str], none_type),
            "available_values_query": (NotebookTemplateVariableAvailableValuesQuery,),
            "data_source_mappings": ({str: (str,)},),
            "default": (str, none_type),
            "defaults": ([str],),
            "name": (str,),
            "placement": (str,),
            "prefix": (str, none_type),
            "type": (str,),
        }

    attribute_map = {
        "available_values": "available_values",
        "available_values_query": "available_values_query",
        "data_source_mappings": "data_source_mappings",
        "default": "default",
        "defaults": "defaults",
        "name": "name",
        "placement": "placement",
        "prefix": "prefix",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        available_values: Union[List[str], none_type, UnsetType] = unset,
        available_values_query: Union[
            NotebookTemplateVariableAvailableValuesQuery,
            NotebookTemplateVariableAvailableValuesQueryLogRumSpans,
            NotebookTemplateVariableAvailableValuesQueryMetrics,
            UnsetType,
        ] = unset,
        data_source_mappings: Union[Dict[str, str], UnsetType] = unset,
        default: Union[str, none_type, UnsetType] = unset,
        defaults: Union[List[str], UnsetType] = unset,
        placement: Union[str, UnsetType] = unset,
        prefix: Union[str, none_type, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Notebook template variable.

        :param available_values: The list of values that the template variable drop-down is limited to.
        :type available_values: [str], none_type, optional

        :param available_values_query: Query used to dynamically populate the list of available values for the template variable.
        :type available_values_query: NotebookTemplateVariableAvailableValuesQuery, optional

        :param data_source_mappings: Mapping of data source names to template variable values.
        :type data_source_mappings: {str: (str,)}, optional

        :param default: (deprecated) The default value for the template variable on notebook load.
            Cannot be used in conjunction with ``defaults``. **Deprecated**.
        :type default: str, none_type, optional

        :param defaults: One or many default values for the template variable. Cannot be used in conjunction with ``default``.
        :type defaults: [str], optional

        :param name: The name of the variable.
        :type name: str

        :param placement: The placement of the template variable in the notebook.
        :type placement: str, optional

        :param prefix: The tag prefix associated with the variable. Only tags with this prefix appear in the variable drop-down.
        :type prefix: str, none_type, optional

        :param type: The type of the template variable.
        :type type: str, optional
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
        if placement is not unset:
            kwargs["placement"] = placement
        if prefix is not unset:
            kwargs["prefix"] = prefix
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.name = name
