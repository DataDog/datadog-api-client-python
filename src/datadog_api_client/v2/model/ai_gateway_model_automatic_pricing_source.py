# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AiGatewayModelAutomaticPricingSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "match_method": (str,),
            "model_id": (str,),
            "name": (str,),
            "provider_id": (str,),
            "revision": (str,),
        }

    attribute_map = {
        "match_method": "match_method",
        "model_id": "model_id",
        "name": "name",
        "provider_id": "provider_id",
        "revision": "revision",
    }

    def __init__(self_, match_method: str, model_id: str, name: str, provider_id: str, revision: str, **kwargs):
        """
        The pricing source entry the price was read from.

        :param match_method: How the gateway matched the model to the source entry, such as ``wire_id``.
        :type match_method: str

        :param model_id: Model identifier in the source.
        :type model_id: str

        :param name: Pricing source name.
        :type name: str

        :param provider_id: Provider identifier in the source.
        :type provider_id: str

        :param revision: Source revision the price was read from.
        :type revision: str
        """
        super().__init__(kwargs)

        self_.match_method = match_method
        self_.model_id = model_id
        self_.name = name
        self_.provider_id = provider_id
        self_.revision = revision
