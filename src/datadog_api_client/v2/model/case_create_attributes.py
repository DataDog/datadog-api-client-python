# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_attribute_value import CustomAttributeValue
    from datadog_api_client.v2.model.case_priority import CasePriority


class CaseCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_attribute_value import CustomAttributeValue
        from datadog_api_client.v2.model.case_priority import CasePriority

        return {
            "custom_attributes": ({str: (CustomAttributeValue,)},),
            "description": (str,),
            "priority": (CasePriority,),
            "title": (str,),
            "type_id": (str,),
        }

    attribute_map = {
        "custom_attributes": "custom_attributes",
        "description": "description",
        "priority": "priority",
        "title": "title",
        "type_id": "type_id",
    }

    def __init__(
        self_,
        title: str,
        type_id: str,
        custom_attributes: Union[Dict[str, CustomAttributeValue], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        priority: Union[CasePriority, UnsetType] = unset,
        **kwargs,
    ):
        """
        Case creation attributes

        :param custom_attributes: Case custom attributes
        :type custom_attributes: {str: (CustomAttributeValue,)}, optional

        :param description: Description
        :type description: str, optional

        :param priority: Case priority
        :type priority: CasePriority, optional

        :param title: Title
        :type title: str

        :param type_id: Case type UUID
        :type type_id: str
        """
        if custom_attributes is not unset:
            kwargs["custom_attributes"] = custom_attributes
        if description is not unset:
            kwargs["description"] = description
        if priority is not unset:
            kwargs["priority"] = priority
        super().__init__(kwargs)

        self_.title = title
        self_.type_id = type_id
