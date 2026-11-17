# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AiGatewayModelAutomaticPricingMapping(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "revision": (str,),
            "scope": (str,),
            "version": (int,),
        }

    attribute_map = {
        "id": "id",
        "revision": "revision",
        "scope": "scope",
        "version": "version",
    }

    def __init__(self_, id: str, revision: str, scope: str, version: int, **kwargs):
        """
        The reviewed endpoint mapping used to identify a custom provider. Omitted when the provider and model identity matched exactly.

        :param id: Mapping identifier.
        :type id: str

        :param revision: Mapping revision.
        :type revision: str

        :param scope: Mapping scope, such as ``provider``.
        :type scope: str

        :param version: Mapping version.
        :type version: int
        """
        super().__init__(kwargs)

        self_.id = id
        self_.revision = revision
        self_.scope = scope
        self_.version = version
