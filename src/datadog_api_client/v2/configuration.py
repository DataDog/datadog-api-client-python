# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.

from datadog_api_client.configuration import BaseConfiguration


class Configuration(BaseConfiguration):
    def __init__(
        self,
        host=None,
        api_key=None,
        api_key_prefix=None,
        access_token=None,
        username=None,
        password=None,
        discard_unknown_keys=True,
        disabled_client_side_validations="",
        server_index=None,
        server_variables=None,
        server_operation_index=None,
        server_operation_variables=None,
        ssl_ca_cert=None,
        compress=True,
    ):
        super(Configuration, self).__init__(
            host,
            api_key,
            api_key_prefix,
            access_token,
            username,
            password,
            discard_unknown_keys,
            disabled_client_side_validations,
            server_index,
            server_variables,
            server_operation_index,
            server_operation_variables,
            ssl_ca_cert,
            compress,
        )

        # Keep track of unstable operations
        self.unstable_operations = {
            "create_incident": False,
            "delete_incident": False,
            "get_incident": False,
            "list_incidents": False,
            "update_incident": False,
            "create_tag_configuration": False,
            "delete_tag_configuration": False,
            "list_tag_configuration_by_name": False,
            "list_tag_configurations": False,
            "update_tag_configuration": False,
            "list_security_monitoring_signals": False,
            "search_security_monitoring_signals": False,
            "create_incident_service": False,
            "delete_incident_service": False,
            "get_incident_service": False,
            "list_incident_services": False,
            "update_incident_service": False,
            "create_incident_team": False,
            "delete_incident_team": False,
            "get_incident_team": False,
            "list_incident_teams": False,
            "update_incident_team": False,
        }

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth = {}
        if self.access_token is not None:
            auth["AuthZ"] = {
                "type": "oauth2",
                "in": "header",
                "key": "Authorization",
                "value": "Bearer " + self.access_token,
            }
        if "apiKeyAuth" in self.api_key:
            auth["apiKeyAuth"] = {
                "type": "api_key",
                "in": "header",
                "key": "DD-API-KEY",
                "value": self.get_api_key_with_prefix(
                    "apiKeyAuth",
                ),
            }
        if "appKeyAuth" in self.api_key:
            auth["appKeyAuth"] = {
                "type": "api_key",
                "in": "header",
                "key": "DD-APPLICATION-KEY",
                "value": self.get_api_key_with_prefix(
                    "appKeyAuth",
                ),
            }
        return auth
