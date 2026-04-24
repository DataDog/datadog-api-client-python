# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestResultDnsRecord(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "type": (str,),
            "values": ([str],),
        }

    attribute_map = {
        "type": "type",
        "values": "values",
    }

    def __init__(self_, type: Union[str, UnsetType] = unset, values: Union[List[str], UnsetType] = unset, **kwargs):
        """
        A DNS record returned in a DNS test response.

        :param type: DNS record type (for example, ``A`` , ``AAAA`` , ``CNAME`` ).
        :type type: str, optional

        :param values: Values associated with the DNS record.
        :type values: [str], optional
        """
        if type is not unset:
            kwargs["type"] = type
        if values is not unset:
            kwargs["values"] = values
        super().__init__(kwargs)
