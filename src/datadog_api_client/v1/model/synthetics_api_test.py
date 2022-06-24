# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsAPITest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_api_test_config import SyntheticsAPITestConfig
        from datadog_api_client.v1.model.synthetics_test_options import SyntheticsTestOptions
        from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus
        from datadog_api_client.v1.model.synthetics_test_details_sub_type import SyntheticsTestDetailsSubType
        from datadog_api_client.v1.model.synthetics_api_test_type import SyntheticsAPITestType

        return {
            "config": (SyntheticsAPITestConfig,),
            "locations": ([str],),
            "message": (str,),
            "monitor_id": (int,),
            "name": (str,),
            "options": (SyntheticsTestOptions,),
            "public_id": (str,),
            "status": (SyntheticsTestPauseStatus,),
            "subtype": (SyntheticsTestDetailsSubType,),
            "tags": ([str],),
            "type": (SyntheticsAPITestType,),
        }

    attribute_map = {
        "config": "config",
        "locations": "locations",
        "message": "message",
        "monitor_id": "monitor_id",
        "name": "name",
        "options": "options",
        "public_id": "public_id",
        "status": "status",
        "subtype": "subtype",
        "tags": "tags",
        "type": "type",
    }
    read_only_vars = {
        "monitor_id",
        "public_id",
    }

    def __init__(self, config, locations, message, name, options, type, *args, **kwargs):
        """
        Object containing details about a Synthetic API test.

        :param config: Configuration object for a Synthetic API test.
        :type config: SyntheticsAPITestConfig

        :param locations: Array of locations used to run the test.
        :type locations: [str]

        :param message: Notification message associated with the test.
        :type message: str

        :param monitor_id: The associated monitor ID.
        :type monitor_id: int, optional

        :param name: Name of the test.
        :type name: str

        :param options: Object describing the extra options for a Synthetic test.
        :type options: SyntheticsTestOptions

        :param public_id: The public ID for the test.
        :type public_id: str, optional

        :param status: Define whether you want to start ( ``live`` ) or pause ( ``paused`` ) a
            Synthetic test.
        :type status: SyntheticsTestPauseStatus, optional

        :param subtype: The subtype of the Synthetic API test, ``http`` , ``ssl`` , ``tcp`` ,
            ``dns`` , ``icmp`` , ``udp`` , ``websocket`` , ``grpc`` or ``multi``.
        :type subtype: SyntheticsTestDetailsSubType, optional

        :param tags: Array of tags attached to the test.
        :type tags: [str], optional

        :param type: Type of the Synthetic test, ``api``.
        :type type: SyntheticsAPITestType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.config = config
        self.locations = locations
        self.message = message
        self.name = name
        self.options = options
        self.type = type

    @classmethod
    def _from_openapi_data(cls, config, locations, message, name, options, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAPITest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.config = config
        self.locations = locations
        self.message = message
        self.name = name
        self.options = options
        self.type = type
        return self
