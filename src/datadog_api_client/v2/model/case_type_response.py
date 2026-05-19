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
    from datadog_api_client.v2.model.case_type_resource import CaseTypeResource


class CaseTypeResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_type_resource import CaseTypeResource

        return {
            "data": (CaseTypeResource,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[CaseTypeResource, UnsetType] = unset, **kwargs):
        """
        Response containing a single case type.

        :param data: A case type that defines a classification category for cases. Each case type can have its own custom attributes, statuses, and automation rules.
        :type data: CaseTypeResource, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
