Feature: Create, edit, and disable roles.

    Background:
        Given a valid API key
        And a valid Application key
        And an instance of "Roles" API

    Scenario: List Roles
        When I call "ListRoles" endpoint
        Then I should get an instance of "RolesResponse"

    Scenario: List Permissions
        When I call "ListPermissions" endpoint
        Then I should get an instance of "PermissionsResponse"
