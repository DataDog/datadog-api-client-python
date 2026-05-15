# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UpdateAppSelfServiceRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "self_service": (bool,),
        }

    attribute_map = {
        "self_service": "selfService",
    }

    def __init__(self_, self_service: bool, **kwargs):
        """
        Attributes for updating an app's self-service status.

        :param self_service: Whether the app is enabled for self-service.
        :type self_service: bool
        """
        super().__init__(kwargs)

        self_.self_service = self_service
