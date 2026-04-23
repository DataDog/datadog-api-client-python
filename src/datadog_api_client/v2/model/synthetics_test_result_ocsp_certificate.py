# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestResultOCSPCertificate(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "revocation_reason": (str,),
            "revocation_time": (int,),
            "serial_number": (str,),
        }

    attribute_map = {
        "revocation_reason": "revocation_reason",
        "revocation_time": "revocation_time",
        "serial_number": "serial_number",
    }

    def __init__(
        self_,
        revocation_reason: Union[str, UnsetType] = unset,
        revocation_time: Union[int, UnsetType] = unset,
        serial_number: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Certificate details returned in an OCSP response.

        :param revocation_reason: Reason code for the revocation, when applicable.
        :type revocation_reason: str, optional

        :param revocation_time: Unix timestamp (ms) of the revocation.
        :type revocation_time: int, optional

        :param serial_number: Serial number of the certificate.
        :type serial_number: str, optional
        """
        if revocation_reason is not unset:
            kwargs["revocation_reason"] = revocation_reason
        if revocation_time is not unset:
            kwargs["revocation_time"] = revocation_time
        if serial_number is not unset:
            kwargs["serial_number"] = serial_number
        super().__init__(kwargs)
