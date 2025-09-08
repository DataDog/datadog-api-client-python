# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.google_meet_configuration_reference_data import (
        GoogleMeetConfigurationReferenceData,
    )


class GoogleMeetConfigurationReference(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_meet_configuration_reference_data import (
            GoogleMeetConfigurationReferenceData,
        )

        return {
            "data": (GoogleMeetConfigurationReferenceData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[GoogleMeetConfigurationReferenceData, none_type], **kwargs):
        """
        A reference to a Google Meet Configuration resource.

        :param data: The Google Meet configuration relationship data object.
        :type data: GoogleMeetConfigurationReferenceData, none_type
        """
        super().__init__(kwargs)

        self_.data = data
