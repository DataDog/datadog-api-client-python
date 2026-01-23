# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceNowTemplateType(ModelSimple):
    """
    Type identifier for ServiceNow template resources

    :param value: If omitted defaults to "servicenow_templates". Must be one of ["servicenow_templates"].
    :type value: str
    """

    allowed_values = {
        "servicenow_templates",
    }
    SERVICENOW_TEMPLATES: ClassVar["ServiceNowTemplateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceNowTemplateType.SERVICENOW_TEMPLATES = ServiceNowTemplateType("servicenow_templates")
