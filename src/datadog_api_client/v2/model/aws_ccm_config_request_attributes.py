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
    from datadog_api_client.v2.model.aws_ccm_config import AWSCcmConfig


class AWSCcmConfigRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_ccm_config import AWSCcmConfig

        return {
            "ccm_config": (AWSCcmConfig,),
        }

    attribute_map = {
        "ccm_config": "ccm_config",
    }

    def __init__(self_, ccm_config: AWSCcmConfig, **kwargs):
        """
        AWS CCM Config attributes for Create/Update requests.

        :param ccm_config: AWS Cloud Cost Management config.
        :type ccm_config: AWSCcmConfig
        """
        super().__init__(kwargs)

        self_.ccm_config = ccm_config
