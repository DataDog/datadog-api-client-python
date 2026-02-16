# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OnPremManagementServiceCreateEnrollmentResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "token": (str,),
        }

    attribute_map = {
        "token": "token",
    }

    def __init__(self_, token: str, **kwargs):
        """
        Attributes for the created enrollment.

        :param token: The enrollment token.
        :type token: str
        """
        super().__init__(kwargs)

        self_.token = token
