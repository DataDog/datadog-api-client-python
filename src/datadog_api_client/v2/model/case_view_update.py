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
    from datadog_api_client.v2.model.case_view_update_attributes import CaseViewUpdateAttributes
    from datadog_api_client.v2.model.case_view_resource_type import CaseViewResourceType


class CaseViewUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_view_update_attributes import CaseViewUpdateAttributes
        from datadog_api_client.v2.model.case_view_resource_type import CaseViewResourceType

        return {
            "attributes": (CaseViewUpdateAttributes,),
            "type": (CaseViewResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, type: CaseViewResourceType, attributes: Union[CaseViewUpdateAttributes, UnsetType] = unset, **kwargs
    ):
        """
        Data object for updating a case view.

        :param attributes: Attributes that can be updated on a case view. All fields are optional; only provided fields are changed.
        :type attributes: CaseViewUpdateAttributes, optional

        :param type: JSON:API resource type for case views.
        :type type: CaseViewResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
