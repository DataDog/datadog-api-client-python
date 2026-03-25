# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_destination_forward_destination_splunk_type import (
        CustomDestinationForwardDestinationSplunkType,
    )


class CustomDestinationForwardDestinationSplunk(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_destination_forward_destination_splunk_type import (
            CustomDestinationForwardDestinationSplunkType,
        )

        return {
            "access_token": (str,),
            "endpoint": (str,),
            "sourcetype": (str, none_type),
            "type": (CustomDestinationForwardDestinationSplunkType,),
        }

    attribute_map = {
        "access_token": "access_token",
        "endpoint": "endpoint",
        "sourcetype": "sourcetype",
        "type": "type",
    }

    def __init__(
        self_,
        access_token: str,
        endpoint: str,
        type: CustomDestinationForwardDestinationSplunkType,
        sourcetype: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        The Splunk HTTP Event Collector (HEC) destination.

        :param access_token: Access token of the Splunk HTTP Event Collector. This field is not returned by the API.
        :type access_token: str

        :param endpoint: The destination for which logs will be forwarded to.
            Must have HTTPS scheme and forwarding back to Datadog is not allowed.
        :type endpoint: str

        :param sourcetype: The Splunk sourcetype for the events sent to this Splunk destination.

            If absent, the default sourcetype ``_json`` is used. If set to ``null`` , the ``sourcetype``
            field is omitted from the Splunk HEC payload entirely. Otherwise, the provided string
            value is used as the sourcetype.
        :type sourcetype: str, none_type, optional

        :param type: Type of the Splunk HTTP Event Collector (HEC) destination.
        :type type: CustomDestinationForwardDestinationSplunkType
        """
        if sourcetype is not unset:
            kwargs["sourcetype"] = sourcetype
        super().__init__(kwargs)

        self_.access_token = access_token
        self_.endpoint = endpoint
        self_.type = type
