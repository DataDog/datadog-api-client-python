# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSNewExternalIDResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "external_id": (str,),
        }

    attribute_map = {
        "external_id": "external_id",
    }

    def __init__(self_, external_id: str, **kwargs):
        """
        AWS External ID response body.

        :param external_id: AWS IAM External ID for associated role.
        :type external_id: str
        """
        super().__init__(kwargs)

        self_.external_id = external_id
