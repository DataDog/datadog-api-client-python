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
    from datadog_api_client.v1.model.synthetics_mobile_tests_mobile_application_reference_type import (
        SyntheticsMobileTestsMobileApplicationReferenceType,
    )


class SyntheticsMobileTestsMobileApplication(ModelNormal):
    validations = {
        "application_id": {
            "max_length": 1500,
        },
        "reference_id": {
            "max_length": 1500,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_mobile_tests_mobile_application_reference_type import (
            SyntheticsMobileTestsMobileApplicationReferenceType,
        )

        return {
            "application_id": (str,),
            "reference_id": (str,),
            "reference_type": (SyntheticsMobileTestsMobileApplicationReferenceType,),
        }

    attribute_map = {
        "application_id": "applicationId",
        "reference_id": "referenceId",
        "reference_type": "referenceType",
    }

    def __init__(
        self_,
        application_id: Union[str, UnsetType] = unset,
        reference_id: Union[str, UnsetType] = unset,
        reference_type: Union[SyntheticsMobileTestsMobileApplicationReferenceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Mobile application for mobile synthetics test.

        :param application_id: Application ID of the mobile application.
        :type application_id: str, optional

        :param reference_id: Reference ID of the mobile application.
        :type reference_id: str, optional

        :param reference_type: Reference type for the mobile application for a mobile synthetics test.
        :type reference_type: SyntheticsMobileTestsMobileApplicationReferenceType, optional
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        if reference_id is not unset:
            kwargs["reference_id"] = reference_id
        if reference_type is not unset:
            kwargs["reference_type"] = reference_type
        super().__init__(kwargs)
