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
    from datadog_api_client.v2.model.application_key_create_data import ApplicationKeyCreateData


class ApplicationKeyCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_key_create_data import ApplicationKeyCreateData

        return {
            "data": (ApplicationKeyCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ApplicationKeyCreateData, *args, **kwargs):
        """
        Request used to create an application key.

        :param data: Object used to create an application key.
        :type data: ApplicationKeyCreateData
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.data = data
