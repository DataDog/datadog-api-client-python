# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class SecurityMonitoringRuleQueryPayloadData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            UUID,
            none_type,
        )

    @cached_property
    def openapi_types(_):
        return {
            "ddsource": (str,),
            "ddtags": (str,),
            "hostname": (str,),
            "message": (str,),
            "service": (str,),
        }

    attribute_map = {
        "ddsource": "ddsource",
        "ddtags": "ddtags",
        "hostname": "hostname",
        "message": "message",
        "service": "service",
    }

    def __init__(
        self_,
        ddsource: Union[str, UnsetType] = unset,
        ddtags: Union[str, UnsetType] = unset,
        hostname: Union[str, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Payload used to test the rule query.

        :param ddsource: Source of the payload.
        :type ddsource: str, optional

        :param ddtags: Tags associated with your data.
        :type ddtags: str, optional

        :param hostname: The name of the originating host of the log.
        :type hostname: str, optional

        :param message: The message of the payload.
        :type message: str, optional

        :param service: The name of the application or service generating the data.
        :type service: str, optional
        """
        if ddsource is not unset:
            kwargs["ddsource"] = ddsource
        if ddtags is not unset:
            kwargs["ddtags"] = ddtags
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if message is not unset:
            kwargs["message"] = message
        if service is not unset:
            kwargs["service"] = service
        super().__init__(kwargs)
