# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EventEmailAddressFormat(ModelSimple):
    """
    The format of events ingested through the email address.

    :param value: Must be one of ["json", "plain-text"].
    :type value: str
    """

    allowed_values = {
        "json",
        "plain-text",
    }
    JSON: ClassVar["EventEmailAddressFormat"]
    PLAIN_TEXT: ClassVar["EventEmailAddressFormat"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EventEmailAddressFormat.JSON = EventEmailAddressFormat("json")
EventEmailAddressFormat.PLAIN_TEXT = EventEmailAddressFormat("plain-text")
