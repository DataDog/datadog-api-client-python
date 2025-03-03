# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_scan_options_attributes import AwsScanOptionsAttributes
    from datadog_api_client.v2.model.aws_scan_options_type import AwsScanOptionsType


class AwsScanOptionsCreateData(ModelNormal):
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

    def __init__(self_, attributes: AwsScanOptionsAttributes, id: str, type: AwsScanOptionsType, **kwargs):
        """
        Object for the scan options of a single AWS account.

        :param attributes: Attributes for the AWS scan options.
        :type attributes: AwsScanOptionsAttributes

        :param id: The ID of an AWS account.
        :type id: str

        :param type: The type of the resource. The value should always be ``aws_scan_options``.
        :type type: AwsScanOptionsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
