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
    from datadog_api_client.v2.model.elastic_cloud_basic_auth_type import ElasticCloudBasicAuthType


class ElasticCloudBasicAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.elastic_cloud_basic_auth_type import ElasticCloudBasicAuthType

        return {
            "password": (str,),
            "type": (ElasticCloudBasicAuthType,),
            "username": (str,),
        }

    attribute_map = {
        "password": "password",
        "type": "type",
        "username": "username",
    }

    def __init__(self_, password: str, type: ElasticCloudBasicAuthType, username: str, **kwargs):
        """
        Username & password authentication for Elastic Cloud.

        :param password: Password used to authenticate against the deployment. This field is not returned by the API.
        :type password: str

        :param type: Authentication method discriminator.
        :type type: ElasticCloudBasicAuthType

        :param username: Username used to authenticate against the deployment.
        :type username: str
        """
        super().__init__(kwargs)

        self_.password = password
        self_.type = type
        self_.username = username
