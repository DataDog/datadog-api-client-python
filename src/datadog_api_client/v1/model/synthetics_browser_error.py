# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsBrowserError(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_browser_error_type import SyntheticsBrowserErrorType

        return {
            "description": (str,),
            "name": (str,),
            "status": (int,),
            "type": (SyntheticsBrowserErrorType,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "status": "status",
        "type": "type",
    }

    def __init__(self_, description, name, type, *args, **kwargs):
        """
        Error response object for a browser test.

        :param description: Description of the error.
        :type description: str

        :param name: Name of the error.
        :type name: str

        :param status: Status Code of the error.
        :type status: int, optional

        :param type: Error type returned by a browser test.
        :type type: SyntheticsBrowserErrorType
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.description = description
        self_.name = name
        self_.type = type
