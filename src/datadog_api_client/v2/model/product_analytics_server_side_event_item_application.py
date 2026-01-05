# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProductAnalyticsServerSideEventItemApplication(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
        }

    attribute_map = {
        "id": "id",
    }

    def __init__(self_, id: str, **kwargs):
        """
        The application in which you want to send your events.

        :param id: The application ID of your application. It can be found in your
            `application management page <https://app.datadoghq.com/rum/list>`_.
        :type id: str
        """
        super().__init__(kwargs)

        self_.id = id
