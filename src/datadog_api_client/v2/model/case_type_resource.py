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
    from datadog_api_client.v2.model.case_type_resource_attributes import CaseTypeResourceAttributes
    from datadog_api_client.v2.model.case_type_resource_type import CaseTypeResourceType


class CaseTypeResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_type_resource_attributes import CaseTypeResourceAttributes
        from datadog_api_client.v2.model.case_type_resource_type import CaseTypeResourceType

        return {
            "attributes": (CaseTypeResourceAttributes,),
            "id": (str,),
            "type": (CaseTypeResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[CaseTypeResourceAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CaseTypeResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A work item type that defines a classification category for work items. Each work item type can have its own custom attributes, statuses, and automation rules.

        :param attributes: Attributes of a work item type, which define a classification category for work items. Organizations use work item types to model different workflows (for example, Security Incident, Bug Report, Change Request).
        :type attributes: CaseTypeResourceAttributes, optional

        :param id: Work item type's identifier
        :type id: str, optional

        :param type: JSON:API resource type for work item types.
        :type type: CaseTypeResourceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
