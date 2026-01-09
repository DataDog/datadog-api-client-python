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
    from datadog_api_client.v2.model.security_findings_attributes import SecurityFindingsAttributes
    from datadog_api_client.v2.model.security_findings_data_type import SecurityFindingsDataType


class SecurityFindingsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_findings_attributes import SecurityFindingsAttributes
        from datadog_api_client.v2.model.security_findings_data_type import SecurityFindingsDataType

        return {
            "attributes": (SecurityFindingsAttributes,),
            "id": (str,),
            "type": (SecurityFindingsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SecurityFindingsAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SecurityFindingsDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single security finding.

        :param attributes: The JSON object containing all attributes of the security finding.
        :type attributes: SecurityFindingsAttributes, optional

        :param id: The unique ID of the security finding.
        :type id: str, optional

        :param type: The type of the security finding resource.
        :type type: SecurityFindingsDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
