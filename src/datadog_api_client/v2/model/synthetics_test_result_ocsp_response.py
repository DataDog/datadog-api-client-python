# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_result_ocsp_certificate import SyntheticsTestResultOCSPCertificate
    from datadog_api_client.v2.model.synthetics_test_result_ocsp_updates import SyntheticsTestResultOCSPUpdates


class SyntheticsTestResultOCSPResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_result_ocsp_certificate import (
            SyntheticsTestResultOCSPCertificate,
        )
        from datadog_api_client.v2.model.synthetics_test_result_ocsp_updates import SyntheticsTestResultOCSPUpdates

        return {
            "certificate": (SyntheticsTestResultOCSPCertificate,),
            "status": (str,),
            "updates": (SyntheticsTestResultOCSPUpdates,),
        }

    attribute_map = {
        "certificate": "certificate",
        "status": "status",
        "updates": "updates",
    }

    def __init__(
        self_,
        certificate: Union[SyntheticsTestResultOCSPCertificate, UnsetType] = unset,
        status: Union[str, UnsetType] = unset,
        updates: Union[SyntheticsTestResultOCSPUpdates, UnsetType] = unset,
        **kwargs,
    ):
        """
        OCSP response received while validating a certificate.

        :param certificate: Certificate details returned in an OCSP response.
        :type certificate: SyntheticsTestResultOCSPCertificate, optional

        :param status: OCSP response status (for example, ``good`` , ``revoked`` , ``unknown`` ).
        :type status: str, optional

        :param updates: OCSP response update timestamps.
        :type updates: SyntheticsTestResultOCSPUpdates, optional
        """
        if certificate is not unset:
            kwargs["certificate"] = certificate
        if status is not unset:
            kwargs["status"] = status
        if updates is not unset:
            kwargs["updates"] = updates
        super().__init__(kwargs)
