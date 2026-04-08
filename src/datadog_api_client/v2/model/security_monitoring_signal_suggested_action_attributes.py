# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_signal_investigation_query_template_variables import (
        SecurityMonitoringSignalInvestigationQueryTemplateVariables,
    )


class SecurityMonitoringSignalSuggestedActionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_investigation_query_template_variables import (
            SecurityMonitoringSignalInvestigationQueryTemplateVariables,
        )

        return {
            "name": (str,),
            "query_filter": (str,),
            "template_variables": (SecurityMonitoringSignalInvestigationQueryTemplateVariables,),
            "title": (str,),
            "url": (str,),
        }

    attribute_map = {
        "name": "name",
        "query_filter": "query_filter",
        "template_variables": "template_variables",
        "title": "title",
        "url": "url",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        query_filter: Union[str, UnsetType] = unset,
        template_variables: Union[SecurityMonitoringSignalInvestigationQueryTemplateVariables, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a suggested action for a security signal. The available fields depend on the action type.

        :param name: The name of the investigation log query.
        :type name: str, optional

        :param query_filter: The log query filter for the investigation.
        :type query_filter: str, optional

        :param template_variables: Template variables applied to the investigation log query, mapping attribute paths to values extracted from the signal.
        :type template_variables: SecurityMonitoringSignalInvestigationQueryTemplateVariables, optional

        :param title: The title of the recommended blog post.
        :type title: str, optional

        :param url: The URL of the suggested action.
        :type url: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        if template_variables is not unset:
            kwargs["template_variables"] = template_variables
        if title is not unset:
            kwargs["title"] = title
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
