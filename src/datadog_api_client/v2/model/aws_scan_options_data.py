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
    from datadog_api_client.v2.model.aws_scan_options_attributes import AwsScanOptionsAttributes
    from datadog_api_client.v2.model.aws_scan_options_type import AwsScanOptionsType


class AwsScanOptionsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_scan_options_attributes import AwsScanOptionsAttributes
        from datadog_api_client.v2.model.aws_scan_options_type import AwsScanOptionsType

        return {
            "attributes": (AwsScanOptionsAttributes,),
            "id": (str,),
            "type": (AwsScanOptionsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[AwsScanOptionsAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[AwsScanOptionsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Single AWS Scan Options entry.

        :param attributes: Attributes for the AWS scan options.
        :type attributes: AwsScanOptionsAttributes, optional

        :param id: The ID of the AWS account.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``aws_scan_options``.
        :type type: AwsScanOptionsType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
