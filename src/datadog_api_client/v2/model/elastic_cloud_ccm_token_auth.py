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
    from datadog_api_client.v2.model.elastic_cloud_ccm_token_auth_type import ElasticCloudCcmTokenAuthType


class ElasticCloudCcmTokenAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_ccm_token_auth_type import ElasticCloudCcmTokenAuthType

        return {
            "api_key": (str,),
            "type": (ElasticCloudCcmTokenAuthType,),
        }

    attribute_map = {
        "api_key": "api_key",
        "type": "type",
    }

    def __init__(self_, api_key: str, type: ElasticCloudCcmTokenAuthType, **kwargs):
        """
        Encrypted token (bearer token) authentication for Elastic Cloud CCM.

        :param api_key: Billing API key. An Elastic Cloud API key with read access to both Billing and Deployments. Create one under Organization settings > API Keys. This field is not returned by the API.
        :type api_key: str

        :param type: Authentication method discriminator.
        :type type: ElasticCloudCcmTokenAuthType
        """
        super().__init__(kwargs)

        self_.api_key = api_key
        self_.type = type
