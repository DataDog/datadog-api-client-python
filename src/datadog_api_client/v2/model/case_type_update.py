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


class CaseTypeUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_type_resource_attributes import CaseTypeResourceAttributes
        from datadog_api_client.v2.model.case_type_resource_type import CaseTypeResourceType

        return {
            "attributes": (CaseTypeResourceAttributes,),
            "type": (CaseTypeResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, type: CaseTypeResourceType, attributes: Union[CaseTypeResourceAttributes, UnsetType] = unset, **kwargs
    ):
        """
        Data object for updating a case type.

        :param attributes: Attributes of a case type, which define a classification category for cases. Organizations use case types to model different workflows (for example, Security Incident, Bug Report, Change Request).
        :type attributes: CaseTypeResourceAttributes, optional

        :param type: JSON:API resource type for case types.
        :type type: CaseTypeResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
