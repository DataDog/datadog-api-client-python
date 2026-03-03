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
    from datadog_api_client.v2.model.aws_ccm_config_request_attributes import AWSCcmConfigRequestAttributes
    from datadog_api_client.v2.model.aws_ccm_config_type import AWSCcmConfigType


class AWSCcmConfigRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_ccm_config_request_attributes import AWSCcmConfigRequestAttributes
        from datadog_api_client.v2.model.aws_ccm_config_type import AWSCcmConfigType

        return {
            "attributes": (AWSCcmConfigRequestAttributes,),
            "type": (AWSCcmConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AWSCcmConfigRequestAttributes, type: AWSCcmConfigType, **kwargs):
        """
        AWS CCM Config Create/Update Request data.

        :param attributes: AWS CCM Config attributes for Create/Update requests.
        :type attributes: AWSCcmConfigRequestAttributes

        :param type: AWS CCM Config resource type.
        :type type: AWSCcmConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
